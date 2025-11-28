import requests
import streamlit as st


def get_groq_response(input_text, language):
    # If no language passed or empty -> default Marathi
    if not language:
        language = "Marathi"

    print("input_text from function", input_text)
    print("language from function", language)

    json_body = {
        "input": {
            "language": language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
    res = response.json()
    print(res)

    return res.get("output")


# Streamlit app
st.title("LLM Application Using LCEL")

language = st.text_input("Choose your language to convert given text (Default = Marathi)")
input_text = st.text_input("Enter the text you want to convert to chosen language")

print("input_text", input_text)
print("language", language)

if input_text:
    st.write(get_groq_response(input_text, language))
