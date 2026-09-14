import streamlit as st

st.set_page_config(page_title="ASCEND")
st.title("ASCEND — Financial Compliance Agent")
st.write("Compliance question? Ask here.")

question = st.text_input("Your question")
if question:
    st.info("Not connected yet.")