from pymongo import MongoClient

def database():
    myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")
    alldepartment = myclient.學系學群學類.學系

    # 使用 find 方法獲取特定集合的數據，這裡使用空的查詢，表示擷取所有文檔
    cursor = alldepartment.find({})

    # 遍歷游標並打印每個文檔
    for document in cursor:
        print(document)

    department = "國立臺灣大學中國文學系"

# 呼叫函數以執行數據庫操作
database()
