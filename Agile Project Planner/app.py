from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def generate_caption(image, num_workers, num_days):

    prompt = f"Develop an Agile sprint project plan for building a web application or app .The output involves creating user stories for {num_workers} team members
      to complete within {num_days} days. Ensure that all  necessary technologies required for the application are covered in the user stories.
      Make the user stories informative and descriptive.Below each user story include the acceptence criteria, and maintain this throughout.
      Even assign user story points for each user story based on complexity"

    response = model.generate_content([prompt,image], stream=True)

    response.resolve()
    return response.text

def main():
    st.title("Agile Project Planner")

    st.sidebar.title("Project Details")
    num_workers = st.sidebar.number_input("Number of User stories ", min_value=1, value=10)
    num_days = st.sidebar.number_input("Deadline for Completion", min_value=1, value=7)

    uploaded_file = st.file_uploader("Upload a Design or Workflow", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

        caption = generate_caption(image, num_workers, num_days)
        st.write(" User Stories: ")
        st.write(caption)

if __name__ == "__main__":
    main()
