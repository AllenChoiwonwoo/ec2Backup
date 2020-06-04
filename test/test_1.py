import requests
from bs4 import BeautifulSoup
import timeit

start = timeit.default_timer() #타이머 시작

headers = {'User-Agent':'Mozilla/5.0'}

URL = 'http://xecond.co.kr/product/list.html?cate_no=64'
# 크롤링하려는  url
response =requests.get(URL, headers=headers)
#requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

html = response.text
#html을 text로 바꾼다.
i = 0

soup = BeautifulSoup(html,'html.parser')
#html.parser를 사용해서 soup에 넣겠다.
for tag in soup.select('div > div.thumbnail > a'):

    i = i+1
    # tag.select('
    # img = tag.find_all("src")
    # img_url = tag.get("src")
    # img = tag.select('img')

    # div > div.thumbnail > a  = 썸네일
    # div.name > a > span:nth-child(2) > b 브랜드


    # img_alt = img.get("src")
    img = tag.find("img")
    # find_all 을 썼을땐 get("")를 쓸 수 없고, find를 썼을때만 get()를 쓸 수 있다.
    print(img.get("src"))
    print(img.get("alt"))
    # print(img.get("strong"))
    print()
    # print(img_alt)

    # name = tag.text.strip()
    # print(name)
   # print(tag.text.strip())
   #tag 에서 텍스트만 보여주고, 쓸대없는 공백도 지운다.


stop = timeit.default_timer()
print(stop - start)
print(i)
#이건 안되는겨?
