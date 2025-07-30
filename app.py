import streamlit as st
import pandas as pd


# --- Streamlit Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Header ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- Sample Data (Edit this with real data or load from a database) ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Arsenal", "Goals": 5},
    {"Name": "Randy", "Position": "Striker", "Traits": "Technical, Fast", "Ambition": "Top scorer in Europe", "Goals": 10},
    {"Name": "Mungai", "Position": "Goalkeeper", "Traits": "Brave, Sharp reflexes", "Ambition": "Best goalkeeper", "Goals": 0},
    {"Name": "Zekiah", "Position": "Defender", "Traits": "Leader, Smart", "Ambition": "Captain Kenya", "Goals": 2},
    {"Name": "Telo", "Position": "Winger", "Traits": "Creative, Fast", "Ambition": "Play in La Liga", "Goals": 6},
    {"Name": "Axel", "Position": "Midfielder", "Traits": "Confident, Skillful", "Ambition": "Be a global star", "Goals": 3}
]

player_df = pd.DataFrame(players)

# --- Menu ---
tabs = st.tabs(["Player Profiles", "Stats", "About Wosh FC"])

# --- Tab 1: Player Profiles ---
with tabs[0]:
    st.header("👟 Player Profiles")
    for i, player in player_df.iterrows():
        with st.expander(f"{player['Name']} - {player['Position']}"):
            st.markdown(f"**Traits:** {player['Traits']}")
            st.markdown(f"**Ambition:** {player['Ambition']}")
            st.markdown(f"**Goals Scored:** {player['Goals']}")

# --- Tab 2: Stats ---
with tabs[1]:
    st.header("📊 Team Stats")

    # Bar chart of top scorers
    try:
        if "Goals" in player_df.columns:
            fig = px.bar(
                player_df.sort_values(by="Goals", ascending=False),
                x="Name", y="Goals", color="Position",
                title="Top Scorers", text="Goals"
            )
            fig.update_layout(xaxis_title="Player", yaxis_title="Goals")
            st.plotly_chart(fig)
        else:
            st.warning("Goal stats not available for players.")
    except Exception as e:
        st.error(f"Error in chart: {e}")

# --- Tab 3: About ---
with tabs[2]:
    st.header("🌍 About Wosh FC")
    st.markdown("""
        **Wosh FC** is a community-driven football club based in Kenya, committed to transforming the lives of young boys through football.  
        We believe in providing opportunities, nurturing talent, and giving boys from underserved communities a path to success — both on and off the pitch.

        - 🏆 Focused on discipline, teamwork, and personal growth  
        - 📈 Providing international exposure and tournament opportunities  
        - 🤝 Partnered with Makadara Children Centre and Waves of Street Hope

        _Join us on our journey from the streets to the stars._
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Football_iu_1996.jpg/640px-Football_iu_1996.jpg", width=500)




