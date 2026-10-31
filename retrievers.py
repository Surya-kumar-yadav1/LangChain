from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(
    collection_name="Mydata",
    embedding_function=embedding
)
vector_store.add_documents(documents)
retriever=vector_store.as_retriever(search_type="mmr",kwargs={"k":2,"lambda_mul":0.5})
results=retriever.invoke("What is chroma?")
# results=vector_store.similarity_search("guya?",k=2)

for result in results:
    print(result.page_content)