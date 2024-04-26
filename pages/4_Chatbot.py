# See streaming example with OpenAI's ChatGPT
# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

import streamlit as st
st.title("Chatbot with Gemini")

import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-pro")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=st.session_state.messages)

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Message to Gemini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat=st.session_state.chat
        response = chat.send_message(prompt).text
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})