import streamlit as st
import google.generativeai as genai

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan I — AI Assistant",
    page_icon="🔶",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:         #080808;
  --s1:         #111111;
  --s2:         #161616;
  --s3:         #1e1e1e;
  --border:     #252525;
  --orange:     #f97316;
  --orange-dim: rgba(249,115,22,0.10);
  --orange-bdr: rgba(249,115,22,0.35);
  --text:       #eeebe6;
  --text2:      #7a7570;
  --text3:      #3f3d3a;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
section.main,
[data-testid="stMainBlockContainer"] {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
}

/* Hide Streamlit chrome */
[data-testid="stHeader"]          { display: none !important; }
[data-testid="stSidebar"]         { display: none !important; }
[data-testid="collapsedControl"]  { display: none !important; }
footer                            { display: none !important; }
#MainMenu                         { display: none !important; }

/* Full-width layout */
[data-testid="stMainBlockContainer"] {
  max-width: 100% !important;
  padding: 0 !important;
}
.block-container {
  max-width: 100% !important;
  padding: 0 !important;
}

/* ── APP SHELL ── */
.app-shell {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 40px 40px;
}

/* ── TOP BAR ── */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 28px 0 28px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 60px;
}
.topbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
}
.brand-dot {
  width: 8px; height: 8px;
  background: var(--orange);
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(249,115,22,0.7);
  animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
  0%,100% { opacity: 1; } 50% { opacity: 0.4; }
}
.brand-text {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--text2);
}
.nav-links { display: flex; gap: 28px; }
.nav-link {
  font-family: 'Fira Code', monospace;
  font-size: 0.67rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
  text-decoration: none;
  transition: color 0.2s;
}
.nav-link:hover { color: var(--orange); }

/* ── IDENTITY ── */
.identity { margin-bottom: 60px; }
.id-eyebrow {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 18px;
}
.id-name {
  font-family: 'Instrument Serif', serif;
  font-size: clamp(3.2rem, 6vw, 5.2rem);
  font-weight: 400;
  line-height: 1.0;
  letter-spacing: -0.02em;
  color: #ffffff;
  margin-bottom: 20px;
}
.id-name em { font-style: italic; color: var(--orange); }
.id-bio {
  font-size: 0.95rem;
  font-weight: 300;
  color: var(--text2);
  line-height: 1.75;
  max-width: 560px;
}
.id-bio strong { color: var(--text); font-weight: 500; }

/* ── RULE ── */
.rule {
  height: 1px;
  background: var(--border);
  margin-bottom: 44px;
}

/* ── CHIPS SECTION ── */
.chips-header {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 16px;
}
.chips-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-bottom: 44px;
}
.chip {
  background: var(--s1);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 13px 16px;
  cursor: pointer;
  transition: all 0.18s ease;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}
.chip:hover {
  background: var(--orange-dim);
  border-color: var(--orange-bdr);
}
.chip-icon {
  font-size: 1rem;
  line-height: 1.4;
  flex-shrink: 0;
}
.chip-text {
  font-size: 0.8rem;
  font-weight: 400;
  color: var(--text2);
  line-height: 1.45;
  word-break: break-word;
  hyphens: auto;
}
.chip:hover .chip-text { color: var(--text); }

/* ── CONVERSATION LABEL ── */
.conv-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}
.conv-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--text3);
}
.online-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.63rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text3);
}
.online-dot {
  width: 6px; height: 6px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 6px #22c55e;
}

