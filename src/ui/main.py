import streamlit as st
import requests

st.title("Customer Support Assistant")

query = st.text_input("Ask a question")

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/query",
        json={
            "session_id": "1",
            "query": query
        }
    )

    st.json(response.json())