import streamlit as st
import pandas as pd
from datetime import date
# --- Streamlit Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")
# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("#### From the Streets to the Stars 🌟")
# --- SAMPLE PLAYER DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Barcelona", "Strength": 85, "Discipline": 88},
    {"Name": "Willy", "Position": "Defender", "Traits": "Aggressive, Tough", "Ambition": "National Team", "Strength": 82, "Discipline": 75},
    {"Name": "Sammy", "Position": "Goalkeeper", "Traits": "Alert, Confident", "Ambition": "Play in Europe", "Strength": 90, "Discipline": 90},
    {"Name": "Branton", "Position": "Winger", "Traits": "Fast, Creative", "Ambition": "EPL", "Strength": 80, "Discipline": 85},
    {"Name": "Ole", "Position": "Striker", "Traits": "Powerful, Composed", "Ambition": "Golden Boot", "Strength": 88, "Discipline": 84},
]
# --- SIDEBAR MENU ---
selected_player = st.sidebar.selectbox("Select Player", [player["Name"] for player in players])
st.sidebar.markdown("Made by Wosh FC ❤️")
# --- DISPLAY PLAYER DETAILS ---
player = next(p for p in players if p["Name"] == selected_player)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"🎯 {player['Name']}")
    st.write(f"**Position:** {player['Position']}")
    st.write(f"**Traits:** {player['Traits']}")
    st.write(f"**Ambition:** {player['Ambition']}")
    st.write(f"**Strength Rating:** {player['Strength']}/100")
    st.write(f"**Discipline Rating:** {player['Discipline']}/100")

with col2:
    df = pd.DataFrame({
        "Metric": ["Strength", "Discipline"],
        "Value": [player["Strength"], player["Discipline"]]
    })
    fig = px.bar(df, x="Metric", y="Value", color="Metric", title="Performance Metrics")
    st.plotly_chart(fig, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.caption(f"📅 Today: {date.today()} | Built by Coach Joshua Kanyeki & Waves of Street Hope 🚀")

