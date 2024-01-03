import pymysql
try:
    connection=pymysql.connect(user='root',password='root',port=3306,database='pythonsql')
    cursor=connection.cursor()
    query='''create table customer(id int primary key,mobile bigint unique,name varchar(100),balance bigint );'''
    cursor.execute(query)
except pymysql.err.OperationalError as e: 
    print(e)
def insert():
    query='''insert into customer(id,mobile,name,balance) values (1,46754673436,"Lokesh",25000)'''
    cursor.execute(query)
    connection.commit()

def get():
    query='select*from customer'
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
def dynamic(cid,mobile,name,bal):
    record=(cid,mobile,name,bal)
    query='insert into customer(id,mobile,name,balance) values (%s,%s,%s,%s)'
    cursor.execute(query,record)
    connection.commit()
def drop(cid):
    query=f'delete from customer where id={cid}'
    cursor.execute(query)
    connection.commit()
    print('record deleted')
def update(name,cid):
    query=f'update customer set column={name} where column={cid}'
    cursor.execute(query)
    connection.commit()
    print('record updated') 