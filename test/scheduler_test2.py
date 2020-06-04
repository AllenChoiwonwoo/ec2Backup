import schedule
import time
import requests
from bs4 import BeautifulSoup
import timeit
from datetime import datetime
import mysql.connector

counter = 0

def job():
    global counter
    now = datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    anounce_message = 'secheduler 테스트  ('+nowDatetime+')'
    # 텔레그램 봇 통해서 메시지 보내기
    teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
    params = {'chat_id':'972295152', 'text':anounce_message}
    res = requests.get(teleurl, params=params)
    print("스케줄러 실행됨@@@@@@@@@@ "+str(counter))
    counter = counter + 1

mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)


schedule.every(10).seconds.do(job)
# schedule.every().day.at("13:31").do(get_latest_prod)

# schedule.every().day.at("09:00").do(job)
# schedule.every().day.at("12:00").do(job)
# schedule.every().day.at("12:20").do(job)
# schedule.every().day.at("12:40").do(job)
# schedule.every().day.at("13:00").do(job)
# schedule.every().day.at("13:20").do(job)
# schedule.every().day.at("13:40").do(job)
# schedule.every().day.at("14:00").do(job)
# schedule.every().day.at("14:20").do(job)
# schedule.every().day.at("14:40").do(job)
# schedule.every().day.at("15:00").do(job)
# schedule.every().day.at("15:20").do(job)
# schedule.every().day.at("15:40").do(job)
# schedule.every().day.at("16:00").do(job)
# schedule.every().day.at("16:20").do(job)
# schedule.every().day.at("16:40").do(job)
# schedule.every().day.at("17:00").do(job)
# schedule.every().day.at("17:20").do(job)
# schedule.every().day.at("17:40").do(job)
# schedule.every().day.at("18:00").do(job)
# schedule.every().day.at("18:20").do(job)
# schedule.every().day.at("18:40").do(job)
# schedule.every().day.at("19:00").do(job)


now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
anounce_message = 'secheduler 테스트 시작합니다. ('+nowDatetime+')'
# 텔레그램 봇 통해서 메시지 보내기
teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
params = {'chat_id':'972295152', 'text':anounce_message}
res = requests.get(teleurl, params=params)

while 1:
    # print("스케줄러 실행전")
    schedule.run_pending()
    # print("스케줄러 실행후")
    time.sleep(1)
    if counter == 5:
        break
    #실행시키면 와일문을 계속 돌고 있다.
    # 현재는 sleep1이 있어서 일초에 한번씩 돈다.
    # run_pending이 실행될때 10초가 지났다면 지정된 작업을 수행한다.
    #    sleep을 8초로하면 2번돌아 16초가 지난뒤 job이 수행된다.

# get_latest_prod()

print("코드실행 완료")
now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
anounce_message = 'secheduler 테스트 종료합니다. ('+nowDatetime+'):while문 out'
# 텔레그램 봇 통해서 메시지 보내기
teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
params = {'chat_id':'972295152', 'text':anounce_message}
res = requests.get(teleurl, params=params)


    # """
    # 리얼브이 쇼핑몰 업데이트 알림 만들기(for yeji)
    #
    # 리얼브이는 빈티지 쇼핑몰로 거의 매일 100개 이상의 상품을 업로드한다.
    # 하지만 사이트에서 재공하는 알림기능이 전혀 없고, 업데이트 예상 시간도 재공하지 않는다.
    # 그래서 업데이트 여부를 알 수 있도록 하게 한다.
    #
    # 필요 라이브러리 :
    #     schedule : 특정 주기를 정해 사이트를 크롤링하는 코드를 실행시켜줄 수 있다.
    #     time     : 시간값을 다룰 수 있게해준다.
    #     request  : 크롤링을 위해 사이트에 요청을 보낸다.
    #     bs4      : BeautifulSoup4 이다. request를 통해 가져온 html에서 원하는 데이터를 추출한다.
    #     mysql.connector : 서버의 mysqldb 에 연결 할 수 있게해준다.
    #       : 챗봇 api - http요청으로 텔레그램 메시지를 보낼 수 있게 해준다.
    #
    # """
