import requests
from bs4 import BeautifulSoup
import timeit
import multiprocessing
import mysql.connector

# import json
# from collections import OrderedDict

# 파싱 방법 관련글
# https://godoftyping.wordpress.com/2017/06/24/python-beautifulsoup/
# https://twpower.github.io/84-how-to-use-beautiful-soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling

mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)

mycursor = mysqlConnector.cursor()
# db연결자 만들기
# start = timeit.default_timer() #타이머 시작
mallNumb = 1
mallName = 'vintagetalk'
mallUrl = 'https://vintagetalk.co.kr/index.html'
# newProdDate = now()
newProdCount = 60
firstNewPage = 583938
firstNewProdNumb = 'H46577'
# createdDate = now()




sql = "INSERT INTO mallUpdateRecord (mallNumb, mallName, mallUrl, newProdDate, newProdCount, firstNewPage, firstNewProdNumb, createdDate) VALUES (%s, %s, %s, NOW(), %s, %s, %s, NOW())"
mycursor.execute(sql, (mallNumb, mallName, mallUrl, newProdCount, firstNewPage, firstNewProdNumb))
    # 3-1. db에 업로드할 준비를 한다.
mysqlConnector.commit()
