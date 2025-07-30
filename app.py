import streamlit as st
import pandas as pd
from datetime import date
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- BACKGROUND IMAGE SETUP ---
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- CALL BACKGROUND FUNCTION ---
set_background("background.jpeg")  # Make sure the image is in the same folder and renamed

# --- HEADER ---
st.image("background.jpeg", width=150)  # Logo at the top
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- PRELOADED PLAYER DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Arsenal"},
    {"Name": "Willy", "Position": "Defender", "Traits": "Aggressive, Reliable", "Ambition": "Become national team player"},
    {"Name": "Sammy", "Position": "Winger", "Traits": "Fast, Creative", "Ambition": "Play in Europe"},
    {"Name": "Branton", "Position": "Striker", "Traits": "Clinical, Agile", "Ambition": "Top scorer in Kenya"},
    {"Name": "Samson", "Position": "Midfielder", "Traits": "Hardworking, Calm", "Ambition": "Coach youth football"},
    {"Name": "Pasi", "Position": "Goalkeeper", "Traits": "Brave, Vocal", "Ambition": "Best GK in Africa"},
    {"Name": "Ole", "Position": "Defender", "Traits": "Disciplined, Powerful", "Ambition": "Play for Gor Mahia"},
    {"Name": "Byron", "Position": "Striker", "Traits": "Strong, Fearless", "Ambition": "Captain Wosh FC"},
    {"Name": "Munene", "Position": "Midfielder", "Traits": "Creative, Fast", "Ambition": "Represent Kenya"},
    {"Name": "Victor", "Position": "Winger", "Traits": "Skillful, Visionary", "Ambition": "Play in La Liga"},
    {"Name": "Mose", "Position": "Defender", "Traits": "Tactical, Brave", "Ambition": "Coach defenders"},
    {"Name": "Jamo", "Position": "Goalkeeper", "Traits": "Flexible, Aggressive", "Ambition": "Top youth GK"}
]

df = pd.DataFrame(players)

# --- DISPLAY PLAYER DATA ---
st.subheader("📋 Player Profiles")
st.dataframe(df, use_container_width=True)

# --- DATE ---
st.caption(f"📅 Last updated on: {date.today()}")


