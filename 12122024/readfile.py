from openai import OpenAI
from pydantic import BaseModel
import io 
import sys
client=OpenAI()

class employee(BaseModel):
    name: str
    email: str 
    empId: str 
    query: str


with io.open("data.txt", "r", encoding="latin-1", errors="replace") as f1:
    data=f1.read()
    f1.close()

lines=data.split("\n")
print(len(lines))
with io.open("output.csv","w",encoding="utf-8") as f1:
    for line in lines[:50]:
        # response=client.chat.completions.create(
        #     model="gpt-4o",
        #     messages=[
        #         {"role":"system","content":"you are an expert assistant at structured data extraction ,you will be given unstructed text line for that you have to extracxt username,email,employeeid and user query , if something is missing make it NA"},
        #         {"role":"user","content":line}
        #     ]
        # )
        # print(response)
        # sys.exit()

        response=client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"you are an expert assistant at structured data extraction ,you will be given unstructed text line for that you have to extracxt username,email,employeeid and user query , if something is missing make it NA"},
                {"role":"user","content":line}
            ],
            response_format=employee
        )
        name=response.choices[0].message.parsed.name
        email=response.choices[0].message.parsed.email
        empid=response.choices[0].message.parsed.empId
        query=response.choices[0].message.parsed.query
        f1.write(name+","+email+","+empid+","+query+"\n")
f1.close()