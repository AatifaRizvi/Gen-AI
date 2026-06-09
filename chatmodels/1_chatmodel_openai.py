from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0.9)

# temperature is a parameter that controls the randomness of a language model’s output. It affects how creative or deterministic the responses are.

# Lower values (0.0 – 0.3) → More deterministic and predictable.
# Higher values (0.7 – 1.5) → More random, creative, and diverse.
# Range (0.0 – 2.0)

result = llm.invoke("What is the capital of India?")
#  print(result)
print(result.content)