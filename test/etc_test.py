from datetime import datetime
now = datetime.now()

today = str(now.year)+str(now.month)+str(now.day)
print(today)
today = now.today().strftime("%Y.%m.%d %H시%M분")
print(today)

 
