# Wosh-fc-analyzer-
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

st.title("⚽ Wosh FC Player Analyzer")
st.subheader("From the Streets to the Stars")

# Sample player data
data = {
    "Player": ["Zekiah Roy", "Randy Kamau", "Telo", "Axel Abisai", "Dylan", "Bowen"],
    "Position": ["Midfielder", "Striker", "Winger", "Defender", "Goalkeeper", "Midfielder"],
    "Strength": ["Leadership", "Finishing", "Courage", "Confidence", "Discipline", "Improved"],
    "Target": ["Dana Cup", "Local League", "Wosh Academy", "International Scouts", "Club Level", "Training Consistency"],
    "Ambition": ["Pro Player", "Top Scorer", "Rising Star", "National Team", "Discipline Role Model", "Consistent Starter"]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

# Charts
st.subheader("📊 Player Ambition Distribution")
ambition_counts = df["Ambition"].value_counts()
st.bar_chart(ambition_counts)

# Add new player
st.subheader("➕ Add a New Player")
with st.form("new_player_form"):
    name = st.text_input("Player Name")
    position = st.selectbox("Position", ["Striker", "Midfielder", "Defender", "Winger", "Goalkeeper"])
    strength = st.text_input("Strength")
    target = st.text_input("Target")
    ambition = st.text_input("Ambition")
    submit = st.form_submit_button("Add Player")

    if submit and name:
        new_row = {"Player": name, "Position": position, "Strength": strength, "Target": target, "Ambition": ambition}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Player {name} added successfully!")

        st.dataframe(df, use_container_width=True)
