# Basic free form text prompt

import streamlit as st

import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Let the user enter a prompt
if prompt := st.text_input("Prompt"):
    response = model.generate_content(prompt)
    st.write(response.text)