import streamlit as st
from openai import OpenAI

# Title
st.title("🌊 Ocean Impact AI – Galveston Edition")
st.caption("Built by Devika Supriya Mohan | Inspired by Houston & Galveston Beach Cleanups")

st.write("Get personalized ways to reduce your ocean plastic footprint 🌎")

# User input
user_input = st.text_area(
    "Describe your lifestyle (e.g., diet, shopping habits, plastic use, location):"
)

# Button
if st.button("Generate My Ocean Impact Plan"):
    if user_input:
        client = OpenAI()

        prompt = f"""
        The user lives in or is connected to Houston, Texas and Galveston beaches.

        Their lifestyle: {user_input}

        Generate:
        1. 5 personalized ways to reduce ocean plastic pollution
        2. Tie at least 2 suggestions specifically to Houston/Galveston or Gulf Coast issues
        3. Estimate weekly plastic reduction (numbers make sense but can be approximate)
        4. Keep it practical and realistic for a student

        Keep tone concise and actionable.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("🌱 Your Personalized Ocean Plan")
        st.write(response.choices[0].message.content)