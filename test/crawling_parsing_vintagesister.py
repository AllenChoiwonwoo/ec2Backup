# https://denia.co.kr/
# https://vintagesister.co.kr/


import requests
from bs4 import BeautifulSoup
import timeit
import multiprocessing

# import json
# from collections import OrderedDict

# 파싱 방법 관련글
# https://godoftyping.wordpress.com/2017/06/24/python-beautifulsoup/
# https://twpower.github.io/84-how-to-use-beautiful-soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling


start = timeit.default_timer() #타이머 시작

headers = {'User-Agent':'Mozilla/5.0'}

URL = 'https://vintagesister.co.kr/'
# 크롤링하려는  url
response =requests.get(URL, headers=headers)
#requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

html = response.text
#html을 text로 바꾼다.
# i = 0

soup = BeautifulSoup(html,'html.parser')
#html.parser를 사용해서 soup에 넣겠다.
selectedList = soup.select('#m_contents > div.xans-element-.xans-product.xans-product-listmain-1.xans-product-listmain.xans-product-1 > ul > li')
print(selectedList.__len__())

def parsing():
    # print(selectedList[0].__len__(),"개")
    for value in selectedList:
        alist = value

        # i = i+1
        atag = alist.find("a")
        href = atag.get("href")
        print("링크", href)

        img = alist.find("img")                                       #이미지 태그 부분을 전부 찾아낸다.
                                                                    # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다.
        print("이미지", img.get("src"))
        img_src = img.get("src")
        # 2-3. 상품 이미지url값을 추출한다. // 왜 추출하는지 써야한다.
        # print("이름", img.get("alt"))
        # prodName = img.get("alt")


        prices = alist.find_all('span')                               # tag 에서 span 을 다 찾아낸다.

        size = prices.__len__()
        print("이름", prices[1].text)
        prodName = prices[1].text
        # 2-4. 상품 이름값을 추출한다.

        print("가격", prices[size-1].text)
        price = prices[size-1].text
        # 2-5. 상품 가격을 추출한다.

        count = 1
        #여기는 메인에 솔드아웃 상품 안보여줌(다 제고 있는겨)
        # icon = alist.find("div", class_="icon") # 솔드아웃
        #
        #
        # test = icon.find('img')
        #
        # count = 0 # 수량 값(솔드아웃)
        # try: #재고가 있을경우 아무값도 반환하지 않고, 재고에는 문자열이 있다.
        #     count = test.__len__() # __len__()은 배열의 길이를 구하는 함수
        #     print("수량", 0)
        #     count = 0
        # except Exception as e:
        #     print("수량", 1)
        #     count = 1

        print()

            #print()

       # print(tag.text.strip())
       #tag 에서 텍스트만 보여주고, 쓸대없는 공백도 지운다.
        # file_data = OrderedDict()

# tesks = [0, 100, 220]
# # i = 0
# for num in tesks:
parsing()

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
