# Here's the absolute minimal page for a streamlit app that calls Gemini.

import streamlit as st
st.title("Minimal Setup")

# You can copy & paste the results for "Get Code" below
# Make sure you enter your GOOGLE_API_KEY
# Any output that you want displayed to the webpage should call st.write("YOUR TEXT")

import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("Write a story about a boy and a backpack.")
st.write(response.text)