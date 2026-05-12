import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mybd=myclient["details"] #database name
mycol=mybd["student"] #collection name

