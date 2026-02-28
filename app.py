import streamlit as st
import google.generativeai as genai
import re

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan I — AI Assistant",
    page_icon="🔶",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:          #080808;
  --s1:          #0f0f0f;
  --s2:          #141414;
  --s3:          #1a1a1a;
  --s4:          #222222;
  --border:      #282828;
  --orange:      #f97316;
  --orange-soft: rgba(249,115,22,0.12);
  --orange-bdr:  rgba(249,115,22,0.30);
  --text:        #edebe6;
  --text2:       #787470;
  --text3:       #3e3c3a;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── Global reset ── */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
section.main {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
}

/* Hide Streamlit chrome */
[data-testid="stHeader"]         { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
footer                           { display: none !important; }
#MainMenu                        { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: #f0f4ff !important;
  border-right: 1px solid #c8d5ee !important;
  min-width: 290px !important;
  max-width: 290px !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding: 0 !important;
}

/* ── MAIN AREA ── */
[data-testid="stMainBlockContainer"] {
  padding: 0 !important;
}
.block-container {
  max-width: 740px !important;
  padding: 0 36px 60px !important;
  margin: 0 auto !important;
}



/* ── IDENTITY ── */
.identity { margin-bottom: 52px; padding-top: 48px; }
.eyebrow {
  font-family: 'Fira Code', monospace;
  font-size: 0.66rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 16px;
}
.name {
  font-family: 'Instrument Serif', serif;
  font-size: clamp(2.8rem, 5.5vw, 4.4rem);
  font-weight: 400;
  line-height: 1.02;
  letter-spacing: -0.02em;
  color: #fff;
  margin-bottom: 18px;
}
.name em { font-style: italic; color: var(--orange); }
.bio {
  font-size: 0.92rem;
  font-weight: 300;
  color: var(--text2);
  line-height: 1.8;
  max-width: 500px;
}
.bio strong { color: var(--text); font-weight: 500; }

/* ── RULE ── */
.rule {
  height: 1px;
  background: linear-gradient(90deg, var(--orange-bdr), var(--border) 60%, transparent);
  margin-bottom: 40px;
}

/* ── SIDEBAR INNER ── */
.sb-wrap {
  padding: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Header band */
.sb-header {
  background: linear-gradient(160deg, #1a2f6e 0%, #0f1e4a 100%);
  border-bottom: 1px solid #243580;
  padding: 24px 20px 20px;
}
.sb-header-top {
  display: flex;
  align-items: center;
  gap: 11px;
  margin-bottom: 14px;
}
.sb-avatar {
  width: 42px; height: 42px;
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  border-radius: 11px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
  box-shadow: 0 4px 14px rgba(59,130,246,0.4);
}
.sb-id { flex: 1; }
.sb-name {
  font-family: 'Sora', sans-serif;
  font-size: 0.92rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: -0.01em;
  line-height: 1.2;
  margin-bottom: 3px;
}
.sb-role {
  font-family: 'Fira Code', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #93c5fd;
}
.sb-company {
  font-family: 'Fira Code', monospace;
  font-size: 0.56rem;
  letter-spacing: 0.07em;
  color: #4a6096;
  margin-top: 2px;
}
.sb-bio {
  font-size: 0.74rem;
  font-weight: 300;
  color: #7b9acf;
  line-height: 1.6;
  margin-bottom: 14px;
}
.sb-links {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}
.sb-link {
  font-family: 'Fira Code', monospace;
  font-size: 0.57rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #93c5fd;
  text-decoration: none;
  border: 1px solid rgba(147,197,253,0.25);
  border-radius: 5px;
  padding: 4px 9px;
  transition: all 0.18s;
  background: rgba(255,255,255,0.06);
}
.sb-link:hover {
  color: #fff;
  border-color: rgba(255,255,255,0.4);
  background: rgba(255,255,255,0.12);
}

/* Body */
.sb-body { padding: 14px 14px 20px; flex: 1; overflow-y: auto; }

.sb-section-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.57rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #94a3c0;
  margin-bottom: 6px;
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}
.sb-section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #d1d9ee;
}

/* Sidebar question buttons */
[data-testid="stSidebar"] .stButton > button {
  all: unset !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  width: 100% !important;
  background: #fff !important;
  border: 1px solid #e2e8f5 !important;
  border-radius: 8px !important;
  padding: 8px 11px !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.78rem !important;
  font-weight: 400 !important;
  color: #3c5080 !important;
  line-height: 1.35 !important;
  cursor: pointer !important;
  transition: all 0.15s ease !important;
  text-align: left !important;
  white-space: normal !important;
  word-break: break-word !important;
  box-sizing: border-box !important;
  margin-bottom: 4px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  background: #1d4ed8 !important;
  border-color: #1d4ed8 !important;
  color: #ffffff !important;
}

