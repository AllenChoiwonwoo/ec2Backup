import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError #404에러 메시지를 받기위해사용
from urllib.request import urlopen #HTTPError가 인지할 수 있는 response를 만들기 위해

import mysql.connector
import schedule
#schedule 예제 : https://lemontia.tistory.com/508
import time
from datetime import datetime
from pyfcm import FCMNotification

"""
    목적 : 쇼핑몰을 상품 업데이트 여부를 자동으로 파악
        + 업데이트시 업데이트 상품 개수
            ##### @@ 목적부터 이해가 가지 않는다.. 나만 이해할 수 있다... , 왜 파악하는지,
        ####의도에 대응되는 구체적 상황

    시나리오 : (전제조건 : #목적어 : 페이지 번호 #상품 추가시 올라간다, db에 기존의 '마지막 상품의 페이지번호'가 저장되어있다.)
            ##### @@ 상황과 목적에 대한 설명어 너무 없거나 부족하다.,
            @@
        1. 업데이트 예상시간이 되면 코드가 실행된다.
        2. DB에서 마지막 상품 페이지번호 를 불러온다.
        3. 그 다음페이지로 접속한다.
        (상품이 업데이트 되었다면 다음페이지가 있고, 안됐다면 다음페이지가 없을 것이다.)
        4. 페이지가 있으면 상품 업데이트 된것으로 간주한다.
        5. 페이지번호를 점점 증가시키면서 계속 접속해본다.
        6. 그러다 없는 페이지가 나오면 그 전페이지까지 업로드 된것으로 간주한다.
            (ex : db의 기존 마지막 페이지= 100 , 현재 검사시 없는 페이지 = 151,
                =>  업데이트 개수는 50개 )
        7. DB에 현재 마지막 상품 페이지 번호를 저장한다.
        8. 업데이트 주기가 되었을시 1번부터 반복 실행

    라이브러리 :
        requests : 페이지 소스를 가져올 수 있게 해준다.
        bs4 : 페이지 소스에서 원하는 정보를 추출할 수 있게 해준다.
        urllib.error : 웹페이지 응답에러코드를 예외처리 할 수 있게 해준다.
        urllib.request : 웹페이지 응답에러코드를 받아 올 수 있게 해준다.
        mysql.connector : db와 연결시켜준다.
        schecule : 원하는 주기에 파이썬 코드를 실행시킬 수 있게 해준다.
        time : 지정한 시간만큼 코드진행을 뭠춰준다.

----------------------- 코드 리뷰 후 수정2  --------------------------------------------

    	목적 수정 : 앱 사용자에게 쇼핑몰의 상품이 업데이트 되었다고 알려주려 한다.
			그러기 위한 쇼핑몰 상품업데이트 정보를 알아내는 코드이다
			(ex : 팀노바 쇼핑몰 에서 60개의 상품이 5월 29일 16시 55분에 업데이트 되었습니다. )

		구현방법 : 지정한 날짜와 시간에 주기적으로 크롤링을 시행하게한다. 크롤링을 통해 타겟 쇼핑몰의 변화를 감지한다

			i. 먼저 쇼핑몰 상품 업데이트 여부를 판별한다.
					(ex : 업데이트전 60번까지 있었다면 업데이트 후 83번까지 페이지가 생성된다고 가정한다.)
				지정한 시간이 되었을때 자동으로 코드가 작동된다.
				Db에 저장되어 있는 마지막 상품페이지 넘버를 불러온다(ex 60)
				마지막 상품페이지 넘버+1 페이지에 방문해본다 (ex 61)
					® 페이지 없음 = 성품 업데이트 안됨
						• 코드 실행 종료
					® 페이지 존재 = 상품 업데이트 됨
						• 쇼핑몰에 업데이트된 상품 개수 파악을 위한 코드 실행


			ii. 쇼핑몰에 몇개의 상품이 업데이트 되었지를 파악한다
				Db에서 불러온 상품 페이지 넘버에 10페이지를 더한 넘버의 페이지에 방문해본다
					® 상품페이지가 있다 = 다시 여기에 다시 10페이지를 더한 페이지에 방문하기를 반복한다 (ex 70. 80. 90. ..)
					® 상품페이지가 없다 = 10을 더하기 전 페이지 넘버에서 +1한 상품페이지에 방문한다 (ex 90 -> 80 + 1
						• 반복하다 상품이 없을 시 현재페이지 -1이 마지막으로 업데이트 된 상품 페이지로 간주한다. (Ex 81. 82. 83. 84 )
						• 현재 마지막 상품페이지 넘버 - 저장되어있던 상품페이지 = 쇼핑몰에 업데이트된 상품 개수 (ex. 83 - 60 = 23 )

"""
lastNewPage = 0
pageToGo = 0 # 접속한 페이지를 저장하기 위한 변수
# pageToGo2 = 0
url_NoPage = "https://vintagetalk.co.kr/product/detail.html?product_no="
# 이 문자열 뒤에 페이지번호를 넣으면 해당 페이지로 갈 수 있는 url이 나온다.
headers = {'User-Agent':'Mozilla/5.0'}
isPageOK = True
# 업데이트 상품 개수를 파악하기 위한 반박문을 제어하는 boolean 변수
isGoMain = True

