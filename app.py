import streamlit as st
import google.generativeai as genai
import time

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan — AI Assistant",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Hide sidebar entirely ─────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Full Design System ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --black:      #080808;
    --black-2:    #0f0f0f;
    --black-3:    #161616;
    --black-4:    #1e1e1e;
    --black-5:    #2a2a2a;
    --red:        #c8102e;
    --red-light:  #e8223e;
    --red-glow:   rgba(200, 16, 46, 0.18);
    --red-dim:    rgba(200, 16, 46, 0.08);
    --white:      #f5f5f5;
    --grey-1:     #b0b0b0;
    --grey-2:     #6a6a6a;
    --border:     rgba(200, 16, 46, 0.20);
    --border-sub: rgba(255,255,255,0.06);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"],
section.main,
.block-container {
    background-color: var(--black) !important;
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stHeader"] { background: var(--black) !important; border-bottom: 1px solid var(--border-sub); }
[data-testid="stMainBlockContainer"] { padding: 0 !important; }
.block-container { max-width: 860px !important; padding: 0 24px 60px !important; margin: 0 auto !important; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 64px 0 40px;
    position: relative;
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 50%; transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(200,16,46,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--red);
    border: 1px solid var(--border);
    padding: 6px 18px;
    border-radius: 100px;
    margin-bottom: 24px;
    background: var(--red-dim);
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.6rem, 6vw, 4rem);
    font-weight: 900;
    line-height: 1.08;
    letter-spacing: -0.02em;
    color: var(--white);
    margin-bottom: 10px;
}
.hero-name span { color: var(--red); }
.hero-role {
    font-size: 1rem;
    font-weight: 400;
    color: var(--grey-1);
    letter-spacing: 0.04em;
    margin-bottom: 28px;
}
.hero-links {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 0;
}
.hero-link {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    color: var(--grey-1);
    text-decoration: none;
    border: 1px solid var(--border-sub);
    padding: 7px 16px;
    border-radius: 6px;
    transition: all 0.2s ease;
    background: var(--black-3);
}
.hero-link:hover { color: var(--white); border-color: var(--red); background: var(--red-dim); }

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 36px 0;
}

/* ── Stats Row ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 36px;
}
.stat-card {
    background: var(--black-3);
    border: 1px solid var(--border-sub);
    border-radius: 10px;
    padding: 18px 14px;
    text-align: center;
    transition: border-color 0.2s;
}
.stat-card:hover { border-color: var(--red); }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: var(--red);
    line-height: 1;
}
.stat-label {
    font-size: 0.7rem;
    color: var(--grey-2);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 5px;
}

/* ── Quick Chips ── */
.chips-label {
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--grey-2);
    margin-bottom: 12px;
}

