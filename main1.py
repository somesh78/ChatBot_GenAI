import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(ques):
    try:
        resp = model.generate_content(ques)
        return resp.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Error processing your request."

st.set_page_config(
    page_title="Gemini pro Q/A project",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Gemini Q/A app")

question = st.text_input("Ask a question: ")

if st.button("Submit"):
    with st.spinner("Processing your request..."):
        response = get_gemini_response(question)
    st.write("*User*:", question)
    st.write("*Bot*:", response)
