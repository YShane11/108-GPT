from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/execute', methods=['POST'])
def execute():
    config = dotenv_values("C:/Users/YShane11/env.txt")
    openai.api_key = config["API_KEY"]
    input_text = request.form['input']
    print(f'執行的內容是：{input_text}')

    messages = [
        {"role": "system", "content": "你是一個AI文字美化機器人"},
        {"role": "system", "content": "只需根據使用者輸入美化文字再輸出"},
        {"role": "system","content": "範例輸入:我好帥 輸出:我的魅力無疑是無人能擋"},    
        {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=4096,
        temperature=0.5
    )

    generated_text = response['choices'][0]['message']['content']
    return render_template("home.html", input=input_text, output=generated_text)

if __name__ == "__main__":
    app.run()
