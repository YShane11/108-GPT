import openai
from dotenv import dotenv_values
import time


support = '多元表現綜整心得'
department = "人工智慧系"

def generate_text(department, support):

    with open(f"Question/{support}.txt", "r", encoding = "utf-8") as file:
        AI_quesntions = [line.strip() for line in file.readlines()]

    config = dotenv_values("C:/Users/YShane11/OneDrive/桌面/env.txt")
    openai.api_key = config["API_KEY"]

    messages = [{
        "role": "system", 
        "content": "語言:zh-Tw 目標客群:準備申請大學的高中生 工作:從學生的角度,輔助生成備審資料的的AI助手(字數大約1000字) 要求:盡量符合真實性、不回覆沒意義的話"
        }]

    for i in range(len(AI_quesntions)):
        # ans = input(f"/n{AI_quesntions[i]}/nAns{i+1}: ")
        ans = "0"
        if ans == "0":
            pass
        else:
            messages.append({"role": "assistant", "content": AI_quesntions[i]},)
            messages.append({"role": "user", "content": ans})


    narration = f'''
        目標學系: {department}
        =====================================
        整合以上問答及提供的學系，生成{support}
    '''
    messages.append({"role": "user", "content": narration})

    print("===========================================================================================")
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",
        messages = messages,
        max_tokens = 2000,
        temperature = 1.3
    )
    end_time = time.time() 
    print(f"程式執行時間: {end_time - start_time} 秒")
    return response['choices'][0]['message']['content']


print(generate_text(department, support))
