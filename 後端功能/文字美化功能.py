import openai
from dotenv import dotenv_values
import gradio as gr
from pymongo import MongoClient



def database():
    myclient = MongoClient("mongodb+srv://YShane11:a44993386@school.hd1nbkk.mongodb.net/")
    alldepartment = myclient.學系學群學類.學系

    department = []
    for i in alldepartment.find():
        department.append(i)
    return department

def main(department, text):
    config = dotenv_values("C:/Users/YShane11/env.txt")
    openai.api_key = config["API_KEY"]  

    allschooldata= database()
    for i in allschooldata:
        if i['學校']+i['系所'] == department:
            aimdepartment = i
            break

    messages = [{"role": "system","content": "你是一個AI文字美化機器人,只需根據使用者輸入美化文字再輸出"},                                
                {"role": "user","content": f"{department}所適合的性格特質:{aimdepartment['性格特質']}"},
                {"role": "user", "content": f'如內容與「{department}適合的性格特質」有雷同的特質，可就此特質適當地多加描述'},        
                {"role": "user", "content": '不要過度誇示'},        
                {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(
        model = "gpt-4-0125-preview",
        messages = messages,
        max_tokens = 4096,
        temperature = 0.9
    )

    return response['choices'][0]['message']['content'] 


if __name__ == "__main__":
    print(main("國立臺灣大學中國文學系","我很聰明"))