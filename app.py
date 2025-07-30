import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# -------------- Streamlit Page Config --------------
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# -------------- Sample Data --------------
players = [
    {"Name": "Ian", "Position": "Midfielder", "Goals": 5, "Assists": 7, "PassAccuracy": 85, "Dribbles": 12, "Minutes": 540, "Traits": "Visionary, Calm"},
    {"Name": "Willy", "Position": "Defender", "Goals": 1, "Assists": 2, "PassAccuracy": 90, "Dribbles": 3, "Minutes": 600, "Traits": "Aggressive, Vocal"},
    {"Name": "Sammy", "Position": "Striker", "Goals": 11, "Assists": 4, "PassAccuracy": 78, "Dribbles": 25, "Minutes": 480, "Traits": "Speedy, Confident"},
    {"Name": "Victor", "Position": "Goalkeeper", "Goals": 0, "Assists": 0, "PassAccuracy": 65, "Dribbles": 1, "Minutes": 630, "Traits": "Focused, Brave"},
    {"Name": "Branton", "Position": "Winger", "Goals": 6, "Assists": 5, "PassAccuracy": 80, "Dribbles": 18, "Minutes": 510, "Traits": "Creative, Agile"},
]

player_df = pd.DataFrame(players)

match_history = pd.DataFrame({
    "Match": ["Wosh FC vs Aces", "Wosh FC vs Stars", "Wosh FC vs Blaze"],
    "Result": ["2-1", "1-3", "0-0"],
    "Win": [1, 0, 0],
    "Loss": [0, 1, 0],
    "Draw": [0, 0, 1],
})

# -------------- Sidebar Navigation --------------
with st.sidebar:
    choice = option_menu("Wosh FC Dashboard", ["Home", "Player Profiles", "Team Stats", "Match History", "Training Suggestions"],
                         icons=["house", "person-circle", "bar-chart", "calendar3", "lightbulb"],
                         default_index=0)

# -------------- Home Page --------------
if choice == "Home":
    st.title("⚽ Wosh FC Analyzer")
    st.markdown("**From the Streets to the Stars 🌟**")
    st.image("https://i.imgur.com/3ZQ3Z2A.png", width=600)
    st.info("Welcome to the official Wosh FC Dashboard — track player performance, team growth, and prepare for greatness.")

# -------------- Player Profiles --------------
elif choice == "Player Profiles":
    st.title("👤 Player Profiles")
    selected_player = st.selectbox("Select Player", player_df["Name"])
    player_data = player_df[player_df["Name"] == selected_player].iloc[0]

    st.subheader(f"Stats for {selected_player}")
    st.metric("Goals", player_data["Goals"])
    st.metric("Assists", player_data["Assists"])
    st.metric("Pass Accuracy (%)", player_data["PassAccuracy"])
    st.metric("Dribbles", player_data["Dribbles"])
    st.metric("Minutes Played", player_data["Minutes"])

    st.success(f"Traits: {player_data['Traits']}")

    growth_tip = ""
    if player_data['PassAccuracy'] < 75:
        growth_tip += "Work on passing under pressure.\n"
    if player_data['Dribbles'] < 5:
        growth_tip += "Improve dribbling drills and creativity.\n"
    if player_data['Goals'] < 2:
        growth_tip += "Focus on finishing and composure in front of goal."

    st.warning("**Growth Recommendation:**\n" + (growth_tip if growth_tip else "Player is showing solid progress."))

# -------------- Team Stats --------------
elif choice == "Team Stats":
    st.title("📊 Team Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Scorers")
        fig = px.bar(player_df.sort_values("Goals", ascending=False), x="Name", y="Goals", color="Position")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Assist Leaders")
        fig2 = px.bar(player_df.sort_values("Assists", ascending=False), x="Name", y="Assists", color="Position")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Pass Accuracy vs Dribbles")
    fig3 = px.scatter(player_df, x="PassAccuracy", y="Dribbles", color="Position", size="Minutes", hover_name="Name")
    st.plotly_chart(fig3, use_container_width=True)

# -------------- Match History --------------
elif choice == "Match History":
    st.title("📅 Match History")
    st.dataframe(match_history)

    st.subheader("Match Results Overview")
    match_summary = match_history[["Win", "Loss", "Draw"]].sum()
    st.bar_chart(match_summary)

# -------------- Training Suggestions --------------
elif choice == "Training Suggestions":
    st.title("💡 Training Recommendations")

    st.markdown("Focus areas for the team based on performance data:")

    st.info("**Strikers** → Finishing drills, off-the-ball movement")
    st.info("**Midfielders** → Vision training, pass accuracy under pressure")
    st.info("**Defenders** → 1v1 defending, aerial dominance")
    st.info("**Goalkeepers** → Reaction time, command of box")

    st.warning("Set individual goals weekly and track improvements here!")





