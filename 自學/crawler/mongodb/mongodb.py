from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")


Test = myclient.學系學群學類.學群

# Test.insert_one({'name':'Sean','class':'AI'})
# mike_id = Test.insert_one({"name":"Mike","age":30}).inserted_id # .inserted_id 可以取得ID
for i in Test.find():
    try:
       print(eval(i['多元能力'])["程式設計"],end='')
    except:
       print(f'No cloumn',end='')
       pass
    
# print([p for p in Test.find({"name":"Mike"})])
# print([p for p in Test.find({"age":{"$lt":60}})]) # $lt => less than

# print(Test.count_documents({"name":"Mike"}))


# Test.update_one({"_id":ObjectId('654d9a1ced29a6b9886db543')},{"$set":{"name":"Sean"}})
# Test.update_one({"_id":ObjectId('654d9814d7baebed4c06ea4d')},{"$set":{"age":25}})
# print([p for p in Test.find({"_id":ObjectId('654d9a1ced29a6b9886db543')})])
# Test.update_one({"_id":ObjectId('654d9a1ced29a6b9886db543')},{"$set":{"name":"SSean"}})
# print([p for p in Test.find({"_id":ObjectId('654d9a1ced29a6b9886db543')})])

# Test.delete_many({"name":"Mike"})

# pipeLine = [
#     {
#         "$group": {
#             "_id": "$name",
#             "averageAge": {"$avg":"$age"}
#         }
#     },
#     {
#         "$sort": SON([("averageAge", -1), ("_id", -1)])
#     }
# ]


# results = Test.aggregate(pipeLine)

# for result in results:
#     print(result)