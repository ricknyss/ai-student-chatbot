import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# App title
st.title("AI Student Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Display AI message
    with st.chat_message("assistant"):
        st.write(reply)

    # Save AI message
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })