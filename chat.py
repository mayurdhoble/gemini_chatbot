import streamlit as st
import os
import pathlib
import textwrap

st.sidebar.write("If you dont have API key get from here : https://aistudio.google.com/app/apikey ")
from IPython.display import display
from IPython.display import Markdown
api_key=st.sidebar.text_input("Enter your Gemini API Key:",type="password")
import os


import google.generativeai as genai
genai.configure(api_key=api_key)
model_name = st.sidebar.selectbox("Select Model", ["gemini-pro",'gemini-1.5-pro','gemini-1.5-flash','gemini-pro-vision'])
## Function to load OpenAI model and get respones
model = genai.GenerativeModel(model_name=model_name)
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

#st.set_page_config(page_title="CONVERSATIONAL BOT ")

st.header("Gemini AI LLM ")

input=st.text_input("Input: ",key="input")


submit=st.button("Answer to your question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)