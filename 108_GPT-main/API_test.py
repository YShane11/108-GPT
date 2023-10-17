import openai
from dotenv import dotenv_values

config=dotenv_values('.env')
openai.api_key =config['api_key']

res=openai.Completion.create(
    model='text-davinci-003',
    prompt='給我一個冷笑話',
    max_tokens=200
)

print(res['choices'][0]['text'])