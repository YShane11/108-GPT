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
                {"role": "system","content": f"{department}所適合的性格特質:{aimdepartment['性格特質']}"},
                {"role": "system", "content": f'如內容與「{department}適合的性格特質」有雷同的特質，可就此特質適當地多加描述'},        
                {"role": "user", "content": '注意:不要過度誇示'},   
                {"role": "user", "content": '語言:zh-Tw'},
                {"role": "user", "content": '輸出:{ 修改後的輸出 }'},
                {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(
        model = "gpt-4-0125-preview",
        messages = messages,
        max_tokens = 4096,
        n=5,
        temperature = 0.9
    )

    return response['choices'][0]['message']['content'] 

if __name__ == "__main__":
    print(main("國立臺灣大學中國文學系",'''
 我覺得我滿喜歡跟別人打交道，也滿想了解他們的。不過，我不只是單單想了解，我也挺在乎怎麼應用這些知識的。所以，我對消費心理學之類的課程超有興趣。我聽說輔仁大學的心理學系挺出名的，對我這樣的高中生來說，蠻吸引人的。我想要在這方面專業技能和知識上有所提升，相信這所大學會有不錯的教授和課程能夠培養我。我喜歡了解別人，陪伴他們，關心他們，也許因為我自己也是需要被關心的。所以，我會盡力去理解別人，有耐心學習這種科學又人文的科系。
               '''))
    

