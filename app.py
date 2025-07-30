import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import random

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Wosh FC Dashboard", layout="wide")

# -------------------- STYLING --------------------
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .block-container {
            padding: 2rem 2rem;
        }
        .stSidebar {
            background-color: #111827;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- DATA --------------------
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Europe"},
    {"Name": "Willy", "Position": "Striker", "Traits": "Clinical, Fast", "Ambition": "Top Scorer"},
    {"Name": "Sammy", "Position": "Defender", "Traits": "Aggressive, Leader", "Ambition": "Captain"},
    {"Name": "Branton", "Position": "Goalkeeper", "Traits": "Brave, Reflexes", "Ambition": "Clean Sheets"},
    {"Name": "Pasi", "Position": "Winger", "Traits": "Flair, Speed", "Ambition": "Highlight Plays"},
]

df = pd.DataFrame(players)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    choice = option_menu("Wosh FC Dashboard", 
        ["Home", "Player Profiles", "Team Stats", "Match History", "Training Suggestions"],
        icons=["house", "person", "bar-chart", "clock-history", "lightbulb"],
        default_index=0)

# -------------------- HOME --------------------
if choice == "Home":
    st.title("⚽ Welcome to Wosh FC Dashboard")
    st.subheader("From the streets to the stars 🌟")
    st.write("Track individual player development, team progress, and AI-based training suggestions. This is more than data — this is your legacy.")
    st.image("https://images.unsplash.com/photo-1618739174394-b28130d6f4c6", use_column_width=True)

# -------------------- PLAYER PROFILES --------------------
elif choice == "Player Profiles":
    st.title("🧍 Player Profiles")
    for player in players:
        with st.expander(player["Name"]):
            st.write(f"**Position:** {player['Position']}")
            st.write(f"**Traits:** {player['Traits']}")
            st.write(f"**Ambition:** {player['Ambition']}")
            notes = st.text_area(f"🔖 Notes for {player['Name']}", "")
            st.write("---")

# -------------------- TEAM STATS --------------------
elif choice == "Team Stats":
    st.title("📊 Team Stats")
    st.subheader("Overall Summary")
    
    total_players = len(players)
    avg_goals = round(random.uniform(1.2, 2.5), 2)
    clean_sheets = random.randint(3, 10)

    col1, col2, col3 = st.columns(3)
    col1.metric("Players", total_players)
    col2.metric("Avg Goals/Game", avg_goals)
    col3.metric("Clean Sheets", clean_sheets)

    st.bar_chart(pd.DataFrame({
        "Training Attendance": [random.randint(75, 100) for _ in range(total_players)],
        "Match Performance": [random.randint(60, 95) for _ in range(total_players)],
    }, index=[p["Name"] for p in players]))

# -------------------- MATCH HISTORY --------------------
elif choice == "Match History":
    st.title("📅 Match History")
    match_data = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=5).strftime('%Y-%m-%d'),
        "Opponent": ["Elite FC", "Kings XI", "Wolf Pack", "Hustlers", "Kawangware United"],
        "Result": ["2-1 W", "1-3 L", "0-0 D", "4-2 W", "1-1 D"],
        "MVP": random.choices([p["Name"] for p in players], k=5)
    })
    st.table(match_data)

# -------------------- TRAINING SUGGESTIONS --------------------
elif choice == "Training Suggestions":
    st.title("💡 AI-Powered Training Suggestions")

    selected = st.selectbox("Choose a player:", [p["Name"] for p in players])
    st.subheader(f"Training Plan for {selected}")

    suggestion_map = {
        "Striker": ["Finishing Drills", "Off-the-ball Movement", "1v1 Situations"],
        "Midfielder": ["Passing Under Pressure", "Vision Enhancement", "Small-sided Games"],
        "Defender": ["Tackling Precision", "Positioning", "Set-Piece Defense"],
        "Goalkeeper": ["Shot Stopping", "Distribution", "1v1s"],
        "Winger": ["Crossing", "Dribbling in Tight Spaces", "Quick Decision-Making"]
    }

    position = next((p["Position"] for p in players if p["Name"] == selected), "Midfielder")
    drills = suggestion_map.get(position, ["Conditioning", "Ball Control", "Game Awareness"])

    st.write("🧠 **Suggested Focus Areas:**")
    for drill in drills:
        st.markdown(f"- {drill}")
    
    st.success("Train smart. Grow fast. Shine brightest. 🌟")


