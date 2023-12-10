import csv
from pymongo import MongoClient


def read_csv_to_dict(file_path):
    data_dict_list = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data_dict_list.append(row)
    return data_dict_list


myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")


Test = myclient.學系學群學類.學類


# 用法示例
file_path = '學類.csv'
data_list = read_csv_to_dict(file_path)

# 打印读取到的数据
for data in data_list:
    Test.insert_one(data)


