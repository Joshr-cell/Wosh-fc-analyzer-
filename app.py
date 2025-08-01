import streamlit as st
import pandas as pd
from datetime import date
import base64

# --- App Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Session Setup ---
if 'player_data' not in st.session_state:
    st.session_state.player_data = {}

if 'bg_image' not in st.session_state:
    st.session_state.bg_image = None

# --- Background Image Upload ---
st.sidebar.markdown("### 🖼️ App Background")
bg_choice = st.sidebar.radio("Choose Background", ["None", "Upload Image", "Enter Image URL"])

if bg_choice == "Upload Image":
    bg_upload = st.sidebar.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg"])
    if bg_upload:
        st.session_state.bg_image = bg_upload
elif bg_choice == "Enter Image URL":
    bg_url = st.sidebar.text_input("Paste Image URL")
    if bg_url:
        st.session_state.bg_image = bg_url

# --- Apply Background ---
def set_background(image_file_or_url):
    if isinstance(image_file_or_url, str):  # URL
        bg_url = image_file_or_url
    else:  # Uploaded File
        bg_bytes = image_file_or_url.read()
        bg_base64 = base64.b64encode(bg_bytes).decode()
        bg_url = f"data:image/png;base64,{bg_base64}"
    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)

if st.session_state.bg_image:
    set_background(st.session_state.bg_image)

# --- App Title ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("##### _From the Streets to the Stars_ 🌟")

# --- Player Lists ---
under_teams = {
    "Under 7": ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"]
}

attribute_list = [
    "Pace", "Acceleration", "Sprint Speed", "Shooting", "Finishing", "Shot Power", "Positioning", "Long Shots",
    "Passing", "Short Passing", "Vision", "Crossing", "Long Passing", "Dribbling", "Agility", "Balance",
    "Ball Control", "Dribbling (again)", "Composure", "Defending", "Heading Accuracy", "Defensive Awareness",
    "Tackling", "Physical", "Strength", "Stamina", "Jumping", "Aggression"
]

# --- Age Group Selector ---
team_tab = st.sidebar.selectbox("🔽 Select Age Group", list(under_teams.keys()))

# --- Player Forms ---
if team_tab in under_teams:
    st.header(f"👟 {team_tab} Player Profiles")

    for player in under_teams[team_tab]:
        with st.expander(f"🔹 {player}"):
            player_key = f"{team_tab}_{player}"
            if player_key not in st.session_state.player_data:
                st.session_state.player_data[player_key] = {"image": None, "stats": {}, "notes": ""}

            # Upload Photo (if not saved)
            if st.session_state.player_data[player_key]["image"] is None:
                uploaded_file = st.file_uploader(f"Upload Photo for {player}", type=["png", "jpg", "jpeg"], key=f"{player}_img")
                if uploaded_file:
                    st.session_state.player_data[player_key]["image"] = uploaded_file
                    st.success(f"{player}'s photo saved!")
            else:
                st.image(st.session_state.player_data[player_key]["image"], width=150, caption=f"{player}'s Photo")

            # Show sliders
            for attr in attribute_list:
                rating = st.slider(f"{attr} - {player}", 0, 100, 70, key=f"{player_key}_{attr}")
                st.session_state.player_data[player_key]["stats"][attr] = rating

            # Notes
            notes = st.text_area(f"📌 Area of Improvement - {player}", key=f"{player_key}_notes")
            st.session_state.player_data[player_key]["notes"] = notes

# --- SAVE ALL BUTTON ---
st.markdown("## 💾 Save All Player Data")
if st.button("🔐 Export All to CSV"):
    all_data = []
    for key, data in st.session_state.player_data.items():
        name = key.split("_")[1]
        row = {"Player": name, "Notes": data["notes"]}
        row.update(data["stats"])
        all_data.append(row)

    df = pd.DataFrame(all_data)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", data=csv, file_name="wosh_fc_players.csv", mime="text/csv")
