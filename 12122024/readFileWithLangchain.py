from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from pydantic import BaseModel
import io

# Initialize the client with a corrected model name
# Replace 'llama2' with the model name accessible to you
client = ChatOpenAI(model="llama3.2")  # Correct the model name here

# Define the Employee data structure
class Employee(BaseModel):
    name: str
    email: str
    empId: str
    query: str

# Read input data
with io.open("data.txt", "r", encoding="latin-1", errors="replace") as f1:
    data = f1.read()

lines = data.split("\n")
print(f"Number of lines: {len(lines)}")

# Process data and write to output CSV
with io.open("output.csv", "w", encoding="utf-8") as f1:
    for idx, line in enumerate(lines[:50]):  # Process the first 50 lines
        # Prepare the message payload with LangChain schema types
        messages = [
            SystemMessage(
                content=(
                    "You are an expert assistant at structured data extraction. "
                    "You will be given an unstructured text line. Extract username, email, "
                    "employee ID, and user query. If something is missing, make it NA."
                )
            ),
            HumanMessage(content=line),
        ]

        # Get the response from the model using `invoke`
        try:
            response = client.invoke(messages)
            parsed_response = Employee.parse_raw(response.content)

            name = parsed_response.name or "NA"
            email = parsed_response.email or "NA"
            empId = parsed_response.empId or "NA"
            query = parsed_response.query or "NA"

            # Write to CSV
            f1.write(f"{name},{email},{empId},{query}\n")
        except Exception as e:
            print(f"Error processing line {idx + 1}: {line}\n{e}")
            continue

print("Processing complete. Output saved to output.csv")
