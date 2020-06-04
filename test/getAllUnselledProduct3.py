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



'''
    이프로그램은 xecond의 모든 제고있는 상품 데이터를 저장하기 위한 프로그램이다.

    품절과 품절아님을 구별하는 법은 div class="icon"에 img태그 값이 있으면 솔드아웃이다.
'''


mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)

mycursor = mysqlConnector.cursor()


start = timeit.default_timer() #타이머 시작


i = 0
isItem = True

def parsing(i):
    global isItem
    # print(selectedList[0].__len__(),"개")
    # for value in range(0,index):
    headers = {'User-Agent':'Mozilla/5.0'}
    URL = "http://xecond.co.kr/product/search.html?view_type=&supplier_code=&category_no=&search_type=product_name&keyword=&exceptkeyword=&product_price1=1000&product_price2=100000000&order_by=&page="+str(i)+"&cate_no="
    # URL = "http://xecond.co.kr/product/search.html?view_type=&supplier_code=&category_no=&search_type=product_name&keyword=&exceptkeyword=&product_price1=1000&product_price2=100000000&order_by=&page="+str(i)+"&cate_no="
    # 크롤링하려는  url
    # print(URL)
    response =requests.get(URL, headers=headers)
    #requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

    mall_name = "xecond"

    html = response.text
    #html을 text로 바꾼다.
    # i = 0

    soup = BeautifulSoup(html,'html.parser')
    #html.parser를 사용해서 soup에 넣겠다.
    selectedList = soup.select('#-common > div > div > div.xans-element-.xans-search.xans-search-result.ec-base-product > ul > li')
    number = 0
    for value in selectedList:
        # alist = selectedList[value]
        alist = value

        # i = i+1
        atag = alist.find("a")
        href = atag.get("href")
        # print("하이퍼링크는 "+href)

        img = alist.find("img")
        # print(img)                                   #이미지 태그 부분을 전부 찾아낸다.
                                                                    # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다


        imgs = alist.find_all("img")
        # print("img태그 개수는 "+str(imgs.__len__()))
        # 원래 9개
        # print(str(imgs))
        # print(imgs)
        soldouts = imgs[imgs.__len__()-1].get("alt")
        if len(soldouts)<4:
            print("품절 break")
            isItem = False
            break
        # print("품절여부 : "+str(soldouts))
        # 상품정보가 담겨있는 li 태그 안에
        # img 태그가 3개면 soldout 된 상품이다. ( = 2번째 img태그가 soldout icon이다.)
        # img 태그가 2개면 제고가 있는 상품이다.
        number = number+1
        # if number == 40:
        #     break
        #print(number)
        # if imgs.__len__()==2:
        #     print("break")
        #     isItem = False
        #     break

        # print(img.get("data-original"))
        img_src = img.get("src")
        # 2-3. 상품 이미지url값을 추출한다. // 왜 추출하는지 써야한다.
        # print("이미지주소는 "+str(img_src))

        splitedImgsrc = img_src.split('/')
        preProdNumb = splitedImgsrc[(splitedImgsrc.__len__()-1)].split('.')
        prodNumb = preProdNumb[0]
        # print("상품번호는 "+str(prodNumb))


        prices = alist.find_all('span')                               # tag 에서 span 을 다 찾아낸다.

        size = prices.__len__()
        # print(str(prices))
        # print(size)
        # for value in prices:
        #     print(value)
        originalPrice=0
        salePrice=0
        # None = null

        #
        print("prices[4]는 상품 이름 : "+prices[3].text)
        prodName = prices[3].text
        # 2-4. 상품 이름값을 추출한다.

        if len(prices[4].text) == 3:
            originalPrice= prices[5].text
            # print("원가는 "+originalPrice)
            if size >= 9:
                salePrice = prices[8].text
                # print("할인가는 "+salePrice)
        else:
            originalPrice = prices[7].text
            # print("원가는 "+originalPrice)
            if size >= 11:
                salePrice = prices[10].text
                # print("할인가는 "+salePrice)

        # originalPrice =

        # # print(prices[size-4])
        # originalPrice = prices[size-4].text
        # print("prices[size-4] 는 원가 : "+str(originalPrice))
        # #세일전 가격
        #
        # print("prices[size-1] 는 세일후 가격 : "+prices[size-1].text)
        # price = prices[size-1].text
        # # 2-5. 상품 가격을 추출한다.



        # print("!@#!")
        # sql = "INSERT INTO allProducts_vintagetalk (mallName, img_src, prodName, prodNumb, price, salePrice, prodHref, modifiedDate, soldout) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s)"
        sql = "INSERT INTO allProducts_xecond (mallName, img_src, prodName, prodNumb, price, salePrice, prodHref, modifiedDate, soldout) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s) ON DUPLICATE KEY UPDATE modifiedDate=NOW()"
        mycursor.execute(sql, (mall_name, img_src, prodName, prodNumb, originalPrice, salePrice, href, 1))
        # print("...")
        # break


tesks = [0, 100, 200]
# i = 0
# for num in tesks:
#     parsing(num)
# i = 105
while isItem:

    i = i+1
    # 119
    # i = 108
    print("------------------------------")
    print(i)
    parsing(i)
    mysqlConnector.commit()
    print(str(i)+"페이지 후 3초 대기")
    time.sleep(3) #차단 방지를 위해 2초 대기
    # if isItem:
    #     break;


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
