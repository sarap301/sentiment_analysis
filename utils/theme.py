import streamlit as st
 
 
def apply_theme():
 
    st.markdown(
        """
        <style>
 
        /* ================================
           GLOBAL
        ================================= */
 
        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #f5f9fc 0%,
                    #ffffff 45%,
                    #eef5fa 100%
                );
            color: #082b4c;
        }
 
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1450px;
        }
 
 
        /* ================================
           SIDEBAR
        ================================= */
 
        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #003b67 0%,
                #00527f 100%
            );
        }
 
        [data-testid="stSidebar"] * {
            color: white !important;
        }
 
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
        }
 
 
        /* ================================
           BRAND HEADER
        ================================= */
 
        .brand-card {
            background: linear-gradient(
                135deg,
                #003b67,
                #005a8d
            );
 
            padding: 28px 34px;
            border-radius: 18px;
            margin-bottom: 25px;
 
            box-shadow:
                0 8px 25px rgba(0, 59, 103, 0.20);
        }
 
        .brand-main {
            color: white;
            font-size: 30px;
            font-weight: 800;
            letter-spacing: 0.3px;
        }
 
        .brand-sub {
            color: #d9edf7;
            font-size: 15px;
            margin-top: 8px;
        }
 
        .labs-badge {
            display: inline-block;
 
            margin-top: 15px;
            padding: 6px 13px;
 
            border-radius: 20px;
 
            background: #e31837;
            color: white;
 
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
        }
 
 
        /* ================================
           SOURCE BADGES
        ================================= */
 
        .source-container {
            display: flex;
            gap: 14px;
            margin: 15px 0 25px 0;
            flex-wrap: wrap;
        }
 
        .source-badge {
            background: white;
 
            border: 1px solid #d9e5ee;
 
            border-radius: 12px;
 
            padding: 12px 18px;
 
            font-size: 14px;
            font-weight: 600;
 
            box-shadow:
                0 4px 12px rgba(0,0,0,0.06);
        }
 
 
        /* ================================
           SECTION HEADERS
        ================================= */
 
        .section-header {
            border-left: 5px solid #e31837;
 
            padding: 8px 0 8px 14px;
 
            margin-top: 30px;
            margin-bottom: 20px;
 
            font-size: 24px;
            font-weight: 750;
 
            color: #003b67;
        }
 
 
        /* ================================
           KPI CARDS
        ================================= */
 
        .kpi-card {
            background: white;
 
            border-radius: 16px;
 
            padding: 22px;
 
            border-left: 5px solid #e31837;
 
            box-shadow:
                0 7px 20px rgba(0, 50, 90, 0.10);
 
            min-height: 125px;
        }
 
        .kpi-label {
            color: #64788a;
 
            font-size: 12px;
 
            font-weight: 700;
 
            letter-spacing: 0.7px;
 
            text-transform: uppercase;
        }
 
        .kpi-value {
            color: #003b67;
 
            font-size: 34px;
 
            font-weight: 800;
 
            margin-top: 8px;
        }
 
 
        /* ================================
           INFORMATION CARDS
        ================================= */
 
        .info-card {
            background: white;
 
            border-radius: 15px;
 
            padding: 20px;
 
            margin-bottom: 15px;
 
            box-shadow:
                0 5px 18px rgba(0,0,0,0.07);
 
            border: 1px solid #e3edf3;
        }
 
 
        /* ================================
           PAGE TITLES
        ================================= */
 
        .page-title {
            color: #003b67;
 
            font-size: 32px;
 
            font-weight: 800;
 
            margin-bottom: 5px;
        }
 
        .page-subtitle {
            color: #60788b;
 
            font-size: 15px;
 
            margin-bottom: 25px;
        }
 
 
        /* ================================
           STREAMLIT ELEMENTS
        ================================= */
 
        div[data-testid="stMetric"] {
            background: white;
 
            border-radius: 14px;
 
            padding: 18px;
 
            box-shadow:
                0 5px 15px rgba(0,0,0,0.06);
        }
 
        div[data-testid="stMetricLabel"] {
            color: #60788b;
        }
 
        div[data-testid="stMetricValue"] {
            color: #003b67;
            font-weight: 800;
        }
 
 
        /* ================================
           BUTTONS
        ================================= */
 
        .stButton > button {
            border-radius: 8px;
 
            border: 1px solid #003b67;
 
            background: #003b67;
 
            color: white;
 
            font-weight: 600;
        }
 
        .stButton > button:hover {
            background: #e31837;
            border-color: #e31837;
            color: white;
        }
 
 
        /* ================================
           DATAFRAME
        ================================= */
 
        [data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }
 
 
        /* ================================
           MOBILE
        ================================= */
 
        @media (max-width: 768px) {
 
            .brand-main {
                font-size: 22px;
            }
 
            .page-title {
                font-size: 25px;
            }
 
            .kpi-value {
                font-size: 27px;
            }
 
        }
 
        </style>
        """,
        unsafe_allow_html=True
    )
 
 
def page_header(title, subtitle=""):
 
    st.markdown(
        f"""
        <div class="page-title">
            {title}
        </div>
 
        <div class="page-subtitle">
            {subtitle}
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def section_header(title):
 
    st.markdown(
        f"""
        <div class="section-header">
            {title}
        </div>
        """,
        unsafe_allow_html=True
    )
 
 
def brand_header():
 
    st.markdown(
        """
        <div class="brand-card">
 
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
        <div class="source-container">
 
            <div class="source-badge">
                💬 WhatsApp EV Community Conversations
            </div>
 
            <div class="source-badge">
                ✈️ Telegram EV Community Conversations
            </div>
 
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
