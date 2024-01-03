import pymysql
connection=pymysql.connect(user='root',password='root',port=3306)
cursor=connection.cursor()
query='create database pythonsql'
cursor.execute(query)