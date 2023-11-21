import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "9aff1bb5acd3758f8847bcfcfb956b30d1c5a58c2c0dad1f0113d2084b44f0a3"

from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")
print(output)

output = conversation.predict(input="I am doing well! Currently, just have a conversation with you, an AI")
print(output)
