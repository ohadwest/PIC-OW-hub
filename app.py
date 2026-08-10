import streamlit as st

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="Silicon Photonics Hub",
    page_icon="🔬",
    layout="wide"
)

# הזרקת עיצוב מותאם אישית (CSS) למראה היי-טקי (Tidy3D / Lumerical Aesthetic)
st.markdown("""
<style>
    /* ייבוא גופנים נקיים ואסתטיים */
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;600;800&family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Heebo', sans-serif;
    }
    
    /* כותרת ראשית עם אפקט גרדיאנט */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00d2ff 0%, #9D4EDD 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 1rem;
    }
    
    .sub-title {
        text-align: center;
        color: #94A3B8;
        font-size: 1.25rem;
        margin-bottom: 50px;
        font-weight: 400;
    }

    /* תגיות סטטוס מודרניות */
    .badge-live {
        background: rgba(0, 245, 212, 0.1);
        color: #00F5D4;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(0, 245, 212, 0.3);
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .badge-soon {
        background: rgba(255, 183, 3, 0.1);
        color: #FFB703;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(255, 183, 3, 0.3);
        display: inline-block;
        margin-bottom: 10px;
    }
    
    /* עיצוב כרטיסיות (עיצוב טיפוגרפי) */
    .card-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    
    .card-text {
        font-size: 0.95rem;
        color: #CBD5E1;
        line-height: 1.5;
        margin-bottom: 20px;
        min-height: 70px; /* שמירה על יישור אחיד בין הכרטיסיות */
    }
    
    /* מתיחת כפתורי קישור */
    .stLinkButton > a {
        width: 100%;
        text-align: center;
        font-weight: 600;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# כותרת האתר
st.markdown('<div class="main-title">Silicon Photonics Simulation Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">פלטפורמת הדור הבא לתכנון, סימולציה וניתוח של רכיבים פוטוניים משולבים</div>', unsafe_allow_html=True)

# ==========================================
# שורה ראשונה - מנועי מודים ומצמד סימטרי
# ==========================================
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.image("card1_mode_std.png", use_container_width=True)
        st.markdown('<span class="badge-live">🟢 Active</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Standard FDE Mode Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מפתר מודים למוליכי גל מלבניים. חישוב מקדמי שבירה אפקטיביים ($n_{eff}$) ופרופיל שדות TE/TM.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-mode-solver-ohadwest.streamlit.app/", use_container_width=True)

with col2:
    with st.container(border=True):
        st.image("card2_mode_adv.png", use_container_width=True)
        st.markdown('<span class="badge-live">🟢 Active</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Advanced Mode Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">תמיכה בחתכים טרפזיים (Sidewall angle), איבודי עיקול (Ring Bending) ופרופיל אינדקס מרוכב.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-mode-solver-davanced-ohadwest.streamlit.app/", use_container_width=True)

with col3:
    with st.container(border=True):
        st.image("card3_coupler_sym.png", use_container_width=True)
        st.markdown('<span class="badge-live">🟢 Active</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Symmetric DC Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">ניתוח מצמד כיווני סימטרי. חישובי אופני-על (Even/Odd), אורך צימוד $L_c$ ודינמיקת העברת הספק.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-coupler-simulator-ohadwest.streamlit.app/", use_container_width=True)


st.write("") # רווח אנכי בין השורות
st.write("") 

# ==========================================
# שורה שנייה - מצמד א-סימטרי + יישומים עתידיים
# ==========================================
col4, col5, col6 = st.columns(3, gap="large")

with col4:
    with st.container(border=True):
        st.image("card4_coupler_asym.png", use_container_width=True)
        st.markdown('<span class="badge-live">🟢 Active</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Asymmetric ADC Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מצמד כיווני א-סימטרי ($w_1 \\neq w_2$). הדמיות Phase Mismatch והעברת הספק מקסימלית תלוית פאזה.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://asymmetric-directional-coupler-ohadwest.streamlit.app/", use_container_width=True)

with col5:
    with st.container(border=True):
        st.image("card5_ring_spectrum.png", use_container_width=True)
        st.markdown('<span class="badge-soon">⏳ Coming Soon</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Ring Resonator Spectrum</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">סימולציית תמסורת לרזונטורים טבעתיים. חילוץ Q-factor, הגדרת FSR, והצגת פרופילי לורנץ דינמיים.</div>', unsafe_allow_html=True)
        st.button("המודול בפיתוח...", disabled=True, use_container_width=True, key="btn_ring")

with col6:
    with st.container(border=True):
        st.image("card6_photoacoustics.png", use_container_width=True)
        st.markdown('<span class="badge-soon">⏳ Coming Soon</span>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Acoustic-Optic Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מנוע אינטראקציה פוטו-אקוסטית. סימולציית התפשטות גלים אקוסטיים והשפעתם על מקדם השבירה.</div>', unsafe_allow_html=True)
        st.button("המודול בפיתוח...", disabled=True, use_container_width=True, key="btn_acoustic")

st.divider()

# פוטר שקט ואלגנטי
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.9rem;'>Powered by Advanced Finite-Difference Algorithms | Engineered for Silicon Photonics</p>", unsafe_allow_html=True)
