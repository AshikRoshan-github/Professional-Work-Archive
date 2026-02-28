import streamlit as st
import google.generativeai as genai

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan I — Portfolio",
    page_icon="🔶",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:          #0a0a0a;
  --surface:     #111111;
  --surface2:    #181818;
  --surface3:    #202020;
  --border:      #2a2a2a;
  --border-hot:  rgba(255,107,0,0.45);
  --orange:      #ff6b00;
  --orange-dim:  rgba(255,107,0,0.10);
  --orange-glow: rgba(255,107,0,0.06);
  --text:        #f0ede8;
  --text-2:      #8a8580;
  --text-3:      #4a4744;
  --white:       #ffffff;
}

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
section.main { background: var(--bg) !important; color: var(--text) !important; }

[data-testid="stHeader"]           { background: var(--bg) !important; border-bottom: 1px solid var(--border); }
[data-testid="stSidebar"]          { display: none !important; }
[data-testid="collapsedControl"]   { display: none !important; }
[data-testid="stMainBlockContainer"]{ padding: 0 !important; }

.block-container {
  max-width: 780px !important;
  padding: 0 28px 80px !important;
  margin: 0 auto !important;
}

/* ── Typography System ── */
h1,h2,h3,h4 { font-family: 'Sora', sans-serif !important; }
p, span, div, label, li { font-family: 'Sora', sans-serif; }

/* ── TOP BAR ── */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 22px 0 22px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 52px;
}
.topbar-left {
  display: flex;
  align-items: center;
  gap: 10px;
}
.topbar-dot {
  width: 8px; height: 8px;
  background: var(--orange);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--orange);
}
.topbar-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  color: var(--text-2);
  text-transform: uppercase;
}
.topbar-links {
  display: flex;
  gap: 24px;
}
.topbar-link {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  color: var(--text-3);
  text-decoration: none;
  text-transform: uppercase;
  transition: color 0.2s;
}
.topbar-link:hover { color: var(--orange); }

/* ── IDENTITY BLOCK ── */
.identity {
  margin-bottom: 56px;
}
.identity-eyebrow {
  font-family: 'Fira Code', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 16px;
}
.identity-name {
  font-family: 'Instrument Serif', serif;
  font-size: clamp(3rem, 8vw, 5rem);
  font-weight: 400;
  line-height: 1.0;
  color: var(--white);
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}
.identity-name em {
  font-style: italic;
  color: var(--orange);
}
.identity-role {
  font-size: 0.95rem;
  font-weight: 300;
  color: var(--text-2);
  letter-spacing: 0.02em;
  line-height: 1.6;
  max-width: 480px;
}
.identity-role strong {
  color: var(--text);
  font-weight: 500;
}

/* ── DIVIDER ── */
.rule {
  height: 1px;
  background: var(--border);
  margin: 0 0 48px;
}

/* ── CHAT LABEL ROW ── */
.chat-label-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}
.chat-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--text-3);
}
.status-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: var(--text-3);
  text-transform: uppercase;
}
.status-dot {
  width: 6px; height: 6px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 6px #22c55e;
}

/* ── QUESTION CHIPS ── */
.chips-section { margin-bottom: 32px; }
.chips-title {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--text-3);
  margin-bottom: 12px;
}

