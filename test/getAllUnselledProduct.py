import requests
from bs4 import BeautifulSoup
import timeit
import multiprocessing
import mysql.connector
import time
from datetime import datetime

# import json
# from collections import OrderedDict

# 파싱 방법 관련글
# https://godoftyping.wordpress.com/2017/06/24/python-beautifulsoup/
# https://twpower.github.io/84-how-to-use-beautiful-soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling

mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)

mycursor = mysqlConnector.cursor()


start = timeit.default_timer() #타이머 시작

# headers = {'User-Agent':'Mozilla/5.0'}
#
# URL = 'https://vintagetalk.co.kr/product/search.html?view_type=&supplier_code=&category_no=&search_type=product_name&keyword=&exceptkeyword=&product_price1=1000&product_price2=100000000&order_by=recent&x=27&y=16&page=350&cate_no='
# # 크롤링하려는  url
# response =requests.get(URL, headers=headers)
# #requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.
#
# mall_name = "vintagetalk"
#
# html = response.text
# #html을 text로 바꾼다.
# # i = 0
#
# soup = BeautifulSoup(html,'html.parser')

#html.parser를 사용해서 soup에 넣겠다.

# selectedList = soup.select('#contents > div.xans-element-.xans-search.xans-search-result.ec-base-product > ul > li')
# div.main_scroll_item.is--product > div > ul > li
#contents > div.xans-element-.xans-search.xans-search-result.ec-base-product > ul > li  > div > a'''
'''
이코드는 vintagetalk의 재고가 있는 상품의 모든 데이터를 서버에 저장하기 위한 코드이다.
재고있는 상품 DB에 저장하는 방법 :
    검색시 모든 상품에 공통되는 조건을 검색하면 (EX: 판매가격 범위 0 ~ 1000000원) 전체상품을 볼 수 있다.
    최신순으로 250개씩 페이징 되어 보여지며, 재고가 있는 상품부터 보여진다.( 재고없는 상품이 있는 페이지가 나올 시 크롤링 종료)
    1페이지부터 페이지에 있는 모든 상품(재고있는 상품)의 데이터를 서버의 각 쇼핑몰의 테이블에 저장한다.
    한페이지가 끝나면 다음 페이지를 같은방식으로 진행한다.
    이러다 팔린상품이 나오면 코드진행을 종료한다.

    이 코드는 쇼핑몰의 트레픽이 덜 몰릴것으로 예상 되는 시간대를 선정해 하루 3번 실행한다.
    그 사이에 팔린 상품은 걸러줄 수 없다.
    # 이경우는 한명의 클라가 A상품 상세포기를 눌렀을때 재고가 없는 상품이었을 경우
        클라가 서버로 이 A상품은 재고가 없다는 것을 알려주어 DB를 업데이트 할 수 있게 한다.
        이렇게 하면 그 후 다른 사용자에게는 A상품이 재고가 없다는 것을 반영하여 데이터를 재공할 수 있다. 

'''

i = 0
isItem = True

