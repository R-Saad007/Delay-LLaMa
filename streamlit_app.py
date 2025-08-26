import streamlit as st
import requests
import streamlit.components.v1 as components
import time
import streamlit as st

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
    <p style="margin-top: -15px;">Wisely Predicting Flight Delays Using AI</p>
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
            <p style="margin-top: 0.5rem;">Temperature (°F)</p>
    """, unsafe_allow_html=True)
    temp = st.slider("", -20.0, 150.0, 12.5,step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
        <div class="card" style="text-align:center;">
                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAdVBMVEX///8AAAAwMDDo6OjCwsKWlpaenp67u7t0dHTc3Nxra2urq6uysrL09PTw8PCZmZl/f3/R0dElJSVpaWnKysrY2Nj4+PhQUFBGRkY4ODjk5OQODg6CgoJgYGA8PDyMjIwdHR1LS0ssLCxXV1elpaUVFRUhISH7pxFpAAAEmElEQVR4nO3ca3OiMBiG4QatqKDioS3YKtrW/v+fuDg9LIdAojm+mef+2HVmuaaNaBLy8IAQQgghhBBC5luuCsY22ZPr6zBWyn6aur4SQ/0BGdu6vhYjPbNaseurMdGkLnxxfTUmeqkL2dL15RgoaghHri/HQBDSD0L6QUg/COkHIf0gpB+E9IOQfhA2Wo72s9lsT2uuQ1Y4zl6KzevPy05RvrZ4jWrJCVPWbmz1KlWSEr51gIEJky6wJUxKf/9qJYSLi1D4WP1k6umvVULYHYRcYVW2e7Zy0TclITxIC71cpBMLtzxgn7Dq+OnXL1IkHDVfICGsmvr0viMQ7vg+gbD6Rabe/CKHhas+oEjI2FfpyYe7QeG8FygWMrayyBhoQNg3BGWFE6uQ3vqF4wFfEMIJ76JDEvLvguEIB4dgCMLeu2AoQsEQvE/obAqII+R+0lYWpiy1p6rXEe6PMsDbhXH1xSNx8VGuLZQYgncLGYsSm7bvmsKFzBBUEDL2+mlTd60pfOFcqF7h9ecLm8AH4Y1Pv5Cx0uYbq1hYcj/eKAmr78gzf4QJ/zuUopCxw84P4Wnd8y1RWVi9sX5aGZDDwvP1e7opYZWNN9ZB4ffedoNCG5vnh4Q/t+dghZffKcFQhfnfVJk14SyaJru9LWH2/yX2hN8/fP/IJkkax+M4TpNV+al4W+kR1j8h2xYOX40e4aUxK+9eyOaahXlzttoDISu1CrPWS3wQKuyD6Qo7nzO8ED5qE166C2NeCHNdwiNnwcgLYaRJyP2MEZSQu+QXlJD7jgUhhBBCCOFNwoJHDErI3TcamJCzchuakB2CF7JjazIoPCFjzbmfEIXNLWlBCtm8tuIeprA+GAMV1gZjsMK/wRiu8HcwBixk0TJ04fdg9EJYmBJeL9ML4f0rjcK9GFs/hPc/wSHeT3PmbpSyLFQ4hczJnqibhe8K+1KaQu6Vuhd+qDyc0przfnrt+U8cCgu1BxvbM1HL3DPhl+pRh925tswnYaF+lCNnNpH32K8b4YeOB29586VricFoQahphyZ3RnghHoymhV/aNi72zHkLB6NR4UnnQ6h9s/qiwWhQOI+17jvtXbd4ciOcxrqfyehfmRkejCaEeyMnMwytPQ0NRqq7L1tLT9zTFKSFzeeAuUKV/WqyDa8f9g9GrjDalpMkHe92u3GcTpp/crPHx/Itmx8+zsdoc63ID1Mbh08LVkgXZynhJC/jtd1HYaQTrgH3DEZPDzLhJF7l5t8ZQxLKzNP43L1COgfUSwg5t4JN6enbCicJYeeWcabzJ/ogdxJW89HnufYnIswmI1yc/r8iI+aTPK9tVPz8+8Heg5HakjxVMN4ei/zNu1OuZMLZl/SDkH4Q0g9C+kFIPwjpByH9IKQfhPSDkH4Q0g9C+kFIPwjpByH9IKQfhPSDkH4Q0g9C+kFIPwjpByH9IKQfhPSDkH4Q0g9C+kFIPwjpByH9IKQfhPSDkH4Q0g9C+kFIv+YxyCqn2frapA5UOHHZ357rQjpHI91S7Vw9GyfgueiPaOMQQzctV0fGNhnJw2cQQgghhBBCSF//AJwQRkFLOSqoAAAAAElFTkSuQmCC" width="50"><br>
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
    visibility = st.slider("", 0.0, 10.0, 2.4, step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# BUTTON & OUTPUT
# -------------------------
result_placeholder = st.empty()
if st.button("🧠 Predict Delay & Generate Advisory"):
    with st.spinner("🛫 Running ML and GenAI models to predict delay and generate advisory..."):
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
                f"🛄 Passenger Guidance:\n\n"
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
            st.markdown("<br>", unsafe_allow_html=True)
            
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