class Global():
    num = 0


# db연결자 만들기
def dbcon():
    mysqlConnector = mysql.connector.connect(
        host="13.209.50.185",
        user="root",
        passwd="cww1003",
        database="choi"
    )
    return mysqlConnector

# 5-1. 상품이 업데이트 되었다고 판단될시 10씩 페이지 숫자를 올리며 몇개까지 업데이트 되었다 확인한다.
def checkUpdateCount():
    print("페이지 10개씩 검사 시작")
    time.sleep(2) #차단 방지를 위해 2초 대기
    global lastNewPage
    global pageToGo
    global url_NoPage
    global header
    global isPageOK
    global isGoMain
    print("검사할 페이지는 "+str(pageToGo))
    response = requests.get(url_NoPage+str(pageToGo) , headers=headers)
            #마지막으로 존제한 페이지 넘버+10 의 페이지로 들어가 본다.
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > div > a')
    # 5-2. 이미지 url값을 가져온다.
    # ('빈티지톡'의 경우 페이지는 미리만들어 놓고 이미지는 넣어놓지 않는 경우가 있다.
    # 그러므로 페이지는 있는데 이미지는 없을경우를 구분해야하기에 아래의 코드가 있다. )

    isGoMain = True
    for atag in selectedList:
        img_tag = atag.find("img")
        img_url = img_tag.get("src")
        # 이미지의 url로 접속한다.
        try:
            # 5-3. 이미지가 url로 접속해본다.
                            # response = requests.get("https:"+img, headers=headers)
            response = urlopen("https:"+img_url) #response 코드를 받아온다.
            # $$ 페이지 넘버가 존제하는 페이지를 넘어가면 페인페이지로 가게하는데.. 여기문제가 생기는데
            # exception 도 안나네.. else도 안되고..

            print(response)
        except HTTPError as e: # 404 에러가 떴을시 발동되는 코드
            #5-3-1. 이미지가 없다면 (404에러가 뜬다면) 상품이 없는것으로 간주한다.
            isGoMain = False
            print(e)
            print("상품 업로드 안됨. 이제 1페이지식 검사")
            pageToGo = pageToGo-10
            print("뒤로가서 "+str(pageToGo)+"부터 다시 1개씩")
            while isPageOK:
                            # global pageToGo
                            # pageToGo=pageToGo-10
                # 5-3-2. 1페이지씩 확인을 시작한다.
                checkUpdateCount2()

        else:   # 200 코드가 오면 성공이다.
        #5-4-1. 상품이 있는것으로 간주하여 다음 페이지(10개)로 가게한다.
            isGoMain = False
            print("상품 업로드 됨. 다시 +10")
            # global pageToGo
            pageToGo = pageToGo+10 #이건 효과가 없다 -while문으로 가면 초기화 되기 때문에
            print("현재 pageToGo = "+str(pageToGo))
        # finally: #존제하는 쇼핑몰 상품페이지 보다 더 큰페이지 넘버로 접속했을시 메인화면으로 이동될때를 처리하기위해
            #10단위 검색에서 1단위 검색을 하게 해야한다.
            # if isGoMain:
            #     print("finally 도 실행이 안됨?")
            #     pageToGo = pageToGo-10
            #     while isPageOK:
            #         checkUpdateCount2()
            # else:
                # isPageOK = False
    if selectedList.__len__()==0:
        # print("이건 실행되것지?")

            # print("finally 도 실행이 안됨?")
        pageToGo = pageToGo-10
        while isPageOK:
            checkUpdateCount2()


