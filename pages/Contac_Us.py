import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
      user_emails = st.text_input("Your email address")
      message = st.text_area("Your message")
      button_submit = st.form_submit_button("Submit")
      if button_submit:
            print("Press button submit")
            print(button_submit)