from config import get_config
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import UpstashVectorStore
import pathlib
from langchain_core.documents import Document
from PyPDF2 import PdfReader
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate


config = get_config()


GOOGLE_API_KEY = config.GOOGLE_API_KEY 

UPSTASH_VECTOR_REST_TOKEN = config.UPSTASH_VECTOR_REST_TOKEN 

UPSTASH_VECTOR_REST_URL = config.UPSTASH_VECTOR_REST_URL


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

store = UpstashVectorStore(
    embedding = embeddings,
    index_url = UPSTASH_VECTOR_REST_URL ,
    index_token = UPSTASH_VECTOR_REST_TOKEN
)

LLM_CONFIG = {
    "model": "gemini-1.5-pro",
    "google_api_key": GOOGLE_API_KEY

}

retriever = store.as_retriever(
    search_type = "similarity",
    search_kwargs = {'k':4}
)




def get_result(question):

    llm = GoogleGenerativeAI(**LLM_CONFIG)

    message = '''
    Answer this question using the provided context only.

    {question}

    Context:
    {context}
    '''

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "if the user is greeting then respond to the greeting"),
            ("human", message)
        ]
    )

    parser = StrOutputParser()

    chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | parser

    result = chain.invoke(question)

    return result