import streamlit as st
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

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

with st.sidebar:
    team_tab = st.selectbox("🔽 Select Age Group or Module", list(under_teams.keys()) + ["Match Analysis", "Video Module"])

# --- Player Profile Section ---
if team_tab in under_teams:
    st.header(f"🎒 {team_tab} Player Profiles")
    for player in under_teams[team_tab]:
        with st.expander(f"🔹 {player}"):
            player_image = st.file_uploader(f"Upload Photo for {player}", type=["png", "jpg", "jpeg"], key=f"{player}_img")
            if player_image:
                st.image(player_image, width=150, caption=f"{player}'s Photo")
            else:
                st.markdown("_No image uploaded_")

            st.markdown(f"### 🎮 Attribute Ratings for {player}")
            for attr in attribute_list:
                st.slider(f"{attr} - {player}", 0, 100, 70)
            st.text_area(f"📌 Area of Improvement - {player}")
            st.button(f"💾 Save {player}'s Data")

# --- Match Analysis Tab ---
elif team_tab == "Match Analysis":
    st.header("📊 Match Analysis")
    st.subheader("📈 Team Stats")
    possession = st.slider("Possession %", 0, 100, 50)
    passes = st.number_input("Total Passes", 0)
    shots = st.number_input("Total Shots", 0)
    corners = st.number_input("Corners", 0)
    aerials = st.number_input("Aerial Balls Won", 0)
    tackles = st.number_input("Tackles", 0)
    heatmap_placeholder = st.text_input("Heat Map Image URL (optional)")
    if heatmap_placeholder:
        st.image(heatmap_placeholder, caption="Heat Map")

    st.subheader("👤 Individual Player Match Data")
    player_name = st.text_input("Player Name")
    team_name = st.text_input("Team")
    opponent = st.text_input("Opponent")
    match_date = st.date_input("Match Date", date.today())
    goals = st.number_input("Goals", 0)
    player_shots = st.number_input("Shots", 0)
    shots_on_target = st.number_input("Shots on Target", 0)
    passes_attempted = st.number_input("Passes Attempted", 0)
    passes_completed = st.number_input("Passes Completed", 0)
    dribbles_attempted = st.number_input("Dribbles Attempted", 0)
    dribbles_completed = st.number_input("Dribbles Completed", 0)
    tackles_player = st.number_input("Tackles", 0)
    interceptions = st.number_input("Interceptions", 0)
    fouls = st.number_input("Fouls Committed", 0)
    minutes_played = st.number_input("Minutes Played", 0)
    st.button("💾 Save Match Data")

# --- Video Module Tab ---
elif team_tab == "Video Module":
    st.header("🎥 Video Module")
    video_option = st.radio("Select Video Type", ["Upload", "YouTube Link"])
    if video_option == "Upload":
        video_file = st.file_uploader("Upload Match Video", type=["mp4", "mov", "avi"])
        if video_file:
            st.video(video_file)
    else:
        video_url = st.text_input("YouTube or Vimeo URL")
        if video_url:
            st.video(video_url)
