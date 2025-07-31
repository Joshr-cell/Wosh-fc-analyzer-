import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
/* Background and text */
body, .stApp {
    background-color: #0d1117;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Player Card */
.player-card {
    background: linear-gradient(145deg, #1f2733, #151a21);
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    transition: transform 0.3s ease;
    border: 1px solid #2a2f38;
}
.player-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.6);
}

/* Stat Bar Container */
.stat-container {
    background-color: #2a2f38;
    border-radius: 10px;
    overflow: hidden;
    height: 20px;
    margin-bottom: 10px;
}

/* Stat Bar Filler */
.stat-fill {
    height: 100%;
    transition: width 0.5s ease-in-out;
    border-radius: 10px;
}
.passing { background-color: #1abc9c; }
.shooting { background-color: #e74c3c; }
.defending { background-color: #3498db; }

/* Subheaders */
h2, h3 {
    color: #f0f6fc;
}
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- Players ---
players = [
    {"Name": "Ian", "Position": "Midfielder"},
    {"Name": "Willy", "Position": "Defender"},
    {"Name": "Sammy", "Position": "Forward"},
    {"Name": "Branton", "Position": "Goalkeeper"},
]

# --- Player Card Renderer ---
def player_panel(player):
    player_name = player["Name"]
    st.markdown(f"<div class='player-card'>", unsafe_allow_html=True)
    st.markdown(f"<h3>🎯 {player_name} ({player['Position']})</h3>", unsafe_allow_html=True)

    # Sliders
    passing = st.slider("Passing", 0, 10, 5, key=f"{player_name}_passing")
    shooting = st.slider("Shooting", 0, 10, 5, key=f"{player_name}_shooting")
    defending = st.slider("Defending", 0, 10, 5, key=f"{player_name}_defending")

    # Display Stat Bars
    st.markdown(f"""
    <div>
        <div>Passing: {passing}</div>
        <div class="stat-container"><div class="stat-fill passing" style="width:{passing*10}%"></div></div>

        <div>Shooting: {shooting}</div>
        <div class="stat-container"><div class="stat-fill shooting" style="width:{shooting*10}%"></div></div>

        <div>Defending: {defending}</div>
        <div class="stat-container"><div class="stat-fill defending" style="width:{defending*10}%"></div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close .player-card

# --- Main Section ---
st.subheader("📋 Player Evaluations")
for player in players:
    player_panel(player)

