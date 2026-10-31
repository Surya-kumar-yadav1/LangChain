from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(
    collection_name="Mydata",
    persist_directory="./Databs",
    embedding_function=embedding
)
docs=[
    Document(
        page_content="Python is a programming language.",
        metadata={"topic":"programming"}
    ),
    Document(
        page_content="Java is an object-oriented language.",
        metadata={"topic": "programming"}
    ),
    Document(
        page_content="Machine learning learns patterns from data",
        metadata={"topic": "AI"}
    )
]

vector_store.add_documents(docs)

results=vector_store.similarity_search("What is machine learning?",k=1)

print(results.page_content,results.metadata)