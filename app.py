import os
import streamlit as st

# הגדרת גרסת המערכת
HUB_VERSION = "v1.1.0"

st.set_page_config(
    page_title="Silicon Photonics Hub",
    page_icon="🔬",
    layout="wide"
)

# ==========================================
# בחירת שפה בראש הדף (He / En)
# ==========================================
top_col1, top_col2 = st.columns([8, 2])
with top_col2:
    lang = st.radio(
        "Language / שפה",
        options=["He", "En"],
        horizontal=True,
        index=0,
        label_visibility="collapsed"
    )

# ==========================================
# מילון תרגומים (Translations Dictionary)
# ==========================================
T = {
    "He": {
        "dir": "rtl",
        "align": "right",
        "main_title": "Silicon Photonics Simulation Hub",
        "sub_title": "פלטפורמה לתכנון, סימולציה וניתוח של רכיבים פוטוניים משולבים",
        "active_sec": "🚀 מנועי סימולציה פעילים",
        "soon_sec": "⏳ מודולים עתידיים בפיתוח",
        "btn_launch": "הפעל מנוע ➔",
        "btn_dev": "בפיתוח...",
        "badge_active": "🟢 פעיל",
        "badge_soon": "⏳ בקרוב",
        # מודולים פעילים
        "m1_title": "Standard Mode Solver",
        "m1_desc": "חישוב אופני התפשטות במוליך גל מלבני, $n_{eff}$ ופרופיל שדות TE/TM.",
        "m2_title": "Advanced Mode Solver",
        "m2_desc": "חתכים טרפזיים (Sidewall angle), איבודי עיקול (Ring Bending) ואינדקס מרוכב.",
        "m3_title": "Symmetric DC",
        "m3_desc": "ניתוח מצמד סימטרי. חישובי Even/Odd supermodes, אורך צימוד $L_c$ והעברת הספק.",
        "m4_title": "Asymmetric ADC",
        "m4_desc": "מצמד א-סימטרי ($w_1 \\neq w_2$). אנליזת Phase Mismatch והעברת הספק מרבית.",
        "m5_title": "Ring Resonator Engine",
        "m5_desc": "אנליזת תהודה בודדת (All-Pass / Add-Drop), סריקת $Q_i / Q_c$, וספקטרום רחב כולל $\\kappa(\\lambda)$.",
        # מודולים עתידיים
        "m6_title": "Acousto-Optics",
        "m6_desc": "אינטראקציה פוטו-אקוסטית, התפשטות גלים אקוסטיים ואפנון מקדם השבירה.",
        "m7_title": "Electro-Optic Modulator",
        "m7_desc": "אנליזת אפנון אלקטרו-אופטי ($V_\\pi L$), הזרקת נשאים ודינמיקת פאזה רחבת סרט.",
        "m8_title": "Bragg Grating Solver",
        "m8_desc": "סימולציית מחזירי בראג ($DBR$), רוחב פס רפלקטיבי ומקדמי צימוד $g(\\lambda)$.",
        "footer_tech": "מבוסס על אלגוריתמים מתקדמים להפרשים סופיים | מתוכנן לפוטוניקת סיליקון",
    },
    "En": {
        "dir": "ltr",
        "align": "left",
        "main_title": "Silicon Photonics Simulation Hub",
        "sub_title": "A platform for design, simulation, and analysis of integrated photonic components",
        "active_sec": "🚀 Active Simulation Engines",
        "soon_sec": "⏳ Future Modules in Development",
        "btn_launch": "Launch Engine ➔",
        "btn_dev": "In Development...",
        "badge_active": "🟢 Active",
        "badge_soon": "⏳ Coming Soon",
        # Active Modules
        "m1_title": "Standard Mode Solver",
        "m1_desc": "Waveguide mode profiles, effective refractive indices ($n_{eff}$), and TE/TM field solver.",
        "m2_title": "Advanced Mode Solver",
        "m2_desc": "Trapezoidal cross-sections (sidewall tilt), ring bending losses, and complex index profile.",
        "m3_title": "Symmetric DC",
        "m3_desc": "Symmetric directional coupler analysis. Even/Odd supermodes, $L_c$, and power transfer.",
        "m4_title": "Asymmetric ADC",
        "m4_desc": "Asymmetric coupler ($w_1 \\neq w_2$). Phase mismatch analysis and max power conversion.",
        "m5_title": "Ring Resonator Engine",
        "m5_desc": "Single resonance analysis (All-Pass / Add-Drop), $Q_i / Q_c$ sweeps, and broadband spectrum with $\\kappa(\\lambda)$.",
        # Future Modules
        "m6_title": "Acousto-Optics",
        "m6_desc": "Photo-acoustic interactions, acoustic wave propagation, and index modulation.",
        "m7_title": "Electro-Optic Modulator",
        "m7_desc": "Electro-optic modulation ($V_\\pi L$), carrier injection, and broadband phase dynamics.",
        "m8_title": "Bragg Grating Solver",
        "m8_desc": "Distributed Bragg Reflector (DBR) simulation, reflection bandwidth, and coupling $g(\\lambda)$.",
        "footer_tech": "Powered by Advanced Finite-Difference Algorithms | Engineered for Silicon Photonics",
    }
}[lang]

