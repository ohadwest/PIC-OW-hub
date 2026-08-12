import os
import streamlit as st

# הגדרת גרסת ה-Hub המרכזית למעקב
HUB_VERSION = "v1.0.0"

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="Silicon Photonics Hub",
    page_icon="🔬",
    layout="wide"
)

# הזרקת עיצוב CSS עם ניגודיות מקסימלית, גופנים בולטים והגנה על ניגודיות
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@500;700;900&family=Inter:wght@500;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Heebo', sans-serif;
    }
    
    /* כותרת ראשית בולטת */
    .main-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #0284C7 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 0.5rem;
    }
    
    .sub-title {
        text-align: center;
        color: #334155;
        font-size: 1.2rem;
        margin-bottom: 30px;
        font-weight: 700;
    }

    .hub-version-badge {
        background: #1E293B;
        color: #38BDF8 !important;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 800;
        border: 1px solid #38BDF8;
        display: inline-block;
        margin-top: 5px;
    }

    /* עיצוב כרטיסיות כהה, אלגנטי ובעל ניגודיות גבוהה קבועה */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0F172A !important; /* רקע כהה קבוע */
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 14px !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }

    /* כותרת הכרטיסייה - צבע תכלת זרחני בולט מאוד */
    .card-title {
        font-size: 1.3rem;
        font-weight: 900;
        color: #38BDF8 !important;
        margin-bottom: 8px;
        line-height: 1.25;
    }
    
    /* טקסט תיאור הכרטיסייה - הדגשה והכהייה להבלטה מקסימלית */
    .card-text {
        font-size: 0.95rem;
        font-weight: 600 !important; /* כתב עבה ובולט */
        color: #F8FAFC !important; /* צבע לבן-בוהק לקריאות מושלמת */
        line-height: 1.55;
        margin-bottom: 18px;
        min-height: 65px;
    }

    /* תגיות סטטוס */
    .badge-live {
        background: rgba(16, 185, 129, 0.25);
        color: #34D399 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        border: 1px solid rgba(52, 211, 153, 0.5);
        display: inline-block;
    }
    
    .badge-soon {
        background: rgba(245, 158, 11, 0.25);
        color: #FBBF24 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        border: 1px solid rgba(251, 191, 36, 0.5);
        display: inline-block;
    }

    .version-tag {
        color: #94A3B8 !important;
        font-size: 0.75rem;
        font-weight: 700;
        float: right;
    }
    
    .card-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    
    .placeholder-box {
        height: 150px;
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
        font-weight: 800;
        border-radius: 8px;
    }
    
    .footer-text {
        text-align: center;
        color: #64748B;
        font-size: 0.9rem;
        margin-top: 10px;
        font-weight: 600;
    }
    
    .copyright-text {
        text-align: center;
        color: #475569;
        font-size: 0.85rem;
        margin-top: 5px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# פונקציית עזר להצגת תמונה או קופסה חלופית
def display_card_image(img_path, default_emoji="🔬"):
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.markdown(f'<div class="placeholder-box">{default_emoji}</div>', unsafe_allow_html=True)

# כותרות הדף בתוספת תגית גרסה ראשית
st.markdown(f'''
    <div class="main-title">Silicon Photonics Simulation Hub</div>
    <div style="text-align: center;">
        <span class="hub-version-badge">System Version {HUB_VERSION}</span>
    </div>
''', unsafe_allow_html=True)

st.markdown('<div class="sub-title">פלטפורמה לתכנון, סימולציה וניתוח של רכיבים פוטוניים משולבים</div>', unsafe_allow_html=True)

# ==========================================
# שורה 1: מנועי סימולציה פעילים (1-4)
# ==========================================
st.markdown("### 🚀 מנועי סימולציה פעילים")
col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    with st.container(border=True):
        display_card_image("img1.png", "📐")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Standard Mode Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">חישוב אופני התפשטות במוליך גל מלבני, $n_{eff}$ ופרופיל שדות TE/TM.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע ➔", "https://pic-mode-solver-ohadwest.streamlit.app/", use_container_width=True)

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
        st.markdown('<div class="card-text">חתכים טרפזיים (Sidewall angle), איבודי עיקול (Ring Bending) ואינדקס מרוכב.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע ➔", "https://pic-mode-solver-davanced-ohadwest.streamlit.app/", use_container_width=True)

with col3:
    with st.container(border=True):
        display_card_image("img3.png", "⚡")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.1.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Symmetric DC</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">ניתוח מצמד סימטרי. חישובי Even/Odd supermodes, אורך צימוד $L_c$ והעברת הספק.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע ➔", "https://pic-coupler-simulator-ohadwest.streamlit.app/", use_container_width=True)

with col4:
    with st.container(border=True):
        display_card_image("img4.png", "🌊")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-live">🟢 Active</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Asymmetric ADC</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">מצמד א-סימטרי ($w_1 \\neq w_2$). אנליזת Phase Mismatch והעברת הספק מרבית.</div>', unsafe_allow_html=True)
        st.link_button("הפעל מנוע ➔", "https://asymmetric-directional-coupler-ohadwest.streamlit.app/", use_container_width=True)

st.write("")
st.divider()

# ==========================================
# שורה 2: מודולים עתידיים בפיתוח (5-8)
# ==========================================
st.markdown("### ⏳ מודולים עתידיים בפיתוח")
col5, col6, col7, col8 = st.columns(4, gap="medium")

with col5:
    with st.container(border=True):
        display_card_image("img5.png", "⭕")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.0.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Ring Resonator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">תמסורת רזונטורים טבעתיים, חילוץ Q-factor, FSR ופרופילי לורנץ דינמיים.</div>', unsafe_allow_html=True)
        st.button("בפיתוח...", disabled=True, use_container_width=True, key="btn_ring")

with col6:
    with st.container(border=True):
        display_card_image("img6.png", "🔊")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.1.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Acousto-Optics</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">אינטראקציה פוטו-אקוסטית, התפשטות גלים אקוסטיים ואפנון מקדם השבירה.</div>', unsafe_allow_html=True)
        st.button("בפיתוח...", disabled=True, use_container_width=True, key="btn_acoustic")

with col7:
    with st.container(border=True):
        display_card_image("img7.png", "💡")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.2.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Electro-Optic Modulator</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">אנליזת אפנון אלקטרו-אופטי ($V_\\pi L$), הזרקת נשאים ודינמיקת פאזה רחבת סרט.</div>', unsafe_allow_html=True)
        st.button("בפיתוח...", disabled=True, use_container_width=True, key="btn_eom")

with col8:
    with st.container(border=True):
        display_card_image("img8.png", "📊")
        st.markdown('''
            <div class="card-header-row">
                <span class="badge-soon">⏳ Coming Soon</span>
                <span class="version-tag">v2.3.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Bragg Grating Solver</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-text">סימולציית מחזירי בראג ($DBR$), רוחב פס רפלקטיבי ומקדמי צימוד $g(\\lambda)$.</div>', unsafe_allow_html=True)
        st.button("בפיתוח...", disabled=True, use_container_width=True, key="btn_bragg")

st.divider()

# פוטר עם גרסת מערכת וזכויות יוצרים
st.markdown(f'<div class="footer-text">Powered by Advanced Finite-Difference Algorithms | Engineered for Silicon Photonics</div>', unsafe_allow_html=True)
st.markdown(f'<div class="copyright-text">© 2026 ohadwest. All rights reserved.</div>', unsafe_allow_html=True)