/* ── CHAT WINDOW ── */
.chat-window {
  background: var(--s1);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 14px;
}
.chat-chrome {
  background: var(--s2);
  border-bottom: 1px solid var(--border);
  padding: 13px 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.chrome-dots { display: flex; gap: 8px; }
.cdot { width: 10px; height: 10px; border-radius: 50%; }
.cdot-r { background: #ff5f57; }
.cdot-y { background: #febc2e; }
.cdot-g { background: #28c840; }
.chrome-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.63rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
}

/* ── MESSAGES ── */
.chat-body { padding: 32px 28px; }

.msg-row {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 32px;
}
.msg-row.user-row { flex-direction: row-reverse; }
.msg-row:last-child { margin-bottom: 0; }

.av {
  width: 38px; height: 38px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
  line-height: 1;
}
.av-ai  { background: var(--s3); border: 1px solid var(--border); }
.av-usr { background: var(--orange); }

.msg-content { flex: 1; min-width: 0; }
.msg-sender {
  font-family: 'Fira Code', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 8px;
}
.user-row .msg-sender { text-align: right; }

.bubble {
  display: inline-block;
  padding: 16px 20px;
  border-radius: 14px;
  font-size: 0.9rem;
  font-weight: 300;
  line-height: 1.82;
  letter-spacing: 0.01em;
  max-width: 100%;
  word-break: break-word;
  white-space: pre-wrap;
}
.bubble-ai {
  background: var(--s2);
  border: 1px solid var(--border);
  color: var(--text);
  border-top-left-radius: 4px;
}
.bubble-user {
  background: var(--orange);
  color: #000;
  font-weight: 500;
  border-top-right-radius: 4px;
  font-size: 0.88rem;
}
.user-row .msg-content { display: flex; flex-direction: column; align-items: flex-end; }

/* ── INPUT ── */
[data-testid="stChatInput"] {
  background: transparent !important;
  padding: 0 !important;
  border: none !important;
}
[data-testid="stChatInput"] > div {
  background: var(--s1) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  padding: 4px 6px !important;
  transition: border-color 0.2s !important;
}
[data-testid="stChatInput"] > div:focus-within {
  border-color: var(--orange-bdr) !important;
  box-shadow: 0 0 0 3px rgba(249,115,22,0.06) !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.9rem !important;
  font-weight: 300 !important;
  line-height: 1.6 !important;
  border: none !important;
  box-shadow: none !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text3) !important; }
[data-testid="stChatInput"] button {
  background: var(--orange) !important;
  border-radius: 10px !important;
  border: none !important;
  color: #000 !important;
  transition: opacity 0.2s !important;
}
[data-testid="stChatInput"] button:hover { opacity: 0.8 !important; }

/* Streamlit buttons → chips */
.stButton > button {
  all: unset !important;
  display: block !important;
  width: 100% !important;
  background: var(--s1) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  padding: 13px 16px !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.8rem !important;
  font-weight: 400 !important;
  color: var(--text2) !important;
  line-height: 1.45 !important;
  cursor: pointer !important;
  transition: all 0.18s ease !important;
  text-align: left !important;
  white-space: normal !important;
  word-break: break-word !important;
}
.stButton > button:hover {
  background: var(--orange-dim) !important;
  border-color: var(--orange-bdr) !important;
  color: var(--text) !important;
}

/* Misc cleanup */
[data-testid="stSpinner"] > div > div { border-top-color: var(--orange) !important; }
div[data-testid="stMarkdownContainer"] > div { all: unset !important; display: block !important; }
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
Cloud & Data Engineering:
  • SnowPro Core Certification — Snowflake
  • Microsoft Certified: Azure Data Fundamentals
  • Databricks Lakehouse Fundamentals
Data Tools: dbt Learn Fundamentals, SQL (Basic) — HackerRank
AI & Programming: Generative AI Fundamentals (Databricks), 100 Days of Code (Udemy), Snowflake Masterclass (Udemy)

AWARDS & RECOGNITION — Optisol Business Solutions (2024–Present)
★ Most Valuable Person (MVP) Award | 2024–2025
★ Spot Award — Project Excellence & Leadership | January 2026 (Awarded by CTO)
★ Spot Award — RS ARP Project Go-Live | November 2025
★ Spot Award — AI Tool Innovation (NotebookLLM) | May 2025
★ Spot Award — Community Mentorship | March 2025
★ OKR Top Contributor — Q4 | October–December 2024
★ Spot Award — Client Excellence (Ontology Mapping) | December 2024
★ Spot Award — Generative AI & Automation | July 2024

DATA ENGINEERING PROJECTS (4 projects)
Project 1: Python-Based Data Migration — Google Sheets to Azure SQL Database
  Tech: Python (Pandas, gspread, pyodbc), Azure SQL Database, Azure VM, Cron Jobs, GitHub

Project 2: On-Premises to Snowflake Data Warehouse Migration
  Client: Republic Services (Waste Disposal)
  Tech: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS (EC2, Step Functions, CloudWatch)

Project 3: Enterprise Database Migration — Oracle to SQL Server
  Client: Republic Services (Waste Disposal)
  Tech: Oracle, SQL Server, Python, Autogen ETL Framework, T-SQL, ServiceNow

Project 4: API-Driven Data Migration — Podio to Azure SQL Database
  Client: Jiffy – Cultural Exchange Agencies
  Tech: Python, REST API, Pandas, Azure Data Factory, Azure SQL Database, Blob Storage, AzCopy

AI & AUTOMATION ENGINEERING PROJECTS (10 projects)
Project 5: Automated Web Data Extraction & Reporting Platform
  Tech: Python (Selenium, PyAutoGUI, smtplib), Chrome WebDriver, Email Automation

Project 6: AI-Driven Web Scraping with LangChain & Apify
  Tech: Python, LangChain, Apify Actors & API, REST APIs

Project 7: AI-Powered Automated Data Profiling Platform
  Tech: Python, Snowflake Connector, Azure OpenAI, Streamlit, Prompt Engineering

Project 8: AI-Powered Pandas Code Generation & Self-Healing Agent
  Tech: Python, Azure OpenAI, Pandas, Prompt Engineering
  Self-healing: detects runtime errors and regenerates corrected code automatically.

Project 9: Ontology Kit — Data Mapping Agent
  Tech: Python, Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
  Impact: Reduced manual data mapping effort by 40–50%.

Project 10: AI-Powered Document Processing & Structured Data Extraction
  Client: Republic Services Hackathon
  Tech: Python, AWS Textract, Amazon Bedrock, EC2, S3, Flask

Project 11: Internationalization HTML Validation Tool
  Tech: Python, HTML Parsing, i18n, JSON, CLI Automation

Project 12: Automated Internationalization Workflow
  Tech: Python, i18n Automation Scripts, JSON, Batch Processing

Project 13: Credit Risk Reporting & JSON Data Intelligence Platform
  Client: Atradius — Trade Credit Insurance
  Tech: Python, Google Gemini 2.5 Pro, asyncio, Plotly, JSON
  Built async rate limiter (token bucket); mapped 40+ credit risk blocks.

Project 14: Knowledge Graph Builder (KGB) with RAG
  Client: Internal Platform | Optisol Business Solutions
  Tech: Python, Streamlit, LangChain, Azure OpenAI, Neo4j, PyVis, PyPDF2, asyncio
  Transforms unstructured documents into interactive knowledge graphs with RAG.
"""

SYSTEM_PROMPT = f"""You are a professional AI Assistant for Ashik Roshan I's career portfolio.

Answer questions about Ashik's skills, experience, projects, education, certifications, and achievements
in a polished, articulate, and confident manner.

Use ONLY the resume information provided. If something is not covered, say so gracefully.

{RESUME_CONTEXT}

Response Guidelines:
- Write in fluent, professional English.
- Refer to Ashik in the third person (e.g., "Ashik brings expertise in…").
- Use clear paragraphs. Use bullet points only when listing multiple distinct items.
- Be concise yet comprehensive. No filler words.
- Highlight business impact and technologies when discussing projects.
- Maintain a warm, confident, and persuasive tone.
"""

# ── Load API Key ──────────────────────────────────────────────────────────────
try:
    api_key = st.secrets["credentials"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("API key not configured. Please add GEMINI_API_KEY to Streamlit secrets.")
    st.stop()

# ── Session State ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending" not in st.session_state:
    st.session_state.pending = None

# ═══════════════════════════════════════════════════════════════════════════════
# RENDER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

# ── TOP BAR ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-brand">
    <div class="brand-dot"></div>
    <span class="brand-text">AI Portfolio Assistant</span>
  </div>
  <div class="nav-links">
    <a class="nav-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub</a>
    <a class="nav-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn</a>
    <a class="nav-link" href="https://arshowcase.streamlit.app" target="_blank">Portfolio</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── IDENTITY ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="identity">
  <div class="id-eyebrow">Data &amp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions &nbsp;·&nbsp; L2</div>
  <div class="id-name">Ashik <em>Roshan</em> I.</div>
  <div class="id-bio">
    Building intelligent data systems at the intersection of
    <strong>Cloud Engineering</strong>, <strong>Generative AI</strong>, and
    <strong>Automation</strong> — turning complex data challenges into
    measurable business outcomes.
  </div>
</div>
""", unsafe_allow_html=True)

# ── RULE ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

# ── SUGGESTION CHIPS ──────────────────────────────────────────────────────────
st.markdown('<div class="chips-header">Ask about me</div>', unsafe_allow_html=True)

CHIPS = [
    ("🛠️", "What are Ashik's core technical skills and technology stack?"),
    ("💼", "Walk me through Ashik's professional work experience"),
    ("🤖", "Tell me about Ashik's AI and Generative AI projects"),
    ("🏆", "What awards and recognition has Ashik received?"),
]

cols = st.columns(4, gap="small")
for i, (col, (icon, question)) in enumerate(zip(cols, CHIPS)):
    with col:
        # Short label for button display
        labels = [
            "Core technical skills",
            "Work experience",
            "AI & GenAI projects",
            "Awards & recognition",
        ]
        if st.button(f"{icon}  {labels[i]}", key=f"chip_{i}"):
            st.session_state.pending = question

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ── CONVERSATION HEADER ───────────────────────────────────────────────────────
st.markdown("""
<div class="conv-row">
  <span class="conv-label">Conversation</span>
  <div class="online-pill">
    <div class="online-dot"></div>
    <span>AI Assistant &nbsp;·&nbsp; Online</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CHAT WINDOW ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-window">
  <div class="chat-chrome">
    <div class="chrome-dots">
      <div class="cdot cdot-r"></div>
      <div class="cdot cdot-y"></div>
      <div class="cdot cdot-g"></div>
    </div>
    <span class="chrome-label">portfolio.assistant — active session</span>
    <span style="width:60px"></span>
  </div>
  <div class="chat-body">
""", unsafe_allow_html=True)

# ── Welcome message ───────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="msg-row">
      <div class="av av-ai">🤖</div>
      <div class="msg-content">
        <div class="msg-sender">Assistant</div>
        <div class="bubble bubble-ai">
          Good day. I am Ashik Roshan's AI Assistant — your dedicated resource for exploring his professional portfolio.<br><br>
          I can provide detailed insights on his <strong style="color:#eeebe6">technical expertise</strong>,
          <strong style="color:#eeebe6">project portfolio</strong>,
          <strong style="color:#eeebe6">career milestones</strong>, and
          <strong style="color:#eeebe6">achievements</strong>.<br><br>
          Select a question above or type your own below to begin.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Render conversation history ───────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        safe = msg["content"].replace("<", "&lt;").replace(">", "&gt;")
        st.markdown(f"""
        <div class="msg-row user-row">
          <div class="av av-usr">🧑</div>
          <div class="msg-content">
            <div class="msg-sender">You</div>
            <div class="bubble bubble-user">{safe}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        import re
        content = msg["content"]
        # Convert **bold** to <strong>
        content = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color:#f0ede8;font-weight:600">\1</strong>', content)
        # Convert bullet lines
        content = re.sub(r'^\s*[\•\-\*]\s+', '• ', content, flags=re.MULTILINE)
        content = content.replace("\n\n", "<br><br>").replace("\n", "<br>")
        st.markdown(f"""
        <div class="msg-row">
          <div class="av av-ai">🤖</div>
          <div class="msg-content">
            <div class="msg-sender">Assistant</div>
            <div class="bubble bubble-ai">{content}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ── Chat Input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Type your question about Ashik's skills, projects, or experience…")

# Chip click
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

st.markdown('</div>', unsafe_allow_html=True)  # close app-shell
