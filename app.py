import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Background Image ---
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpeg;base64,{encoded_string}");
             background-size: cover;
             background-position: center;
         }}
         </style>
         """, unsafe_allow_html=True)

set_background("background.jpeg")  # ← Your background image here

# --- Header Logo ---
st.image("background.jpeg", width=150)  # Use same image as logo for now
st.title("⚽ Wosh FC Analyzer")
st.markdown("From the streets to the stars 🌟")

# --- Browser-Based Voice Assistant (JS) ---
st.markdown("""
    <script>
    function speak(text) {
        var msg = new SpeechSynthesisUtterance();
        msg.text = text;
        window.speechSynthesis.speak(msg);
    }
    </script>
""", unsafe_allow_html=True)

# --- Voice Input Prompt ---
if st.button("🎙️ Welcome Message"):
    st.markdown('<script>speak("Welcome to Wosh FC Analyzer. Let\'s build champions from the streets to the stars.")</script>', unsafe_allow_html=True)

# --- Sample Data Section ---
players = [
    {"Name": "Ian", "Position": "Midfielder", "Goals": 5},
    {"Name": "Randy", "Position": "Striker", "Goals": 8},
    {"Name": "Zekiah", "Position": "Defender", "Goals": 2},
]
st.subheader("Player Stats")
for player in players:
    st.markdown(f"**{player['Name']}** – {player['Position']}, Goals: {player['Goals']}")

