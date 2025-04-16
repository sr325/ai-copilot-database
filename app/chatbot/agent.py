# app/chatbot/agent.py

from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langsmith import Client
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks.manager import CallbackManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_agent_executor():
    # Initialize LangSmith client
    client = Client()
    
    # Create callback manager with LangSmith tracer
    callback_manager = CallbackManager([LangChainTracer()])
    
    db_path = os.path.abspath("finance.db")  # same path
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
    
    llm = ChatOllama(
        model="llama3",
        system_prompt="""You are a financial data analyst. When counting records or performing aggregations:
        1. Always use COUNT(*) for total counts
        2. Do not apply any filters unless explicitly requested
        3. Return the exact number without any additional text
        4. For account counts, use: SELECT COUNT(*) FROM accounts""",
        callback_manager=callback_manager
    )

    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        callback_manager=callback_manager
    )
    return agent_executor