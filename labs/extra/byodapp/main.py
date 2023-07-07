import os

# Import Azure OpenAI Related Libraries
import tiktoken
from langchain.llms import AzureOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

# Import dotenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Azure OpenAI API
openai_api_type = os.getenv("OPENAI_TYPE")
openai_api_version = os.getenv("OPENAI_VERSION")
openai_api_base = os.getenv("OPENAI_API_BASE")
openai_api_key = os.getenv("OPENAI_API_KEY")
COMPLETION_DEPLOYMENT = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
encoding = tiktoken.get_encoding('cl100k_base')

# Load Documents
loader = TextLoader('custommovie.md')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Create Embeddings for loaded documents.
embeddings = OpenAIEmbeddings(
    openai_api_type = openai_api_type,
    openai_api_version = openai_api_version,
    openai_api_base = openai_api_base,
    openai_api_key = openai_api_key,
    deployment = EMBEDDING_DEPLOYMENT
)

# Create an instance of Azure OpenAI
llm = AzureOpenAI(
    openai_api_type = openai_api_type,
    openai_api_version = openai_api_version,
    openai_api_base = openai_api_base,
    openai_api_key = openai_api_key,
    deployment_name = COMPLETION_DEPLOYMENT,
    temperature = 0
)

# Create Vector Store of document embeddings in memory.
qdrant = Qdrant.from_documents(
    docs,
    embeddings,
    location=":memory:",  # Local mode with in-memory storage only
    collection_name="my_movies",
)

# Start the App
app = FastAPI()

class Question(BaseModel):
    question: str
    max_tokens: int

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/modelandprompt/")
async def execute_completion(input: Question):
    prompt_template = """
{question}
If there are no movies that meet the criteria, return 'No movies found', don't try to make up an answer.
The list is a maximum of 3 results and only return the movie title.
Only include the movie if the release date is in the year 2023.

Take a step-by-step approach in your response, cite sources and give reasoning before sharing final answer.

Movie List:
"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["question"]
    )

    # Create a chain
    chain = LLMChain(llm=llm, prompt=PROMPT)
    response = chain.run(input.question)
    return {"response": response}


@app.post("/modelanddatainprompt/")
async def execute_completion(input: Question):
    prompt_template = """
Use the following pieces of context to answer the question at the end.
If there are no movies that meet the criteria, return 'No movies found', don't try to make up an answer.
The list is a maximum of 3 results and only return the movie title.
Only include the movie if the release date is in the year 2023.

---
# Title: EMEA GBBs

## Overview

 The untold story of EMEA App Innovation GBBs who help customers build really cool Intelligent App solutions on top of Azure. Starring Mark, Steve, Yasmin, Rita, Mohammad, Mohamed, Dennis, Robin-Manuel, Kosta, Gustav, Roy and Kevin.

## Details

**Release Date:** 2023-07-01

**Genres:** Action, Thriller

**Popularity:** 199.999

**Vote Average:** 9.9

**Keywords:** GBB, Intelligent Apps
---

Question: {question}

Take a step-by-step approach in your response, cite sources and give reasoning before sharing final answer.

Movie List:
"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["question"]
    )

    # Create a chain
    chain = LLMChain(llm=llm, prompt=PROMPT)
    response = chain.run(input.question)
    return {"response": response}


@app.post("/modelanddatainvectordb/")
async def execute_completion(input: Question):
    prompt_template = """
    Use the following pieces of context to answer the question at the end.
    If there are no movies that meet the criteria, return 'No movies found', don't try to make up an answer.
    The list is a maximum of 3 results and only return the movie title.
    Only include the movie if the release date is in the year 2023.

    ---
    {context}
    ---

    Question: {question}

    Take a step-by-step approach in your response, cite sources and give reasoning before sharing final answer.

    Movie List:
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    # Expose Vector Store as a Langchain Retriever
    retriever = qdrant.as_retriever()
    # Create chain
    chain_type_kwargs = {"prompt": PROMPT}
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs=chain_type_kwargs
    )
    response = qa.run(input.question)
    return {"response": response}