def parsing(i):
    global isItem
    # print(selectedList[0].__len__(),"개")
    # for value in range(0,index):
    headers = {'User-Agent':'Mozilla/5.0'}

    URL = 'https://vintagetalk.co.kr/product/search.html?view_type=&supplier_code=&category_no=&search_type=product_name&keyword=&exceptkeyword=&product_price1=1000&product_price2=100000000&order_by=recent&x=27&y=16&page='+str(i)+'&cate_no='
    # 크롤링하려는  url
    # print(URL)
    response =requests.get(URL, headers=headers)
    #requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

    mall_name = "vintagetalk"

    html = response.text
    #html을 text로 바꾼다.
    # i = 0

    soup = BeautifulSoup(html,'html.parser')
    #html.parser를 사용해서 soup에 넣겠다.
    selectedList = soup.select('#contents > div.xans-element-.xans-search.xans-search-result.ec-base-product > ul > li')
    number = 0
    for value in selectedList:
        # alist = selectedList[value]
        alist = value

        # i = i+1
        atag = alist.find("a")
        href = atag.get("href")
        # print(href)

        img = alist.find("img")
        # print(img)                                   #이미지 태그 부분을 전부 찾아낸다.
                                                                    # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다


        imgs = alist.find_all("img")
        # print(imgs.__len__())
        # print(imgs)
        # 상품정보가 담겨있는 li 태그 안에
        # img 태그가 3개면 soldout 된 상품이다. ( = 2번째 img태그가 soldout icon이다.)
        # img 태그가 2개면 제고가 있는 상품이다.
        number = number+1
        # if number == 30:
        #     break
        # print(number)
        if imgs.__len__()==3:
            print("break")
            isItem = False
            break

        # print(img.get("data-original"))
        img_src = img.get("data-original")
        # 2-3. 상품 이미지url값을 추출한다. // 왜 추출하는지 써야한다.
            # 이미지 url로 앱에서 이미지를 로드해 보여주기 때문에
        # print(img.get("alt"))
        # prodName = img.get("alt")
        splitedImgsrc = img_src.split('/')
        preProdNumb = splitedImgsrc[(splitedImgsrc.__len__()-1)].split('.')
        prodNumb = preProdNumb[0]
        # print(prodNumb)


        prices = alist.find_all('span')                               # tag 에서 span 을 다 찾아낸다.

        size = prices.__len__()
        #
        # print(prices[size-6].text)
        prodName = prices[size-6].text
        # 2-4. 상품 이름값을 추출한다.

        # print(prices[size-4])
        originalPrice = prices[size-4].text
        # print(originalPrice)
        #세일전 가격

        # print(prices[size-1].text)
        price = prices[size-1].text
        # 2-5. 상품 가격을 추출한다.




        # sql = "INSERT INTO allProducts_vintagetalk (mallName, img_src, prodName, prodNumb, price, salePrice, prodHref, modifiedDate, soldout) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s)"
        sql = "INSERT INTO allProducts_vintagetalk (mallName, img_src, prodName, prodNumb, price, salePrice, prodHref, modifiedDate, soldout) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s) ON DUPLICATE KEY UPDATE modifiedDate=NOW()"
        mycursor.execute(sql, (mall_name, img_src, prodName, prodNumb, originalPrice, price, href, 1))


        # print()
        # break

            #print()

       # print(tag.text.strip())
       #tag 에서 텍스트만 보여주고, 쓸대없는 공백도 지운다.
        # file_data = OrderedDict()

tesks = [0, 100, 200]
# i = 0
# for num in tesks:
#     parsing(num)

while isItem:
    i = i+1
    #119
    # i = 1
    print("------------------------------")
    print(i)
    parsing(i)
    mysqlConnector.commit()
    print(str(i)+"페이지 후 3초 대기")
    time.sleep(3) #차단 방지를 위해 2초 대기


    # break;
    # pass



# if __name__ == '__main__':
#     #멀티쓰레딩 pool 사용
#     pool = multiprocessing.Pool(processes=3)
#     pool.map(parsing, tesks)
#     pool.close()
#     pool.join()

stop = timeit.default_timer()
print(stop - start)
# print(i)
#이건 안되는겨?


# # tag.select('
# # img = tag.find_all("src")
# # img_url = tag.get("src")
# # img = tag.select('img')
#
# # div > div.thumbnail > a  = 썸네일
# # div.name > a > span:nth-child(2) > b 브랜드
#
#
# # img_alt = img.get("src")
# img = tag.find("img") #이미지 태그 부분을 전부 찾아낸다.
# # print(img)
# # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다.
# print(img.get("src"))
# print(img.get("alt"))
#
# prices = tag.find_all('span')
# #tag 에서 span 을 다 찾아낸다.
#
# size = prices.__len__()
# print(prices[size-2].text) #r가격
#
# # coasts = tag.find_all("li", rel="판매가")
# # print(coasts[0].get_text)
# # # for coast in coasts.find_all('span'):
# # #     print(coast)
#
#
# icon = tag.find("div", class_="icon") # 솔드아웃
# # print(icon.get('alt'))
# # soldout = icon.get("alt")
# # print(soldout)
# # 상품가격을 가져온다. (= 5번째 span 값)
# # soldout = icon[0].find("img")
# # print(icon)
# test = icon.find('img')
# print(test)
#     # 이렇게 하면 풀저x  =  none,   품절o = 값이 있음
#     # none 인지 아닌지로 구분하면 된다.
