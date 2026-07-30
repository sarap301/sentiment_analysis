import streamlit as st
import base64
 
 
# ============================================================
# TATA MOTORS / DIGITAL.AI LABS THEME
# ============================================================
 
TATA_BLUE = "#1F3A5F"
TATA_DARK_BLUE = "#102A43"
TATA_LIGHT_BLUE = "#EAF2F8"
TATA_RED = "#E31837"
TATA_GREY = "#F4F6F8"
TATA_DARK_GREY = "#34495E"
WHITE = "#FFFFFF"
 
 
def apply_theme():
 
    st.markdown(
        """
        <style>
 
        /* =====================================================
           GLOBAL
        ===================================================== */
 
        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #F7F9FC 0%,
                    #EEF4F8 50%,
                    #F8FAFC 100%
                );
            color: #102A43;
        }
 
        .main .block-container {
            padding-top: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
            padding-bottom: 3rem;
            max-width: 1500px;
        }
 
 
        /* =====================================================
           SIDEBAR
           ===================================================== */
 
        section[data-testid="stSidebar"] {
 
            background:
                linear-gradient(
                    180deg,
                    #102A43 0%,
                    #1F3A5F 55%,
                    #274E70 100%
                );
 
            border-right: 1px solid rgba(255,255,255,0.08);
        }
 
        section[data-testid="stSidebar"] * {
            color: white !important;
        }
 
        section[data-testid="stSidebar"] .stMarkdown {
            color: white;
        }
 
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.20);
        }
 
 
        /* =====================================================
           SIDEBAR NAVIGATION
           ===================================================== */
 
        section[data-testid="stSidebar"] a {
            border-radius: 8px;
            padding: 8px 10px;
        }
 
        section[data-testid="stSidebar"] a:hover {
            background: rgba(255,255,255,0.12);
        }
 
 
        /* =====================================================
           TITLES
           ===================================================== */
 
        h1 {
            color: #102A43 !important;
            font-weight: 750 !important;
            letter-spacing: -0.5px;
        }
 
        h2 {
            color: #1F3A5F !important;
            font-weight: 700 !important;
        }
 
        h3 {
            color: #1F3A5F !important;
            font-weight: 650 !important;
        }
 
 
        /* =====================================================
           PAGE HEADER
           ===================================================== */
 
        .page-header {
 
            background:
                linear-gradient(
                    100deg,
                    #102A43,
                    #1F3A5F
                );
 
            padding: 24px 30px;
 
            border-radius: 16px;
 
            margin-bottom: 25px;
 
            box-shadow:
                0 8px 25px rgba(16,42,67,0.12);
        }
 
        .page-header h1 {
 
            color: white !important;
 
            margin: 0;
 
            font-size: 30px;
 
        }
 
        .page-header p {
 
            color: #DCE8F2;
 
            margin-top: 7px;
 
            font-size: 15px;
 
        }
 
 
        /* =====================================================
           DIGITAL AI LABS HEADER
           ===================================================== */
 
        .labs-header {
 
            display: flex;
 
            justify-content: space-between;
 
            align-items: center;
 
            padding: 14px 4px 22px 4px;
 
            border-bottom:
                1px solid #D9E2EC;
 
            margin-bottom: 25px;
        }
 
        .labs-brand {
 
            font-size: 14px;
 
            font-weight: 700;
 
            color: #1F3A5F;
 
            letter-spacing: 0.3px;
        }
 
        .labs-subtitle {
 
            font-size: 12px;
 
            color: #627D98;
 
            margin-top: 3px;
        }
 
        .tata-mark {
 
            font-size: 13px;
 
            font-weight: 700;
 
            color: #E31837;
 
        }
 
 
        /* =====================================================
           KPI CARDS
           ===================================================== */
 
        .kpi-card {
 
            background: white;
 
            border-radius: 15px;
 
            padding: 22px 24px;
 
            border:
 
                1px solid #E1E8ED;
 
            box-shadow:
 
                0 5px 18px
                rgba(16,42,67,0.08);
 
            position: relative;
 
            overflow: hidden;
 
            min-height: 125px;
        }
 
        .kpi-card:before {
 
            content: "";
 
            position: absolute;
 
            left: 0;
 
            top: 0;
 
            width: 5px;
 
            height: 100%;
 
            background: #E31837;
        }
 
        .kpi-label {
 
            font-size: 13px;
 
            color: #627D98;
 
            font-weight: 600;
 
            text-transform: uppercase;
 
            letter-spacing: 0.6px;
        }
 
        .kpi-value {
 
            font-size: 32px;
 
            font-weight: 750;
 
            color: #102A43;
 
            margin-top: 7px;
        }
 
        .kpi-description {
 
            font-size: 12px;
 
            color: #829AB1;
 
            margin-top: 5px;
        }
 
 
        /* =====================================================
           SECTION CARDS
           ===================================================== */
 
        .section-card {
 
            background: white;
 
            border-radius: 15px;
 
            padding: 24px;
 
            margin-top: 18px;
 
            margin-bottom: 18px;
 
            border:
                1px solid #E1E8ED;
 
            box-shadow:
                0 4px 16px
                rgba(16,42,67,0.06);
        }
 
 
        /* =====================================================
           INSIGHT CARDS
           ===================================================== */
 
        .insight-card {
 
            background: #FFFFFF;
 
            border-left:
                5px solid #1F3A5F;
 
            border-radius: 10px;
 
            padding: 17px 20px;
 
            margin-bottom: 12px;
 
            box-shadow:
                0 3px 12px
                rgba(16,42,67,0.06);
        }
 
        .insight-title {
 
            font-weight: 700;
 
            color: #1F3A5F;
 
            font-size: 15px;
        }
 
        .insight-text {
 
            color: #486581;
 
            font-size: 14px;
 
            margin-top: 5px;
        }
 
 
        /* =====================================================
           SOURCE BADGES
           ===================================================== */
 
        .source-row {
 
            display: flex;
 
            gap: 10px;
 
            margin-top: 10px;
 
            margin-bottom: 18px;
        }
 
        .source-badge {
 
            padding: 7px 13px;
 
            border-radius: 20px;
 
            font-size: 12px;
 
            font-weight: 650;
 
            background: #EAF2F8;
 
            color: #1F3A5F;
 
            border: 1px solid #D5E3ED;
        }
 
 
        /* =====================================================
           BUTTONS
           ===================================================== */
 
        .stButton > button {
 
            border-radius: 8px;
 
            border: 1px solid #1F3A5F;
 
            background: #1F3A5F;
 
            color: white;
 
            font-weight: 600;
        }
 
        .stButton > button:hover {
 
            background: #102A43;
 
            border-color: #102A43;
 
            color: white;
        }
 
 
        /* =====================================================
           SELECTBOX
           ===================================================== */
 
        div[data-baseweb="select"] > div {
 
            border-radius: 9px;
 
            border-color: #D9E2EC;
 
            background: white;
        }
 
 
        /* =====================================================
           DATAFRAME
           ===================================================== */
 
        div[data-testid="stDataFrame"] {
 
            border-radius: 12px;
 
            overflow: hidden;
 
            border: 1px solid #D9E2EC;
        }
 
 
        /* =====================================================
           ALERTS
           ===================================================== */
 
        div[data-testid="stAlert"] {
 
            border-radius: 10px;
        }
 
 
        /* =====================================================
           FOOTER
           ===================================================== */
 
        .dashboard-footer {
 
            text-align: center;
 
            color: #829AB1;
 
            font-size: 12px;
 
            padding-top: 30px;
 
            padding-bottom: 10px;
 
            border-top:
                1px solid #D9E2EC;
 
            margin-top: 40px;
        }
 
 
        /* =====================================================
           MOBILE
           ===================================================== */
 
        @media (max-width: 768px) {
 
            .main .block-container {
 
                padding-left: 1rem;
 
                padding-right: 1rem;
 
            }
 
            .page-header h1 {
 
                font-size: 23px;
 
            }
 
            .kpi-value {
 
                font-size: 26px;
 
            }
 
        }
 
        </style>
        """,
        unsafe_allow_html=True
    )
 
 
def show_brand_header():
 
    st.markdown(
        """
        <div class="labs-header">
 
            <div>
 
                <div class="labs-brand">
                    TATA MOTORS DIGITAL.AI LABS
                </div>
 
                <div class="labs-subtitle">
                    AI-Powered Customer Intelligence
                </div>
 
            </div>
 
            <div class="tata-mark">
                TATA MOTORS
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def page_header(title, subtitle=""):
 
    st.markdown(
        f"""
        <div class="page-header">
 
            <h1>{title}</h1>
 
            <p>{subtitle}</p>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def kpi_card(label, value, description=""):
 
    st.markdown(
        f"""
        <div class="kpi-card">
 
            <div class="kpi-label">
                {label}
            </div>
 
            <div class="kpi-value">
                {value}
            </div>
 
            <div class="kpi-description">
                {description}
            </div>
 
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def section_title(title, subtitle=""):
 
    if subtitle:
 
        st.markdown(
            f"""
            <h2 style="margin-bottom:2px;">
                {title}
            </h2>
 
            <p style="
                color:#627D98;
                margin-top:0px;
                margin-bottom:18px;
            ">
                {subtitle}
