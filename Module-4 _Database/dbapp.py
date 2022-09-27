import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
create_tbl="create table studinfo(id int primary key, name text, sub text)"

try:
    dbcon.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into studinfo values(1,'mitesh','php'),(2,'hitesh','python'),(3,'ashok','java'),(4,'meet','html'),(5,'harsh','android')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)

# Update Data
"""update_data="update studinfo set name='pratik',sub='React' where id=5"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted successfully!")
except Exception as e:
    print(e)"""

# Select Data

cr=dbcon.cursor()

show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        #print(i)
        print(i[2])

except Exception as e:
    print(e)
    