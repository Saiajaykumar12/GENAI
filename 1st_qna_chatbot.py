from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile")

st.title("🎉Ask Anything I am here to help you ! 😎")
st.markdown("I am a GenAI chatbot built using LangChain and Groq's LLM. Ask me anything!")

query = st.chat_input("Ask me anything!")

if query:
    print(query)
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)

