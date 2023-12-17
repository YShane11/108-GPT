from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://YShane11:<a44993386>@school.hd1nbkk.mongodb.net/")
Test = myclient.學系學群學類.學群

for i in Test.find():
    print(i)