/* ── CONV HEADER ── */
.conv-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}
.conv-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text3);
}
.online-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text3);
}
.o-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
}

/* ── CHAT WINDOW ── */
.chat-win {
  background: var(--s1);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 14px;
}
.chat-chrome {
  background: var(--s2);
  border-bottom: 1px solid var(--border);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.cdots { display: flex; gap: 7px; }
.cd { width: 10px; height: 10px; border-radius: 50%; }
.cd-r{background:#ff5f57} .cd-y{background:#febc2e} .cd-g{background:#28c840}
.chrome-text {
  font-family: 'Fira Code', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.1em;
  color: var(--text3);
  text-transform: uppercase;
}

.chat-body { padding: 28px 24px; }

/* ── MESSAGE ROWS ── */
.mrow {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 28px;
}
.mrow:last-child { margin-bottom: 0; }
.mrow.urow { flex-direction: row-reverse; }

.av {
  width: 36px; height: 36px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem;
  flex-shrink: 0;
}
.av-ai  { background: var(--s3); border: 1px solid var(--border); }
.av-usr { background: var(--orange); }

.mcontent { flex: 1; min-width: 0; }
.msender {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 7px;
}
.urow .mcontent { display: flex; flex-direction: column; align-items: flex-end; }
.urow .msender  { text-align: right; }

.bubble {
  display: inline-block;
  padding: 14px 18px;
  border-radius: 13px;
  font-size: 0.875rem;
  font-weight: 300;
  line-height: 1.82;
  letter-spacing: 0.01em;
  max-width: 100%;
  word-break: break-word;
}
.bai {
  background: var(--s2);
  border: 1px solid var(--border);
  color: var(--text);
  border-top-left-radius: 4px;
}
.busr {
  background: var(--orange);
  color: #000;
  font-weight: 500;
  font-size: 0.86rem;
  border-top-right-radius: 4px;
}

/* ── INPUT ── */
[data-testid="stChatInput"] { background: transparent !important; padding: 0 !important; }
[data-testid="stChatInput"] > div {
  background: var(--s1) !important;
  border: 1px solid var(--border) !important;
  border-radius: 13px !important;
}
[data-testid="stChatInput"] > div:focus-within {
  border-color: var(--orange-bdr) !important;
  box-shadow: 0 0 0 3px rgba(249,115,22,0.05) !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 300 !important;
  line-height: 1.6 !important;
  border: none !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text3) !important; }
[data-testid="stChatInput"] button {
  background: var(--orange) !important;
  border-radius: 9px !important;
  border: none !important;
  color: #000 !important;
}
[data-testid="stChatInput"] button:hover { opacity: 0.82 !important; }

/* Spinner */
[data-testid="stSpinner"] > div > div { border-top-color: var(--orange) !important; }
</style>
""", unsafe_allow_html=True)

# ── Resume Data ───────────────────────────────────────────────────────────────
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
Languages              : Python, SQL, JavaScript, HTML, CSS
Cloud — Azure          : Blob Storage, Data Lake, Azure SQL Database, Azure OpenAI,
                         Databricks, ADF, Azure VM, Azure Document Intelligence, Function App
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
1. Data Engineer — L2    | Optisol Business Solutions | April 2025 – Present
2. Data Engineer — L1    | Optisol Business Solutions | August 2024 – March 2025
3. Data Engineer Intern  | Optisol Business Solutions | March 2024 – July 2024
4. Trainee Soft. Engineer | Blue Cloud                | June 2023 – March 2024

EDUCATION
Bachelor of Engineering — Computer Science
KLN College of Engineering | 2019 – 2023 | Grade: A+

CERTIFICATIONS
Cloud & Data Engineering: SnowPro Core (Snowflake), Azure Data Fundamentals (Microsoft),
  Databricks Lakehouse Fundamentals
Data Tools: dbt Learn Fundamentals (dbt Labs), SQL Basic (HackerRank)
AI & Programming: Generative AI Fundamentals (Databricks), 100 Days of Code (Udemy), Snowflake Masterclass (Udemy)

AWARDS & RECOGNITION — Optisol Business Solutions (2024–Present)
★ Most Valuable Person (MVP) Award | 2024–2025 — Highest organisational honour.
★ Spot Award — Project Excellence & Leadership | January 2026 — Awarded by CTO.
★ Spot Award — RS ARP Project Go-Live | November 2025
★ Spot Award — AI Tool Innovation (NotebookLLM) | May 2025
★ Spot Award — Community Mentorship | March 2025
★ OKR Top Contributor — Q4 | October–December 2024
★ Spot Award — Client Excellence (Ontology Mapping) | December 2024
★ Spot Award — Generative AI & Automation | July 2024

PROJECTS — DATA ENGINEERING (4 projects)
P1: Python Data Migration: Google Sheets → Azure SQL Database
  Tech: Python (Pandas, gspread, pyodbc), Azure SQL, Azure VM, Cron Jobs
P2: On-Premises to Snowflake Data Warehouse Migration | Client: Republic Services
  Tech: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS (EC2, Step Functions, CloudWatch)
P3: Enterprise DB Migration: Oracle → SQL Server | Client: Republic Services
  Tech: Oracle, SQL Server, Python, Autogen ETL, T-SQL, ServiceNow
P4: API Data Migration: Podio → Azure SQL | Client: Jiffy – Cultural Exchange Agencies
  Tech: Python, REST API, Pandas, Azure Data Factory, Azure SQL, Blob Storage, AzCopy

PROJECTS — AI & AUTOMATION (10 projects)
P5: Automated Web Data Extraction & Reporting Platform
  Tech: Selenium, PyAutoGUI, smtplib, Chrome WebDriver
P6: AI-Driven Web Scraping — LangChain & Apify Integration
  Tech: Python, LangChain, Apify, REST APIs
P7: AI-Powered Data Profiling Platform
  Tech: Python, Snowflake, Azure OpenAI, Streamlit, Prompt Engineering
P8: AI Pandas Code Generation & Self-Healing Agent
  Tech: Python, Azure OpenAI, Pandas — auto-heals runtime errors
P9: Ontology Kit — Data Mapping Agent | Impact: 40–50% effort reduction
  Tech: Python, Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
P10: AI Document Processing & Structured Data Extraction | Client: Republic Services
  Tech: AWS Textract, Amazon Bedrock, EC2, S3, Flask
P11: Internationalisation HTML Validation Tool
  Tech: Python, HTML Parsing, i18n, JSON
P12: Automated Internationalisation Workflow
  Tech: Python, i18n Scripts, JSON, Batch Processing
P13: Credit Risk Reporting & JSON Data Intelligence | Client: Atradius – Trade Credit Insurance
  Tech: Python, Gemini 2.5 Pro, asyncio, Plotly — 40+ credit risk blocks, token-bucket rate limiter
P14: Knowledge Graph Builder (KGB) with RAG | Client: Internal Platform
  Tech: Python, Streamlit, LangChain, Azure OpenAI, Neo4j, PyVis, PyPDF2, asyncio
  Transforms unstructured docs into interactive knowledge graphs with RAG query layer.
"""

SYSTEM_PROMPT = f"""You are a professional AI Assistant representing Ashik Roshan I's career portfolio.

Answer questions about Ashik's skills, experience, projects, education, certifications, and achievements
in a polished, articulate, and confident manner.

Use ONLY the resume information below. If not covered, say so gracefully.

{RESUME_CONTEXT}

Guidelines:
- Write in fluent, professional English.
- Refer to Ashik in the third person ("Ashik brings...", "His expertise covers...").
- Use well-structured paragraphs. Bullet points only for listing multiple distinct items.
- Be concise yet comprehensive — no filler language.
- Highlight business impact and technologies when discussing projects.
- Warm, confident, and persuasive tone throughout.
"""

# ── API Key ───────────────────────────────────────────────────────────────────
try:
    api_key = st.secrets["credentials"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("API key not configured. Add GEMINI_API_KEY to Streamlit secrets.")
    st.stop()

# ── Session State ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending" not in st.session_state:
    st.session_state.pending = None

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    st.markdown("""
    <div class="sb-wrap">
      <div class="sb-header">
        <div class="sb-header-top">
          <div class="sb-avatar">🤖</div>
          <div class="sb-id">
            <div class="sb-name">Ashik Roshan I.</div>
            <div class="sb-role">Data &amp; AI Engineer — L2</div>
            <div class="sb-company">Optisol Business Solutions</div>
          </div>
        </div>
        <div class="sb-bio">
          Specialising in Cloud Data Engineering, Generative AI, and intelligent automation
          across Azure and AWS ecosystems.
        </div>
        <div class="sb-links">
          <a class="sb-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub ↗</a>
          <a class="sb-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn ↗</a>
          <a class="sb-link" href="https://medium.com/@ashikroshan261" target="_blank">Medium ↗</a>
          <a class="sb-link" href="https://arshowcase.streamlit.app" target="_blank">Portfolio ↗</a>
        </div>
      </div>
      <div class="sb-body">
        <div class="sb-section-label">Ask About Me</div>
    """, unsafe_allow_html=True)

    QUESTIONS = [
        ("🛠️", "Core technical skills",       "What are Ashik's core technical skills and technology stack?"),
        ("💼", "Work experience",              "Walk me through Ashik's professional work experience and career progression."),
        ("🤖", "AI & GenAI projects",          "Tell me about Ashik's AI and Generative AI projects in detail."),
        ("📊", "Data engineering projects",    "What data engineering projects has Ashik delivered?"),
        ("🏆", "Awards & recognition",         "What awards and recognition has Ashik received in his career?"),
        ("📜", "Certifications",               "Which professional certifications does Ashik hold?"),
        ("🎓", "Education",                    "What is Ashik's educational background?"),
        ("⚡", "Most impactful project",       "What is Ashik's most impactful project and what was its business outcome?"),
        ("🧠", "Generative AI expertise",      "How does Ashik apply Generative AI and LLMs in his professional work?"),
        ("☁️", "Cloud expertise",             "What is Ashik's experience with Azure and AWS cloud platforms?"),
    ]

    for icon, label, question in QUESTIONS:
        if st.button(f"{icon}  {label}", key=f"sb_{label}"):
            st.session_state.pending = question

    st.markdown("""
          <div class="sb-section-label" style="margin-top:12px">Actions</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("↺  Reset Conversation", key="reset"):
        st.session_state.messages = []
        st.session_state.pending = None
        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

# ── Identity ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="identity">
  <div class="eyebrow">Data &amp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions &nbsp;·&nbsp; Level 2</div>
  <div class="name">Ashik <em>Roshan</em> I.</div>
  <div class="bio">
    Building intelligent data systems at the intersection of
    <strong>Cloud Engineering</strong>, <strong>Generative AI</strong>, and
    <strong>Automation</strong> — transforming complex data challenges
    into measurable business outcomes.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Divider ───────────────────────────────────────────────────────────────────
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# ── Conversation header ───────────────────────────────────────────────────────
st.markdown("""
<div class="conv-header">
  <span class="conv-label">Conversation</span>
  <div class="online-pill">
    <div class="o-dot"></div>
    <span>AI Assistant &nbsp;·&nbsp; Online</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Chat Window ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-win">
  <div class="chat-chrome">
    <div class="cdots">
      <div class="cd cd-r"></div>
      <div class="cd cd-y"></div>
      <div class="cd cd-g"></div>
    </div>
    <span class="chrome-text">portfolio.assistant — active session</span>
  </div>
  <div class="chat-body">
""", unsafe_allow_html=True)

# Welcome
if not st.session_state.messages:
    st.markdown("""
    <div class="mrow">
      <div class="av av-ai">🤖</div>
      <div class="mcontent">
        <div class="msender">Assistant</div>
        <div class="bubble bai">
          Good day. I am Ashik Roshan's dedicated AI Assistant — your comprehensive resource for
          exploring his professional journey.<br><br>
          I can walk you through his <strong style="color:#edebe6">technical expertise</strong>,
          <strong style="color:#edebe6">14 delivered projects</strong>,
          <strong style="color:#edebe6">career milestones</strong>,
          <strong style="color:#edebe6">certifications</strong>, and
          <strong style="color:#edebe6">8 professional awards</strong>.<br><br>
          Select a topic from the sidebar on the left, or type your question below.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Render messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        safe = msg["content"].replace("<", "&lt;").replace(">", "&gt;")
        st.markdown(f"""
        <div class="mrow urow">
          <div class="av av-usr">🧑</div>
          <div class="mcontent">
            <div class="msender">You</div>
            <div class="bubble busr">{safe}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        content = msg["content"]
        content = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color:#edebe6;font-weight:600">\1</strong>', content)
        content = re.sub(r'^\s*[•\-\*]\s+', '• ', content, flags=re.MULTILINE)
        content = content.replace("\n\n", "<br><br>").replace("\n", "<br>")
        st.markdown(f"""
        <div class="mrow">
          <div class="av av-ai">🤖</div>
          <div class="mcontent">
            <div class="msender">Assistant</div>
            <div class="bubble bai">{content}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask anything about Ashik's skills, projects, or experience…")

if st.session_state.pending:
    user_input = st.session_state.pending
    st.session_state.pending = None

# ── Generate ──────────────────────────────────────────────────────────────────
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
