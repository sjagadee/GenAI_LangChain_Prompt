from langchain_core.prompts import ChatPromptTemplate

# in some places .from_mesages are not used - but it will work in that case as well
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} assistant."),
    ("human", "Explain in simple terms what is {topic}.")
])

prompt = chat_template.invoke({"domain": "mathematics", "topic": "complex numbers"})

print(prompt)