# ==========================================
# הזרקת עיצוב CSS דינמי
# ==========================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@500;700;900&family=Inter:wght@500;700;900&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', 'Heebo', sans-serif;
        direction: {T['dir']};
    }}
    
    .main-title {{
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #0284C7 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 0.2rem;
    }}
    
    .sub-title {{
        text-align: center;
        color: #475569;
        font-size: 1.2rem;
        margin-bottom: 30px;
        font-weight: 700;
    }}

    .hub-version-badge {{
        background: #0F172A;
        color: #38BDF8 !important;
        padding: 4px 14px;
        border-radius: 12px;
        font-size: 0.82rem;
        font-weight: 800;
        border: 1px solid #38BDF8;
        display: inline-block;
        margin-top: 5px;
    }}

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: #0F172A !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
        padding: 14px !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.35);
        text-align: {T['align']};
    }}

    .card-title {{
        font-size: 1.3rem;
        font-weight: 900;
        color: #38BDF8 !important;
        margin-bottom: 8px;
        line-height: 1.25;
        text-align: {T['align']};
    }}
    
    .card-text {{
        font-size: 0.95rem;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.9);
        line-height: 1.55;
        margin-bottom: 18px;
        min-height: 70px;
        text-align: {T['align']};
    }}

    .badge-live {{
        background: rgba(16, 185, 129, 0.3);
        color: #34D399 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        border: 1px solid #34D399;
        display: inline-block;
    }}
    
    .badge-soon {{
        background: rgba(245, 158, 11, 0.3);
        color: #FBBF24 !important;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 800;
        border: 1px solid #FBBF24;
        display: inline-block;
    }}

    .version-tag {{
        color: #94A3B8 !important;
        font-size: 0.75rem;
        font-weight: 700;
        float: {'left' if T['dir'] == 'rtl' else 'right'};
    }}
    
    .card-header-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }}
    
    .placeholder-box {{
        height: 150px;
        background: #1E293B;
        border: 1px dashed #475569;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        margin-bottom: 15px;
    }}

    .stLinkButton > a {{
        width: 100%;
        text-align: center;
        font-weight: 800;
        border-radius: 8px;
    }}
    
    .footer-text {{
        text-align: center;
        color: #64748B;
        font-size: 0.9rem;
        margin-top: 10px;
        font-weight: 600;
    }}
    
    .copyright-text {{
        text-align: center;
        color: #475569;
        font-size: 0.85rem;
        margin-top: 5px;
        font-weight: 700;
    }}
