import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='pydb')
    print("Database connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()

# Table Create
create_tbl="create table studinfo(id int primary key, name text, sub text)"

try:
    cr.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into studinfo values(1,'mitesh','php'),(2,'hitesh','python'),(3,'ashok','java'),(4,'meet','html'),(5,'harsh','android')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)
