import streamlit as st

# --- Streamlit Config ---
st.set_page_config(page_title="Wosh FC Player Development Tracker", layout="wide")

st.title("⚽ Wosh FC Player Development Tracker")

# --- Function to Render Player Panel ---
def render_player_panel(name, team):
    st.subheader(f"{name}'s Panel")
    col1, col2, col3 = st.columns(3)
    with col1:
        goals = st.number_input(f"Goals", min_value=0, key=f"{team}_goals_{name}")
    with col2:
        assists = st.number_input(f"Assists", min_value=0, key=f"{team}_assists_{name}")
    with col3:
        matches = st.number_input(f"Matches Played", min_value=0, key=f"{team}_matches_{name}")
    st.markdown("---")

# --- Players by Team ---
teams = {
    "Home": [],
    "Under 7": ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"],
    "Under 11": ["Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo", "Emmanuel", "Ngesa", "Imani", "John", "Biden"]
}

# --- Sidebar Navigation ---
selected_team = st.sidebar.selectbox("Select Team", list(teams.keys()))

# --- Page Content ---
if selected_team == "Home":
    st.markdown("### Welcome to Wosh FC Dashboard 🏠")
    st.markdown("Use the sidebar to navigate to your team and start tracking development.")
else:
    st.header(f"{selected_team} Player Panels")
    for player in teams[selected_team]:
        render_player_panel(player, selected_team.replace(" ", "").lower())


