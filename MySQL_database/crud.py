from conn import get_connection

# get connections
connnection=get_connection()
cursor=connnection.cursor()

# functions
def create():
    query="""CREATE TABLE student(
        id INT,
        name VARCHAR(50),
        age INT,
        city VARCHAR(50)
        )"""
    cursor.execute(query)
    print("table created")
# create()   
def insert():
    # query="""INSERT INTO student(id,name,age,city) VALUES(1,'jaga','22','mannai')"""
    query="INSERT INTO student(id,name,age,city) VALUES(%s,%s,%s,%s)"
    id=int(input("enter id:"))
    name=str(input("enter name:"))
    age=int(input("enter age:"))
    city=str(input("enter city:"))
    cursor.execute(query,(id,name,age,city))
    connnection.commit()
    print("inserted")
# insert()
def update():
    name=str(input("enter name:"))
    age=int(input("enter age:"))
    query="UPDATE student SET age=%s WHERE name=%s"
    cursor.execute(query,(name,age))
    connnection.commit()
    print("updated")
# update()
def delete():
    name=str(input("enter name:"))
    query="DELETE FROM student WHERE name=%s"
    cursor.execute(query,(name))
    connnection.commit()
    print("deleted")
# delete()
def select():
    query="SELECT * FROM student"
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)
# select()

while True:
    print("\n1.create\n2.insert\n3.update\n4.select\n5.delete\n6.exit")
    choose=int(input("choose: "))
    if choose==1:
        create()
    elif choose==2:
        insert()
    elif choose==3:
        update()
    elif choose==4:
        select()
    elif choose==5:
        delete()
    elif choose==6:
        break
    else:
        print("invalid choose")
        
# close
cursor.close()
connnection.close()

