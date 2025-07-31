import streamlit as st
from datetime import datetime

# --- Streamlit Config ---
st.set_page_config(page_title="⚽ Wosh FC Player Tracker", layout="wide")

st.title("⚽ Wosh FC Player Development Tracker")
st.markdown("### From the Streets to the Stars 🌟")

# --- Player Groups ---
teams = {
    "Under 7 Team": [
        "Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan",
        "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"
    ],
    "Under 11 Team": [
        "Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo",
        "Emmanuel", "Ngesa", "Imani", "John", "Biden"
    ],
    "Under 15 Team": [
        "Ian", "Sammy", "Victor", "Pasi", "Ole", "Branton", "Mose",
        "Munene", "Jamo", "Byron", "Samson", "Willy"  # You can adjust
    ]
}

# --- Player Panel Renderer ---
def render_player_panel(name):
    with st.expander(f"{name}'s Panel", expanded=False):
        cols = st.columns([1, 1, 1])
        goals = cols[0].number_input(f"{name} - Goals", min_value=0, key=f"goals_{name}")
        assists = cols[1].number_input(f"{name} - Assists", min_value=0, key=f"assists_{name}")
        tackles = cols[2].number_input(f"{name} - Tackles", min_value=0, key=f"tackles_{name}")

        saves = st.number_input(f"{name} - Saves", min_value=0, key=f"saves_{name}")
        rating = st.slider(f"{name} - Rating (out of 10)", 0.0, 10.0, step=0.1, key=f"rating_{name}")
        improvement = st.text_area(f"{name} - Area of Improvement", key=f"improvement_{name}")
        video_link = st.text_input(f"{name} - Training Video Link (optional)", key=f"video_{name}")

        # Save or download functionality could be integrated with Firebase here
        st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# --- Home Panel ---
st.markdown("## 📋 Home Panel")
st.info("Use this panel to track player development for each age group.")

# --- Loop Through Teams ---
for category, players in teams.items():
    st.markdown(f"## 🔹 {category}")
    for player in players:
        render_player_panel(player)

# Optional: Export data button (placeholder)
st.markdown("---")
if st.button("📤 Export Match Reports (Coming Soon)"):
    st.warning("Export feature will be connected to Firebase soon.")
