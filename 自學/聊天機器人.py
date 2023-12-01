import os
import openai
import time
from dotenv import dotenv_values
openai.api_key = f'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'
config = dotenv_values("C:/Users/YShane11/OneDrive/桌面/env.txt")
openai.api_key = config["API_KEY"]

messages = []
while True:  
    messages.append({"role": "user", "content": input("me > ")})
    start_time = time.time()
    response = openai.ChatCompletion.create(
      model = "gpt-4",
      messages = messages,
      max_tokens = 200
    )
    ai_msg = response.choices[0].message.content.replace('\n','')
    messages.append({"role": "assistant", "content":ai_msg})
    end_time = time.time() 
    print(f"程式執行時間: {end_time - start_time} 秒")
    print(f'ai > {ai_msg}')