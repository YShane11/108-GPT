import os
import openai
openai.api_key = f'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'

messages = []
while True:  
    messages.append({"role": "user", "content": input("me > ")})
    response = openai.ChatCompletion.create(
      model = "gpt-4",
      messages = messages,
      max_tokens = 100
    )
    ai_msg = response.choices[0].message.content.replace('\n','')
    messages.append({"role": "assistant", "content":ai_msg})
    print(f'ai > {ai_msg}')