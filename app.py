import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟 | Youth Football Development Platform")

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.radio("📂 Navigate", [
    "Home", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Analysis"
])
st.sidebar.markdown("👥 Total Players: 3")  # Update if you add more

# --- SAMPLE PLAYER DATA ---
players = [
    {"name": "Munene", "team": "Under 14", "strength": 80, "ambition": 90, "area_of_improvement": "Passing", "coach_remarks": "Very disciplined."},
    {"name": "Byron", "team": "Under 14", "strength": 75, "ambition": 85, "area_of_improvement": "Tackling", "coach_remarks": "Shows improvement weekly."},
    {"name": "Victor", "team": "Under 14", "strength": 72, "ambition": 88, "area_of_improvement": "Positioning", "coach_remarks": "Needs confidence."},
]

# --- HOME ---
if menu == "Home":
    st.subheader("🏠 Welcome to Wosh FC")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Pad")
    st.markdown("""
    **Wosh FC** is dedicated to nurturing young football talent from underprivileged communities.
    
    We work across five age categories:
    - ⚽ Under 7 (12 players)
    - ⚽ Under 10 (12 players)
    - ⚽ Under 12 (12 players)
    - ⚽ Under 14 (12 players)
    - ⚽ Under 16 (7 players)
    
    Use this platform to track player performance, plan drills, and review match data.
    """)

# --- PLAYER PROFILES ---
elif menu == "Players":
    st.subheader("👥 Player Profiles")
    for player in players:
        with st.expander(f"{player['name']} - {player['team']}"):
            st.write(f"**Team:** {player['team']}")
            st.write(f"**Strength:** {player['strength']}")
            st.write(f"**Ambition:** {player['ambition']}")
            st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
            st.write(f"**Coach's Remarks:** {player['coach_remarks']}")

            # Bar Chart
            df = pd.DataFrame({
                "Metric": ["Strength", "Ambition"],
                "Value": [player["strength"], player["ambition"]]
            })
            fig = px.bar(df, x="Metric", y="Value", color="Metric", title=f"{player['name']}'s Metrics")
            st.plotly_chart(fig, use_container_width=True)

            # Static Match Stats (demo)
            st.markdown("### Match Stats")
            st.write("📊 Possession: 65%")
            st.write("🥅 Attempts on Goal: 4")
            st.write("🏃‍♂️ Distance Covered: 6.5 km")
            st.write("🎯 Passes Completed: 32")
            st.write("🚫 Fouls Committed: 1")
            st.info("🔥 Heatmap: Coming soon")

# --- TRAINING DRILLS ---
elif menu == "Training Drills":
    st.subheader("🏋️ Training Drills")
    uploaded_file = st.file_uploader("Upload Drill Image or Video")
    description = st.text_area("Describe the drill")

    if uploaded_file and description:
        st.success("✅ Drill Uploaded!")
        if uploaded_file.name.endswith(".mp4"):
            st.video(uploaded_file)
        else:
            st.image(uploaded_file)
        st.write(f"📝 Description: {description}")

# --- MATCH ANALYSIS ---
elif menu == "Match Analysis":
    st.subheader("📊 Match Analysis")
    st.markdown("Upload or input match stats below.")

    possession = st.slider("Possession %", 0, 100, 50)
    attempts = st.number_input("Attempts on Goal", 0)
    corners = st.number_input("Corners", 0)
    fouls = st.number_input("Fouls Committed", 0)
    distance = st.number_input("Average Distance Covered (km)", 0.0)
    passes = st.number_input("Passes Completed", 0)

    if st.button("Analyze Match"):
        st.success("✅ Match stats analyzed")
        st.write(f"• Possession: {possession}%")
        st.write(f"• Attempts on Goal: {attempts}")
        st.write(f"• Corners: {corners}")
        st.write(f"• Fouls Committed: {fouls}")
        st.write(f"• Distance Covered: {distance} km")
        st.write(f"• Passes Completed: {passes}")

# --- TACTICAL BOARD ---
elif menu == "Tactical Board":
    st.subheader("📌 Tactical Board")
    st.markdown("Use this space to draw tactics or formations.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Pad")

# --- VIDEO ANALYSIS ---
elif menu == "Video Analysis":
    st.subheader("🎥 Video Analysis")
    video = st.file_uploader("Upload Match or Training Video")
    notes = st.text_area("Coach's Notes")

    if video:
        st.video(video)
    if notes:
        st.markdown("**📝 Coach Notes:**")
        st.info(notes)

