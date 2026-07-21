import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get("selected_groq_model")

            print("API KEY:", groq_api_key)
            print("MODEL:", selected_groq_model)

            if not groq_api_key:
                st.error("Please Enter Groq API KEY")
                return None

            llm = ChatGroq(
                api_key=groq_api_key,
                model=selected_groq_model
            )

            print("LLM created successfully")

            return llm

        except Exception as e:
            st.exception(e)
            return None