from openai import OpenAI
import streamlit as st
client=OpenAI()


st.title("Material generation by AI")
topic=st.text_input("enter your topic")
if topic is not None:
    btn=st.button("submit")
    if btn:
        response=client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"system","content":"you are exper with 20 years experience in physics , you can craft and write anything in physics like a pro author"},
                {"role":"user","content":f"write an 5 page study material in with required headings, sub headings  {topic}"}
            ]
        )

        st.write(response.choices[0].message.content)