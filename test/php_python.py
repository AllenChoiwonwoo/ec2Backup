# # print("hello, world!")
# a = u'가나다'
p = '가나다'
# p = '[{"name":"서태지","height":"173cm","weight":"55kg"},{"name":"양현석","height":"180cm","weight":"70kg"},{"name":"이주노","height":"172cm","weight":"53kg"}]'
# p = ("가나다").encode("cp949")
p = (p).encode()
# print(p)
# b = a.encode('cp949')
# print(p.decode("utf-8"))
# print(call(['ec dho', 'I like potatos']))
# def utf2euc(str):
#     return unicode(str, 'utf-8').encode('euc-kr')
# print(utf2euc(a))
# print(p)

import base64
import binascii

# encode = base64.('가나다')
# encode = base64.b64encode('가나다').decode('UTF-8')
# encode = binascii.b2a_base64(p, newline=False) #이것도 가능
encode = base64.b64encode(("가나다").encode('utf-8'))
print(encode)
# encode = encode[:-1]
# encode = encode[2:]
# print(encode)
