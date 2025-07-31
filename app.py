import streamlit as st
import pandas as pd
from datetime import date

# --- Streamlit Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- PLAYER DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Arsenal"},
    {"Name": "Willy", "Position": "Striker", "Traits": "Fast, Clinical", "Ambition": "Golden Boot Winner"},
    {"Name": "Sammy", "Position": "Defender", "Traits": "Aggressive, Strong", "Ambition": "Best Defender"},
    {"Name": "Branton", "Position": "Goalkeeper", "Traits": "Alert, Confident", "Ambition": "Save a penalty in a final"},
    {"Name": "Samson", "Position": "Winger", "Traits": "Creative, Fast", "Ambition": "Assist King"},
    {"Name": "Pasi", "Position": "Defender", "Traits": "Disciplined, Tough", "Ambition": "Lead the backline"},
    {"Name": "Ole", "Position": "Midfielder", "Traits": "Energetic, Tenacious", "Ambition": "Team engine"},
    {"Name": "Byron", "Position": "Striker", "Traits": "Powerful, Fearless", "Ambition": "Break scoring records"},
    {"Name": "Munene", "Position": "Goalkeeper", "Traits": "Composed, Brave", "Ambition": "Clean sheet leader"},
    {"Name": "Victor", "Position": "Midfielder", "Traits": "Sharp, Visionary", "Ambition": "Control midfield"},
    {"Name": "Mose", "Position": "Defender", "Traits": "Hard-hitting, Reliable", "Ambition": "Best tackler"},
    {"Name": "Jamo", "Position": "Winger", "Traits": "Creative, Tricky", "Ambition": "Top assists"},
]

# --- SAVE MATCH REPORT FUNCTION ---
def save_match_report(name, goals, assists):
    report = f"{date.today()} - {name}: {goals} goals, {assists} assists\n"
    with open("match_reports.txt", "a") as f:
        f.write(report)

# --- PLAYER PANEL FUNCTION ---
def render_player_panel(player, index):
    name = player["Name"]
    position = player["Position"]
    traits = player["Traits"]
    ambition = player["Ambition"]

    st.subheader(name)
    st.markdown(f"**Position:** {position}  \n**Traits:** {traits}  \n**Ambition:** {ambition}")

    col1, col2 = st.columns(2)
    with col1:
        goals = st.number_input(f"Goals - {name}", min_value=0, key=f"goals_{index}")
    with col2:
        assists = st.number_input(f"Assists - {name}", min_value=0, key=f"assists_{index}")

    if st.button(f"Save Match Report for {name}", key=f"save_{index}"):
        save_match_report(name, goals, assists)
        st.success(f"Match report saved for {name} ✅")

# --- MAIN SECTION ---
st.markdown("### Player Performance Input")

for i, player in enumerate(players):
    with st.expander(player["Name"]):
        render_player_panel(player, i)
