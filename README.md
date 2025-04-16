# AI Copilot Database: Natural Language Interface for Financial Data Analysis

## Introduction
The AI Copilot Database is an innovative application that bridges the gap between natural language and database queries. It allows users to interact with their financial database using plain English, making data analysis more accessible to non-technical users. Built with modern AI technologies and a user-friendly interface, this project demonstrates the power of combining large language models with traditional database systems.

## Technical Overview
The project is built using several cutting-edge technologies:
- **Streamlit**: For creating a beautiful, interactive web interface
- **LangChain**: For orchestrating the AI agent and tools
- **Ollama**: For running the local LLM (Llama 3)
- **SQLAlchemy**: For database operations
- **SQLite**: As the database backend

## How It Works
1. Users input their questions in natural language through the Streamlit interface
2. The application uses LangChain to create an SQL agent that:
   - Understands the user's intent
   - Converts natural language to SQL queries
   - Executes the queries against the financial database
   - Returns human-readable results
3. The system uses Llama 3 as the underlying language model, running locally through Ollama

## Technical Setup and Running
To run the project:

1. **Prerequisites**:
   - Python 3.x
   - Ollama installed and running locally
   - Llama 3 model downloaded in Ollama

2. **Installation**:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate 

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Running the Application**:
   ```bash
   streamlit run main.py
   ```

## Key Benefits
1. **Natural Language Interface**: Users can query financial data without knowing SQL
2. **Local Processing**: Uses local LLM through Ollama, ensuring data privacy
3. **Real-time Analysis**: Get instant insights from financial data
4. **User-friendly**: Clean, intuitive interface built with Streamlit
5. **Extensible**: Can be adapted to different types of databases and use cases

## Conclusion
The AI Copilot Database represents a significant step forward in making database interactions more accessible. By combining the power of large language models with traditional database systems, it opens up data analysis to a wider audience while maintaining the precision and reliability of SQL queries. The project's modular architecture and use of modern technologies make it both powerful and maintainable, with plenty of room for future enhancements.