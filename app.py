import streamlit as st
from PIL import Image
# --- Page Config ---
st.set_page_config(page_title="Wosh FC Player Development", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
        font-family: 'Arial';
    }
    .stExpanderHeader {
        font-size: 18px;
        font-weight: bold;
        color: #33ffcc;
    }
    </style>
""", unsafe_allow_html=True)

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

# --- Player Panel with Radar Chart ---
def player_panel(player_name):
    with st.expander(player_name):
        st.image("https://via.placeholder.com/150", width=150)
        st.subheader("📊 Technical Ratings")

        categories = ["Passing", "Dribbling", "Shooting", "Heading", "Crossing", "Shot Range"]
        scores = [st.slider(cat, 0, 10, 5) for cat in categories]

        radar_fig = go.Figure()
        radar_fig.add_trace(go.Scatterpolar(
            r=scores + [scores[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name=player_name
        ))
        radar_fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10]),
                bgcolor="#1e1e1e"
            ),
            showlegend=False,
            paper_bgcolor="#0e1117",
            font_color="white"
        )
        st.plotly_chart(radar_fig, use_container_width=True)

        st.subheader("📈 Match Stats")
        st.text("Goals: \nAssists: \nTackles:")

        st.subheader("🛠️ Area of Improvement")
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


