from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
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

prompt_template = PromptTemplate(
    template="""Summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}
        Explanation Length: {length_input}
        1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
        2. Analogies:
            - Use relatable analogies to simplify complex ideas.
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
        Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
    input_variables=["paper_input", "style_input", "length_input"]
)

prompt = prompt_template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.write(response.content)