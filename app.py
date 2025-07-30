import streamlit as st
import pyttsx3
from datetime import date
import pandas as pd

# --- Streamlit Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Voice Assistant Function ---
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# --- Speak Welcome Message ---
speak_text("Welcome to Wosh FC Analyzer. From the streets to the stars.")

# --- App Title and Tagline ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- Player Data ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Barcelona"},
    {"Name": "Willy", "Position": "Defender", "Traits": "Strong, Reliable", "Ambition": "Captain Kenya National Team"},
    {"Name": "Sammy", "Position": "Striker", "Traits": "Quick, Sharp", "Ambition": "Top scorer in Europe"},
    {"Name": "Branton", "Position": "Goalkeeper", "Traits": "Agile, Brave", "Ambition": "Play in the Premier League"},
    {"Name": "Samson", "Position": "Winger", "Traits": "Fast, Creative", "Ambition": "Become a global star"},
    {"Name": "Pasi", "Position": "Midfielder", "Traits": "Tactical, Calm", "Ambition": "Coach youth players"},
    {"Name": "Ole", "Position": "Defender", "Traits": "Disciplined, Tall", "Ambition": "Study in Europe"},
    {"Name": "Byron", "Position": "Forward", "Traits": "Skillful, Focused", "Ambition": "Play for PSG"},
    {"Name": "Munene", "Position": "Utility", "Traits": "Flexible, Hard-working", "Ambition": "Be a mentor"},
    {"Name": "Victor", "Position": "Striker", "Traits": "Accurate, Powerful", "Ambition": "Be the best"},
    {"Name": "Mose", "Position": "Defender", "Traits": "Smart, Brave", "Ambition": "Join Kenya Police FC"},
    {"Name": "Jamo", "Position": "Winger", "Traits": "Energetic, Determined", "Ambition": "Get a scholarship"}
]

df = pd.DataFrame(players)

# --- Display Data ---
st.subheader("🌟 Player Profiles")
st.dataframe(df, use_container_width=True)

# --- Voice Feedback Button ---
if st.button("🔊 Say All Player Names"):
    names = ", ".join(player["Name"] for player in players)
    speak_text(f"The players are: {names}")