# 5-2. 페이지가 업데이트 되었고 10개씩 페이지를 검사하다 없는 페이지를 만났을때
#       -10페이지로 되돌아가 1개씩 늘리며 다시 검사한다.
def checkUpdateCount2():
    global lastNewPage
    global pageToGo
    global isPageOK
    pageToGo = pageToGo+1
    print(str(pageToGo)+"검사 시작")
    time.sleep(2) #차단 방지를 위해 2초 대기
    response = requests.get(url_NoPage+str(pageToGo), headers=headers)
                    #업는페이지의 -10페이지로 가서  +1 한 페이지 부터 다시 방문
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > div > a')
    for atag in selectedList:
        img_tag = atag.find("img")
        print(img_tag)
        img_url = img_tag.get("src")
        print(img_url)
        try:
                                            # response = requests.get("https:"+img, headers=headers)
            time.sleep(2) #차단 방지를 위해 2초 대기
            response = urlopen("https:"+str(img_url))
            print("페이지의 img 페이지 확인하기")
            print(response)
        except HTTPError as e: # 404 에러가 떴을시 발동되는 코드
            print(e)
            # print("상품 업로드 안됨")
            print("상품 업로드 안됨. 현재 페이지 +"+str(pageToGo))
            print("끝!")
            isPageOK = False


        else:
            print("상품 업로드 됨. 다음 +1 로 넘어감")
                                            # pageToGo = pageToGo+1
        # finally:
    if selectedList.__len__() == 0:
        print("상품 업로드 안됨. 현재 페이지 +"+str(pageToGo))
        print("끝!")
        print("기존 마지막 페이지 : "+str(lastNewPage)+", 현재 마지막 페이지 : "+str(pageToGo-1))
        newProdCount = pageToGo-1-lastNewPage
        print("업데이트된 상품 개수 : "+str(newProdCount))
        isPageOK = False

        # 7-1. 쇼핑몰의 마지막 상품 페이지 넘버를 DB에 저장
        mysqlConnector = dbcon()
        mycursor = mysqlConnector.cursor()
        sql = "INSERT INTO mallUpdateRecord\
         ( mallNumb, mallName, mallUrl, newProdDate, newProdCount, firstNewPage, lastNewPage, createddate )\
         values (%s, %s, %s, NOW(), %s, %s, %s, NOW() )"
        mycursor.execute(sql, ( 1, 'vintagetalk', 'https://vintagetalk.co.kr/index.html', newProdCount, lastNewPage+1, pageToGo-1) )
        mysqlConnector.commit()

        #노티를 주기위한 코드
        push_service = FCMNotification(api_key="AAAAl7NnNWQ:APA91bFAgIWcesU6lSac6lxazKtt-TPAtH_2mnonEhtQ9TOyO3S6u3ZvSxZN2hQj_vJQzTE4h10j9-GKGMiFlQHDDcSoFD2h1sR5zQ6azKssvh4zjNAGLgSOMPfmthW5RPqQ8gKmszpt")
        registration_id = "etm6cyIuqfc:APA91bFzX8V-MaeIH9D6bMaZQAjwExeksmUGbD87QGKFaGguFrjIICEpkRMfE3jvyGlhpHtAuiRRb3rja3slAiJHBrm2AoN8TXd7bF3g74aJfrogadBstvsfdU5j_JpCB_v60uJtz-AX"
        #@getStyle 용 토큰

        now = datetime.now()
        today = now.today().strftime("%Y.%m.%d %H시%M분")

        message_title = "쇼핑몰 업데이트"
        message_body = "vintagetalk의 상품이 "+str(newProdCount)+"개 업데이트 되었습니다. "+today
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
        print(result)



