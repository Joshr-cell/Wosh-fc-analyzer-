import streamlit as st
import pandas as pd
from datetime import date
import base64
import time

# --- App Config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Custom CSS for FIFA-like UI ---
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #ffffff;
            font-weight: 700;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            transition: transform 0.2s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #005dc1;
        }
        .stSlider > div {
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 10px;
        }
        header[data-testid="stHeader"] {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 999;
            background-color: #0e1117;
            border-bottom: 1px solid #444;
        }
        section[data-testid="stSidebar"] {
            position: fixed;
            top: 3.5rem;
            height: 100%;
            overflow-y: auto;
        }
        .block-container {
            margin-top: 4rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Session Initialization ---
if 'player_data' not in st.session_state:
    st.session_state.player_data = {}
if 'bg_image' not in st.session_state:
    st.session_state.bg_image = None

# --- Background Image Upload ---
st.sidebar.markdown("### 🖼️ App Background")
bg_choice = st.sidebar.radio("Choose Background", ["None", "Upload Image", "Enter Image URL"])
if bg_choice == "Upload Image":
    bg_upload = st.sidebar.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg"])
    if bg_upload:
        st.session_state.bg_image = bg_upload
elif bg_choice == "Enter Image URL":
    bg_url = st.sidebar.text_input("Paste Image URL")
    if bg_url:
        st.session_state.bg_image = bg_url

# --- Set Background Function ---
def set_background(image_file_or_url):
    if isinstance(image_file_or_url, str):
        bg_url = image_file_or_url
    else:
        bg_bytes = image_file_or_url.read()
        bg_base64 = base64.b64encode(bg_bytes).decode()
        bg_url = f"data:image/png;base64,{bg_base64}"
    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)

if st.session_state.bg_image:
    set_background(st.session_state.bg_image)

# --- Sidebar Logo Upload ---
st.sidebar.markdown("### 🖼️ Upload Wosh FC Logo")
logo = st.sidebar.file_uploader("Choose Logo Image", type=["png", "jpg", "jpeg"])
if logo:
    st.image(logo, width=180)
else:
    st.sidebar.markdown("_No logo uploaded_")

# --- Title ---
st.title("\u26bd Wosh FC Analyzer")
st.markdown("##### _From the Streets to the Stars_ \ud83c\udf1f")

# --- Tactical Section ---
st.header("\ud83c\udfaf Tactical Identity")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("\ud83d\udfe2 Build-Up")
    st.text_input("Build-Up Style", "Slow Build-Up")
    st.text_input("Width", "Balanced")
    st.text_area("Key Roles", "Fullbacks stay back, Midfielders drop deep")
with col2:
    st.subheader("\ud83d\udd35 Chance Creation")
    st.text_input("Chance Creation Style", "Possession")
    st.text_input("Support Type", "Support Runs")
    st.text_input("Players in Box", "Moderate")
with col3:
    st.subheader("\ud83d\udfe1 Defense")
    st.text_input("Shape", "Mid Block")
    st.text_input("Pressure Trigger", "On Heavy Touch")
    st.text_input("Line Height", "Medium")
st.text_area("\ud83d\udccc Tactical Notes", """
- Control the tempo of the game
- Maintain short passing triangles
- Force mistakes in the midfield
- Patience over panic
- Wingers drop to receive in buildup
""")

# --- Team Selection ---
teams = {"Under 7": ["Fidel", "Kijokilangs", "Kasmall"]}
attrs = ["Pace", "Shooting", "Passing", "Dribbling", "Defending", "Physical"]
tab = st.sidebar.selectbox("Select Age Group", list(teams.keys()))

# --- Player Panels ---
if tab in teams:
    st.header(f"\ud83c\udf93 {tab} Player Profiles")
    for player in teams[tab]:
        with st.expander(f"\u25b6\ufe0f {player}"):
            key = f"{tab}_{player}"
            if key not in st.session_state.player_data:
                st.session_state.player_data[key] = {"stats": {}, "notes": ""}
            for attr in attrs:
                val = st.slider(f"{attr} - {player}", 0, 100, 70)
                st.session_state.player_data[key]["stats"][attr] = val
            st.session_state.player_data[key]["notes"] = st.text_area(f"Notes - {player}")

    # Save Button with Spinner
    if st.button("\ud83d\udd10 Save All Players"):
        with st.spinner("Saving all data..."):
            time.sleep(2)  # simulate save delay
        st.success("All player data saved!")

# --- Floating Save Button CSV ---
if st.button("\ud83d\udcc5 Export to CSV"):
    rows = []
    for k, v in st.session_state.player_data.items():
        name = k.split("_")[1]
        row = {"Player": name, **v["stats"], "Notes": v["notes"]}
        rows.append(row)
    df = pd.DataFrame(rows)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("\ud83d\udcc4 Download CSV", csv, "wosh_fc_data.csv", "text/csv")

