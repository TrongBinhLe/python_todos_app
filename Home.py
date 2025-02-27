import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1 ,empty_col, col2 = st.columns([1.8, 0.5, 1.8])

with col1:
    st.image("/Users/admin/Documents/Others/python-projects/TodoListApp/python_todos_app/images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I'm TRBINH! I am Python programer, teacher, and founder of Python Home. I have worked companies from
    various countries, such as the Center for Convervation Geography, to map and understand Australian ecosystem, image processing
    with the Swiss in Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """
    st.info(content)

content = "Below you can find some of the apps I have built in Python. Feel free contact me!"
st.write(content)

df = pandas.read_csv("data.csv",sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
       st.header(row["title"])
       st.write(row["description"])
       st.image(f'/Users/admin/Documents/Others/python-projects/TodoListApp/python_todos_app/images/{index + 1}.png')
       st.write(f'[Source code]({row["url"]})')
    
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f'/Users/admin/Documents/Others/python-projects/TodoListApp/python_todos_app/images/{index + 1}.png')
        st.write(f'[Source code]({row["url"]})')
