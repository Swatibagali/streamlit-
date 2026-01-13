import streamlit as st
import google.generativeai as genai

st.title("Welcome to My Streamlit AI")
user_input = st.text_area("Enter your text here for simulation:  ")
genai.configure(api_key ="AIzaSyDpO6vCSyfWTkIXRKyb7NV7gvcwtou8PS0")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)

    st.write("AI Response:",response.text)