from langchain_community.document_loaders import TextLoader, CSVLoader, JSONLoader, DirectoryLoader
import os
cwd=os.getcwd()

# Function to process and print documents
def print_documents(documents, loader_name):
    print(f"\n--- Documents from {loader_name} ---\n")
    for document in documents:
        print("Metadata:", document.metadata)
        print("Content:", document.page_content)
        print("-" * 50)  # Separator for clarity
    print(f"Total number of documents loaded: {len(documents)}\n")

# TextLoader
loader=TextLoader("D:/LLM_Training/18122024/sample.txt")
docs_text=loader.load()
#print(docs)
#print (type(docs))
#print(len(docs))

# for doc in docs:
#     #print(doc)
#     #print(type(doc))
#     print(doc.page_content)
print_documents(docs_text, "TextLoader")

# CSVLoader
# loader_csv = CSVLoader(file_path="D:/LLM_Training/18122024/data.csv")
loader_csv = CSVLoader(file_path="D:/LLM_Training/18122024/data.csv", source_column="Age")
documents = loader_csv.load()
# print(documents)
# for document in documents:
#     content = document.page_content
#     metadata = document.metadata
 
#     print("Metadata:", metadata)
#     print("Content:", content)
#     print("-" * 50)  # Separator for clarity
print_documents(documents, "CSVLoader")

# JSONLoader
loader_json = JSONLoader(
    file_path='example.json',
    jq_schema='map({ name, email })',
    text_content=False)
data_json = loader_json.load()
#print(data_json)

# Print each document's content and metadata
# for document in data_json:
#     print("Metadata:", document.metadata)
#     print("Content:", document.page_content)
#     print("-" * 50)
print_documents(data_json, "JSONLoader")

# DirectoryLoader - It loads all the documents in a directory, it uses UnstructuredLoader under the hood, by default.

loader_dir = DirectoryLoader(path=cwd, glob="*.txt")
docs_dir = loader_dir.load()
#len(docs_dir)
print_documents(docs_dir, "DirectoryLoader")

# Print the total number of documents loaded
# print(f"Total number of documents loaded: {len(docs)}")

# # Print content for verification
# for doc in docs_dir[:3]:  # Print first 3 documents for validation
#     print("Metadata:", doc.metadata)
#     print("Content:", doc.page_content)
#     print("-" * 50)