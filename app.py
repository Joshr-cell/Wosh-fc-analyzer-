import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os
from datetime import datetime

# Firebase Initialization
try:
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_credentials.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print("Firebase not connected:", e)
    db = None

# App Config
st.set_page_config(page_title="Wosh FC Player Dashboard", layout="wide")
st.title("⚽ Wosh FC Player Development App")
st.markdown("From the streets to the stars 🌟")

# Age Groups and Players
age_groups = {
    "Under 7": ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"],
    "Under 11": ["Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo", "Emmanuel", "Ngesa", "Imani", "John", "Biden"],
    "Under 14": ["Byron", "Mokaya", "Branton", "Sakwa", "Victor", "Pasi", "Samuel", "Ole", "Samson", "Munene", "Moses", "Godfrey", "Messi", "Kiptoo", "Elvis", "Chacha"],
    "Under 15": ["Massai", "Brighton", "Ponic", "Mutua", "Turu", "Frank", "Zablon", "Joseph"]
}

# CSS Styling and Animations
st.markdown("""
    <style>
        .player-panel {
            background-color: #1e1e2f;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            transition: 0.3s;
        }
        .player-panel:hover {
            transform: scale(1.02);
            background-color: #292940;
        }
        .player-pic {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
            border: 2px solid #eee;
        }
    </style>
""", unsafe_allow_html=True)

# Player Stat Panel Generator
def render_player_panel(name):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(f"https://randomuser.me/api/portraits/men/{hash(name) % 100}.jpg", width=100)
    with col2:
        st.subheader(name)
        goals = st.number_input(f"{name} - Goals", min_value=0, key=f"goals_{name}")
        assists = st.number_input(f"{name} - Assists", min_value=0, key=f"assists_{name}")
        tackles = st.number_input(f"{name} - Tackles", min_value=0, key=f"tackles_{name}")
        improvement = st.text_area(f"{name} - Area of Improvement", key=f"improve_{name}")
        save_data = st.button(f"Save Stats for {name}", key=f"save_{name}")
        if save_data:
            player_data = {
                "goals": goals,
                "assists": assists,
                "tackles": tackles,
                "improvement": improvement,
                "timestamp": datetime.now().isoformat()
            }
            if db:
                db.collection("players").document(name).set(player_data)
                st.success("Saved to Firebase")
            else:
                os.makedirs("local_data", exist_ok=True)
                with open(f"local_data/{name}.json", "w") as f:
                    json.dump(player_data, f)
                st.success("Saved locally")

# Display All Age Groups
for group, players in age_groups.items():
    st.header(group)
    for player in players:
        with st.container():
            render_player_panel(player)

# Match Analysis Section
st.header("📊 Match Analysis Input")
passes = st.number_input("Total Passes", 0)
possession = st.slider("Possession %", 0, 100)
shots_on_goal = st.number_input("Shots on Goal", 0)
corners = st.number_input("Corners", 0)
tackles = st.number_input("Tackles", 0)
aerials = st.number_input("Aerial Balls", 0)

heatmap_data = pd.DataFrame({
    'x': [10, 30, 50, 70, 90],
    'y': [20, 40, 30, 50, 60],
    'intensity': [5, 2, 3, 4, 1]
})
st.subheader("Heat Map")
st.plotly_chart(px.density_heatmap(heatmap_data, x='x', y='y', z='intensity', nbinsx=10, nbinsy=10))

match_save = st.button("Save Match Report")
if match_save:
    match_stats = {
        "passes": passes,
        "possession": possession,
        "shots_on_goal": shots_on_goal,
        "corners": corners,
        "tackles": tackles,
        "aerials": aerials,
        "timestamp": datetime.now().isoformat()
    }
    if db:
        db.collection("match_reports").add(match_stats)
        st.success("Match Report Saved to Firebase")
    else:
        os.makedirs("local_data", exist_ok=True)
        with open("local_data/match_report.json", "w") as f:
            json.dump(match_stats, f)
        st.success("Match Report Saved Locally")

st.download_button("Download Match Report", json.dumps(match_stats, indent=4), file_name="match_report.json")


