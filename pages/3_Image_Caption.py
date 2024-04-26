# Take an image input and prompt for caption describing, poem, blog, or your own use

import streamlit as st
st.title("Image Caption")

import PIL.Image
import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-pro-vision")

# Use streamlit widgets an image file
uploaded_file = st.file_uploader("Upload an image and let's talk about it.", 
                                 type=["png", "jpg", "jpeg"])

tmp_file = ".streamlit/tmp.jpg"
if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    with open(tmp_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    st.image(tmp_file)
    img = PIL.Image.open(tmp_file)

    # Let the user enter a prompt
    if prompt := st.text_input("Prompt"):
        # Call gemini with the image along with your prompt instructions
        response = model.generate_content([prompt, img])
        st.write(response.text)