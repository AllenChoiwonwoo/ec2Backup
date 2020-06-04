import schedule
import time
import requests
from bs4 import BeautifulSoup
import timeit
from datetime import datetime
import mysql.connector

def job():
    print("스케줄러 실행됨@@@@@@@@@@")

print("시작")




# if isRecord == 0:
#     pass


def get_latest_prod():
    # print(1)
    mysqlConnector = mysql.connector.connect(
        host="13.209.50.185",
        user="root",
        passwd="cww1003",
        database="choi"
    )
    mycursor = mysqlConnector.cursor()
    sql = 'SELECT mall_name, latest_product_name, createdDate FROM yj_mall_update_record WHERE mall_name = "vinclothes" ORDER BY createdDate DESC LIMIT 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    # print(myresult)
    # isRecord = myresult.__len__()
    if myresult != None :
        print("db에 데이터 잇음 _ before_latestProd_name : "+myresult[1])
        before_latestProd_name = myresult[1]
    else:
        print("db에 데이터 없음 ")
        before_latestProd_name = ""

    start = timeit.default_timer() #타이머 시작

    headers = {'User-Agent':'Mozilla/5.0'}

    # URL = 'https://vintagesister.co.kr/'
    URL = "http://vinclothes.co.kr/product/search.html?view_type=&supplier_code=&category_no=&search_type=product_name&keyword=&product_price1=1000&product_price2=1000000&order_by=recent&x=51&y=60&page=1&cate_no="
    # 크롤링하려는  url
    try:
        response =requests.get(URL, headers=headers)
    except Exception as e:
        print("빈옷 크롤링중 request를 보내는 코드에서 에러 발생(return로 메서드를 종료시켜 다음 반복문이 실행되게함)")
        print(e)
        return

    #requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

    #반복적인 접속으로 인해 사이트에서 자동으로 이 아이피의 접근은 차단하는 것으로 보인다. 그러므로 코드가 마무리 되지 못하고 끝나느것 같다.
    # 그래서 응답코드를 확인해보려고 한다.
    # 만약 쇼핑몰에서 나를 막았다면 404 가 나오면서 에러가 뜨지 않을가 생각한다.
    # 에러를 확인하면 좋은데..
    statuseCode = response.status_code

    now = datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    anounce_message = 'vinclothes: response.status_code 입니다. = '+str(statuseCode)+' ('+nowDatetime+')'
    # 텔레그램 봇 통해서 메시지 보내기
    # teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
    # params = {'chat_id':'972295152', 'text':anounce_message}
    # res = requests.get(teleurl, params=params)
    print(statuseCode)

    html = response.text
    #html을 text로 바꾼다.
    # i = 0

    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    #html.parser를 사용해서 soup에 넣겠다.
    # selectedList = soup.select('#form')
    # selectedList = soup.select('#anchorBoxId_110969 > div > a')
    selectedList = soup.select('div.xans-element-.xans-search.xans-search-result > ul > li > div > a')
    print(selectedList.__len__())
    # print(selectedList)
    # print("")
    # print(selectedList[0].text)
    # print("완료")


        # print(selectedList[0].__len__(),"개")
    for value in selectedList:
        alist = value

        # i = i+1
        atag = alist.find('img')
        # print(atag)
        # print("--")
        # print("atag : "+atag.attr("src"))

        # print("#form 안의 div 개수 ",atag.__len__())
        # counter = 0
        # for one_div in atag:
        #     counter = counter+1
        #     print(counter,"번 div : ",one_div.text.strip())

        # print("- - - - - - - - - - - - - - - - - - - - - ")
        # print("최근 업데이트 상품 : ",atag[3].text.strip())
        latest_product_name = atag.get('src')
        print("latest_product_name : "+latest_product_name)
        splited_imgsrc_array = latest_product_name.split("/")
        sia_len = splited_imgsrc_array.__len__()
        # print("splited_imgsrc_array 길이 : "+ str(splited_imgsrc_array.__len__()))
        # print(splited_imgsrc_array[(sia_len-1)])
        latest_product_name = splited_imgsrc_array[(sia_len-1)]
        print("latest_product_name : "+latest_product_name)
        break

    stop = timeit.default_timer()
    # print(stop - start)
    # return latest_product_name
    # latest_product_name = get_latest_prod()
    if before_latestProd_name == latest_product_name:
        print("아직 업데이터 안됨")
        # String now_data_time = '%s-%s-%s %s:%s' % ( now.year, now.month, now.day, now.hour, now.minute )
        # print (now_data_time)
        # now = datetime.now()
        # nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        # anounce_message = 'learv[리얼브이] 아직입니다.. ('+nowDatetime+')'
        # # 텔레그램 봇 통해서 메시지 보내기
        # teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
        # params = {'chat_id':'972295152', 'text':anounce_message}
        # res = requests.get(teleurl, params=params)
        #
        # print(anounce_message)

    else:
        print("업데이트 됨 . latest_product_name = ",latest_product_name)
        # 현재 시간

        now = datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        anounce_message = 'vinclothes 상품 업데이트 되었습니다$$$$$$ . ('+nowDatetime+')'
        # 텔레그램 봇 통해서 메시지 보내기 ( 예지도 있는 채팅방)
        teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
        params = {'chat_id':'-1001276900321', 'text':anounce_message}
        res = requests.get(teleurl, params=params)


        if(mysqlConnector.is_connected()):

            sql = "INSERT INTO yj_mall_update_record (mall_name, kor_mall_name, latest_product_name, product_before_update, createdDate) VALUES (%s, %s, %s, %s, NOW())"
            mycursor.execute(sql, ("vinclothes", "빈옷", latest_product_name, before_latestProd_name))
            # mysqlConnector.commit()
            mysqlConnector.commit()
            print("db에 상품 이미지 이름 저장 완료")
            # print(anounce_message)
            # mysql 에 잘 저장되었는지를 텔레그렘으로 보낸다.
            params = {'chat_id':'972295152', 'text':'mysql에 정상 저장 왼료'}
            res = requests.get(teleurl, params=params)
        else:
            print("mysql 과의 연결이 끊어졌습니다.")
            # mysql과 연결이 끊어졌음을 텔레그램으로 보낸다.
            params = {'chat_id':'972295152', 'text':'mysql에 저장 실패!!!!!@@@@ 연결끊어짐'}
            res = requests.get(teleurl, params=params)



    if (mysqlConnector.is_connected()):
        mycursor.close()
        mysqlConnector.close()


    URL = "http://vinclothes.co.kr/product/detail.html?product_no=111183&cate_no=53&display_group=1"

    try:
        response =requests.get(URL, headers=headers)
    except Exception as e:
        print("빈옷 크롤링중 request를 보내는 코드에서 에러 발생(return로 메서드를 종료시켜 다음 반복문이 실행되게함)")
        print(e)
        return
    response.encoding='utf-8'
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    #html.parser를 사용해서 soup에 넣겠다.
    # selectedList = soup.select('#form')
    # selectedList = soup.select('#anchorBoxId_110969 > div > a')
    selectedList = soup.select('div.mWarn > div > h3')
    print(selectedList.__len__())
    # print(selectedList)
    if selectedList.__len__() == 0:
        print("알림 이란 글씨를 찾을 수 없음 = 업데이트 준비중이거나 됨")
        now = datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        anounce_message = '@#@ 빈옷이 페이지를 만들고 있는거나 , 이미 만듬'
        # 텔레그램 봇 통해서 메시지 보내기
        teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
        params = {'chat_id':'972295152', 'text':anounce_message}
        res = requests.get(teleurl, params=params)

    for value in selectedList:
        text = value.text
        print(text)

        # en_text = text.decode('euc-kr','replace')
        # print(en_text)


