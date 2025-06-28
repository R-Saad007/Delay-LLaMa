import streamlit as st
import random
import requests

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Delay 🦙",
    page_icon="",
    layout="wide"
)

# -------------------------
# FULL BACKGROUND IMAGE CSS
# -------------------------
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://www.atlasair.com/wp-content/uploads/2023/09/boeing-747-400-vip-plus.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .card {
        background: rgba(20, 20, 20, 0.8);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.7);
        margin-top: 2rem;
        color: #f0f0f0;
        line-height: 1.6;
    }
    .card:hover {
    box-shadow: 0 0 20px rgba(0, 191, 255, 0.7);
    transform: translateY(-2px);
    transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)


# -------------------------
# HEADER
# -------------------------
st.markdown("""
<div style='position: relative; z-index: 2; text-align: center; color: #f0f0f0;'>
    <h1>Delay 🦙</h1>
    <p> Wisely predicts delays.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# INPUT SLIDERS WRAPPED IN CARD
# -------------------------
st.markdown("""
    <div class="card">
        <h3 style='text-align:center;'>🛠️ Set Current Weather Conditions</h3>
    </div>
""", unsafe_allow_html=True)
# Create three columns for input sliders
cols = st.columns(3)

with cols[0]:
    st.markdown("""
        <div class="card" style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/869/869869.png" width="50"><br>
            <p style="margin-top: 0.5rem;">Temperature (°C)</p>
    """, unsafe_allow_html=True)
    temp = st.slider("", -20.0, 50.0, 12.5,step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
        <div class="card" style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/4150/4150897.png" width="50"><br>
            <p style="margin-top: 0.5rem;">Wind Speed (knots)</p>
    """, unsafe_allow_html=True)
    wind_speed = st.slider("", 0.0, 50.0, 23.5, step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
        <div class="card" style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/2819/2819592.png" width="50"><br>
            <p style="margin-top: 0.5rem;">Visibility (km)</p>
    """, unsafe_allow_html=True)
    visibility = st.slider("", 0.0, 50.0, 2.4, step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# BUTTON & OUTPUT
# -------------------------
if st.button("🧠 Predict Delay & Generate Advisory"):
    data = {
        "temp": temp,
        "wind_speed": wind_speed,
        "visibility": visibility
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        result = response.json()

        # Format delay
        delay_min = result['predicted_delay_min']
        if delay_min >= 60:
            hrs = delay_min // 60
            mins = delay_min % 60
            delay_display = f"{hrs} hr {format(mins, '.1f')} min"

        else:
            delay_display = f"{format(delay_min, '.1f')} min"

        # -------------------------
        # SHOW PREDICTION CARD
        # -------------------------
        st.markdown(f"""
            <div class="card" style="text-align: center;">
                <h2>✈️ Predicted Flight Delay: {delay_display}</h2>
                <p><i>Based on current conditions: {temp}°C, Wind {wind_speed} knots, Visibility {visibility} km</i></p>
            </div>
        """, unsafe_allow_html=True)

        # -------------------------
        # ENRICHED COMBINED NOTE WITH NEW GROUND OPS DETAILS
        # -------------------------
        full_advisory = result['advisory']

        combined_note = (
            f"🛄 **Passenger Guidance:**\n\n"
            f"Stay alert for any last-minute scheduling changes. Keep essentials such as medications, chargers, and snacks handy. "
            f"Use airline mobile notifications and know flexible rebooking policies in case delays extend.\n\n"

            f"🧑‍✈️ **Pilot Operations:**\n\n"
            f"Review crosswind strategy and prepare for variable visibility on approach. Ensure thorough pre-flight checks "
            f"of alternate runways and coordinate closely with ATC for updated METAR/TAF briefings.\n\n"

            f"🏢 **Airport Ground Operations:**\n\n"
            f"- Prioritize fueling and catering trucks for this flight to minimize turnaround.\n"
            f"- Coordinate early pushback clearances with ground control to avoid ramp congestion.\n"
            f"- Ensure baggage handling is ready for priority loading.\n"
            f"- Cross-check deicing teams if temperatures near freezing.\n"
            f"- Communicate with cleaning and maintenance staff to expedite cabin readiness.\n\n"

            f"**✈️ AI Insights from Gemini:**\n\n"
            f"{full_advisory}"
        )

        # -------------------------
        # SHOW UNIFIED ADVISORY CARD
        # -------------------------
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="card">
                <h3>📌 Combined Advisory</h3>
                <p>{combined_note}</p>
            </div>
        """, unsafe_allow_html=True)

        
        # -------------------------
        # DOWNLOAD BUTTON
        # -------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="⬇️ Download Advisory Report",
            data=combined_note,
            file_name="Flight_Advisory_Report.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"🚨 Error connecting to backend: {e}")

