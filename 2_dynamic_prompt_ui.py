from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Prompt UI - Research Tool")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

paper_input =st.selectbox("Select a Research Paper", 
                          [ "Attention is all you need", 
                            "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",  
                            "GPT-3: Language Models are Few-shot Learners",
                            "Diffusion Models Beat GANs on Image Synthesis",
                            "ReAct: Synergizing Reasoning and Acting in Language Models",]
                        )

style_input = st.selectbox("Select an Explanation Style", 
                          ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select a Length", 
                          ["Short (1 - 2 paragraphs)", "Medium (3 - 5 paragraphs)", "Long (detailes explained)"])

prompt_template = load_prompt("template.json")

prompt = prompt_template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.write(response.content)