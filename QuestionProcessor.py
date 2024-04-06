from fastapi import FastAPI, Body
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.post("/question")
def question(question: str = Body(...)):
    llm = Ollama(model="gemma:2b", base_url="http://ollama:11434")
    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class anckerman"),
        ("user", "{input}")
    ])

    chain = prompt | llm | output_parser

    response = chain.invoke({"input": f"{question}"})
    return (response)