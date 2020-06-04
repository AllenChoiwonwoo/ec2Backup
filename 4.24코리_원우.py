import requests
from bs4 import BeautifulSoup
import timeit
import mysql.connector
from collections import OrderedDict
import mysqlConnector


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

mycursor = mysqlConnector.cursor()
start = timeit.default_timer() #타이머 시작

headers = {'User-Agent':'Mozilla/5.0'}
# 크롤링임을 걸리지 않기위해 파이어폭스에서 접속한것으로 header를 바꾼다.
URL = 'http://xecond.co.kr/product/list.html?cate_no=64'
# 1-1. 크롤링하려는 페이지 주소 입력
response =requests.get(URL, headers=headers)
# 1-2. 쇼핑몰 페이지에 header를 통해 크롤러인걸 걸리지 않게 접속한다.
html = response.text
# 1-3. 가져온 html문서를 파싱할 수 있게 text로 바꾼다.
i = 0

soup = BeautifulSoup(html,'html.parser')
# 2-1. 파싱(검색)을 할 수 있는 형태로 바꾼다.
            #html.parser를 사용해서 soup에 넣겠다
for tag in soup.select('div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li'):
# 2-2. 상품정보가 들어있는 태그(39개)로 범위를 줄인다.

    i = i+1

    img = tag.find("img")                                       #이미지 태그 부분을 전부 찾아낸다.
                                                                # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다.
    print(img.get("src"))
    img_src = img.get("src")
    # 2-3. 상품 이미지url값을 추출한다. // 왜 추출하는지 써야한다.
    print(img.get("alt"))
    prodName = img.get("alt")
    # 2-4. 상품 이름값을 추출한다.

    prices = tag.find_all('span')                               # tag 에서 span 을 다 찾아낸다.

    size = prices.__len__()
    print(prices[size-2].text)
    price = prices[size-2].text
    # 2-5. 상품 가격을 추출한다.



    icon = tag.find("div", class_="icon") # 솔드아웃


    test = icon.find('img')

    count = 0 # 수량 값(솔드아웃)
    try: #재고가 있을경우 아무값도 반환하지 않고, 재고에는 문자열이 있다.
        count = test.__len__() # __len__()은 배열의 길이를 구하는 함수
        print(0)
        count = 0
    except Exception as e:
        print(1)
        count = 1
    # 2-6. 상품 수량을 추출한다. ( 수량이 없으면 0)

    sql = "INSERT INTO new_products (mall_name, img_src, prodname, price, count, createddate) VALUES (%s, %s, %s, %s, %s, NOW())"
    # val = ("John1", "Highway1 21")
    mycursor.execute(sql, (mall_name, img_src, prodName, price, count))
    # 3-1. db에 업로드할 준비를 한다.
    print()

                                                                    #배열에 넣어놓고 마지막에 한번에 DB에 넣기 vs #반복문속에서 하나씩 db에 넣기


stop = timeit.default_timer()
print(stop - start)
print(i)



mysqlConnector.commit()
#3-2. 그동안 준비시킨 모든 데이터를 업로드한다.
print(mycursor.rowcount, "record inserted.")