/* ── CHAT WINDOW ── */
.chat-window {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 16px;
}
.chat-chrome {
  background: var(--surface2);
  border-bottom: 1px solid var(--border);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.chrome-dots { display: flex; gap: 7px; }
.cdot {
  width: 10px; height: 10px;
  border-radius: 50%;
}
.cdot-r { background: #ff5f57; }
.cdot-y { background: #febc2e; }
.cdot-g { background: #28c840; }
.chrome-title {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  color: var(--text-3);
  text-transform: uppercase;
}

/* ── MESSAGES ── */
.chat-body { padding: 28px 24px; }

.msg-row { display: flex; gap: 14px; margin-bottom: 28px; }
.msg-row.user { flex-direction: row-reverse; }

.av {
  width: 36px; height: 36px;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Fira Code', monospace;
  font-size: 0.62rem;
  font-weight: 500;
  flex-shrink: 0;
  letter-spacing: 0.05em;
}
.av-ai  { background: var(--orange); color: #000; }
.av-usr { background: var(--surface3); color: var(--text-2); border: 1px solid var(--border); }

.bubble-wrap { max-width: 82%; }
.bubble-name {
  font-size: 0.67rem;
  letter-spacing: 0.06em;
  color: var(--text-3);
  margin-bottom: 6px;
  font-family: 'Fira Code', monospace;
  text-transform: uppercase;
}
.msg-row.user .bubble-name { text-align: right; }

.bubble {
  padding: 14px 18px;
  border-radius: 12px;
  font-size: 0.905rem;
  line-height: 1.78;
  letter-spacing: 0.008em;
  font-weight: 300;
}
.bubble-ai {
  background: var(--surface2);
  border: 1px solid var(--border);
  color: var(--text);
  border-top-left-radius: 3px;
}
.bubble-user {
  background: var(--orange);
  color: #000;
  font-weight: 500;
  border-top-right-radius: 3px;
  font-size: 0.88rem;
}

/* ── INPUT ── */
[data-testid="stChatInput"] {
  background: transparent !important;
  padding: 0 !important;
}
[data-testid="stChatInput"] > div {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  transition: border-color 0.2s !important;
}
[data-testid="stChatInput"] > div:focus-within {
  border-color: var(--border-hot) !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.9rem !important;
  font-weight: 300 !important;
  line-height: 1.6 !important;
  border: none !important;
}
[data-testid="stChatInput"] textarea::placeholder {
  color: var(--text-3) !important;
}
[data-testid="stChatInput"] button {
  background: var(--orange) !important;
  border-radius: 8px !important;
  border: none !important;
  color: #000 !important;
}
[data-testid="stChatInput"] button:hover {
  opacity: 0.85 !important;
}

/* ── STREAMLIT BUTTONS (chips + clear) ── */
.stButton > button {
  font-family: 'Sora', sans-serif !important;
  font-size: 0.8rem !important;
  font-weight: 400 !important;
  background: var(--surface) !important;
  color: var(--text-2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  padding: 8px 14px !important;
  transition: all 0.18s ease !important;
  letter-spacing: 0.01em !important;
  white-space: nowrap !important;
}
.stButton > button:hover {
  background: var(--orange-dim) !important;
  color: var(--orange) !important;
  border-color: var(--border-hot) !important;
}

/* Clear button override */
.clear-btn > button {
  background: transparent !important;
  color: var(--text-3) !important;
  border: 1px solid var(--border) !important;
  font-family: 'Fira Code', monospace !important;
  font-size: 0.68rem !important;
  letter-spacing: 0.1em !important;
  padding: 6px 14px !important;
  border-radius: 6px !important;
}
.clear-btn > button:hover {
  border-color: #ff5f57 !important;
  color: #ff5f57 !important;
  background: rgba(255,95,87,0.06) !important;
}

/* ── FOOTER ── */
.footer {
  margin-top: 60px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.footer-left {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: var(--text-3);
  text-transform: uppercase;
}
.footer-left span { color: var(--orange); }
.footer-right {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.08em;
  color: var(--text-3);
}

/* Streamlit misc cleanup */
[data-testid="stSpinner"] > div > div { border-top-color: var(--orange) !important; }
div[data-testid="stMarkdownContainer"] > div { all: unset; display: block; }
</style>
""", unsafe_allow_html=True)

# ── Resume Knowledge Base ─────────────────────────────────────────────────────
RESUME_CONTEXT = """
PROFESSIONAL PROFILE — ASHIK ROSHAN I
======================================
Current Role  : Data & AI Engineer — Level 2
Email         : ashikroshan261@gmail.com
GitHub        : https://github.com/AshikRoshan-github
LinkedIn      : https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium        : https://medium.com/@ashikroshan261
Portfolio     : https://arshowcase.streamlit.app

TECHNICAL EXPERTISE
-------------------
Languages              : Python, SQL, JavaScript, HTML, CSS
Cloud — Azure          : Blob Storage, Data Lake, Azure SQL Database, Azure OpenAI,
                         Databricks, Azure Data Factory (ADF), Azure VM,
                         Azure Document Intelligence, Function App
Cloud — AWS            : S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock
Data Engineering       : PySpark, DBT, Informatica, Snowflake, Pandas, ADF
Databases              : SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics         : Power BI, ThoughtSpot, Plotly, Streamlit
AI & Generative AI     : Azure OpenAI, Amazon Bedrock, Gemini 2.5 Pro, LangChain,
                         Neo4j, RAG, Prompt Engineering, Azure Document Intelligence
Automation & Web       : Selenium, Web Scraping, Web Crawling, FastAPI, PyAutoGUI, Apify, Flask
DevOps & Tooling       : GitHub, Azure DevOps, CI/CD, PuTTY, ServiceNow, Rally, SharePoint
Libraries & Frameworks : asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict,
                         smtplib, oracledb, pywin, pytesseract, python-dotenv

PROFESSIONAL EXPERIENCE
-----------------------
1. Data Engineer — L2    | Optisol Business Solutions | April 2025 – Present
2. Data Engineer — L1    | Optisol Business Solutions | August 2024 – March 2025
3. Data Engineer Intern  | Optisol Business Solutions | March 2024 – July 2024
4. Trainee Soft. Engineer | Blue Cloud                | June 2023 – March 2024

EDUCATION
---------
Bachelor of Engineering — Computer Science
KLN College of Engineering | 2019 – 2023 | Grade: A+

CERTIFICATIONS
--------------
Cloud & Data Engineering:
  • SnowPro Core Certification — Snowflake
  • Microsoft Certified: Azure Data Fundamentals
  • Databricks Lakehouse Fundamentals

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
  The organisation's highest honour, awarded for consistent performance excellence,
  cross-functional leadership, and contribution to long-term project success.

★ Spot Award — Project Excellence & Leadership | January 2026
  Awarded by the CTO for mature, solution-driven management of a high-impact project delivery.

★ Spot Award — RS ARP Project Go-Live | November 2025
  Recognised for exceptional contribution to the Beatty Go-Live rollout and managing
  complex Delta Load operations under tight timelines.

★ Spot Award — AI Tool Innovation (NotebookLLM) | May 2025
  Drove organisation-wide adoption of NotebookLLM to measurably improve project efficiency.

★ Spot Award — Community Mentorship | March 2025
  Delivered technical sessions for college students on interview preparation and emerging technologies.

★ OKR Top Contributor — Q4 | October–December 2024
  Honoured for a pivotal role in achieving company-wide Objectives and Key Results.

★ Spot Award — Client Excellence (Ontology Mapping) | December 2024
★ Spot Award — Generative AI & Automation | July 2024

DATA ENGINEERING PROJECTS
--------------------------
Project 1: Python-Based Data Migration — Google Sheets to Azure SQL Database
  Role: Data Engineer | Client: Internal | Optisol Business Solutions
  Tech: Python (Pandas, gspread, pyodbc), Azure SQL Database, Azure VM, Cron Jobs, GitHub

Project 2: On-Premises to Snowflake Data Warehouse Migration
  Role: Data Engineer | Client: Republic Services (Waste Disposal)
  Tech: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS (EC2, Step Functions, CloudWatch)

Project 3: Enterprise Database Migration — Oracle to SQL Server
  Role: Data Engineer | Client: Republic Services (Waste Disposal)
  Tech: Oracle, SQL Server, Python, Autogen ETL Framework, T-SQL, ServiceNow, GitHub

Project 4: API-Driven Data Migration — Podio to Azure SQL Database
  Role: Data Engineer | Client: Jiffy – Cultural Exchange Agencies
  Tech: Python, REST API, Pandas, Azure Data Factory, Azure SQL Database, Blob Storage, AzCopy

AI & AUTOMATION ENGINEERING PROJECTS
--------------------------------------
Project 5: Automated Web Data Extraction & Reporting Platform
  Tech: Python (Selenium, PyAutoGUI, smtplib), Chrome WebDriver, Email Automation

Project 6: AI-Driven Web Scraping with LangChain & Apify
  Tech: Python, LangChain, Apify Actors & API, REST APIs

Project 7: AI-Powered Automated Data Profiling Platform
  Tech: Python, Snowflake Connector, Azure OpenAI, Streamlit, Prompt Engineering

Project 8: AI-Powered Pandas Code Generation & Self-Healing Agent
  Tech: Python, Azure OpenAI, Pandas, Prompt Engineering
  Self-healing: detects runtime errors, regenerates corrected code automatically.

Project 9: Ontology Kit — Data Mapping Agent
  Tech: Python, Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
  Impact: Reduced manual data mapping effort by 40–50%.

Project 10: AI-Powered Document Processing & Structured Data Extraction
  Client: Republic Services Hackathon
  Tech: Python, AWS Textract, Amazon Bedrock, EC2, S3, Flask
  Converts scanned PDFs and images into structured, integration-ready JSON.

Project 11: Internationalization HTML Validation Tool
  Tech: Python, HTML Parsing, i18n, JSON, CLI Automation

Project 12: Automated Internationalization Workflow
  Tech: Python, i18n Automation Scripts, JSON, Batch Processing, CI/CD integration

Project 13: Credit Risk Reporting & JSON Data Intelligence Platform
  Client: Atradius — Trade Credit Insurance
  Tech: Python, Google Gemini 2.5 Pro, asyncio, Plotly, JSON
  Built async rate limiter (token bucket) for Gemini API; mapped 40+ credit risk blocks.

Project 14: Knowledge Graph Builder (KGB) with RAG
  Client: Internal Platform | Optisol Business Solutions
  Tech: Python, Streamlit, LangChain, Azure OpenAI, Neo4j, PyVis, PyPDF2, asyncio
  Transforms unstructured documents into interactive, queryable knowledge graphs with RAG.
"""

SYSTEM_PROMPT = f"""You are a highly professional AI Assistant representing Ashik Roshan I's career portfolio.

Answer questions about Ashik's skills, experience, projects, education, certifications, and achievements
in a polished, articulate, and confident manner.

Use ONLY the resume information below. If something is not covered, say so graciously.

{RESUME_CONTEXT}

Response Guidelines:
- Write in fluent, professional English with precise word choices.
- Refer to Ashik in the third person (e.g., "Ashik brings expertise in…").
- Use well-structured paragraphs. Use bullet points only when listing multiple distinct items.
- Be concise yet comprehensive — no filler words or unnecessary repetition.
- Highlight business impact and specific technologies when discussing projects.
- Maintain a warm, confident, and persuasive tone throughout.
"""

# ── Load API Key ──────────────────────────────────────────────────────────────
try:
    api_key = st.secrets["credentials"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠️ API key not configured. Please add GEMINI_API_KEY to Streamlit secrets.")
    st.stop()

# ── Session State ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending" not in st.session_state:
    st.session_state.pending = None

# ═══════════════════════════════════════════════════════════════════════════════
# LAYOUT
# ═══════════════════════════════════════════════════════════════════════════════

# ── Top Bar ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-left">
    <div class="topbar-dot"></div>
    <span class="topbar-label">AI Portfolio — Ashik Roshan I</span>
  </div>
  <div class="topbar-links">
    <a class="topbar-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub</a>
    <a class="topbar-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn</a>
    <a class="topbar-link" href="https://arshowcase.streamlit.app" target="_blank">Portfolio</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Identity Block ────────────────────────────────────────────────────────────
st.markdown("""
<div class="identity">
  <div class="identity-eyebrow">Data &amp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions &nbsp;·&nbsp; L2</div>
  <div class="identity-name">Ashik <em>Roshan</em> I.</div>
  <div class="identity-role">
    Building intelligent data systems at the intersection of
    <strong>Cloud Engineering</strong>, <strong>Generative AI</strong>,
    and <strong>Automation</strong> — turning complex data challenges into
    measurable business outcomes.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Rule ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# ── Chips label + Clear button row ───────────────────────────────────────────
col_label, col_spacer, col_clear = st.columns([5, 1, 2])
with col_label:
    st.markdown('<div class="chips-title" style="padding-top:6px">Ask about me</div>', unsafe_allow_html=True)
with col_clear:
    st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
    if st.button("✕  Clear Chat", key="clear"):
        st.session_state.messages = []
        st.session_state.pending = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ── Suggestion Chips (2 rows of 4) ────────────────────────────────────────────
QUESTIONS = [
    "What are Ashik's core technical skills?",
    "Walk me through his work experience",
    "Tell me about his AI & GenAI projects",
    "What data engineering projects has he done?",
    "What awards and recognition has he received?",
    "Which certifications does he hold?",
    "What is his educational background?",
    "What is his most impactful project?",
]

row1 = st.columns(4)
row2 = st.columns(4)
all_cols = row1 + row2

for i, (col, q) in enumerate(zip(all_cols, QUESTIONS)):
    with col:
        short = q.replace("What are Ashik's ", "").replace("What ", "").replace("Tell me about his ", "").replace("Walk me through his ", "").replace("Which ", "").replace("What is his ", "").replace("What is his most ", "").capitalize()
        short = short[:28] + ("…" if len(short) > 28 else "")
        if st.button(short, key=f"chip_{i}"):
            st.session_state.pending = q

st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

# ── Chat Header Row ───────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-label-row">
  <span class="chat-label">Conversation</span>
  <div class="status-pill">
    <div class="status-dot"></div>
    <span>AI Assistant — Online</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Chat Window ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-window">
  <div class="chat-chrome">
    <div class="chrome-dots">
      <div class="cdot cdot-r"></div>
      <div class="cdot cdot-y"></div>
      <div class="cdot cdot-g"></div>
    </div>
    <span class="chrome-title">portfolio.assistant</span>
    <span style="width:52px"></span>
  </div>
  <div class="chat-body">
""", unsafe_allow_html=True)

# Welcome message when empty
if not st.session_state.messages:
    st.markdown("""
    <div class="msg-row">
      <div class="av av-ai">AI</div>
      <div class="bubble-wrap">
        <div class="bubble-name">Assistant</div>
        <div class="bubble bubble-ai">
          Good day. I am Ashik Roshan's dedicated AI Assistant — your gateway to exploring his professional journey.<br><br>
          Whether you are a recruiter, collaborator, or curious visitor, I am here to walk you through his
          <strong style="color:#f0ede8">technical expertise</strong>,
          <strong style="color:#f0ede8">project portfolio</strong>,
          <strong style="color:#f0ede8">career milestones</strong>, and
          <strong style="color:#f0ede8">achievements</strong>.<br><br>
          Select a question above or type your own below to get started.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Render conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg-row user">
          <div class="av av-usr">YOU</div>
          <div class="bubble-wrap">
            <div class="bubble-name">You</div>
            <div class="bubble bubble-user">{msg["content"]}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        content = msg["content"].replace("**", "").replace("\n\n", "<br><br>").replace("\n", "<br>")
        st.markdown(f"""
        <div class="msg-row">
          <div class="av av-ai">AI</div>
          <div class="bubble-wrap">
            <div class="bubble-name">Assistant</div>
            <div class="bubble bubble-ai">{content}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)  # close chat-body, chat-window

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask anything about Ashik's skills, projects, or experience…")

# Handle chip click
if st.session_state.pending:
    user_input = st.session_state.pending
    st.session_state.pending = None

# ── Generate Response ─────────────────────────────────────────────────────────
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
            answer = f"An error occurred. Please try again.\n\n`{e}`"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div class="footer-left"><span>Ashik Roshan I</span> &nbsp;·&nbsp; Data &amp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions</div>
  <div class="footer-right">ashikroshan261@gmail.com</div>
</div>
""", unsafe_allow_html=True)
