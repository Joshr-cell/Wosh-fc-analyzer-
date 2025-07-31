def render_player_panel(player):
    name = player["Name"]

    with st.expander(f"{name}'s Panel"):
        st.subheader(f"🎽 {name} - Player Report")

        # --- Basic Stats ---
        col1, col2, col3 = st.columns(3)
        with col1:
            goals = st.number_input(f"Goals", min_value=0, key=f"goals_{name}")
        with col2:
            assists = st.number_input(f"Assists", min_value=0, key=f"assists_{name}")
        with col3:
            saves = st.number_input(f"Saves (if GK)", min_value=0, key=f"saves_{name}")

        # --- Ratings ---
        st.markdown("**🔢 Rate the Player (1-10)**")
        col4, col5, col6 = st.columns(3)
        with col4:
            pace = st.slider("Pace", 1, 10, key=f"pace_{name}")
        with col5:
            shooting = st.slider("Shooting", 1, 10, key=f"shooting_{name}")
        with col6:
            passing = st.slider("Passing", 1, 10, key=f"passing_{name}")

        # --- Area of Improvement ---
        st.markdown("**🛠️ Area of Improvement**")
        improvement_area = st.text_area("Write specific areas", key=f"improvement_{name}")

        # --- Video Analysis Upload ---
        st.markdown("**🎥 Upload Match Video**")
        uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "mov"], key=f"video_{name}")

        # --- Downloadable Report Button (Mocked) ---
        st.download_button(
            label="📄 Download Match Report",
            data=f"{name}'s report\nGoals: {goals}\nAssists: {assists}\nImprovement: {improvement_area}",
            file_name=f"{name}_match_report.txt",
            mime="text/plain"
        )
