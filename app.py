import streamlit as st
import pandas as pd
from datetime import date
# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- PLAYER DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Goals": 3, "Assists": 5, "Traits": "Visionary, Calm", "Ambition": "Play for AFC Leopards"},
    {"Name": "Willy", "Position": "Defender", "Goals": 1, "Assists": 2, "Traits": "Tactical, Tough", "Ambition": "Be a coach"},
    {"Name": "Sammy", "Position": "Striker", "Goals": 8, "Assists": 1, "Traits": "Fast, Finisher", "Ambition": "Play abroad"},
    {"Name": "Branton", "Position": "Midfielder", "Goals": 4, "Assists": 6, "Traits": "Creative, Confident", "Ambition": "Join national team"},
    {"Name": "Samson", "Position": "Goalkeeper", "Goals": 0, "Assists": 0, "Traits": "Brave, Vocal", "Ambition": "Be Kenya 1"},
    {"Name": "Pasi", "Position": "Winger", "Goals": 6, "Assists": 4, "Traits": "Skilful, Agile", "Ambition": "Play in Europe"},
    {"Name": "Ole", "Position": "Midfielder", "Goals": 2, "Assists": 3, "Traits": "Smart, Composed", "Ambition": "Coach kids"},
    {"Name": "Byron", "Position": "Defender", "Goals": 1, "Assists": 1, "Traits": "Hardworking", "Ambition": "Play for Gor Mahia"},
    {"Name": "Munene", "Position": "Striker", "Goals": 7, "Assists": 2, "Traits": "Strong, Sharp", "Ambition": "Be pro"},
    {"Name": "Victor", "Position": "Winger", "Goals": 5, "Assists": 3, "Traits": "Speedster", "Ambition": "Travel the world"},
    {"Name": "Mose", "Position": "Midfielder", "Goals": 2, "Assists": 2, "Traits": "Quiet leader", "Ambition": "Coach someday"},
    {"Name": "Jamo", "Position": "Striker", "Goals": 4, "Assists": 1, "Traits": "Bold, Brave", "Ambition": "Play in KPL"},
]

player_df = pd.DataFrame(players)

# --- PLAYER TABLE ---
with st.expander("📋 Full Player Stats"):
    st.dataframe(player_df)

# --- TOP SCORERS CHART ---
top_scorers = player_df.sort_values(by="Goals", ascending=False).head(10)
fig = px.bar(top_scorers, x="Name", y="Goals", color="Position",
             title="🌟 Top 10 Goal Scorers - Wosh FC", text="Goals", template="plotly_dark")
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

# --- MATCH ANALYSIS SECTION ---
st.markdown("## 📊 Match Analysis")
with st.form("match_form"):
    match_date = st.date_input("Match Date")
    opponent = st.text_input("Opponent Team")
    possession = st.slider("Possession %", 0, 100, 50)
    passes = st.number_input("Passes Completed", min_value=0)
    shots = st.number_input("Shots on Target", min_value=0)
    fouls = st.number_input("Fouls Committed", min_value=0)
    corners = st.number_input("Corners Taken", min_value=0)
    submitted = st.form_submit_button("Save Match Stats")

    if submitted:
        st.success(f"✅ Match against {opponent} on {match_date} recorded.")
        st.write("**Summary:**")
        st.write(f"Possession: {possession}%")
        st.write(f"Passes: {passes}, Shots: {shots}, Fouls: {fouls}, Corners: {corners}")

# --- PLAYER DEVELOPMENT TRACKING ---
st.markdown("## 🚀 Player Development")
selected_player = st.selectbox("Choose a Player", player_df["Name"].unique())
st.write(f"Tracking development for **{selected_player}**")

col1, col2, col3 = st.columns(3)
with col1:
    stamina = st.slider("Stamina", 0, 100, 50)
with col2:
    confidence = st.slider("Confidence", 0, 100, 50)
with col3:
    discipline = st.slider("Discipline", 0, 100, 50)

coach_notes = st.text_area("Coach Notes", placeholder="Write observations here...")

if st.button("Save Development Record"):
    st.success("✅ Player development record saved.")
    st.write(f"**Stamina:** {stamina}, **Confidence:** {confidence}, **Discipline:** {discipline}")
    if coach_notes:
        st.markdown(f"**Coach Notes:** {coach_notes}")

# --- FOOTER ---
st.markdown("---")
st.caption(f"Last updated: {date.today()} | Powered by Waves of Street Hope 💙")


