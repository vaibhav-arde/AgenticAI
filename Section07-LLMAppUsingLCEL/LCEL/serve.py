from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
# from langserve.validation import chainBatchRequest
load_dotenv()


# chainBatchRequest.model_rebuild()  # ✅ Fix Pydantic v2 issue

groq_api_key=os.getenv("GROQ_API_KEY")

assert groq_api_key is not None, "GROQ_API_KEY not set"

try:
    model=ChatGroq(model="mixtral-8x7b-32768",groq_api_key=groq_api_key)
except Exception as e:
    raise RuntimeError(f"Failed to initialize Groq model: {e}")


# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser=StrOutputParser()

##create chain
chain=prompt_template|model|parser



## App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")

## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)


