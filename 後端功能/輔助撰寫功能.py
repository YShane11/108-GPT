import openai
from dotenv import dotenv_values
import time
from pymongo import MongoClient
import csv

def database():
    myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")
    alldepartment = myclient.學系學群學類.學系

    department = []
    for i in alldepartment.find():
        department.append(i)
    return department

def allquestions(support):
    with open(f"後端功能/Question/{support}.txt", "r", encoding = "utf-8") as file:
        AI_quesntions = [line.strip() for line in file.readlines()]
    return AI_quesntions

def main(department, support):
    AI_quesntions = allquestions(support)
    allschooldata= database()
    for i in allschooldata:
        if i['學校']+i['系所'] == department:
            aimdepartment = i
            break

    config = dotenv_values("C:/Users/YShane11/env.txt")
    openai.api_key = config["API_KEY"]

    messages = [{"role": "system","content": "語言:zh-Tw 目標客群:準備申請大學的高中生 工作:從學生的角度,輔助生成備審資料且文筆極佳的AI助手(字數大約1000字) 重點:內容須符合所提供資訊，不可憑空捏造事實、文筆需接近高中生所寫 "}]
    messages.append({"role": "system","content": f"目標校系:{department}"})
    if support == '多元表現綜整心得':
        messages.append({"role": "system","content": "多元綜整的定義:將高中參加的自主學習、社團活動、擔任幹部經驗、服務學習經驗、競賽表現、非修課紀錄的成果作品、檢定證照、特殊優良表現證明進行彙整，並說明從這些經驗中，所學到內容和成長，盡可能展現自己的 { 此校系所需多元能力、此校系所適合的性格特質 } 的人格特質與具備的能力。"})
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
    
    elif support == '就讀動機':
        messages.append({"role": "system","content": "就讀動機的定義:請將申請進入這個學系的個人動機、學系有哪些吸引人的特點、個人經歷等進行彙整，結合 { 目標校系 } 的 { 此校系之學系特色、此校系所需學科意涵、此校系所需多元能力、此校系所適合的性格特質 }，展現出學生適合就讀該科系的強烈動機以及和該科系對能力特質非常契合。"})
        messages.append({"role": "system","content": f"此校系之學系特色:{aimdepartment['學系特色']}"})
        messages.append({"role": "system","content": f"此校系所需學科意涵:{aimdepartment['學科意涵']}"})
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})

    elif support == '未來學習計畫及生活規劃':
        messages.append({"role": "system","content": "未來學習計畫及生活規劃的定義:結合申請校系的 { 此校系之學系特色、此校系所需學科意涵、此校系適合之從事工作 }，撰寫進入大學後的未來學習計畫及生活規劃，分別說明進入該大學校系前會做的學習銜接、入學後大一到大二的能力培養計畫、大三到大四學習規畫以及職涯規劃。"})
        messages.append({"role": "system","content": f"此校系之學系特色:{aimdepartment['學系特色']}"})
        messages.append({"role": "system","content": f"此校系所需學科意涵:{aimdepartment['學科意涵']}"})
        messages.append({"role": "system","content": f"此校系適合之從事工作:{aimdepartment['適合從事工作']}"})

    elif support == '高中學習歷程反思':
        messages.append({"role": "system","content": "高中學習歷程反思定義:請將最優異的經歷進行學習歷程反思、遇到過挑戰或困難的情況和克服方式、和大學科系相關經驗等進行彙整，說明高中學習歷程中的反思，可以提及高中各方面的成長及反思、自我認識與成長、學習困境及所做努力、自我的態度及行為轉變等，並從描述中展現學生具備 { 此校系所需多元能力、此校系所適合的性格特質 } 的人格特質與具備的能力。"})
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
    
    messages.append({"role": "user", "content": f'整合以上問答及提供的資訊，分成一到四段來生成{support}'})
    messages.append({"role": "user", "content": '輸出:{ 只需顯示內文 }'})


    for i in range(0,len(AI_quesntions)):
        # ans = input(f"\n{AI_quesntions[i]}\nAns{i+1}: ")
        ans = "0"
        if ans == "0":
            pass
        else:
            messages.append({"role": "assistant", "content": AI_quesntions[i]},)
            messages.append({"role": "user", "content": ans})

    print("===========================================================================================")
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",
        messages = messages,
        max_tokens = 3000,
        temperature = 0.6
    )
    end_time = time.time() 
    print(f"程式執行時間: {end_time - start_time} 秒")
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    # allsupport = ['多元表現綜整心得', '就讀動機','未來學習計畫及生活規劃','高中學習歷程反思']
    # allschoolname = [i['學校']+i['系所'] for i in database()]
    print(main('國立臺灣大學中國文學系','多元表現綜整心得'))

    # with open('result.csv', 'a', newline='',encoding='big5') as csvfile:   
    #     csv_writer = csv.DictWriter(csvfile, fieldnames = ["result"])
    #     # 寫入標題（字典的鍵）
    #     csv_writer.writeheader()
    #     for i in main('國立臺灣大學中國文學系','多元表現綜整心得'):
    #         csv_writer.writerow({"result":i})