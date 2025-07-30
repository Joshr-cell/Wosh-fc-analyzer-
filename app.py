import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wosh FC | From Streets to Stars", layout="wide")

# --- HEADER ---
st.title("⚽ Wosh FC Analyzer")
st.markdown("### From the Streets to the Stars 🌟")
st.markdown("Empowering youth through football under Waves of Street Hope")

# --- SIDEBAR ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Players", "Stats Dashboard", "Support Us", "Contact"])

# --- DATA ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Traits": "Visionary, Calm", "Ambition": "Play for Harambee Stars", "Goals": 4},
    {"Name": "Willy", "Position": "Defender", "Traits": "Aggressive, Vocal", "Ambition": "Coach in future", "Goals": 1},
    {"Name": "Sammy", "Position": "Goalkeeper", "Traits": "Reliable, Brave", "Ambition": "Be a pro keeper", "Goals": 0},
    {"Name": "Victor", "Position": "Striker", "Traits": "Sharp, Fast", "Ambition": "Play in Europe", "Goals": 7},
    {"Name": "Jamo", "Position": "Winger", "Traits": "Creative, Confident", "Ambition": "Be a coach and a player", "Goals": 5},
]
player_df = pd.DataFrame(players)

# --- HOME PAGE ---
if page == "Home":
    st.image("https://i.imgur.com/UYiroysl.jpg", use_column_width=True)
    st.markdown("""
    ### Our Story
    Wosh FC is a community-driven football club nurturing street-connected youth with purpose and passion.

    We believe in second chances, talent development, and building a better future through sport. 
    "From the Streets to the Stars" is not just our motto — it's our mission.
    """)
    st.success("Currently training 40+ youth with 3 different age groups")
    st.info("Follow us on TikTok, Instagram & YouTube for match updates and behind-the-scenes content.")

# --- PLAYERS PAGE ---
elif page == "Players":
    st.subheader("👥 Meet Our Players")
    selected_position = st.selectbox("Filter by position", ["All"] + list(player_df["Position"].unique()))
    if selected_position != "All":
        filtered_df = player_df[player_df["Position"] == selected_position]
    else:
        filtered_df = player_df
    st.dataframe(filtered_df.drop(columns=["Goals"]))

# --- STATS PAGE ---
elif page == "Stats Dashboard":
    st.subheader("📊 Player Stats")
    fig = px.bar(player_df, x="Name", y="Goals", color="Position", title="Top Scorers")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Motivational Quote")
    st.code("\"Talent wins games, but teamwork and intelligence win championships.\" – Michael Jordan")

# --- SUPPORT PAGE ---
elif page == "Support Us":
    st.subheader("💖 Support Wosh FC")
    st.markdown("""
    Help us empower youth through football:

    - Donate equipment (boots, kits)
    - Sponsor a player
    - Fund transport for matches

    M-PESA Paybill: `123456`  
    PayPal: `wavesofstreethope@gmail.com`
    """)
    st.image("https://i.imgur.com/8zjGQpT.jpg", caption="Training session at Wosh FC", use_column_width=True)

# --- CONTACT PAGE ---
elif page == "Contact":
    st.subheader("📬 Contact Us")
    st.markdown("""
    Have questions, want to volunteer or collaborate?

    - WhatsApp: [+254 702 816 585](https://wa.me/254702816585)
    - Email: [wavesofstreethope@gmail.com](mailto:wavesofstreethope@gmail.com)
    - Instagram: [@woshfc](https://instagram.com)
    """)

    st.text_input("Your Name")
    st.text_area("Your Message")
    st.button("Send Message")


