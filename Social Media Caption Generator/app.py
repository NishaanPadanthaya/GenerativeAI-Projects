from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def generate_caption(image):

    prompt = "Please generate a captivating social media caption for the uploaded picture that reflects its content, mood, and any relevant hashtags or mentions. The caption should be engaging and suitable for sharing on platforms like Instagram, Twitter, or Facebook."

    # Generate content based on the prompt and the uploaded image
    response = model.generate_content([prompt,image], stream=True)

    response.resolve()
    return response.text

def main():
    st.title("Social Media Caption Generator")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

        caption = generate_caption(image)
        st.write("Generated Social Media Caption: ")
        st.write(caption)

if __name__ == "__main__":
    main()

