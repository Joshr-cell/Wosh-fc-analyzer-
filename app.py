import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Header ---
st.title("⚽ Wosh FC Analyzer App")
st.markdown("Analyze, Train, and Improve Players from U7 to U16")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigate", [
    "Home", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Analysis"
])
st.sidebar.markdown("👥 Total Players: 3")  # Update this as player count increases

# --- Sample Players Data ---
players = [
    {"name": "Munene", "team": "Under 14", "strength": 80, "ambition": 90, "area_of_improvement": "Passing", "coach_remarks": "Very disciplined."},
    {"name": "Byron", "team": "Under 14", "strength": 75, "ambition": 85, "area_of_improvement": "Tackling", "coach_remarks": "Shows improvement weekly."},
    {"name": "Victor", "team": "Under 14", "strength": 72, "ambition": 88, "area_of_improvement": "Positioning", "coach_remarks": "Needs confidence."},
]

# --- HOME ---
if menu == "Home":
    st.subheader("🏠 Welcome to Wosh FC")
    st.markdown("""
    This platform helps Wosh FC monitor, evaluate, and develop youth players across different age categories:
    - **Under 7**: 12 players
    - **Under 10**: 12 players
    - **Under 12**: 12 players
    - **Under 14**: 12 players
    - **Under 16**: 7 players

    Use the sidebar to navigate through player data, training drills, match analysis, and more.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Wosh FC Tactical Layout")

# --- PLAYER PROFILES ---
elif menu == "Players":
    st.subheader("👥 Player Profiles")

    for player in players:
        with st.expander(player['name']):
            st.write(f"**Team:** {player['team']}")
            st.write(f"**Strength:** {player['strength']}")
            st.write(f"**Ambition:** {player['ambition']}")
            st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
            st.write(f"**Coach's Remarks:** {player['coach_remarks']}")

            df = pd.DataFrame({
                'Metric': ['Strength', 'Ambition'],
                'Value': [player['strength'], player['ambition']]
            })
            fig = px.bar(df, x='Metric', y='Value', title=f"{player['name']}'s Metrics", color='Metric')
            st.plotly_chart(fig)

            st.markdown("### Match Stats")
            st.write("• Possession: 65%")
            st.write("• Attempts on Goal: 4")
            st.write("• Distance Covered: 6.5 km")
            st.write("• Passes Completed: 32")
            st.write("• Fouls Committed: 1")
            st.info("🔥 Heatmap: Coming Soon")

# --- TRAINING DRILLS ---
elif menu == "Training Drills":
    st.subheader("🏋️ Training Drills")
    uploaded_file = st.file_uploader("Upload Drill Image/Video")
    description = st.text_area("Describe the Drill")

    if uploaded_file and description:
        st.success("✅ Drill Uploaded!")
        if uploaded_file.name.endswith('.mp4'):
            st.video(uploaded_file)
        else:
            st.image(uploaded_file)
        st.markdown(f"**Drill Description:** {description}")

# --- MATCH ANALYSIS ---
elif menu == "Match Analysis":
    st.subheader("📊 Match Analysis")
    st.markdown("Enter post-match stats to get visual insights.")

    possession = st.slider("Possession %", 0, 100, 50)
    attempts = st.number_input("Attempts on Goal", 0)
    corners = st.number_input("Corners", 0)
    fouls = st.number_input("Fouls Committed", 0)
    distance = st.number_input("Average Distance Covered (km)", 0.0)
    passes = st.number_input("Passes Completed", 0)

    if st.button("Analyze"):
        st.success("Analysis Complete ✅")
        st.write(f"• Possession: {possession}%")
        st.write(f"• Attempts on Goal: {attempts}")
        st.write(f"• Corners: {corners}")
        st.write(f"• Fouls: {fouls}")
        st.write(f"• Distance Covered: {distance} km")
        st.write(f"• Passes Completed: {passes}")

# --- TACTICAL BOARD ---
elif menu == "Tactical Board":
    st.subheader("📌 Tactical Board")
    st.markdown("Draw tactics or formations here.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Pad - Visualize Formations")

# --- VIDEO ANALYSIS ---
elif menu == "Video Analysis":
    st.subheader("🎥 Video Analysis")
    video = st.file_uploader("Upload Match or Training Video")
    notes = st.text_area("Coach's Notes")

    if video:
        st.video(video)
    if notes:
        st.markdown("**Coach Notes:**")
        st.info(notes)
