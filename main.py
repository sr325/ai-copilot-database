# main.py
import streamlit as st
from app.chatbot.agent import get_agent_executor

st.title("💰 AI Copilot Database")

query = st.text_input("Ask a question about your database")

if query:
    with st.spinner("Thinking..."):
        agent_executor = get_agent_executor()  # Lazy load
        result = agent_executor.run(query)  # Pass 'handle_parsing_errors' as a positional argument
        st.write(result)
