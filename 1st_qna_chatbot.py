from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile")

st.title("🎉Ask Anything I am here to help you ! 😎")
st.markdown("I am a GenAI chatbot built using LangChain and Groq's LLM. Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

for messages in st.session_state.messages:
    role = messages["role"]
    content = messages["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask me anything!")

# if query:
#     st.session_state.messages.append({"role": "user", "content": query})
#     st.chat_message("user").markdown(query)
#     res = llm.invoke(query)
#     st.chat_message("ai").markdown(res.content)
#     st.session_state.messages.append({"role":"ai","content":res.content})


if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user","content": query})
    st.session_state.history.append(HumanMessage(content=query))
    res = llm.invoke(st.session_state.history)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role": "ai","content": res.content})
    st.session_state.history.append(AIMessage(content=res.content))
