import streamlit as st
import os
import google.generativeai as genai
import json

st.title("🌊 Ocean Impact AI – Galveston Edition")
st.caption("Built by Devika Supriya Mohan | Inspired by Houston & Galveston Beach Cleanups")
st.write("Get personalized ways to reduce your ocean plastic footprint 🌎")

user_input = st.text_area(
    "Describe your lifestyle (e.g., diet, shopping habits, plastic use, location):"
)

if st.button("Generate My Ocean Impact Plan"):
    if user_input:
        # Initialize Gemini API
        # Make sure you uploaded your JSON key as a secret in Streamlit
        # and set environment variable GOOGLE_APPLICATION_CREDENTIALS
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        prompt = f"""
        The user lives in or is connected to Houston, Texas and Galveston beaches.
        Their lifestyle: {user_input}
        Generate:
        1. 5 personalized ways to reduce ocean plastic pollution
        2. Tie at least 2 suggestions specifically to Houston/Galveston or Gulf Coast issues
        3. Estimate weekly plastic reduction (numbers approximate)
        4. Keep it practical and realistic for a student
        """

        response = genai.chat.create(
            model="gemini-1.5-t",
            messages=[{"author": "user", "content": prompt}]
        )

        st.subheader("🌱 Your Personalized Ocean Plan")
        st.write(response.last.content)
