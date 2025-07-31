import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Wosh FC Player Development", layout="wide")

# --- TEAM DATA ---
teams = {
    "Under 7": [
        "Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan",
        "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"
    ],
    "Under 11": [
        "Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo",
        "Emmanuel", "Ngesa", "Imani", "John", "Biden"
    ],
    "Under 14": [
        "Byron", "Mokaya", "Branton", "Sakwa", "Victor", "Pasi", "Samuel",
        "Ole", "Samson", "Munene", "Moses", "Godfrey", "Messi", "Kiptoo",
        "Elvis", "Chacha"
    ],
    "Under 15": [
        "Massai", "Brighton", "Ponic", "Mutua", "Turu", "Frank", "Zablon", "Joseph"
    ]
}

# --- PLAYER PANEL ---
def render_player_panel(name):
    with st.expander(f"{name}'s Panel"):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image("https://placehold.co/150x150", caption=name)

        with col2:
            st.markdown("**Player Stats**")
            goals = st.number_input(f"{name} - Goals", min_value=0, key=f"goals_{name}")
            assists = st.number_input(f"{name} - Assists", min_value=0, key=f"assists_{name}")
            tackles = st.number_input(f"{name} - Tackles", min_value=0, key=f"tackles_{name}")
            passes = st.number_input(f"{name} - Passes", min_value=0, key=f"passes_{name}")
            saves = st.number_input(f"{name} - Saves", min_value=0, key=f"saves_{name}")

            st.markdown("**Match Statistics**")
            match_rating = st.slider(f"{name} - Match Rating", 0, 10, key=f"rating_{name}")
            st.text_area(f"{name} - Area of Improvement", key=f"improve_{name}")

# --- PLAYER SECTION ---
st.title("⚽ Wosh FC Player Development Tracker")

for category, players in teams.items():
    st.header(f"{category} Team")
    for player in players:
        render_player_panel(player)

# --- MATCH ANALYSIS INPUT PANEL ---
st.title("📊 Match Analysis")
with st.form("match_analysis"):
    st.subheader("Enter Match Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        passes = st.number_input("Number of Passes", min_value=0)
        possession = st.slider("Possession %", 0, 100)
        shots = st.number_input("Shots on Goal", min_value=0)
    with col2:
        corners = st.number_input("Corners", min_value=0)
        tackles = st.number_input("Tackles", min_value=0)
        aerials = st.number_input("Aerial Balls Won", min_value=0)
    with col3:
        yellow_cards = st.number_input("Yellow Cards", min_value=0)
        red_cards = st.number_input("Red Cards", min_value=0)
        offsides = st.number_input("Offsides", min_value=0)

    notes = st.text_area("Game Notes")
    submitted = st.form_submit_button("Submit Match Report")
    if submitted:
        st.success("Match report submitted successfully.")

# --- VIDEO MODULE PLACEHOLDER ---
st.title("🎥 Video Module")
st.info("To upload or review match footage, integrate a video upload or YouTube embed module.")

# --- FUTURE INTEGRATIONS ---
st.markdown("---")
st.caption("Data can be saved in Firebase or other backends. Add export to Excel/CSV as needed.")

