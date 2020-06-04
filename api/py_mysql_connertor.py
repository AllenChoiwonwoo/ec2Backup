import requests
from bs4 import BeautifulSoup
import timeit
import mysql.connector
from collections import OrderedDict
import mysqlConnector
# print(mysqlConnector.i)



# 파싱 방법 관련글
# https://godoftyping.wordpress.com/2017/06/24/python-beautifulsoup/
# https://twpower.github.io/84-how-to-use-beautiful-soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling

# 목적 : 쇼핑몰(excond)의 메인페이지의 상품정보를 가져와서 db에 저장한다.
# //@왜 가져오는지도 => 메인화면에서 쇼핑몰들의 신상품들 보여주기 위한 데이터 수집을 위해
#     (현재는 남자 자켓페이지를 크롤링하고, 수동으로 켜줘야만 저장한다.)
#     (추후에는 메인페이지로 바꾼다.)
#       //@왜 이렇게 만드려 했는지 => 현재는 빠른개발을 위해 상품이 적은페이지를 크롤링중이기에
#
# @사용 라이브러리 :
#         @a. requests 라이브러리 : 원하는 페이지의 요소(html)를 모두 가져온다.
#         @b. bs4 라이브러리 :  html에서 원하는 값을 추출할 수 있게 해준다.
#         @c. mysqlConnector : mysql과 연결시켜준다.
#
# 전체적인 시나리오 :
#         1. url 을 입력하여 html을 받아온다.
#         2. html 에서 원하는 데이터를 추출한다.
#         3. 추출한 데이터를 db에 넣는다.
# @{아래에서 "번호-1,2.."로 가면 해당 시나리오의 코드진행과정을 볼 수 있다.}
# @  // 주석을 보는법에대한설명도 필요 , 요소별과 시나리오의 구분자를 구분하자


mall_name = "excond" # 쇼핑몰 이름

# mysqlConnector = mysql.connector.connect(
#     host=myhost,
#     user=myuser,
#     passwd=mypasswd,
#     database=mydatabase
# )

mycursor = mysqlConnector.mysqlConnector.cursor()
start = timeit.default_timer() #타이머 시작
mycursor.execute("truncate new_products")


# sql = "INSERT INTO new_products (mall_name, img_src, prodname, price, count, createddate) VALUES (%s, %s, %s, %s, %s, NOW())"
#     # val = ("John1", "Highway1 21")
# mycursor.execute(sql, (mall_name, img_src, prodName, price, count))


mysqlConnector.mysqlConnector.commit()
#3-2. 그동안 준비시킨 모든 데이터를 업로드한다.
# print(mycursor.rowcount, "record inserted.")
print("abcd")
