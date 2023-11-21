import openai
from dotenv import dotenv_values
import time

with open("AI.txt", "r", encoding = "utf-8") as file:
    AI_quesntions = [line.strip() for line in file.readlines()]
    file.close()

def generate_text(department="人工智慧系",support="撰寫學習歷程",ans_1="因為我想要AI機器人陪我聊天"):
    config = dotenv_values("env.txt")
    openai.api_key = config["API_KEY"]

    a_1 = input("\n"+AI_quesntions[0]+"\nAns1: ") # 因為我想要AI機器人陪我聊天
    a_2 = input("\n"+AI_quesntions[5]+"\nAns2: ") # 我認為它會成為未來的主要趨勢，並取代大部分工作
    narration = f'''
        目標學系: {department}
        輔助項目: {support}
        =====================================
        問題1:{AI_quesntions[0]}
        Ans:{a_1}

        問題2:{AI_quesntions[5]}
        Ans:{a_2}
        =====================================
        根據以上問答及提供的學系資料，完成我要求的輔助項目
    '''

    start_time = time.time()
    #======================================================================================================
    messages = [
        {"role": "system", "content": "你是一個專門幫學生撰寫學習歷程的AI小助手"},
        {"role": "user", "content": narration}
    ]

    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 1000
    )
    #======================================================================================================

    end_time = time.time()  # 記錄結束時間
    print(f"程式執行時間: {end_time - start_time} 秒")

    return response['choices'][0]['message']['content']


print(generate_text())

# 生成文字字數
# 可使用token數(考慮到未來花費)  https://openai.com/pricing  https://platform.openai.com/tokenizer
# 資料庫方面連接多少內容
# 題目如何設計
