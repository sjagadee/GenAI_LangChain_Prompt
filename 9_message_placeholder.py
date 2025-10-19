from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []

#load chat history from file
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({"domain": "Customer Support", "chat_history": chat_history, "query": "Where is my refund!!"})

print(prompt)