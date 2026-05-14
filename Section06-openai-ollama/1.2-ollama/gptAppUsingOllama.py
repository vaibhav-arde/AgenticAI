import os
from dotenv import load_dotenv

from langchain_ollama.llms import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Gemma Chat", page_icon="🤖", layout="wide")

# Custom CSS for ChatGPT-like appearance
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* Centering and widening the chat input relative to the main content area */
    div[data-testid="stChatInput"] {
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.title("🤖 Chat Settings")
    model_name = st.selectbox(
        "Choose Model",
        ["gemma4:31b-cloud", "llama3", "mistral"],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("Gemma AI Assistant")
st.caption("Powered by LangChain & Ollama")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question:{question}")
])

# Initialize LLM
llm = OllamaLLM(model=model_name, temperature=temperature)
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

# Chat input
if prompt := st.chat_input("What is on your mind?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Streaming response
        try:
            for chunk in llm.stream(prompt):
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error generating response: {e}")
            full_response = "Sorry, I encountered an error."
            response_placeholder.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})


