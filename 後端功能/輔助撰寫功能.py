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

    messages = [{"role": "system","content": "目標客群:準備申請大學的高中生 工作:從學生的角度，輔助生成備審資料且文筆極佳的AI助手"}]
    messages.append({"role": "system","content": f"目標校系:{department}"})

    if support == '多元表現綜整心得':
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
        messages.append({"role": "system","content": '''
                        多元表現綜整心得的定義：
                        - 目的：展示學生的個人多樣性和全面發展。
                        - 內容：經歷過的自主學習、參與社團、擔任幹部、服務學習、競賽成果、非課程學習成果、證書、特殊表現等。
                        - 要求：說明這些經驗如何促進個人成長，並展現學生符合特定學系要求的多元能力和適合性格特質。
                         '''})
    
    elif support == '就讀動機':
        messages.append({"role": "system","content": f"此校系之學系特色:{aimdepartment['學系特色']}"})
        messages.append({"role": "system","content": f"此校系所需學科意涵:{aimdepartment['學科意涵']}"})
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
        messages.append({"role": "system","content": '''
                        就讀動機的簡化定義：
                        - 目的：闡述學生選擇該學系的動機和對該學系的瞭解。
                        - 內容：結合個人動機、學系特色、學科意涵和多元能力需求，以及適合的性格特質。
                        - 表達：展示學生對該學系的熱情和適合就讀的理由。
                         '''})
        
    elif support == '未來學習計畫及生活規劃':
        messages.append({"role": "system","content": f"此校系之學系特色:{aimdepartment['學系特色']}"})
        messages.append({"role": "system","content": f"此校系所需學科意涵:{aimdepartment['學科意涵']}"})
        messages.append({"role": "system","content": f"此校系適合之從事工作:{aimdepartment['適合從事工作']}"})
        messages.append({"role": "system","content": '''
                        未來學習計畫及生活規劃的簡化定義：
                        - 目的：規劃大學生涯和職業生涯的藍圖。
                        - 步驟：包含學習銜接準備、大一到大二的能力培養、大三到大四的學習規劃和職涯發展。
                        - 針對：具體結合該學系特色、學科要求和職業方向。
                         '''})

    elif support == '高中學習歷程反思':
        messages.append({"role": "system","content": f"此校系所需多元能力:{aimdepartment['多元能力']}"})
        messages.append({"role": "system","content": f"此校系所適合的性格特質:{aimdepartment['性格特質']}"})
        messages.append({"role": "system","content": '''
                        高中學習歷程反思的簡化定義：
                        - 目的：回顧和反思高中階段的學習和經歷。
                        - 內容：包括學生的優異表現、遇到挑戰、克服困難和與大學科系相關經驗。
                        - 重點：從中展示學生的成長、自我認知提升、學習努力和態度變化，並突出學生具備的多元能力和性格特質。
                         '''})
    
    for i in range(0,len(AI_quesntions)):
        # ans = input(f"\n{AI_quesntions[i]}\nAns{i+1}: ")
        ans = "0"
        if ans == "0":
            messages.append({"role": "assistant", "content": AI_quesntions[i]},)
            messages.append({"role": "user", "content": '無'})
        else:
            messages.append({"role": "assistant", "content": AI_quesntions[i]},)
            messages.append({"role": "user", "content": ans})

    messages.append({"role": "user", "content": f'''
                        目的:整合以上問答，分成一到四段來生成{support}

                        注意:
                        1.內容須先根據問答充分了解學生，再去根據學生資料生成、
                        2.文筆需接近高中生所寫，不要過度誇示
                        3.不要提及未做過的東西
                     '''})
    messages.append({"role": "user", "content": '語言:zh-Tw'})
    messages.append({"role": "user", "content": '輸出:{ 只需顯示內文 }'})



    print("===========================================================================================")
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model = "gpt-4-0125-preview",
        messages = messages,
        max_tokens = 3000,
        temperature = 0.8,
        n=3
    )
    end_time = time.time() 
    print(f"程式執行時間: {end_time - start_time} 秒")
    # return response['choices'][0]['message']['content']
    return [i['message']['content'] for i in response['choices']]

if __name__ == "__main__":
    # allsupport = ['多元表現綜整心得', '就讀動機','未來學習計畫及生活規劃','高中學習歷程反思']
    # allschoolname = [i['學校']+i['系所'] for i in database()]
    for i in main('國立臺灣大學中國文學系','多元表現綜整心得'):
        print(i)
        print("===========================================================================================")
