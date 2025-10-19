from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Prompt UI - Research Tool")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = st.text_input("Enter your prompt:")

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.write(response.content)