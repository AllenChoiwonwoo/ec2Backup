import requests

# print("asdf")
#
# teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
#
# params = {'chat_id':'972295152', 'text':'adfadsf'}
#
# res = requests.get(teleurl, params=params)

teleurl = "https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/sendMessage"
params = {'chat_id':'-1001276900321', 'text':'hihi'}
res = requests.get(teleurl, params=params)

"""
리눅스 백그라운드 실행 :
https://sjwiq200.tistory.com/16

텔레그램 챗봇 user_id 구하기 :
"https://api.telegram.org/bot935475572:AAFnM0-sOYGhaUNaMbMD68dEeF7v24tCBu4/getUpdates"
위 url에서 bot뒤에 내 봇의 토큰값을 입력하고 엔터치면
json형태로 해당 봇이 받았던 메시지를 볼 수 있고 , 여기서 메시지를 보낸이의 user_id를 확인할 수 있다.

텔레그램 restAPI를 활용한 파이썬으로 메시지 보내기
https://hatpub.tistory.com/60


"""
