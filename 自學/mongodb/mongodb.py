from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

myclient = MongoClient("mongodb://localhost:27017/")


Test = myclient.Test.Test
# mike_id = Test.insert_one({"name":"Mike","age":30}).inserted_id # .inserted_id 可以取得ID
# Test.insert_one({'name':'Sean','class':'AI'})

# for i in Test.find():
#     try:
#        print(i['class'],end='')
#     except:
#        print(f'No cloumn',end='')
#        pass
    
# print([p for p in Test.find({"name":"Mike"})])
# print([p for p in Test.find({"age":{"$lt":60}})]) # $lt => less than

# print(Test.count_documents({"name":"Mike"}))


# Test.update_one({"_id":ObjectId('654d9a1ced29a6b9886db543')},{"$set":{"name":"Sean"}})
Test.update_one({"_id":ObjectId('654d9814d7baebed4c06ea4d')},{"$set":{"age":25}})
# print([p for p in Test.find({"_id":ObjectId('654d9a1ced29a6b9886db543')})])
# Test.update_one({"_id":ObjectId('654d9a1ced29a6b9886db543')},{"$set":{"name":"SSean"}})
# print([p for p in Test.find({"_id":ObjectId('654d9a1ced29a6b9886db543')})])

# Test.delete_many({"name":"Mike"})

pipeLine = [
    {
        "$group": {
            "_id": "$name",
            "averageAge": {"$avg":"$age"}
        }
    },
    {
        "$sort": SON([("averageAge", -1), ("_id", -1)])
    }
]


results = Test.aggregate(pipeLine)

for result in results:
    print(result)