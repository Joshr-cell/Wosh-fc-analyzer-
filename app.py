import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Home", "👤 Player Profiles", "📊 Team Stats", "📅 Match History", "🏋️ Training Suggestions"]
)

# --- DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Age": 14, "Goals": 4, "Assists": 5, "Fitness": 80, "Traits": "Visionary, Calm"},
    {"Name": "Willy", "Position": "Forward", "Age": 13, "Goals": 7, "Assists": 3, "Fitness": 88, "Traits": "Pacy, Sharp finisher"},
    {"Name": "Sammy", "Position": "Defender", "Age": 14, "Goals": 1, "Assists": 1, "Fitness": 90, "Traits": "Tactical, Brave"},
    {"Name": "Branton", "Position": "Goalkeeper", "Age": 13, "Goals": 0, "Assists": 0, "Fitness": 92, "Traits": "Shot-stopper"},
    {"Name": "Victor", "Position": "Midfielder", "Age": 14, "Goals": 3, "Assists": 4, "Fitness": 84, "Traits": "Creative, Agile"},
]
player_df = pd.DataFrame(players)

# --- HOME PAGE ---
if menu == "🏠 Home":
    st.subheader("Welcome to Wosh FC Analyzer")
    st.image("https://images.unsplash.com/photo-1604079628043-94302f7f1c3e", caption="Wosh FC in Action", use_column_width=True)
    st.markdown("This platform empowers Wosh FC players by analyzing stats, tracking progress, and offering training suggestions.")

# --- PLAYER PROFILES ---
elif menu == "👤 Player Profiles":
    st.subheader("Player Profiles")
    selected_player = st.selectbox("Select Player", player_df["Name"])
    player_info = player_df[player_df["Name"] == selected_player].iloc[0]

    st.markdown(f"**Name:** {player_info['Name']}")
    st.markdown(f"**Position:** {player_info['Position']}")
    st.markdown(f"**Age:** {player_info['Age']}")
    st.markdown(f"**Goals:** {player_info['Goals']}")
    st.markdown(f"**Assists:** {player_info['Assists']}")
    st.markdown(f"**Fitness Level:** {player_info['Fitness']}%")
    st.markdown(f"**Traits:** {player_info['Traits']}")

# --- TEAM STATS ---
elif menu == "📊 Team Stats":
    st.subheader("Team Performance Statistics")

    st.markdown("### Goals by Player")
    fig = px.bar(player_df, x="Name", y="Goals", color="Position", title="Top Scorers")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Fitness Overview")
    fig2 = px.line(player_df, x="Name", y="Fitness", markers=True, title="Player Fitness Levels")
    st.plotly_chart(fig2, use_container_width=True)

# --- MATCH HISTORY ---
elif menu == "📅 Match History":
    st.subheader("Match History")
    match_data = {
        "Date": ["2025-07-01", "2025-07-15", "2025-07-20"],
        "Opponent": ["Zorphar SC", "Makadara United", "Young Stars"],
        "Result": ["2-1 W", "0-2 L", "3-3 D"],
        "Man of the Match": ["Willy", "Victor", "Ian"]
    }
    match_df = pd.DataFrame(match_data)
    st.table(match_df)

# --- TRAINING SUGGESTIONS ---
elif menu == "🏋️ Training Suggestions":
    st.subheader("AI Training Suggestions")
    st.markdown("Select a player to get personalized training recommendations.")

    selected_player = st.selectbox("Choose Player", player_df["Name"], key="training")
    player_info = player_df[player_df["Name"] == selected_player].iloc[0]

    # Simple logic-based AI suggestion
    st.markdown(f"### For {selected_player}")
    if player_info["Position"] == "Forward":
        st.markdown("- Improve shooting accuracy")
        st.markdown("- Sprint drills and agility")
    elif player_info["Position"] == "Midfielder":
        st.markdown("- Vision and passing accuracy")
        st.markdown("- Long-range shooting")
    elif player_info["Position"] == "Defender":
        st.markdown("- 1v1 defending drills")
        st.markdown("- Tackling and positioning")
    elif player_info["Position"] == "Goalkeeper":
        st.markdown("- Reaction training")
        st.markdown("- Distribution under pressure")

    st.markdown(f"**Fitness Tip**: Maintain above {90 if player_info['Fitness'] < 90 else 95}% fitness with hydration, recovery, and proper sleep.")

# --- FOOTER ---
st.markdown("---")
st.markdown("📍 Powered by Coach Kanyeki • Wosh FC • 2025")

    