</style>
""", unsafe_allow_html=True)

def display_card_image(img_path, default_emoji="🔬"):
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.markdown(f'<div class="placeholder-box">{default_emoji}</div>', unsafe_allow_html=True)

# כותרת ראשית
st.markdown(f'''
    <div class="main-title">{T['main_title']}</div>
    <div style="text-align: center;">
        <span class="hub-version-badge">System Version {HUB_VERSION}</span>
    </div>
''', unsafe_allow_html=True)

st.markdown(f'<div class="sub-title">{T["sub_title"]}</div>', unsafe_allow_html=True)

# ==========================================
# שורה 1: מנועי סימולציה פעילים (עכשיו כולל את 5 המודולים הפעילים!)
# ==========================================
st.markdown(f"### {T['active_sec']}")
col1, col2, col3, col4, col5_active = st.columns(5, gap="medium")

with col1:
    with st.container(border=True):
        display_card_image("img1.png", "📐")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-live">{T['badge_active']}</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m1_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m1_desc"]}</div>', unsafe_allow_html=True)
        st.link_button(T['btn_launch'], "https://pic-mode-solver-ohadwest.streamlit.app/", use_container_width=True)

with col2:
    with st.container(border=True):
        display_card_image("img2.png", "🌀")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-live">{T['badge_active']}</span>
                <span class="version-tag">v1.2.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m2_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m2_desc"]}</div>', unsafe_allow_html=True)
        st.link_button(T['btn_launch'], "https://pic-mode-solver-davanced-ohadwest.streamlit.app/", use_container_width=True)

with col3:
    with st.container(border=True):
        display_card_image("img3.png", "⚡")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-live">{T['badge_active']}</span>
                <span class="version-tag">v1.1.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m3_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m3_desc"]}</div>', unsafe_allow_html=True)
        st.link_button(T['btn_launch'], "https://pic-coupler-simulator-ohadwest.streamlit.app/", use_container_width=True)

with col4:
    with st.container(border=True):
        display_card_image("img4.png", "🌊")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-live">{T['badge_active']}</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m4_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m4_desc"]}</div>', unsafe_allow_html=True)
        st.link_button(T['btn_launch'], "https://asymmetric-directional-coupler-ohadwest.streamlit.app/", use_container_width=True)

# המודול החדש והפעיל של ה-Ring Resonator!
with col5_active:
    with st.container(border=True):
        display_card_image("img5.png", "⭕")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-live">{T['badge_active']}</span>
                <span class="version-tag">v1.0.0</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m5_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m5_desc"]}</div>', unsafe_allow_html=True)
        st.link_button(T['btn_launch'], "https://rr-app.streamlit.app/", use_container_width=True)

st.write("")
st.divider()

# ==========================================
# שורה 2: מודולים עתידיים בפיתוח (3 כרטיסיות נותרות)
# ==========================================
st.markdown(f"### {T['soon_sec']}")
col6, col7, col8 = st.columns(3, gap="medium")

with col6:
    with st.container(border=True):
        display_card_image("img6.png", "🔊")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-soon">{T['badge_soon']}</span>
                <span class="version-tag">v2.1.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m6_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m6_desc"]}</div>', unsafe_allow_html=True)
        st.button(T['btn_dev'], disabled=True, use_container_width=True, key="btn_acoustic")

with col7:
    with st.container(border=True):
        display_card_image("img7.png", "💡")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-soon">{T['badge_soon']}</span>
                <span class="version-tag">v2.2.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m7_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m7_desc"]}</div>', unsafe_allow_html=True)
        st.button(T['btn_dev'], disabled=True, use_container_width=True, key="btn_eom")

with col8:
    with st.container(border=True):
        display_card_image("img8.png", "📊")
        st.markdown(f'''
            <div class="card-header-row">
                <span class="badge-soon">{T['badge_soon']}</span>
                <span class="version-tag">v2.3.0-dev</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{T["m8_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-text">{T["m8_desc"]}</div>', unsafe_allow_html=True)
        st.button(T['btn_dev'], disabled=True, use_container_width=True, key="btn_bragg")

st.divider()

# פוטר וזכויות יוצרים
st.markdown(f'<div class="footer-text">{T["footer_tech"]}</div>', unsafe_allow_html=True)
st.markdown('<div class="copyright-text">© 2026 ohadwest. All rights reserved.</div>', unsafe_allow_html=True)
