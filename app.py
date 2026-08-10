import os
import streamlit as st

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="Silicon Photonics Hub",
    page_icon="🔬",
    layout="wide"
)

# הזרקת עיצוב מותאם אישית (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;600;800&family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Heebo', sans-serif;
    }
    
    .main-title {
        font-size: 3.2rem;
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
        font-size: 1.2rem;
        margin-bottom: 40px;
        font-weight: 400;
    }

    .badge-live {
        background: rgba(0, 245, 212, 0.1);
        color: #00F5D4;
        padding: 4px 10px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(0, 245, 212, 0.3);
        display: inline-block;
    }
    
    .badge-soon {
        background: rgba(255, 183, 3, 0.1);
        color: #FFB703;
        padding: 4px 10px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(255, 183, 3, 0.3);
        display: inline-block;
    }

    .version-tag {
        color: #64748B;
        font-size: 0.75rem;
        font-weight: 600;
        float: right;
    }
    
    .card-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    
    .card-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    
    .card-text {
        font-size: 0.92rem;
        color: #CBD5E1;
        line-height: 1.5;
        margin-bottom: 20px;
        min-height: 65px;
    }
    
    .placeholder-box {
        height: 160px;
        background: rgba(30, 41, 59, 0.5);
        border: 1px dashed #334155;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        margin-bottom: 15px;
    }

    .stLinkButton > a {
        width: 100%;
        text-align: center;
        font-weight: 600;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# פונקציית עזר להצגת תמונה או קופסה חלופית במידה והקובץ חסר
def display_card_image(img_path, default_emoji="🔬"):
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.markdown(f'<div class="placeholder-box">{default_emoji}</div>', unsafe_allow_html=True)

# כותרת הדף
st.markdown('<div class="main-title">Silicon Photonics Simulation Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">פלטפורמה לתכנון, סימולציה וניתוח של רכיבים פוטוניים משולבים</div>', unsafe_allow_html=True)

# ==========================================
# שורה ראשונה
# ==========================================
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        display_card_image("img1.png", "📐")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Standard FDE Mode Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">חישוב אופני התפשטות במוליך גל מלבני, מקדמי שבירה אפקטיביים ($n_{eff}$) ופרופיל שדות TE/TM.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-mode-solver-ohadwest.streamlit.app/", use_container_width=True)

with col2:
    with st.container(border=True):
        display_card_image("img2.png", "🌀")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.2.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Advanced Mode Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">תמיכה בחתכים טרפזיים (Sidewall angle), איבודי עיקול (Ring Bending) ופרופיל אינדקס מרוכב.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-mode-solver-davanced-ohadwest.streamlit.app/", use_container_width=True)

with col3:
    with st.container(border=True):
        display_card_image("img3.png", "⚡")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.1.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Symmetric DC Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">ניתוח מצמד כיווני סימטרי. חישובי אופני-על (Even/Odd), אורך צימוד $L_c$ ודינמיקת העברת הספק.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://pic-coupler-simulator-ohadwest.streamlit.app/", use_container_width=True)

st.write("") 
st.write("") 

# ==========================================
# שורה שנייה
# ==========================================
col4, col5, col6 = st.columns(3, gap="large")

with col4:
    with st.container(border=True):
        display_card_image("img4.png", "🌊")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Asymmetric ADC Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מצמד כיווני א-סימטרי ($w_1 \\neq w_2$). הדמיות Phase Mismatch והעברת הספק מקסימלית.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע סימולציה ➔", "https://asymmetric-directional-coupler-ohadwest.streamlit.app/", use_container_width=True)

with col5:
    with st.container(border=True):
        display_card_image("img5.png", "⭕")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.0.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Ring Resonator Spectrum</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">סימולציית תמסורת לרזונטורים טבעתיים. חילוץ Q-factor, הגדרת FSR, והצגת פרופילי לורנץ דינמיים.</div>', unsafe_allow_html=True)
        st.button("המודול בפיתוח...", disabled=True, use_container_width=True, key="btn_ring")

with col6:
    with st.container(border=True):
        display_card_image("img6.png", "🔊")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.1.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Acousto-Optic Simulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מנוע אינטראקציה פוטו-אקוסטית. סימולציית התפשטות גלים אקוסטיים והשפעתם על מקדם השבירה.</div>', unsafe_allow_html=True)
        st.button("המודול בפיתוח...", disabled=True, use_container_width=True, key="btn_acoustic")

st.divider()
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.9rem;'>Powered by Advanced Finite-Difference Algorithms | Engineered for Silicon Photonics</p>", unsafe_allow_html=True)
