from openai import OpenAI

client=OpenAI()

response=client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"you are a smart and helpful ai assistant"},
                {
                    "role":"user",
                    "content":"Todays MYR to INR Currency rate"
                }
            ]

        )

print(response)