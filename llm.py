import os
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

## load the Groq API key
groq_api_key=os.environ['GROQ_API_KEY']

llm=ChatGroq(model="mixtral-8x7b-32768",temperature=0.0)
prompt="Can you provide me the code for the following comand using os:"
