import openai
from dotenv import dotenv_values
import gradio as gr


def generate_text(text):
    config = dotenv_values("env.txt")

    openai.api_key = config["API_KEY"]

    prompt = f"""
        搜尋以下文字產生2到6個顏色

        輸出格式: python列表,  列表的值是16禁制的顏色編碼
        
        ###
        google
        ###
        ['#4285F4', '#34A853', '#FBBC05', '#EA4335', '#FFD32F', '#7B74D2']

        ###
        {text}
        ###
      """

    res = openai.Completion.create(
                model = "text-davinci-003",
                prompt = prompt,
                max_tokens = 200)

    colors = res["choices"][0]["text"].replace('[','').replace(']','').replace("'",'').split(',')
    
    html = ""

    for i in colors:
        html += f"<div style='background-color:{i}'>{i}</div>"

    return html


demo =  gr.Interface(
        fn = generate_text,
        inputs="text",
        outputs="html",
        title="顏色產生器",
        description="輸入一段文字，產生2~6個顏色",
        allow_flagging="never",
)


demo.launch()