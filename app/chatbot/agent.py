# app/chatbot/agent.py

from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
import os

def get_agent_executor():
    db_path = os.path.abspath("finance.db")  # same path
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    llm=ChatOllama(model="llama3",
                   system_prompt="You are a financial data analyst.")

    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    return agent_executor