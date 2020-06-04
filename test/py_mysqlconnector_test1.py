import mysql.connector

mysqlConnector = mysql.connector.connect(
    host="13.209.50.185",
    user="root",
    passwd="cww1003",
    database="choi"
)

mycursor = mysqlConnector.cursor()

latest_product_name = "test11"
before_latestProd_name = "b-test11"

sql = "INSERT INTO yj_mall_update_record (mall_name, kor_mall_name, latest_product_name, product_before_update, createdDate) VALUES (%s, %s, %s, %s, NOW())"
mycursor.execute(sql, ("realv", "리얼브이", latest_product_name, before_latestProd_name))
# mysqlConnector.commit()
mysqlConnector.commit()
