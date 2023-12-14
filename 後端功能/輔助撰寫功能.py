import openai
from dotenv import dotenv_values
import time
from pymongo import MongoClient

def database():
    myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")
    alldepartment = myclient.學系學群學類.學系

    department = []
    for i in alldepartment.find():
        department.append(i)

    return department

# def text, target_language='en'): # en
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

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

    messages = [{"role": "system","content": "語言:zh-Tw 目標客群:準備申請大學的高中生 工作:從學生的角度,輔助生成備審資料且文筆極佳的AI助手(字數大約1000字) 重點:內容須符合所提供資訊，不可憑空捏造事實 "}]
    messages.append({"role": "system","content": f"目標校系:{department}"})
    messages.append({"role": "system","content": f"多元綜整的定義:{AI_quesntions[0]}"})
    messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
    messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
    messages.append({"role": "system","content": f"學生的性格特質:很有自信"})
    
    messages.append({"role": "user", "content": f'整合以上問答及提供的資訊，分成一到四段來生成{support}'})
    messages.append({"role": "user", "content": '如提供學生的性格特質與校系適合的性格特質有雷同，可就此特質適當地多加描述'})
    messages.append({"role": "user", "content": '輸出:{ 只需顯示內文 }'})


    for i in range(1,len(AI_quesntions)):
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
        temperature = 0.8
    )
    end_time = time.time() 
    print(f"程式執行時間: {end_time - start_time} 秒")
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    # allsupport = ['多元表現綜整心得', '就讀動機','未來學習計畫及生活規劃','高中學習歷程反思']
    # allschoolname = [i['學校']+i['系所'] for i in database()]
    print(main('國立臺灣大學中國文學系','多元表現綜整心得'))
