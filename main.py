import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I'm TRBINH! I am Python programer, teacher, and founder of Python Home. I have worked companies from
    various countries, such as Center
    """
    st.info(content)