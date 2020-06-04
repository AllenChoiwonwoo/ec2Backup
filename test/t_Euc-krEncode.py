var = ("한글").encode('euc-kr')
print(var) #b'\xc7\xd1\xb1\xdb'

var2 = var.decode('euc-kr')
# print(var2) #한글
