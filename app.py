import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Wosh FC Player Development", layout="wide")
st.title("⚽ Wosh FC Player Development Tracker")
st.markdown("From the streets to the stars 🌟")

# --- Tabs ---
tabs = st.tabs(["Under 7", "Under 11", "Under 14", "Under 15", "Match Analysis", "Video Module"])

# --- Players by Age Group ---
under_7 = ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"]
under_11 = ["Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo", "Emmanuel", "Ngesa", "Imani", "John", "Biden"]
under_14 = ["Byron", "Mokaya", "Branton", "Sakwa", "Victor", "Pasi", "Samuel", "Ole", "Samson", "Munene", "Moses", "Godfrey", "Messi Kiptoo", "Elvis Chacha"]
under_15 = ["Massai", "Brighton", "Ponic", "Mutua", "Turu", "Frank", "Zablon", "Joseph"]

player_groups = {
    "Under 7": under_7,
    "Under 11": under_11,
    "Under 14": under_14,
    "Under 15": under_15,
}

# --- Helper to Show Player Panel ---
def player_panel(player_name):
    with st.expander(player_name):
        st.image("https://via.placeholder.com/150", width=150)
        st.subheader("Player Stats")
        st.text("Speed: \\nDribbling: \\nPassing:")

        st.subheader("Match Stats")
        st.text("Goals: \\nAssists: \\nTackles:")

        st.subheader("Area of Improvement")
        st.text("- Enter areas here")

# --- Populate Each Age Tab ---
for i, (age_group, players) in enumerate(player_groups.items()):
    with tabs[i]:
        st.header(f"{age_group} Squad")
        for player in players:
            player_panel(player)

# --- Match Analysis ---
with tabs[4]:
    st.header("📊 Match Analysis Input")
    passes = st.number_input("Number of Passes", min_value=0)
    possession = st.slider("Possession (%)", 0, 100)
    shots = st.number_input("Shots on Goal", min_value=0)
    corners = st.number_input("Number of Corners", min_value=0)
    tackles = st.number_input("Number of Tackles", min_value=0)
    fouls = st.number_input("Number of Fouls", min_value=0)
    aerial_duels = st.number_input("Aerial Balls Won", min_value=0)
    if st.button("Save Match Stats"):
        st.success("Match stats saved (placeholder — not yet connected to database)")

# --- Video Module ---
with tabs[5]:
    st.header("🎥 Video Module")
    video = st.file_uploader("Upload Match Video", type=["mp4", "mov"])
    video_title = st.text_input("Video Title")
    video_description = st.text_area("Video Description")
    if st.button("Upload Video"):
        st.success("Video uploaded (placeholder — not yet connected to storage)")

