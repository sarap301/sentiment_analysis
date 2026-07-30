import streamlit as st
 
 
# =========================================================
# TATA MOTORS EV DASHBOARD THEME
# =========================================================
 
TATA_BLUE = "#003B70"
TATA_DARK_BLUE = "#002B52"
TATA_RED = "#E31837"
TATA_LIGHT_BLUE = "#EAF3FA"
TATA_GREY = "#F4F6F8"
TATA_DARK_GREY = "#4B5563"
WHITE = "#FFFFFF"
 
 
def apply_theme():
 
    st.markdown(
        f"""
        <style>
 
        /* =================================================
           GLOBAL
        ================================================= */
 
        .stApp {{
            background:
                linear-gradient(
                    135deg,
                    #ffffff 0%,
                    #f5f9fc 55%,
                    #edf5fa 100%
                );
            color: #172033;
        }}
 
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1450px;
        }}
 
 
        /* =================================================
           SIDEBAR
        ================================================= */
 
        section[data-testid="stSidebar"] {{
            background:
                linear-gradient(
                    180deg,
                    {TATA_DARK_BLUE} 0%,
                    {TATA_BLUE} 100%
                );
        }}
 
        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}
 
        section[data-testid="stSidebar"] hr {{
            border-color: rgba(255,255,255,0.25);
        }}
 
 
        /* =================================================
           TITLES
        ================================================= */
 
        h1 {{
            color: {TATA_DARK_BLUE};
            font-weight: 800;
            letter-spacing: -0.5px;
        }}
 
        h2 {{
            color: {TATA_BLUE};
            font-weight: 750;
        }}
 
        h3 {{
            color: {TATA_DARK_BLUE};
            font-weight: 700;
        }}
 
 
        /* =================================================
           BRAND HEADER
        ================================================= */
 
        .brand-header {{
            background:
                linear-gradient(
                    100deg,
                    {TATA_DARK_BLUE},
                    {TATA_BLUE}
                );
 
            padding: 22px 28px;
            border-radius: 18px;
            margin-bottom: 25px;
 
            box-shadow:
                0 8px 25px rgba(0,59,112,0.15);
        }}
 
        .brand-main {{
            color: white;
            font-size: 30px;
            font-weight: 800;
            margin-bottom: 3px;
        }}
 
        .brand-sub {{
            color: #dbeaf7;
            font-size: 15px;
            font-weight: 500;
        }}
 
        .labs-badge {{
            display: inline-block;
            background: white;
            color: {TATA_BLUE};
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 10px;
        }}
 
 
        /* =================================================
           SOURCE BADGES
        ================================================= */
 
        .source-row {{
            display: flex;
            gap: 10px;
            margin: 10px 0 22px 0;
        }}
 
        .source-badge {{
            padding: 8px 15px;
            border-radius: 20px;
            background: white;
            border: 1px solid #d9e3ec;
            color: {TATA_DARK_BLUE};
            font-size: 13px;
            font-weight: 600;
 
            box-shadow:
                0 3px 10px rgba(0,0,0,0.05);
        }}
 
 
        /* =================================================
           KPI CARDS
        ================================================= */
 
        .kpi-card {{
            background: white;
            padding: 20px 22px;
            border-radius: 16px;
 
            border-left: 5px solid {TATA_RED};
 
            box-shadow:
                0 5px 18px rgba(0,0,0,0.07);
 
            min-height: 125px;
        }}
 
        .kpi-label {{
            color: {TATA_DARK_GREY};
            font-size: 13px;
            font-weight: 600;
        }}
 
        .kpi-value {{
            color: {TATA_DARK_BLUE};
            font-size: 31px;
            font-weight: 800;
            margin-top: 7px;
        }}
 
 
        /* =================================================
           CONTENT CARDS
        ================================================= */
 
        .info-card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
 
            box-shadow:
                0 4px 16px rgba(0,0,0,0.06);
 
            border: 1px solid #e5ebf0;
 
            margin-bottom: 15px;
        }}
 
        .info-title {{
            color: {TATA_BLUE};
            font-size: 17px;
            font-weight: 750;
            margin-bottom: 8px;
        }}
 
        .info-text {{
            color: #4b5563;
            font-size: 14px;
            line-height: 1.6;
        }}
 
 
        /* =================================================
           SECTION HEADER
        ================================================= */
 
        .section-header {{
            border-left: 5px solid {TATA_RED};
            padding-left: 13px;
            margin-top: 28px;
            margin-bottom: 15px;
        }}
 
 
        /* =================================================
           FOOTER
        ================================================= */
 
        .footer {{
            margin-top: 45px;
            padding-top: 18px;
            border-top: 1px solid #dce4eb;
            text-align: center;
            color: #6b7280;
            font-size: 12px;
        }}
 
        </style>
        """,
        unsafe_allow_html=True
    )
 
 
def brand_header():
 
    st.markdown(
        """
        <div class="brand-header">
 
            <div class="brand-main">
                🚗 Tata Motors EV Customer Intelligence
            </div>
 
            <div class="brand-sub">
                Digital.AI Labs • Customer Voice & Business Intelligence
            </div>
 
            <div class="labs-badge">
                DIGITAL.AI LABS
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def source_badges():
 
    st.markdown(
        """
        <div class="source-row">
 
            <div class="source-badge">
                💬 WhatsApp EV Community Conversations
            </div>
 
            <div class="source-badge">
                📡 Telegram EV Community Conversations
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def section_header(title):
 
    st.markdown(
        f"""
        <div class="section-header">
            <h2>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def kpi_card(label, value):
 
    st.markdown(
        f"""
        <div class="kpi-card">
 
            <div class="kpi-label">
                {label}
            </div>
 
            <div class="kpi-value">
                {value}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def footer():
 
    st.markdown(
        """
        <div class="footer">
            Tata Motors EV Customer Intelligence Dashboard
            <br>
            Built using NLP, Topic Modelling, Embeddings and Generative AI
        </div>
        """,
        unsafe_allow_html=True
    )
