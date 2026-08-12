import os
import streamlit as st

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="Silicon Photonics Hub",
    page_icon="🔬",
    layout="wide"
)

# הזרקת עיצוב מותאם אישית (CSS) עם ניגודיות גבוהה ותמיכה מלאה ב-Light & Dark Mode
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;600;800&family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Heebo', sans-serif;
    }
    
    /* כותרת ראשי עם גרדיאנט בולט */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #0284C7 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 1rem;
    }
    
    .sub-title {
        text-align: center;
        color: var(--text-color, #475569);
        font-size: 1.2rem;
        margin-bottom: 35px;
        font-weight: 500;
        opacity: 0.9;
    }

    /* עיצוב כרטיסיות קבוע עם ניגודיות גבוהה בולטת */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: var(--background-secondary-color, #0F172A) !important;
        border: 1px solid var(--border-color, #334155) !important;
        border-radius: 12px !important;
        padding: 12px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    /* כותרת הכרטיסייה - צבע בולט וקריא בכל מצב מסך */
    .card-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #38BDF8 !important; /* תכלת-בוהק בולט וקריא במיוחד */
        margin-bottom: 10px;
        line-height: 1.25;
    }
    
    /* טקסט תיאור הכרטיסייה */
    .card-text {
        font-size: 0.95rem;
        color: #F1F5F9 !important; /* לבן-אופווייט בולט מאוד */
        line-height: 1.5;
        margin-bottom: 18px;
        min-height: 65px;
    }

    /* תגיות סטטוס מודרניות */
    .badge-live {
        background: rgba(16, 185, 129, 0.2);
        color: #34D399 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(52, 211, 153, 0.4);
        display: inline-block;
    }
    
    .badge-soon {
        background: rgba(245, 158, 11, 0.2);
        color: #FBBF24 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(251, 191, 36, 0.4);
        display: inline-block;
    }

    .version-tag {
        color: #94A3B8 !important;
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
    
    .placeholder-box {
        height: 160px;
        background: #1E293B;
        border: 1px dashed #475569;
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
        font-weight: 700;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# פונקציית עזר להצגת תמונה או קופסה חלופית
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
st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>Powered by Advanced Finite-Difference Algorithms | Engineered for Silicon Photonics</p>", unsafe_allow_html=True)
