from langchain_community.document_loaders import TextLoader,PyMuPDFLoader,DirectoryLoader,WebBaseLoader
# loader1=TextLoader("./data/read.txt",encoding="utf-8")
# loader2=PyMuPDFLoader("./data/FullHTML.pdf")
# loader3=DirectoryLoader(
#     path="data",
#     glob="*.pdf",
#     loader_cls=PyMuPDFLoader
# )

# docs1=loader1.load()
# docs2=loader2.load()
# docs3=loader3.lazy_load()
# print(docs1[0].page_content)
# print(docs1[0].metadata)
# print(docs2[1])
# for doc in docs3:
#     print(doc.page_content[:100])
path="https://www.flipkart.com/lloyd-2026-model-2-ton-3-star-split-inverter-ac/p/itm4aa424f34d8d1?pid=ACNHHG4MAG8RUDFG&lid=LSTACNHHG4MAG8RUDFGTBME3M&marketplace=FLIPKART&store=j9e%2Fabm%2Fc54&srno=b_1_1&otracker=browse&fm=organic&iid=en_DlzMbQ-nNoJzNTbM_QToMEdXH2KAm4SQLfHHPSzP4hwdnPJLI-_ttpwg7HHimNtW1nduvtCcgFL-p43dWNCDLaLuUiotv0ShVc-Y4iRzBa-gn8iKny2wEJ2g8Z7AmYER&ppt=browse&ppn=browse&ov_redirect=true"
loader=WebBaseLoader(path)
docs=loader.load()
print(docs)