# 3-1. 기존의 최신 페이지를 가져와 다음페이지에 접속하여 업데이트 여부를 체크한다.
def checkMall1(): #빈티지 톡 체크하기
    global pageToGo
    global lastNewPage

    # mysqlConnector = mysql.connector.connect(
    #     host="13.209.50.185",
    #     user="root",
    #     passwd="cww1003",
    #     database="choi"
    # )
    mysqlConnector = dbcon()
                                #커넥터가 job 밖에 정의 되어있으면 mysql.connector 에러가 난다.
    mycursor = mysqlConnector.cursor()
                                # print('test1')
    # mycursor.execute("select lastNewPage from mallUpdateRecord")
    mycursor.execute("select lastNewPage from mallUpdateRecord WHERE mallNumb=1 ORDER BY newProdDate DESC LIMIT 1")
    myresult = mycursor.fetchone()
                                #  print(myresult[0])
    lastNewPage = myresult[0]
    print(lastNewPage)
    nextOflastPage = 592300
                                # nextOflastPage = lastNewPage+1 #db에 저장된 상품이 있는 마지막 페이지 + 1 을 방문하기위해
    url_NoPage = "https://vintagetalk.co.kr/product/detail.html?product_no="

    lastNewPage_next =url_NoPage +str(nextOflastPage)
    print(str(lastNewPage_next)+"부터 방문")
    headers = {'User-Agent':'Mozilla/5.0'}

    URL = lastNewPage_next
    # 크롤링하려는  url

    mall_name = 'vintagetalk'

    response =requests.get(URL, headers=headers)
                                    #requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.
                                    # print(response)
                                    # print(response.text)

    html = response.text
    #html을 text로 바꾼다.

    soup = BeautifulSoup(html, 'html.parser')

    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > div > a')
    # print(selectedList)
    if selectedList.__len__() == 0:
        # 아직 없는페이지라 메인화면으로 넘어가게 될 경우
        # selectedList 의 길이는 0이다.
        print("없는페이지 => 업데이트 안됨. 끝")
                ## 여기까지는 성공
    else:
        print("페이지 발견 계속 검사시작")
        for value in selectedList:
            img_tag = value.find("img")
            # print(img_tag)
            img = img_tag.get("src")
            # print(img)
            try:
                # response = requests.get("https:"+img, headers=headers)
                time.sleep(2) #차단 방지를 위해 2초 대기
                response = urlopen("https:"+img)
                print(response)
            except HTTPError as e: # 404 에러가 떴을시 발동되는 코드
                print(e)
                print("상품 업로드 준비중(임박) 하지만 아직 이미지가 없음. 끝")
            else:
                print("상품 업로드 됨")
                #상품이 업로드 되면 else문이 실행이 된다.
                                    # '''
                                    # 처음에 검사를 할때 기존에 마지막 페이지 + 1 한 페이지가 존제하는지 검사했을때
                                    # else로 왔다는 것은 "상품이 없로드 되었다" 라는 것이다.
                                    #  이제 몇페이지까지 업로드 된건지 알아야한다.
                                    # 빈티지톡은 제외하고는 다 많아야 100개정도 씩 업데이트 된다.
                                    # 그러므로 10개씩 증가시키면서 페이지를 체크한다.
                                    # 크롤링을 한번 수행하면 2초의 텀을 두고 다시 크롤링을한다.
                                    # 10개씩 증가하다가 없는 페이지가 나올 시
                                    # -10으로 가서 +1씩 증가하기를 반복한다.
                                    # 그러다 없는페이지가 나오면 끝
                                    #
                                    # '''

                                            # +10 페이지로 가보자
            # 업데이트가 되었다는 것을 확인했을때, 몇개의 상품이 업데이트 된것지 확인하는 코드를 시작한다.
                global isPageOK
                global isGoMain
                isPageOK = True
                pageToGo = 592300
                # pageToGo = nextOflastPage+10
                # pageToGo = lastNewPage + 10
                while isPageOK:
                                                    # global pageToGo2
                                                    # pageToGo2 = nextOflastPage + 10

                                                    # global pageToGo #여기서 다시 숫자가 리셋이 된다.
                                                    # pageToGo = lastNewPage+10# 그래서 여기서 숫자를 더했다.
                                                        # 그전에 글로벌 변수에 숫자를 더해놓고 다시 db에서 가져온 숫자를 가져와서 글로벌 변수에 넣고 있느라 되지 않는것였다..
                                                    # pageToGo = nextOflastPage+10
                    print("while 전 pageToGo "+str(pageToGo))
                    checkUpdateCount()
                    # print("이건 실행되것지?")
                    # if isGoMain:
                    #     print("finally 도 실행이 안됨?")
                    #     pageToGo = pageToGo-10
                    #     while isPageOK:
                    #         checkUpdateCount2()

                            #상품이 업로드 되면 else문이 실행이 된다.


                            #
                            # print(response)
                            # if str(response) == '<Response [200]>':
                            #     print("상품 업로드 됨")
                            # else str(response) == '<Response [404]>':
                            #     print("상품 업로드 준비중(임박)")

                            #  response 404 면 아직 업데이트 준비중인 상품
                            #  response 200 이면 업데이트 된 상품

                            # html = response.text
                            # print(html)
                            #
                            # soup = BeautifulSoup(html, 'html.parser')
                            # print(soup.text)
                            # selectedList = soup.select('img')
                            # print(selectedList)
                            # img_tag = selectedList[0].find("img")
                            # img = img_tag.get("src")
                            # print(img)
                            # print(selectedList.text)
            break


def job2():
    print('test2')

## 이 코드로 원하는 시간에 코드가 동작하게 할 수 있다.
# schedule.every(5).seconds.do(checkMall1)
# # schedule.every(13).seconds.do(job2)
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)

checkMall1()


# db에서 데이터 가져오게 하기 ( 마지막 페이지 url)







# for value in myresult:
#     print(value[0])
