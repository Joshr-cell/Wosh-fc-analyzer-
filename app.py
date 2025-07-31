# Wosh FC Visual Dashboard - Python + Streamlit
# ---------------------------------------------
# Inspired by PES 2014 / PS2 style with player panels and match stat input.

import streamlit as st
import random
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# --- Firebase Setup (requires your serviceAccountKey.json file) ---
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- CONFIG ---
st.set_page_config(page_title="Wosh FC Dashboard", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    body {
        background-color: #0d1117;
        color: white;
        font-family: 'Arial';
    }
    .player-card {
        background: linear-gradient(145deg, #1f1f1f, #2e2e2e);
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        text-align: center;
        color: #ffffff;
        margin: 10px;
    }
    .stat-bar {
        background: #333;
        height: 10px;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    .stat-fill {
        height: 100%;
        background: #00ff00;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- PLAYER DATA ---
players = {
    "Under 7": ["Fidel", "Kijokilangs", "Kasmall", "Izo", "Matthew", "Biden", "Ramadhan", "Riya", "David", "Iman", "Moses", "Priest", "Lewis", "Deno"],
    "Under 11": ["Willy", "Evans", "Dan", "Jayjen", "Alvin", "Chacha", "Stivo", "Emmanuel", "Ngesa", "Imani", "John", "Biden"],
    "Under 14": ["Byron", "Mokaya", "Branton", "Sakwa", "Victor", "Pasi", "Samuel", "Ole", "Samson", "Munene", "Moses", "Godfrey", "Messi Kiptoo", "Elvis Chacha"],
    "Under 15": ["Massai", "Brighton", "Ponic", "Mutua", "Turu", "Frank", "Zablon", "Joseph"]
}

# --- FUNCTIONS ---
def random_stat():
    return random.randint(30, 100)

def display_player(name, age_group):
    pic_url = f"https://picsum.photos/seed/{name}/100/100"
    stats = {"Pace": random_stat(), "Passing": random_stat(), "Shooting": random_stat(), "Defense": random_stat()}

    with st.container():
        st.markdown(f"""
        <div class='player-card'>
            <img src='{pic_url}' width='100' style='border-radius: 50%;'>
            <h4>{name}</h4>
            <p><b>Group:</b> {age_group}</p>
        """, unsafe_allow_html=True)

        for stat, value in stats.items():
            st.markdown(f"""
                <div>{stat}: {value}</div>
                <div class='stat-bar'>
                    <div class='stat-fill' style='width: {value}%'></div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<p><b>Improvement Area:</b> Stamina / Team Play</p></div>", unsafe_allow_html=True)

        # Firebase Save
        doc_ref = db.collection("players").document(name)
        doc_ref.set({
            "name": name,
            "age_group": age_group,
            "stats": stats,
            "updated": datetime.now()
        })

# --- DISPLAY ---
st.title("⚽ Wosh FC Player Development Dashboard")
for group, names in players.items():
    st.header(f"{group}")
    cols = st.columns(4)
    for i, name in enumerate(names):
        with cols[i % 4]:
            display_player(name, group)

# --- MATCH ANALYSIS PANEL ---
st.markdown("---")
st.subheader("📊 Match Analysis Input")
match_data = {
    "Game Date": st.date_input("Match Date"),
    "Opponent": st.text_input("Opponent Team"),
    "Goals Scored": st.number_input("Goals Scored", 0),
    "Goals Conceded": st.number_input("Goals Conceded", 0),
    "Possession %": st.slider("Possession", 0, 100),
    "Shots on Target": st.number_input("Shots on Target", 0),
    "Tackles": st.number_input("Tackles", 0),
    "Corners": st.number_input("Corners", 0),
    "Fouls": st.number_input("Fouls", 0),
    "Notes": st.text_area("Game Notes")
}

if st.button("📥 Save Match Report"):
    db.collection("match_reports").add({"data": match_data, "timestamp": datetime.now()})
    st.success("Saved to Firebase!")

# --- EXPORT SECTION ---
if st.button("⬇️ Download All Match Reports"):
    all_reports = db.collection("match_reports").stream()
    reports_text = ""
    for r in all_reports:
        d = r.to_dict()
        reports_text += f"\n\nDate: {d['data'].get('Game Date')}\nOpponent: {d['data'].get('Opponent')}\nGoals: {d['data'].get('Goals Scored')} - {d['data'].get('Goals Conceded')}\nNotes: {d['data'].get('Notes')}"

    st.download_button("Download Report", reports_text, file_name="woshfc_match_reports.txt")