schedule.every(20).seconds.do(get_latest_prod)

# schedule.every().day.at("13:31").do(get_latest_prod)

# schedule.every().day.at("12:00").do(get_latest_prod)
# schedule.every().day.at("12:20").do(get_latest_prod)
# schedule.every().day.at("12:40").do(get_latest_prod)
# schedule.every().day.at("13:00").do(get_latest_prod)
# schedule.every().day.at("13:20").do(get_latest_prod)
# schedule.every().day.at("13:40").do(get_latest_prod)
# schedule.every().day.at("14:00").do(get_latest_prod)
# schedule.every().day.at("14:20").do(get_latest_prod)
# schedule.every().day.at("14:40").do(get_latest_prod)
# schedule.every().day.at("15:00").do(get_latest_prod)
# schedule.every().day.at("15:20").do(get_latest_prod)
# schedule.every().day.at("15:40").do(get_latest_prod)
# schedule.every().day.at("16:00").do(get_latest_prod)
# schedule.every().day.at("16:20").do(get_latest_prod)
# schedule.every().day.at("16:40").do(get_latest_prod)
# schedule.every().day.at("17:00").do(get_latest_prod)
# schedule.every().day.at("17:20").do(get_latest_prod)
# schedule.every().day.at("17:40").do(get_latest_prod)
# schedule.every().day.at("18:00").do(get_latest_prod)
# schedule.every().day.at("18:20").do(get_latest_prod)
# schedule.every().day.at("18:40").do(get_latest_prod)
# schedule.every().day.at("19:00").do(get_latest_prod)
# get_latest_prod()
# now = datetime.now()
# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# anounce_message = 'learv[리얼브이] 상품 업데이트 되었습니다. ('+nowDatetime+')'
# # 텔레그램 봇 통해서 메시지 보내기
# teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
# params = {'chat_id':'972295152', 'text':anounce_message}
# res = requests.get(teleurl, params=params)

# print(today)
# print("업데이트 됨 . latest_product_name = ",latest_product_name)
# 현재 시간

now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
anounce_message = 'vinclothes[빈옷] 체크 시작합니다. ('+nowDatetime+')'
# 텔레그램 봇 통해서 메시지 보내기
teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
params = {'chat_id':'972295152', 'text':anounce_message}
res = requests.get(teleurl, params=params)

while 1:
    try:
        # print("스케줄러 실행전")
        schedule.run_pending()
        # get_latest_prod()
        # print("스케줄러 실행후")
        # time.sleep(10)
        time.sleep(1200)
        #실행시키면 와일문을 계속 돌고 있다.
        # 현재는 sleep1이 있어서 일초에 한번씩 돈다.
        # run_pending이 실행될때 10초가 지났다면 지정된 작업을 수행한다.
        #    sleep을 8초로하면 2번돌아 16초가 지난뒤 job이 수행된다.
    except Exception as e:
        print("스케줄 러에서 에러발생 (continune를 통해 while문을 진행시킴)")
        print(e)
        continue



get_latest_prod()

print("코드실행 완료")
now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
anounce_message = '빈옷 체크 코드 종료합니다. ('+nowDatetime+'):while문 out'
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
