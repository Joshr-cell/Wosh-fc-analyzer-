import streamlit as st
import pandas as pd
import pyttsx3
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- VOICE ASSISTANT SETUP ---
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- SET BACKGROUND IMAGE ---
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpeg")  # ✅ Make sure this file exists in the same folder

# --- HEADER WITH LOGO ---
st.image("background.jpeg", width=100)  # You can replace with a logo if different
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- SAMPLE PLAYER DATA ---
player_data = [
    {"Name": "Ian", "Position": "Midfielder", "Goals": 3, "Assists": 2, "Speed": 7},
    {"Name": "Willy", "Position": "Defender", "Goals": 1, "Assists": 1, "Speed": 5},
    {"Name": "Sammy", "Position": "Striker", "Goals": 5, "Assists": 3, "Speed": 8},
]

player_df = pd.DataFrame(player_data)

# --- DISPLAY PLAYER STATS ---
st.subheader("📊 Player Stats")
fig = px.bar(player_df, x="Name", y="Goals", color="Position", title="Top Scorers")
st.plotly_chart(fig, use_container_width=True)

# --- SELECT PLAYER TO VIEW DETAILS ---
selected_player = st.selectbox("Choose a player to view details", player_df["Name"])
player_details = player_df[player_df["Name"] == selected_player].iloc[0]
st.write(f"**Position:** {player_details['Position']}")
st.write(f"**Goals:** {player_details['Goals']}")
st.write(f"**Assists:** {player_details['Assists']}")
st.write(f"**Speed:** {player_details['Speed']}")

# --- VOICE ASSISTANT TRIGGER ---
if st.button("🎙 Speak Player Stats"):
    text = f"{selected_player} plays as a {player_details['Position']} with {player_details['Goals']} goals and {player_details['Assists']} assists."
    speak(text)



    



