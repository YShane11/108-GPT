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
    config = dotenv_values("C:/Users/jason/.env.txt")
    openai.api_key = config["API_KEY"]  

    allschooldata= database()
    for i in allschooldata:
        if i['學校']+i['系所'] == department:
            aimdepartment = i
            break

    messages = [{"role": "system","content": "你是一個AI文字美化機器人"},
                {"role": "system","content": "只需根據使用者輸入美化文字再輸出"},                
                {"role": "system","content": "範例輸入:我好帥 輸出:我的魅力無疑是無人能擋"},     
                {"role": "system","content": f"{department}所適合的性格特質:{aimdepartment['性格特質']}"},
                {"role": "system","content": f"學生的性格特質:很有自信"},
                {"role": "user", "content": '如提供學生的性格特質與校系適合的性格特質有雷同，可就此特質適當地多加描述'},        
                {"role": "user", "content": text}]
    
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 4096,
        temperature = 0.5
    )

    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    print(main("國立臺灣大學中國文學系","我討厭你"))
    # demo = gr.Interface(fn=main, inputs="text", outputs="text",title="文字美化功能",description="輸入文字",allow_flagging="never",)

    # demo.launch()
