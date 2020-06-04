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



lastNewPage = 0
pageToGo = 0 # 접속한 페이지를 저장하기 위한 변수
# pageToGo2 = 0
url_NoPage = "http://xecond.co.kr/board/free/list.html?board_no=1"
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


def checkMall1(): #빈티지 톡 체크하기
    global pageToGo
    global lastNewPage

    mysqlConnector = dbcon()
                                #커넥터가 job 밖에 정의 되어있으면 mysql.connector 에러가 난다.
    mycursor = mysqlConnector.cursor()
                                # print('test1')
    # mycursor.execute("select lastNewPage from mallUpdateRecord")
    sql = 'SELECT mall_name, latest_product_name, createdDate FROM yj_mall_update_record WHERE mall_name = "vintagetalk" ORDER BY createdDate DESC LIMIT 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
                                #  print(myresult[0])
    if myresult is None:
        print("db에 데이터 없음")
        lastPostNumb = 0
    else:
        print("db에 데이터 있음")
        isRecord = myresult.__len__()
        # print(myresult[1])
        lastPostNumb = int(myresult[1])
                                # nextOflastPage = lastNewPage+1 #db에 저장된 상품이 있는 마지막 페이지 + 1 을 방문하기위해
    url = "https://vintagetalk.co.kr/board/free/list.html?board_no=1"

    # print("0"+str(lastNewPage_next)+"번째 부터 방문")
    headers = {'User-Agent':'Mozilla/5.0'}

    # 크롤링하려는  url
    mall_name = 'vintagetalk'
    response =requests.get(url, headers=headers)
    html = response.text
    #html을 text로 바꾼다.
    soup = BeautifulSoup(html, 'html.parser')
    selectedList = soup.select('table > tbody.xans-element-.xans-board.xans-board-list-1002.xans-board-list.xans-board-1002.center > tr > td')
    #** 시 spector 에 td:nth-child(1) 이런식으로 몇번째 태그는 쓸 수 없다고나온다.
    # 그래서 td 만 쓴 후 1번째 값을 가져 올 거라는건 코드로 구현해야한다.
    # print(selectedList.__len__())
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
            postNumb = value.text.strip()
            # print(postNumb)
            intPostNumb = int(postNumb)
            # $$$$$$$$$$$$$$$                 일단 최신글 번호 받아오기는 성공
            """
            크롤링을 통해 받아온 최신글 번호와 db에 저장되 있던 글번호를 비교한다.
                먼저 db에 저장된 글번호를 받아온다.
            db에 저장되 있던 글번호 보다 지금 받아온 글번호가 더 크다면 업데이트 된것으로 간주한다.
                크롤링한 최신글 번호의 자료형을 int로 바꾼다
                저장된글 번호와 비교한다.

            업데이트가 되었다면 새 글번호와 업데이트 내용을 db에 저장하고, 업데이트 알림을 보낸다.
                업데이트 내용을 가져오기위해 "2019. 5. 30 50여개 업데이트 완료!", "2018. 11. 21 120여개 업데이트 완료!" 에서 날짜와 개수를 추출해야한다.
                    공백을 기준으로 먼저 나눈다. '2018.' , '11.' , '21' , '120여개', '업데이트', '완료!'
                        '2018.'에서 뒤에서 1번째 문자(.)를 지운다
                        '11.' 도 '.'을 지운다.
                        '21'은 통과
                        '120여개' 는 뒤 2개의 문자를 지운다.
                        이렇게 하면 년,월,일, 상품개수 를 구할 수 있다.
                mysqlConnector를 통해서 db에 저장한다
                fcm 을 통해서 noti를 클라이언트에 보낸다.

            """
            if intPostNumb==lastPostNumb:
                print("업데이트 아직 안됨(업데이트 게시판의 글번호가 같다.)")
                return
            else:
                print("업데이트 됨(업데이트 게시판의 글번호가 다름)")
                tag_a = selectedList[2].find("a")
                updateInfo = tag_a.text.strip() # 업데이트 메시지 ex: 8월 21일 수요일 2,000장 업데이트 되었습니다.
                # print(updateInfo)
                array = updateInfo.split(' ')
                # print(array)
                # year = array[0][:-1] # 월
                # print(array[0][:-1])
                # month = array[1][:-1] # 일
                # print(month)
                # day = array[2] # 요일
                # print("날")
                # print(day)
                # count = array[3][:-2] # 개수
                # print("count")
                # print(count)
                # dot ='-'
                # date = year+dot+month+dot+day

                if (mysqlConnector.is_connected()):
                    sql = "INSERT INTO yj_mall_update_record (mall_name, kor_mall_name, latest_product_name, product_before_update, createdDate) VALUES (%s, %s, %s, %s, NOW())"
                    mycursor.execute(sql, ("vintagetalk", "빈티지톡", intPostNumb, lastPostNumb))
                    # mysqlConnector.commit()
                    mysqlConnector.commit()
                else:
                    print("mysql 에 연력이 끊어짐")

                now = datetime.now()
                today = now.today().strftime("%Y.%m.%d %H시%M분")
                message = "상품 업데이트 됨"

                teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
                params = {'chat_id':'-1001276900321', 'text':updateInfo}
                res = requests.get(teleurl, params=params) # 마지막에 이거 풀 # 업데


            global isPageOK
            global isGoMain

            if (mysqlConnector.is_connected()):
                mycursor.close()
                mysqlConnector.close()

            break

schedule.every(500).seconds.do(checkMall1)
while 1:
    schedule.run_pending()
    time.sleep(600)

# checkMall1()
print("vintagetalk 업데이트 감지 종료")
