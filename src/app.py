import streamlit as st
from utilities import format_and_get_response

st.set_page_config(layout="wide", page_title="Food KG + LLM")
st.title("Food QA")
st.write("Write your questions about food and our model will answer you!")

prompt = st.text_area("Prompt", height=200, key="prompt")
if prompt:
    with st.spinner("Generating response..."):
        kg_prompt, response = format_and_get_response(prompt)
    st.title("Prompt")
    st.write(kg_prompt)
    st.title("Response")
    st.write(response)
