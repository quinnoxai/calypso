from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client.calypso
mycollection = mydatabase.calypso_user
for i in mydatabase.myTable.find({'username': 'Shivam'}):
    print(i)
