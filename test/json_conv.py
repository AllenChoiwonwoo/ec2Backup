import json
from collections import OrderedDict

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

file_data = OrderedDict()

# file_data["name"] = "computer"
# file_data["language"] = "kor"
# file_data["words"] = {'ram':'램', 'process':'프로세스', 'processor':'프로세서', 'cpu':'씨피유'}
# file_data["number"] = 4

# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))


# https://m.blog.naver.com/PostView.nhn?blogId=nackji80&logNo=221263224490&proxyReferer=https%3A%2F%2Fwww.google.com%2F

file_data["item1"] = {'img_url':'//xecond.co.kr/web/product/medium/j5847.jpg'
                    , 'productName':'JPNcote'
                    , 'price':'89,000won'
                    , 'quantity':'1'}

file_data["item2"] = {'img_url':'//xecond.co.kr/web/product/medium/j2920.jpg'
                    , 'productName':'cww'
                    , 'price':'35,000won'
                    , 'quantity':'0'}

testjson = json.dumps(file_data, ensure_ascii=False, indent="\t")
# s = "한글"
# u = str(s, "utf-8")

text = u"한글".encode("UTF-8")
# strtext = '\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
# strtext = "abcd"
print("abc")
# print(testjson)
