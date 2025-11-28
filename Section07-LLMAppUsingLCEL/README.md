# LangChain Translation App (LCEL)

This project is a simple web application that demonstrates the use of LangChain Expression Language (LCEL) to create a translation service. The application is composed of a FastAPI backend and a Streamlit frontend.

## Architecture

The application has two main components located in the `LCEL/` subdirectory:

1.  **Backend (`LCEL/serve.py`)**: A FastAPI server that exposes a translation endpoint using `langserve`. It hosts a LangChain chain that translates text into a specified language using the Groq API.

2.  **Frontend (`LCEL/client.py`)**: A Streamlit application that provides a simple UI for users to enter text for translation. It communicates with the FastAPI backend to get the translation and displays it.

## Setup Instructions

Follow these steps to set up and run the application.

### 1. Prerequisites

-   Python 3.8+
-   `pip` for package management

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment. From within this directory (`Section07-LLMAppUsingLCEL`), run:

```bash
python -m venv .venv
source .venv/bin/activate
```
*On Windows, use `.venv\Scripts\activate`*

### 3. Install Dependencies

Create a `requirements.txt` file in this directory with the content below.

**`requirements.txt`:**
```
fastapi
langchain-core
langchain-groq
langserve
uvicorn
python-dotenv
streamlit
requests
```

Then, install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

The application requires an API key from Groq.

1.  Create a file named `.env` in this directory (`Section07-LLMAppUsingLCEL`).
2.  Add your Groq API key to the `.env` file:

```
GROQ_API_KEY="your_groq_api_key_here"
```

You can get a free API key from the [Groq website](https://console.groq.com/keys).

## How to Run the Application

You need to run the backend server and the frontend application in two separate terminals. Make sure you are in the `Section07-LLMAppUsingLCEL` directory and have your virtual environment activated.

### 1. Start the Backend Server

In your first terminal, run the following command:

```bash
uvicorn LCEL.serve:app --reload
```

The backend server will start on `http://127.0.0.1:8000`.

### 2. Run the Frontend Application

In your second terminal, run the Streamlit app:

```bash
streamlit run LCEL/client.py
```

The Streamlit application will open in your web browser, usually at `http://localhost:8501`.

## How to Use the App

1.  Open the Streamlit app in your browser.
2.  Enter the text you want to translate in the input box.
3.  The application will automatically call the backend and display the translated text. The default translation language is Marathi, but the code can be modified to accept other languages.
