import streamlit as st
from PIL import Image
import pandas as pd

# --- App Config ---
st.set_page_config(page_title="Wosh FC Player Development Dashboard", layout="wide")

# --- CSS Styling ---
st.markdown("""
    <style>
        body {
            background-color: #1b1f27;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .player-card {
            background-color: #2a2f3b;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
            transition: transform 0.3s ease;
        }
        .player-card:hover {
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# --- Player Data Example ---
under7_players = [
    {"name": "Fidel", "picture": "", "position": "Forward", "pace": 80, "passing": 75, "shooting": 78, "improvement": "Finishing"},
    {"name": "Kijokilangs", "picture": "", "position": "Midfielder", "pace": 70, "passing": 82, "shooting": 65, "improvement": "Pace"},
    {"name": "Kasmall", "picture": "", "position": "Defender", "pace": 65, "passing": 70, "shooting": 50, "improvement": "Positioning"}
]

# --- Sidebar Navigation ---
menu = st.sidebar.selectbox("Select Age Category", ["Under 7", "Under 11", "Under 14", "Under 15", "Match Analysis"])

# --- Player Panel Function ---
def show_players(players):
    for player in players:
        with st.container():
            cols = st.columns([1, 3])
            with cols[0]:
                st.image("https://via.placeholder.com/150", caption=player["name"], width=100)
            with cols[1]:
                st.markdown(f"""
                    <div class="player-card">
                        <h3>{player['name']}</h3>
                        <p><strong>Position:</strong> {player['position']}</p>
                        <p><strong>Pace:</strong> {player['pace']}</p>
                        <p><strong>Passing:</strong> {player['passing']}</p>
                        <p><strong>Shooting:</strong> {player['shooting']}</p>
                        <p><strong>Area of Improvement:</strong> {player['improvement']}</p>
                    </div>
                """, unsafe_allow_html=True)

# --- Pages ---
if menu == "Under 7":
    st.title("👶 Under 7 Player Development")
    show_players(under7_players)

elif menu == "Match Analysis":
    st.title("📊 Match Analysis Input")
    st.text_input("Opponent Team")
    st.number_input("Number of Passes", min_value=0)
    st.number_input("Possession %", min_value=0, max_value=100)
    st.number_input("Shots on Goal", min_value=0)
    st.number_input("Corners", min_value=0)
    st.number_input("Tackles", min_value=0)
    st.file_uploader("Upload Match Video", type=["mp4", "mov", "avi"])
    st.button("Submit Match Report")

else:
    st.title(f"{menu} - Coming Soon")