/* ── Chat Container ── */
.chat-wrap {
    background: var(--black-3);
    border: 1px solid var(--border-sub);
    border-radius: 16px;
    padding: 0;
    overflow: hidden;
    margin-bottom: 0;
}
.chat-header {
    background: var(--black-4);
    border-bottom: 1px solid var(--border-sub);
    padding: 14px 22px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.chat-dot { width: 9px; height: 9px; border-radius: 50%; }
.dot-red { background: var(--red); }
.dot-y   { background: #f59e0b; }
.dot-g   { background: #10b981; }
.chat-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    color: var(--grey-2);
    margin-left: 6px;
}
.chat-messages { padding: 24px 22px; min-height: 200px; }

/* Message Bubbles */
.msg { display: flex; gap: 12px; margin-bottom: 22px; align-items: flex-start; }
.msg.user { flex-direction: row-reverse; }
.avatar {
    width: 34px; height: 34px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; flex-shrink: 0; font-weight: 600;
}
.avatar.ai-av  { background: var(--red); color: white; }
.avatar.usr-av { background: var(--black-5); color: var(--grey-1); border: 1px solid var(--border-sub); }
.bubble {
    max-width: 78%;
    padding: 13px 18px;
    border-radius: 14px;
    font-size: 0.92rem;
    line-height: 1.7;
    letter-spacing: 0.01em;
}
.bubble.ai-bubble {
    background: var(--black-4);
    border: 1px solid var(--border-sub);
    border-top-left-radius: 4px;
    color: var(--white);
}
.bubble.user-bubble {
    background: var(--red);
    border-top-right-radius: 4px;
    color: white;
}
.msg-time {
    font-size: 0.65rem;
    color: var(--grey-2);
    font-family: 'JetBrains Mono', monospace;
    margin-top: 5px;
    text-align: right;
}
.msg.user .msg-time { text-align: right; }

/* Typing indicator */
.typing { display: flex; gap: 5px; padding: 14px 18px; align-items: center; }
.typing-dot {
    width: 7px; height: 7px; border-radius: 50%; background: var(--red);
    animation: bounce 1.2s infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%,60%,100% { transform: translateY(0); } 30% { transform: translateY(-7px); } }

/* ── Input Area ── */
[data-testid="stChatInput"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
[data-testid="stChatInput"] > div {
    background: var(--black-4) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 4px 8px !important;
}
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.93rem !important;
    line-height: 1.6 !important;
    border: none !important;
    outline: none !important;
    resize: none !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--grey-2) !important; }
[data-testid="stChatInput"] button {
    background: var(--red) !important;
    border-radius: 8px !important;
    color: white !important;
    border: none !important;
}
[data-testid="stChatInput"] button:hover { background: var(--red-light) !important; }

/* ── Streamlit Buttons ── */
.stButton > button {
    background: var(--black-4) !important;
    color: var(--grey-1) !important;
    border: 1px solid var(--border-sub) !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 400 !important;
    padding: 8px 14px !important;
    transition: all 0.18s ease !important;
    letter-spacing: 0.01em !important;
    text-align: left !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    background: var(--red-dim) !important;
    color: var(--white) !important;
    border-color: var(--red) !important;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 40px 0 20px;
    color: var(--grey-2);
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.08em;
}
.footer span { color: var(--red); }

/* Streamlit misc cleanup */
[data-testid="stSpinner"] > div > div { border-top-color: var(--red) !important; }
.stAlert { background: var(--black-4) !important; border-color: var(--border) !important; color: var(--white) !important; }
div[data-testid="stMarkdownContainer"] p { line-height: 1.75; letter-spacing: 0.01em; }
</style>
""", unsafe_allow_html=True)

# ── Resume Knowledge Base ─────────────────────────────────────────────────────
RESUME_CONTEXT = """
PROFESSIONAL PROFILE — ASHIK ROSHAN I
======================================
Current Role  : Data & AI Engineer – Level 2
Email         : ashikroshan261@gmail.com
GitHub        : https://github.com/AshikRoshan-github
LinkedIn      : https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium        : https://medium.com/@ashikroshan261
Portfolio     : https://arshowcase.streamlit.app

TECHNICAL EXPERTISE
-------------------
Programming Languages  : Python, SQL, JavaScript, HTML, CSS
Cloud – Microsoft Azure: Blob Storage, Data Lake, Azure SQL Database, Azure OpenAI,
                         Databricks, Azure Data Factory (ADF), Azure VM,
                         Azure Document Intelligence, Function App
Cloud – Amazon AWS     : S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock
Data Engineering       : PySpark, DBT, Informatica, Snowflake, Pandas, ADF
Databases              : SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics         : Power BI, ThoughtSpot, Plotly, Streamlit
AI & Generative AI     : Azure OpenAI, Amazon Bedrock, Gemini API Key, LangChain,
                         Neo4j, Retrieval-Augmented Generation (RAG), Prompt Engineering,
                         Azure Document Intelligence
Automation & Web       : Selenium, Web Scraping, Web Crawling, FastAPI, PyAutoGUI, Apify, Flask
DevOps & Tooling       : GitHub, Azure DevOps, CI/CD Pipelines, PuTTY, ServiceNow, Rally, SharePoint
Libraries & Frameworks : asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict,
                         smtplib, oracledb, pywin, pytesseract, python-dotenv

PROFESSIONAL EXPERIENCE
-----------------------
1. Data Engineer – L2   | Optisol Business Solutions | April 2025 – Present
2. Data Engineer – L1   | Optisol Business Solutions | August 2024 – March 2025
3. Data Engineer Intern | Optisol Business Solutions | March 2024 – July 2024
4. Trainee Software Engineer | Blue Cloud            | June 2023 – March 2024

EDUCATION
---------
Bachelor of Engineering — Computer Science
KLN College of Engineering | 2019 – 2023 | Grade: A+

CERTIFICATIONS
--------------
Cloud & Data Engineering:
  • SnowPro Core Certification — Snowflake
  • Microsoft Certified: Azure Data Fundamentals — Microsoft
  • Databricks Lakehouse Fundamentals — Databricks

Data Tools & Engineering:
  • dbt Learn Fundamentals — dbt Labs
  • SQL (Basic) Certificate — HackerRank

AI & Programming:
  • Generative AI Fundamentals — Databricks Academy
  • 100 Days of Code: Python Pro Bootcamp — Udemy
  • Snowflake Masterclass — Udemy

AWARDS & RECOGNITION — Optisol Business Solutions (2024–Present)
-----------------------------------------------------------------
★ Most Valuable Person (MVP) Award | 2024–2025
  The organisation's highest honour, recognising consistent performance excellence,
  cross-functional leadership, and significant contribution to long-term project success.

★ Spot Award — Project Excellence & Leadership | January 2026
  Awarded by the CTO for mature, solution-driven management of a high-impact project delivery.

★ Spot Award — RS ARP Project Go-Live | November 2025
  Recognised for exceptional contribution to the "Beatty Go-Live" rollout and managing
  complex Delta Load operations under tight delivery timelines.

★ Spot Award — AI Tool Innovation (NotebookLLM) | May 2025
  Took initiative to evaluate, demo, and drive organisation-wide adoption of NotebookLLM
  to measurably improve project efficiency.

★ Spot Award — Community Mentorship | March 2025
  Delivered technical sessions for college students on interview preparation and emerging technologies.

★ OKR Top Contributor — Q4 | October–December 2024
  Honoured for a pivotal role in achieving company-wide Objectives and Key Results.

★ Spot Award — Client Excellence (Ontology Mapping) | December 2024
  Received high client praise for a solution-oriented presentation during an on-site visit.

★ Spot Award — Generative AI & Automation | July 2024
  Implemented a GenAI-based solution to automate data inventory; served as SME resolving DBT blockers.

DATA ENGINEERING PROJECTS
--------------------------
Project 1: Python-Based Data Migration — Google Sheets to Azure SQL Database
  Role  : Data Engineer | Client: Internal Business Team | Optisol Business Solutions
  Tech  : Python (Pandas, gspread, pyodbc), SQL, Azure SQL Database, Azure VM, Cron Jobs, GitHub
  Impact: Automated full and incremental data load logic; reduced manual effort significantly.

Project 2: On-Premises to Snowflake Data Warehouse Migration
  Role  : Data Engineer | Client: Republic Services (Waste Disposal) | Optisol Business Solutions
  Tech  : Snowflake, Informatica, dbt, Oracle, SQL Server, AWS (EC2, Step Functions, CloudWatch)
  Impact: Migrated enterprise data warehouse; built CDC-based pipelines and dbt ELT transformations.

Project 3: Enterprise Database Migration — Oracle to SQL Server (On-Premises)
  Role  : Data Engineer | Client: Republic Services (Waste Disposal) | Optisol Business Solutions
  Tech  : Oracle, SQL Server, Python, Autogen ETL Framework, T-SQL, SharePoint, ServiceNow, GitHub
  Impact: End-to-end schema migration with structured environment promotion and UAT support.

Project 4: API-Driven Data Migration — Podio to Azure SQL Database
  Role  : Data Engineer | Client: Jiffy – Cultural Exchange Agencies | Optisol Business Solutions
  Tech  : Python, REST API, Pandas, Azure Data Factory, Azure SQL Database, Blob Storage, AzCopy
  Impact: Built ADF pipelines across Staging → Mirror → Test → Production layers.

AI & AUTOMATION ENGINEERING PROJECTS
--------------------------------------
Project 5: Automated Web Data Extraction & Reporting Platform
  Role  : Automation Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python (Selenium, PyAutoGUI, smtplib), Chrome WebDriver, Email Automation, Azure DevOps
  Impact: Eliminated recurring manual operations through end-to-end browser and report automation.

Project 6: AI-Driven Web Scraping with LangChain & Apify Integration
  Role  : Automation Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python, LangChain, Apify (Actors & API), REST APIs, GitHub
  Impact: Scalable cloud-based web crawling with LLM-ready structured data output.

Project 7: AI-Powered Automated Data Profiling Platform
  Role  : Data & AI Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python (pyodbc), Snowflake Connector, Azure OpenAI, Streamlit, Prompt Engineering, GitHub
  Impact: Automated profiling across heterogeneous sources with AI-generated quality insights.

Project 8: AI-Powered Pandas Code Generation & Self-Healing Data Transformation Agent
  Role  : Data & AI Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python, Azure OpenAI, Pandas, JSON, Prompt Engineering, GitHub
  Impact: Self-healing agent regenerates corrected transformation code upon runtime errors.

Project 9: Ontology Kit — Data Mapping Agent
  Role  : Data & AI Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python, Gemini API Key, Streamlit, Pandas, PyODBC, GitHub
  Impact: Reduced manual data mapping effort by 40–50% through AI-driven ontology alignment.

Project 10: AI-Powered Document Processing & Structured Data Extraction Tool
  Role  : AI Engineer | Client: Republic Services Hackathon | Optisol Business Solutions
  Tech  : Python, AWS Textract, Amazon Bedrock, EC2, S3, JSON, Flask, Prompt Engineering, GitHub
  Impact: Converts scanned PDFs and images into structured, integration-ready JSON.

Project 11: Internationalization HTML Validation & Automation Tool
  Role  : AI / Data Engineer | Client: Optisol Business Solutions
  Tech  : Python, HTML Parsing, i18n, JSON, CLI Automation, GitHub
  Impact: Detects missing localisation keys and generates structured JSON developer reports.

Project 12: Automated Internationalization Workflow
  Role  : Automation Engineer | Client: IBEAM – Internal Product Team | Optisol Business Solutions
  Tech  : Python, i18n Automation Scripts, JSON, Batch Processing, GitHub
  Impact: Integrates i18n validation directly into CI/CD pipelines.

Project 13: Credit Risk Reporting & JSON Data Intelligence Platform
  Role  : Data & AI Engineer | Client: Atradius – Trade Credit Insurance | Optisol Business Solutions
  Tech  : Python, Google Gemini API Key, asyncio, Plotly, JSON, CLI Automation, GitHub
  Impact: Mapped, classified, and enriched company data across 40+ credit risk blocks;
          built custom async rate limiter using token bucket algorithm for Gemini API Key API.

Project 14: Knowledge Graph Builder (KGB) with RAG
  Role  : Data & AI Engineer | Client: Internal Platform | Optisol Business Solutions
  Tech  : Python, Streamlit, LangChain, Azure OpenAI, Neo4j, PyVis, PyPDF2, asyncio, JSON/XML, GitHub
  Impact: Transforms unstructured documents (PDF, DOCX, TXT, JSON, XML, SQL) into interactive,
          queryable knowledge graphs with natural-language-to-Cypher query generation and RAG.
"""

SYSTEM_PROMPT = f"""You are a highly professional AI Assistant representing Ashik Roshan I's career portfolio.

Your role is to answer questions about Ashik's professional background — his skills, experience, projects,
education, certifications, and achievements — in a polished, articulate, and confident manner.

STRICTLY use only the information provided below. If something is not covered, say so graciously.

{RESUME_CONTEXT}

Response Guidelines:
- Write in fluent, professional British-style English with precise word choices.
- Use well-structured paragraphs with clear topic sentences.
- Use bullet points only when listing multiple distinct items (skills, tech stacks, achievements).
- Keep responses concise yet comprehensive — avoid unnecessary filler words.
- Refer to Ashik in the third person (e.g., "Ashik brings expertise in…").
- Be warm, confident, and persuasive — position Ashik's experience in the best professional light.
- When discussing projects, highlight the business impact and technologies used.
- Always maintain a high standard of written English — no informal language.
"""

# ── Load API Key from Secrets ─────────────────────────────────────────────────
try:
    api_key = st.secrets["credentials"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("API key not configured. Please add GEMINI_API_KEY to your Streamlit secrets.")
    st.stop()

# ── Session State ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">⚡ AI-Powered Career Portfolio</div>
    <div class="hero-name">Ashik <span>Roshan</span> I.</div>
    <div class="hero-role">Data &amp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions &nbsp;·&nbsp; L2</div>
    <div class="hero-links">
        <a class="hero-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub ↗</a>
        <a class="hero-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn ↗</a>
        <a class="hero-link" href="https://medium.com/@ashikroshan261" target="_blank">Medium ↗</a>
        <a class="hero-link" href="https://arshowcase.streamlit.app" target="_blank">Portfolio ↗</a>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Stats Row ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-num">2+</div>
        <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">14</div>
        <div class="stat-label">Projects Delivered</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">8</div>
        <div class="stat-label">Awards Won</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">9</div>
        <div class="stat-label">Certifications</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Quick Questions ───────────────────────────────────────────────────────────
st.markdown('<div class="chips-label">💬 &nbsp; Suggested Questions</div>', unsafe_allow_html=True)

questions = [
    ("🛠️", "Top technical skills"),
    ("💼", "Work experience timeline"),
    ("🤖", "AI & GenAI projects"),
    ("📊", "Data engineering projects"),
    ("🏆", "Awards & recognition"),
    ("📜", "Certifications held"),
    ("🎓", "Educational background"),
    ("🔥", "Most impactful project"),
]

cols = st.columns(4)
for i, (icon, label) in enumerate(questions):
    with cols[i % 4]:
        if st.button(f"{icon}  {label}", key=f"q_{i}"):
            st.session_state.pending_question = label

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

# ── Chat Interface ────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-wrap">
    <div class="chat-header">
        <div class="chat-dot dot-red"></div>
        <div class="chat-dot dot-y"></div>
        <div class="chat-dot dot-g"></div>
        <span class="chat-title">AI ASSISTANT — ASHIK ROSHAN PORTFOLIO</span>
    </div>
    <div class="chat-messages">
""", unsafe_allow_html=True)

