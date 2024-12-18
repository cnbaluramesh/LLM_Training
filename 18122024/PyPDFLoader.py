from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader, OnlinePDFLoader
import onnx
print("ONNX version:", onnx.__version__)
loader = PyPDFLoader(r"D:\LLM_Training\18122024\pdf-sample.pdf")
pages_1 = loader.load()

#Each page is a Document. A Document contains text (page_content) and metadata.

len(pages_1)

"""22"""

page = pages_1[0]

#print(page.page_content[:500]) 

#print(page.page_content) 

print(f"Total pages loaded (PyPDFLoader): {len(pages_1)}")
print(pages_1[0].page_content[:500])  # Print first 500 characters


loader_un = UnstructuredPDFLoader(r"D:\LLM_Training\18122024\pdf-sample.pdf")
data = loader_un.load()

print(f"Total elements loaded (UnstructuredPDFLoader): {len(data)}")
print(data[0].page_content[:500])  # Print first 500 characters


loader_on = OnlinePDFLoader("https://arxiv.org/pdf/2302.03803.pdf")
data_on = loader_on.load()

print(f"Total elements loaded (OnlinePDFLoader): {len(data_on)}")
print(data_on[0].page_content[:500])  # Print first 500 characters