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

    	목적 :
            사용자에게 쇼핑몰 'vintagesister'의 상품 업데이트 정보를 알려주고자 한다.
            그러기 위한 쇼핑몰의 상품 업데이트 내용을 알아내는 코드이다.
            (ex : 'vintagesister' 60개 업데이트. 2019-06-05 17:00 )
            # 사용자에게 쇼핑몰의 상품이 업데이트 되었을때 그 정보를 알려주고자한다.

		구현방법 :
            쇼핑몰의 업데이트 예상 시간에 주기적으로 크롤링을 시행하게한다.
            쇼핑몰이 업데이트 되었는지를 먼저 확인하고, 되었다면 몇개의 상품이 업데이트 되었는지를 알아낸다.
                -업데이트가 안됬다면 코드실행을 종료한다.
                -업데이트가 되었다면 몇개의 상품이 업데이트 되었는지 확인한다.
                # 데이터를 가져온다는 내용이 없다.
                # 구현방법, 세부 프로세스 가 따로 있을 이유가 없다. 구현방법에 포함시키자.
                # 세부 프로세스를 썼다고 다른 사람이 그대로 구현할 수 없다.



        세부 프로세스 :
    			i. 먼저 쇼핑몰 상품 업데이트 여부를 판별한다.
    					(ex : 업데이트전 60번까지 있었다면 업데이트 후 83번까지 페이지가 생성된다고 가정한다.)
    				지정한 시간이 되었을때 자동으로 코드가 작동된다.
    				Db에 저장되어 있는 마지막 상품페이지 넘버를 불러온다 (ex 60)
    				저장되어있던 마지막 상품페이지 넘버+1 페이지에 방문해본다 (ex 61)
    					® 페이지 없음 = 성품 업데이트 안됨
    						• 코드 실행 종료
    					® 페이지 있음 = 상품 업데이트 됨
    						• 쇼핑몰에 업데이트된 상품 개수 파악을 위한 코드 실행
                    # 다른사람이 이해할 수 없다.
                    # 도구는 읽는 사람이 선택할 수있게


    			ii. (업데이트 됐을시) 쇼핑몰에 몇개의 상품이 업데이트 되었지를 파악한다
    				Db에서 불러온 상품 페이지 넘버에 10페이지를 더한 넘버의 페이지에 방문해본다
                        상품
    					® 상품페이지가 있다 = 다시 여기에 다시 10페이지를 더한 페이지에 방문하기를 반복한다 (ex 70. 80. 90. ..)
    					® 상품페이지가 없다 = 10을 더하기 전 페이지 넘버에서 +1한 상품페이지에 방문한다 (ex 90 -> 80 + 1
    						• 반복하다 상품이 없을 시 현재페이지 -1이 마지막으로 업데이트 된 상품 페이지로 간주한다. (Ex 81. 82. 83. 84 )
    						• 현재 마지막 상품페이지 넘버 - 저장되어있던 상품페이지 = 쇼핑몰에 업데이트된 상품 개수 (ex. 83 - 60 = 23 )

                        업데이트 내용을 db에 저장한다.
                            현재 업데이트된 마지막 상품페이지 번호도 저장한다.
                            왜냐하면 다음번 업데이트 확인지 저장된 마지막 상품 페이지번호로 사용하기 위해서이다.

홈페이지에 접속한다.
로그인 화면으로 이동한다.
아이디와 비번을 입력한다.
아이디 비번 일치여부를 확인해서 보여준다.
#코딩샌드위치
"""
lastNewPage = 0
pageToGo = 0 # 접속한 페이지를 저장하기 위한 변수
# pageToGo2 = 0
url_NoPage = "http://vintagesister.co.kr/product/detail.html?product_no="
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
    print("3. 페이지 10개씩 검사 시작")
    time.sleep(2) #차단 방지를 위해 2초 대기
    global lastNewPage
    global pageToGo
    global url_NoPage
    global header
    global isPageOK
    global isGoMain
    print("4. 검사할 페이지는 "+str(pageToGo))
    response = requests.get(url_NoPage+str(pageToGo) , headers=headers)
            #마지막으로 존제한 페이지 넘버+10 의 페이지로 들어가 본다.
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > a')
    print(selectedList.__len__())
    print(str(selectedList))
    # 5-2. 이미지 url값을 가져온다.
    # ('빈티지톡'의 경우 페이지는 미리만들어 놓고 이미지는 넣어놓지 않는 경우가 있다.
    # 그러므로 페이지는 있는데 이미지는 없을경우를 구분해야하기에 아래의 코드가 있다. )
    if selectedList.__len__()!=0:
        print("상품 있음")
        #또 +10해서 검사
        isGoMain = False
        # print("상품 업로드 됨. 다시 +10")
        # global pageToGo
        pageToGo = pageToGo+10 #이건 효과가 없다 -while문으로 가면 초기화 되기 때문에
        print("5. 현재 pageToGo = "+str(pageToGo))
    else:
        print("상품 없음 xxxx")
        #돌아가 한개씩 검사
        print("상품 업로드 안됨. 이제 1페이지식 검사")
        pageToGo = pageToGo-10
        print("뒤로가서 "+str(pageToGo)+"부터 다시 1개씩")
        while isPageOK:
                        # global pageToGo
                        # pageToGo=pageToGo-10
            # 5-3-2. 1페이지씩 확인을 시작한다.
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
    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > a')
    if selectedList.__len__()!=0:
        print("상품있음 계속 진행")
    else:
        print("상품없음 xxxxxxx")
        isPageOK = False

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
        mycursor.execute(sql, ( 2, 'vintagesister', 'https://vintagesister.co.kr/index.html', newProdCount, lastNewPage, pageToGo-1) )
        mysqlConnector.commit()

        #노티를 주기위한 코드
        push_service = FCMNotification(api_key="AAAAl7NnNWQ:APA91bFAgIWcesU6lSac6lxazKtt-TPAtH_2mnonEhtQ9TOyO3S6u3ZvSxZN2hQj_vJQzTE4h10j9-GKGMiFlQHDDcSoFD2h1sR5zQ6azKssvh4zjNAGLgSOMPfmthW5RPqQ8gKmszpt")
        registration_id = "etm6cyIuqfc:APA91bFzX8V-MaeIH9D6bMaZQAjwExeksmUGbD87QGKFaGguFrjIICEpkRMfE3jvyGlhpHtAuiRRb3rja3slAiJHBrm2AoN8TXd7bF3g74aJfrogadBstvsfdU5j_JpCB_v60uJtz-AX"
        #@getStyle 용 토큰

        now = datetime.now()
        today = now.today().strftime("%Y.%m.%d %H시%M분")

        message_title = "쇼핑몰 업데이트"
        message_body = "vintagesister의 상품이 "+str(newProdCount)+"개 업데이트 되었습니다. "+today
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
    mycursor.execute("select lastNewPage from mallUpdateRecord WHERE mallNumb=2 ORDER BY newProdDate DESC LIMIT 1")
    # 몰번호(mallNumb) 2 는 빈티지 언니
    myresult = mycursor.fetchone()
                                #  print(myresult[0])
    lastNewPage = myresult[0]
    # print(lastNewPage)
    nextOflastPage = lastNewPage+1
                                # nextOflastPage = lastNewPage+1 #db에 저장된 상품이 있는 마지막 페이지 + 1 을 방문하기위해
    url_NoPage = "http://vintagesister.co.kr/product/detail.html?product_no="

    lastNewPage_next =url_NoPage +str(nextOflastPage)
    print("0"+str(lastNewPage_next)+"부터 방문")
    headers = {'User-Agent':'Mozilla/5.0'}

    URL = lastNewPage_next
    # 크롤링하려는  url
    mall_name = 'vintagesister'
    response =requests.get(URL, headers=headers)
    html = response.text
    #html을 text로 바꾼다.
    soup = BeautifulSoup(html, 'html.parser')
    selectedList = soup.select('#contents > div.xans-element-.xans-product.xans-product-detail > div.detailArea > div.xans-element-.xans-product.xans-product-image.imgArea > div.keyImg > a')
    print(selectedList.__len__())
    # print(str(selectedList))
    if selectedList.__len__() == 0:
        # 아직 없는페이지라 메인화면으로 넘어가게 될 경우
        # selectedList 의 길이는 0이다.
        print("없는페이지 => 업데이트 안됨. 끝")
                ## 여기까지는 성공
    else:
        print("페이지 발견 , 업데이트 됨, 계속 검사시작")
        for value in selectedList:
            # print(str(value))
            img_tag = value.find("img")
            # print(img_tag)
            img = img_tag.get("src")
            # img = selectedList.get("src")
            print("1. 추출된 이미지 : "+img)

            global isPageOK
            global isGoMain
            isPageOK = True
            # pageToGo = 105225
                # pageToGo = nextOflastPage+10
            pageToGo = lastNewPage + 10
            while isPageOK:

                print("2. while 전 pageToGo "+str(pageToGo))
                checkUpdateCount()

            break

checkMall1()


# db에서 데이터 가져오게 하기 ( 마지막 페이지 url)
