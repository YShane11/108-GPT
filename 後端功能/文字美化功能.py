import openai
from dotenv import dotenv_values
import gradio as gr

config = dotenv_values("C:/Users/YShane11/env.txt")
openai.api_key = config["API_KEY"]


def main(text):
    messages = [{"role": "system","content": "你是一個AI文字美化機器人"},
                {"role": "system","content": "只需根據使用者輸入美化文字再輸出"},                
                # {"role": "system","content": "範例輸入:我好帥 輸出:我的魅力無疑是無人能擋"},                
                {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 4096,
        temperature = 0.5
    )

    return [i['message']['content'] for i in response['choices']]


if __name__ == "__main__":
    print(main("這歌曲真的很棒！好好聽，很多回憶在我和腦海裡出現"))
    # demo = gr.Interface(fn=main, inputs="text", outputs="text",title="文字美化功能",description="輸入文字",allow_flagging="never",)

    # demo.launch()
