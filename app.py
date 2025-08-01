import streamlit as st
import pandas as pd
from datetime import date
import base64

# --- Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Session Initialization ---
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

# --- Set Background Function ---
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

# --- Custom CSS for FIFA-style ---
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            padding: 1rem;
        }
        h1, h2, h3, h4 {
            color: #ffffff;
            font-weight: 700;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
        .stSlider > div {
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Logo Upload ---
st.sidebar.markdown("### 🖼️ Upload Wosh FC Logo")
logo = st.sidebar.file_uploader("Choose Logo Image", type=["png", "jpg", "jpeg"])
if logo:
    st.image(logo, width=180)
else:
    st.sidebar.markdown("_No logo uploaded_")

# --- App Title ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("##### _From the Streets to the Stars_ 🌟")

# --- Tactical Identity ---
st.header("🎯 Tactical Identity")
with st.container():
    st.subheader("🔧 Formation: 4-3-3")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Build-Up")
        st.write("Style:", st.text_input("Build-Up Style", "Slow Build-Up"))
        st.write("Width:", st.text_input("Width", "Balanced"))
        st.write("Key Players:", st.text_area("Build-Up Roles", "Fullbacks stay back, Midfielders drop deep"))

    with col2:
        st.markdown("### 🔵 Chance Creation")
        st.write("Style:", st.text_input("Chance Creation Style", "Possession"))
        st.write("Support:", st.text_input("Support Type", "Support Runs"))
        st.write("Players in Box:", st.text_input("Players in Box", "Moderate"))

    with col3:
        st.markdown("### 🟡 Defensive Style")
        st.write("Shape:", st.text_input("Defensive Shape", "Mid Block"))
        st.write("Pressure:", st.text_input("Pressure Trigger", "On Heavy Touch"))
        st.write("Line Height:", st.text_input("Line Height", "Medium"))

    st.markdown("### 📌 Tactical Notes")
    st.text_area("Tactical Notes", """
- Control the tempo of the game
- Maintain short passing triangles
- Force mistakes in the midfield
- Patience over panic
- Wingers drop to receive in buildup
""")

# --- Sidebar Team Selector ---
under_teams = {
    "Under 7": ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"],
    "Under 11": ["Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo", "Emmanuel", "Ngesa", "Imani", "John", "Biden"],
    "Under 14": ["Byron", "Mokaya", "Branton", "Sakwa", "Victor", "Pasi", "Samuel", "Ole", "Samson", "Munene", "Moses", "Godfrey", "Messi Kiptoo", "Elvis Chacha"],
    "Under 15": ["Massai", "Brighton", "Ponic", "Mutua", "Turu", "Frank", "Zablon", "Joseph"]
}

attribute_list = [
    "Pace", "Acceleration", "Sprint Speed", "Shooting", "Finishing", "Shot Power", "Positioning", "Long Shots",
    "Passing", "Short Passing", "Vision", "Crossing", "Long Passing", "Dribbling", "Agility", "Balance",
    "Ball Control", "Dribbling (again)", "Composure", "Defending", "Heading Accuracy", "Defensive Awareness",
    "Tackling", "Physical", "Strength", "Stamina", "Jumping", "Aggression"
]

team_tab = st.sidebar.selectbox("🔽 Select Age Group or Module", list(under_teams.keys()) + ["Match Analysis", "Video Module"])

if team_tab in under_teams:
    st.header(f"🎒 {team_tab} Player Profiles")
    for player in under_teams[team_tab]:
        with st.expander(f"🔹 {player}"):
            player_key = f"{team_tab}_{player}"
            if player_key not in st.session_state.player_data:
                st.session_state.player_data[player_key] = {"image": None, "stats": {}, "notes": ""}

            if st.session_state.player_data[player_key]["image"] is None:
                image = st.file_uploader(f"Upload Photo for {player}", type=["png", "jpg", "jpeg"], key=f"{player}_img")
                if image:
                    st.session_state.player_data[player_key]["image"] = image
                    st.success(f"{player}'s image saved!")
            else:
                st.image(st.session_state.player_data[player_key]["image"], width=150, caption=f"{player}'s Photo")

            for attr in attribute_list:
                key = f"{player_key}_{attr}"
                value = st.slider(f"{attr} - {player}", 0, 100, 70, key=key)
                st.session_state.player_data[player_key]["stats"][attr] = value

            notes = st.text_area(f"📌 Area of Improvement - {player}", key=f"{player_key}_notes")
            st.session_state.player_data[player_key]["notes"] = notes

    # Save All
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

elif team_tab == "Match Analysis":
    st.header("📊 Match Analysis")
    st.subheader("📈 Team Stats")
    st.slider("Possession %", 0, 100, 50)
    st.number_input("Total Passes", 0)
    st.number_input("Total Shots", 0)
    st.number_input("Corners", 0)
    st.number_input("Aerial Balls Won", 0)
    st.number_input("Tackles", 0)
    url = st.text_input("Heat Map URL")
    if url: st.image(url)

    st.subheader("👤 Player Match Data")
    st.text_input("Player Name")
    st.text_input("Team")
    st.text_input("Opponent")
    st.date_input("Match Date", date.today())
    st.number_input("Goals", 0)
    st.number_input("Shots", 0)
    st.number_input("Shots on Target", 0)
    st.number_input("Passes Attempted", 0)
    st.number_input("Passes Completed", 0)
    st.number_input("Dribbles Attempted", 0)
    st.number_input("Dribbles Completed", 0)
    st.number_input("Tackles", 0)
    st.number_input("Interceptions", 0)
    st.number_input("Fouls Committed", 0)
    st.number_input("Minutes Played", 0)
    st.button("💾 Save Match Data")

elif team_tab == "Video Module":
    st.header("🎥 Video Module")
    method = st.radio("Select Video Type", ["Upload", "YouTube Link"])
    if method == "Upload":
        file = st.file_uploader("Upload Match Video", type=["mp4", "mov", "avi"])
        if file:
            st.video(file)
    else:
        link = st.text_input("YouTube or Vimeo URL")
        if link:
            st.video(link)
