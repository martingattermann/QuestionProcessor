from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Question(BaseModel):
    message: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.post("/question")
def question(question:Question):
    llm = Ollama(model="gemma")
    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class comdidian"),
        ("user", "{input}")
    ])

    chain = prompt | llm | output_parser

    response = chain.invoke({"input": f"{question.message}"})
    return (response)