# Welcome message
if not st.session_state.messages:
    st.markdown("""
    <div class="msg">
        <div class="avatar ai-av">AR</div>
        <div>
            <div class="bubble ai-bubble">
                Welcome. I am Ashik Roshan's AI Assistant — your dedicated resource for exploring his professional profile.<br><br>
                I can provide detailed insights on his <strong>technical expertise</strong>, <strong>project portfolio</strong>,
                <strong>professional experience</strong>, <strong>certifications</strong>, and <strong>career achievements</strong>.<br><br>
                How may I assist you today?
            </div>
            <div class="msg-time">Just now</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Render conversation history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg user">
            <div class="avatar usr-av">You</div>
            <div>
                <div class="bubble user-bubble">{msg["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        content = msg["content"].replace("\n", "<br>")
        st.markdown(f"""
        <div class="msg">
            <div class="avatar ai-av">AR</div>
            <div>
                <div class="bubble ai-bubble">{content}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

# ── Input & Response Logic ────────────────────────────────────────────────────
user_input = st.chat_input("Ask about skills, projects, experience, awards…")

if st.session_state.pending_question:
    user_input = st.session_state.pending_question
    st.session_state.pending_question = None

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner(""):
        try:
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=SYSTEM_PROMPT,
            )
            history = []
            for m in st.session_state.messages[:-1]:
                role = "user" if m["role"] == "user" else "model"
                history.append({"role": role, "parts": [m["content"]]})

            chat = model.start_chat(history=history)
            response = chat.send_message(user_input)
            answer = response.text

        except Exception as e:
            answer = f"An error occurred while processing your request. Please try again.\n\n`{e}`"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

# ── Reset Button ──────────────────────────────────────────────────────────────
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("↺  Reset", key="reset"):
        st.session_state.messages = []
        st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div>Ashik Roshan I &nbsp;·&nbsp; Data &amp; AI Engineer &nbsp;·&nbsp; <span>Optisol Business Solutions</span></div>
    <div style="margin-top:6px; color:#3a3a3a;">AI Assistant &nbsp;·&nbsp; Professional Portfolio &nbsp;·&nbsp; All information sourced from official resume</div>
</div>
""", unsafe_allow_html=True)
