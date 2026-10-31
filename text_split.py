from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter,TokenTextSplitter

text = """LangChain is a powerful framework for developing applications powered by language models.
It enables developers to chain together components like LLMs, prompts, and memory to create advanced conversational AI systems.
Text splitters in LangChain help break large documents into smaller pieces for processing."""

splitter=TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2
)

# splitter=RecursiveCharacterTextSplitter(
#     chunk_size=25,
#     chunk_overlap=3,
#     separators=["\n\n","\n"," ",""]
# )
chunks=splitter.split_text(text)
for doc in chunks:
    print(doc)
# splitter1=CharacterTextSplitter(
#     chunk_size=25,
#     chunk_overlap=3,
#     separator=" "
# )
# chunks1=splitter1.split_text(text)
# print(len(chunks1))
# print(chunks1)