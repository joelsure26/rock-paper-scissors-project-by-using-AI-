import streamlit as st
import random

st.set_page_config(page_title="AI Rock Paper Scissors")

st.title("✊🖐️✌️ AI Rock-Paper-Scissors Game")

choices = ["rock", "paper", "scissors"]

# Basic AI model using user history
if "history" not in st.session_state:
    st.session_state.history = []

def predict_next_move(history):
    if not history:
        return random.choice(choices)
    most_common = max(set(history), key=history.count)
    # AI tries to beat the most common move
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def determine_winner(user, ai):
    if user == ai:
        return "It's a draw!"
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        return "You win!"
    else:
        return "AI wins!"

user_choice = st.selectbox("Choose your move:", choices)
if st.button("Play"):
    ai_choice = predict_next_move(st.session_state.history)
    result = determine_winner(user_choice, ai_choice)

    st.session_state.history.append(user_choice)

    st.markdown(f"**You chose:** {user_choice}")
    st.markdown(f"**AI chose:** {ai_choice}")
    st.success(result)

st.markdown("---")
if st.button("Reset History"):
    st.session_state.history = []
    st.info("History reset. AI will guess randomly again.")