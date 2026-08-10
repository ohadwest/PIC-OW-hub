import streamlit as st

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="Silicon Photonics Simulation Hub",
    page_icon="⚡",
    layout="wide"
)

# עיצוב מותאם אישית (CSS) לשפור המראה והפונטים
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #4B5563;
        margin-bottom: 2.5rem;
    }
    .stLinkButton > a {
        width: 100%;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת ראשית ותיאור
st.markdown('<div class="main-title">🔬 Silicon Photonics Simulation Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">מרכז הסימולציות האופטיות – בחר את הכלי המבוקש למעבר למחשבון ייעודי</div>', unsafe_allow_html=True)

st.divider()

# יצירת גריד של 2x2 כרטיסיות עבור 4 המחשבונים
col1, col2 = st.columns(2, gap="large")

with col1:
    # 1. פתרון מוד רגיל
    with st.container(border=True):
        st.subheader("📐 1. פתרון מוד רגיל (FDE Standard)")
        st.markdown("""
        **מאפיינים עיקריים:**
        * חישוב אופני התפשטות במוליך גל מלבני קלאסי ($Si / SiN$).
        * חילוץ מקדמי שבירה אפקטיביים ($n_{\\text{eff}}$), $n_g$ ושטח מוד אפקטיבי ($A_{\\text{eff}}$).
        * פרופיל שדה דו-ממדי וחד-ממדי בקיטוב TE ו-TM.
        """)
        st.link_button(
            "🚀 פתח מחשבון מוד רגיל",
            "https://pic-mode-solver-ohadwest.streamlit.app/",
            use_container_width=True
        )

    st.write("") # רווח אנכי

    # 3. פתרון מצמד סימטרי
    with st.container(border=True):
        st.subheader("⚡ 3. מצמד כיווני סימטרי (Symmetric DC)")
        st.markdown("""
        **מאפיינים עיקריים:**
        * אנליזת אופני-על סימטריים ואנטי-סימטריים ($Even / Odd Supermodes$).
        * חישוב מקדם הצימוד $\\kappa$ ואורך הצימוד $L_c$.
        * מעבר הספק מלא ודינמיקת צימוד לאורך הרכיב.
        """)
        st.link_button(
            "🚀 פתח מחשבון מצמד סימטרי",
            "https://pic-coupler-simulator-ohadwest.streamlit.app/",
            use_container_width=True
        )

with col2:
    # 2. פתרון מוד מתקדם
    with st.container(border=True):
        st.subheader("🌀 2. פתרון מוד מתקדם (Trapezoid / Bending)")
        st.markdown("""
        **מאפיינים עיקריים:**
        * תמיכה בחתך רוחב טרפזי (Sidewall Angle / Etch Profile).
        * התחשבות ברדיוס קימור רזונטור ($Ring\ Resonator\ Bending$).
        * מפת מקדם שבירה מורכב ואיבודי הקרנה ($Bending\ Losses$).
        """)
        st.link_button(
            "🚀 פתח מחשבון מוד מתקדם",
            "https://pic-mode-solver-davanced-ohadwest.streamlit.app/",
            use_container_width=True
        )

    st.write("") # רווח אנכי

    # 4. פתרון מצמד לא סימטרי
    with st.container(border=True):
        st.subheader("🌊 4. מצמד לא סימטרי (Asymmetric ADC)")
        st.markdown("""
        **מאפיינים עיקריים:**
        * ניתוח צימוד בין מוליכי גל ברוחבים שונים ($w_1 \\neq w_2$).
        * חישוב אי-התאמה בפאזה ($Phase\ Mismatch\ \\Delta\\beta$).
        * הכללת מקדם צימוד מקסימלי, ספקטרום ואנליזת הדיסמצ'.
        """)
        st.link_button(
            "🚀 פתח מחשבון מצמד לא סימטרי",
            "https://asymmetric-directional-coupler-ohadwest.streamlit.app/",
            use_container_width=True
        )

st.divider()

# פוטר בתחתית הדף
st.caption("Developed for Silicon Photonics Research & Engineering | Powered by Streamlit Community Cloud")
