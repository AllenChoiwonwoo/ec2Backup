#-*- coding: utf-8 -*-

import mysql.connector
i =123
# myhost ="13.209.50.185"
# myuser ="wonwoo"
# mypasswd="cww1003"
# mydatabase="choi"

mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)


# mycursor = mysqlConnector.cursor()
# --------- select
# mycursor.execute("SELECT * FROM test1")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
# print("한글")

#----------- INSERT
# valss = '{"City":"Galle", "Description":"Best damn city in the world"}'
# sql = "INSERT INTO testjson (name, jsondata) VALUES (%s, %s)"
# val = ("John1", "Highway1 21")
# mycursor.execute(sql, ("string", valss))
# mycursor.execute(sql, ("geting", valss))
#
# mydb.commit()
# -------------
# print(mycursor.rowcount, "record inserted.")
