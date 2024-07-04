from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

#Configure the generative AI model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Load Gemini Pro model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(question):
    if input!=' ':
        response = chat.send_message(question, stream=True)
    else:
        response = chat.send_message(question)
    return response

st.set_page_config(page_title='Chatbot', layout='wide')
st.title('QA Chatbot')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input('Input:', key='input')
submit = st.button('Submit')

if submit and input:
    response = get_response(input)
    st.session_state['chat_history'].append(('User', input))
    st.subheader('Response:')

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot', chunk.text))

st.subheader('Chat history:')

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

# Sidebar
st.sidebar.header("About")
st.sidebar.info("This application uses Generative AI to answer questions. Enter your question in the input box and click 'Submit' to get a response.")
    

