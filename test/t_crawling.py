import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0'}

URL = 'http://www.vingols.co.kr/product/list.html?cate_no=49&page='
# 크롤링하려는  url
##response =requests.get(URL, headers=headers)
#requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

##html = response.text
#html을 text로 바꾼다.

##soup = BeautifulSoup(html,'html.parser')
#html.parser를 사용해서 soup에 넣겠다.
##for tag in soup.select('p[class=name]'):
##   print(tag.text.strip())

i = 1
while i < 37:
    filledURL = URL + str(i)
    response =requests.get(filledURL, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    for tag in soup.select('p[class=name]'):
        print(tag.text.strip())
    i= i+1