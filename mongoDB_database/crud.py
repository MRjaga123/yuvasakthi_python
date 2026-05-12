from conn import mycol,mybd

# insert one 
def insert_one():
    data={ "rollno": 1, "name": "Ram", "age": 20, "dept": "CSE", "marks": 85 }
    mycol.insert_one(data)
    print("inserted")
# insert_one()

# insert many
def insert_many():
    data=[{ "rollno": 2, "name": "Sita", "age": 21, "dept": "IT", "marks": 90 },
            { "rollno": 3, "name": "John", "age": 22, "dept": "ECE", "marks": 75 },
            { "rollno": 4, "name": "Arun", "age": 20, "dept": "CSE", "marks": 88 },
            { "rollno": 5, "name": "Priya", "age": 21, "dept": "IT", "marks": 92 },
            { "rollno": 6, "name": "Kumar", "age": 23, "dept": "EEE", "marks": 70 },
            { "rollno": 7, "name": "Anu", "age": 20, "dept": "CSE", "marks": 95 },
            { "rollno": 8, "name": "Vijay", "age": 22, "dept": "ECE", "marks": 78 },
            { "rollno": 9, "name": "Meena", "age": 21, "dept": "IT", "marks": 84 },
            { "rollno": 10, "name": "Ravi", "age": 23, "dept": "EEE", "marks": 65 },
            { "rollno": 11, "name": "Divya", "age": 20, "dept": "CSE", "marks": 89 },
            { "rollno": 12, "name": "Surya", "age": 22, "dept": "ECE", "marks": 76 },
            { "rollno": 13, "name": "Karthik", "age": 21, "dept": "IT", "marks": 91 },
            { "rollno": 14, "name": "Nisha", "age": 20, "dept": "CSE", "marks": 87 },
            { "rollno": 15, "name": "Rahul", "age": 23, "dept": "EEE", "marks": 72 },
            { "rollno": 16, "name": "Pooja", "age": 21, "dept": "IT", "marks": 93 },
            { "rollno": 17, "name": "Mani", "age": 22, "dept": "ECE", "marks": 77 },
            { "rollno": 18, "name": "Sangeetha", "age": 20, "dept": "CSE", "marks": 90 },
            { "rollno": 19, "name": "Vimal", "age": 23, "dept": "EEE", "marks": 68 },
            { "rollno": 20, "name": "Sneha", "age": 21, "dept": "IT", "marks": 85 },
            { "rollno": 21, "name": "Deepak", "age": 22, "dept": "ECE", "marks": 79 },
            { "rollno": 22, "name": "Lavanya", "age": 20, "dept": "CSE", "marks": 94 },
            { "rollno": 23, "name": "Suresh", "age": 23, "dept": "EEE", "marks": 66 },
            { "rollno": 24, "name": "Gayathri", "age": 21, "dept": "IT", "marks": 88 },
            { "rollno": 25, "name": "Hari", "age": 22, "dept": "ECE", "marks": 77 },
            { "rollno": 26, "name": "Swathi", "age": 20, "dept": "CSE", "marks": 90 },
            { "rollno": 27, "name": "Prakash", "age": 23, "dept": "EEE", "marks": 73 },
            { "rollno": 28, "name": "Revathi", "age": 21, "dept": "IT", "marks": 91 },
            { "rollno": 29, "name": "Naveen", "age": 22, "dept": "ECE", "marks": 80 },
            { "rollno": 30, "name": "Bhavya", "age": 20, "dept": "CSE", "marks": 92 },
            { "rollno": 31, "name": "Ganesh", "age": 23, "dept": "EEE", "marks": 69 },
            { "rollno": 32, "name": "Harini", "age": 21, "dept": "IT", "marks": 87 },
            { "rollno": 33, "name": "Arvind", "age": 22, "dept": "ECE", "marks": 78 },
            { "rollno": 34, "name": "Latha", "age": 20, "dept": "CSE", "marks": 95 },
            { "rollno": 35, "name": "Vignesh", "age": 23,("dept"): ("EEE"),("marks"): (71) },
            { "rollno": 36,("name"):("Kavya"),("age"): (21),("dept"): ("IT"),("marks"): (89) },
            { "rollno": 37,("name"):("Ramesh"),("age"): (22),("dept"): ("ECE"),("marks"): (76) },
            { "rollno": 38,("name"):("Anitha"),("age"): (20),("dept"): ("CSE"),("marks"): (93) },
            { "rollno": 39,("name"):("Murali"),("age"): (23),("dept"): ("EEE"),("marks"): (67) },
            { "rollno": 40, "name": "Preethi", "age": 21, "dept": "IT", "marks": 90 },
            { "rollno": 41, "name": "Sanjay", "age": 22, "dept": "ECE", "marks": 81 },
            { "rollno": 42, "name": "Divakar", "age": 23, "dept": "EEE", "marks": 74 },
            { "rollno": 43, "name": "Shalini", "age": 20, "dept": "CSE", "marks": 97 },
            { "rollno": 44, "name": "Varun", "age": 21, "dept": "IT", "marks": 86 },
            { "rollno": 45, "name": "Mohan", "age": 22, "dept": "ECE",("marks"): (75) },
            { "rollno": 46,("name"):("Uma"),("age"): (20),("dept"): ("CSE"),("marks"): (91) },
            { "rollno": 47,("name"):("Raja"),("age"): (23),("dept"): ("EEE"),("marks"): (70) },
            { "rollno": 48,("name"):("Deepa"),("age"): (21),("dept"): ("IT"),("marks"): (92) },
            { "rollno": 49, "name": "Kiran", "age": 22, "dept": "ECE", "marks": 79 },
            { "rollno": 50, "name": "Sandhya", "age": 20, "dept": "CSE", "marks": 94 }
                ]
    mycol.insert_many(data)
    print("inserted")
# insert_many()

# find one
def find_one():
    print(mycol.find_one())
# find_one()

# find all
def find_all():
    for i in mycol.find():
        print(i)
# find_all()

# update one
def update_one():
    mycol.update_one({"rollno": 1}, {"$set": {"marks": 95}})
    print("updated")
# update_one()

# update many
def update_many():
    mycol.update_many({"dept": "CSE"}, {"$set": {"marks": 100}})
    print("updated")
# update_many()

# delete one
def delete_one():
    mycol.delete_one({"rollno": 1})
    print("deleted")
# delete_one()

# delete many
def delete_many():
    mycol.delete_many({"dept": "EEE"})
    print("deleted")
# delete_many()

# drop collection
def drop_collection():
    mycol.drop()
    print("collection dropped")
# drop_collection()

# drop database
def drop_database():
    mybd.drop_database("details")
    print("database dropped")
# drop_database()

# count documents
def count_documents():
    count=mycol.count_documents({})
    print("total documents: ",count)    
# count_documents()

##### task #####
# find top five students based on marks
def top_five_students():
    for i in mycol.find().sort("marks",-1).limit(5):
        print(i)
# top_five_students()

# Department-wise average (Aggregation) 
def department_wise_average():
    pipeline=[
        {"$group": {"_id": "$dept", "average_marks": {"$avg": "$marks"}}}
    ]
    for i in mycol.aggregate(pipeline):
        print(i)
# department_wise_average() 

# Add subjects array 
def add_subjects_array():
    mycol.update_many({}, {"$set": {"subjects": ["Maths", "Physics", "Chemistry", "English", "Computer Science"]}})
    print("subjects array added")
# add_subjects_array()
