
 #test.py 와 거의 같은 코드지만 속도 테스트를 위해서 xecond 라는 싸이트에서 테스트 한다. ( 차단당해도 무관 )
import requests
from bs4 import BeautifulSoup
import timeit

start = timeit.default_timer() #타이머 시작

headers = {'User-Agent':'Mozilla/5.0'}

URL = 'http://xecond.co.kr/'
# 크롤링하려는  url
response =requests.get(URL, headers=headers)
#requests 를 활용하여 header를 붙인 url 접속으로 html을 가져온다.

html = response.text
#html을 text로 바꾼다.
i = 0

soup = BeautifulSoup(html,'html.parser')
#html.parser를 사용해서 soup에 넣겠다.
for tag in soup.select('a span[style]'):
    print(tag.text.strip())
   #tag 에서 텍스트만 보여주고, 쓸대없는 공백도 지운다.
    i = i+1

stop = timeit.default_timer()
print(stop - start)
print(i)
#이건 안되는겨?
