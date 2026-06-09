from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatAnthropic(model="claude-2", temperature=0.9)

result = llm.invoke("What is the capital of India?")

print(result.content)
