from conn import get_connection1

connection=get_connection1()
cursor=connection.cursor()

# create database
def create_DB():
    query="CREATE DATABASE school;"
    cursor.execute(query)
    print("DB created")
# create_DB()
cursor.execute("USE school;")

# functions
def create_TB():
    query="""CREATE TABLE students(
        rollno INT,
        name VARCHAR(50),
        tamil INT,
        english INT,
        maths INT,
        science INT,
        social INT,
        total INT
    )"""
    cursor.execute(query)
    print("Table created")
# create_TB()
def insert():
    query="INSERT INTO students(rollno,name,tamil,english,maths,science,social,total) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    rollno=int(input("enter rollno: "))
    name=str(input("enter name: "))
    tamil=int(input("enter tamil: "))    
    english=int(input("enter english: "))
    maths=int(input("enter maths: "))
    science=int(input("enter science: "))   
    social=int(input("enter social: "))
    total=tamil+english+maths+science+social 
    cursor.execute(query,(rollno,name,tamil,english,maths,science,social,total))
    connection.commit()
    print("inserted")
# insert()
def update():
    name=str(input("enter name:"))
    rollno=int(input("enter rollno:"))
    inputs_subject=input("enter subject:")
    inputs_marks=input("enter mark:")
    query=f"UPDATE students SET {inputs_subject}=%s,total=tamil+english+maths+science+social WHERE name=%s and rollno=%s"
    cursor.execute(query,(inputs_marks,name,rollno))
    # query1=f"UPDATE students SET total=tamil+english+maths+science+social WHERE name=%s and rollno=%s"
    # cursor.execute(query1,(name,rollno))
    connection.commit()
    print("updated")
update()
def delete():
    name=str(input("enter name:"))
    query="DELETE FROM students WHERE name=%s"
    cursor.execute(query,(name))
    connection.commit()
    print("deleted")
# delete()
def select():
    inputs=str(input("enter row: "))
    query=f"SELECT {inputs} FROM students"
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)
# select()

# while True:
#     print("\n1.create\n2.insert\n3.update\n4.select\n5.delete\n6.exit")
#     choose=int(input("choose: "))
#     if choose==1:
#         create_TB()
#     elif choose==2:
#         insert()
#     elif choose==3:
#         update()
#     elif choose==4:
#         select()
#     elif choose==5:
#         delete()
#     elif choose==6:
#         break
#     else:
#         print("invalid choose")
# # close
# cursor.close()  
# connection.close()


    