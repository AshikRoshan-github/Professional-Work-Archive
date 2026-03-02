import streamlit as st
import google.generativeai as genai
import re

st.set_page_config(
    page_title="Ashik Roshan I — AI Assistant",
    page_icon="🔶",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:          #080808;
  --s1:          #0f0f0f;
  --s2:          #141414;
  --s3:          #1c1c1c;
  --border:      #252525;
  --orange:      #f97316;
  --orange-soft: rgba(249,115,22,0.10);
  --orange-bdr:  rgba(249,115,22,0.28);
  --orange-glow: rgba(249,115,22,0.06);
  --text:        #edebe6;
  --text2:       #787470;
  --text3:       #3e3c3a;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── Global ── */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
section.main {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'Sora', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
[data-testid="stHeader"]         { display: none !important; }
[data-testid="stSidebar"]        { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
footer                           { display: none !important; }
#MainMenu                        { display: none !important; }

/* ── Show + style the collapse toggle ── */
[data-testid="collapsedControl"] {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  background: #111 !important;
  border: 1px solid #2a2a2a !important;
  border-radius: 0 8px 8px 0 !important;
  min-width: 20px !important;
  width: 20px !important;
  height: 48px !important;
  align-items: center !important;
  justify-content: center !important;
  top: 50% !important;
  transform: translateY(-50%) !important;
  box-shadow: 2px 0 12px rgba(0,0,0,0.6) !important;
  z-index: 99999 !important;
  position: fixed !important;
  transition: background 0.2s !important;
  pointer-events: all !important;
}
[data-testid="collapsedControl"]:hover {
  background: var(--orange) !important;
  border-color: var(--orange) !important;
}
[data-testid="collapsedControl"] svg {
  fill: #888 !important;
  width: 12px !important;
  height: 12px !important;
}
[data-testid="collapsedControl"]:hover svg {
  fill: #000 !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: #0a0a0a !important;
  border-right: 1px solid #1e1e1e !important;
  min-width: 300px !important;
  max-width: 300px !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding: 0 !important;
}
/* Remove default streamlit padding inside sidebar */
[data-testid="stSidebar"] .stButton {
  padding: 0 !important;
}

/* ── MAIN AREA ── */
[data-testid="stMainBlockContainer"] { padding: 0 !important; }
.block-container {
  max-width: 720px !important;
  padding: 0 36px 60px !important;
  margin: 0 auto !important;
}

/* ── IDENTITY ── */
.identity { margin-bottom: 48px; padding-top: 52px; }
.eyebrow {
  font-family: 'Fira Code', monospace;
  font-size: 0.64rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 14px;
}
.name {
  font-family: 'Instrument Serif', serif;
  font-size: clamp(2.8rem, 5vw, 4.2rem);
  font-weight: 400;
  line-height: 1.02;
  letter-spacing: -0.02em;
  color: #fff;
  margin-bottom: 16px;
}
.name em { font-style: italic; color: var(--orange); }
.bio {
  font-size: 0.9rem;
  font-weight: 300;
  color: var(--text2);
  line-height: 1.82;
  max-width: 500px;
}
.bio strong { color: var(--text); font-weight: 500; }

/* ── RULE ── */
.rule {
  height: 1px;
  background: linear-gradient(90deg, var(--orange-bdr), var(--border) 55%, transparent);
  margin-bottom: 40px;
}

/* ──────────────────────────────────────────
   SIDEBAR COMPONENTS
────────────────────────────────────────── */

/* Profile header */
.sb-header {
  background: #0e0e0e;
  border-bottom: 1px solid #1e1e1e;
  padding: 28px 22px 24px;
  position: relative;
}
.sb-header::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--orange), transparent);
}
.sb-header-top {
  display: flex;
  align-items: center;
  gap: 13px;
  margin-bottom: 16px;
}
.sb-avatar {
  width: 46px; height: 46px;
  background: linear-gradient(135deg, var(--orange) 0%, #c25510 100%);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.35rem;
  flex-shrink: 0;
  box-shadow: 0 0 20px rgba(249,115,22,0.25);
}
.sb-id { flex: 1; min-width: 0; }
.sb-name {
  font-family: 'Sora', sans-serif;
  font-size: 0.94rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.01em;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.sb-role {
  font-family: 'Fira Code', monospace;
  font-size: 0.57rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--orange);
  margin-top: 3px;
}
.sb-company {
  font-family: 'Fira Code', monospace;
  font-size: 0.55rem;
  letter-spacing: 0.07em;
  color: #3a3a3a;
  margin-top: 2px;
}

/* Stats row */
.sb-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 18px;
}
.sb-stat {
  background: #111;
  border: 1px solid #1e1e1e;
  border-radius: 8px;
  padding: 10px 12px;
  text-align: center;
}
.sb-stat-num {
  font-family: 'Instrument Serif', serif;
  font-size: 1.4rem;
  color: var(--orange);
  line-height: 1;
  margin-bottom: 3px;
}
.sb-stat-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.53rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #3a3a3a;
}

/* Links */
.sb-links {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}
.sb-link {
  font-family: 'Fira Code', monospace;
  font-size: 0.56rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #555;
  text-decoration: none;
  border: 1px solid #222;
  border-radius: 5px;
  padding: 4px 10px;
  transition: all 0.18s;
  background: #0d0d0d;
}
.sb-link:hover {
  color: var(--orange);
  border-color: var(--orange-bdr);
  background: var(--orange-glow);
}

/* Sidebar body */
.sb-body {
  padding: 20px 18px 24px;
}

/* Divider inside sidebar */
.sb-divider {
  height: 1px;
  background: #1a1a1a;
  margin: 0 0 20px;
}

/* Info tags */
.sb-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 24px;
}
.sb-tag {
  font-family: 'Fira Code', monospace;
  font-size: 0.56rem;
  letter-spacing: 0.06em;
  color: #555;
  border: 1px solid #1e1e1e;
  border-radius: 4px;
  padding: 4px 8px;
  background: #0d0d0d;
}

/* Reset button */
[data-testid="stSidebar"] .stButton > button {
  all: unset !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  width: 100% !important;
  background: transparent !important;
  border: 1px solid #222 !important;
  border-radius: 10px !important;
  padding: 12px 16px !important;
  font-family: 'Sora', sans-serif !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  color: #444 !important;
  letter-spacing: 0.02em !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  box-sizing: border-box !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  background: var(--orange) !important;
  border-color: var(--orange) !important;
  color: #000 !important;
  box-shadow: 0 0 20px rgba(249,115,22,0.25) !important;
}

/* ── CONV HEADER ── */
.conv-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.conv-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text3);
}
.online-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.58rem;
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
.cd-r { background: #ff5f57; }
.cd-y { background: #febc2e; }
.cd-g { background: #28c840; }
.chrome-text {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text3);
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
  font-size: 0.58rem;
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
  box-shadow: 0 0 0 3px var(--orange-glow) !important;
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
AI & Programming: Generative AI Fundamentals (Databricks), 100 Days of Code (Udemy),
  Snowflake Masterclass (Udemy)

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
P6: AI-Driven Web Scraping — LangChain & Apify
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


# ── JS: Force sidebar toggle always visible (MutationObserver) ───────────────
from streamlit.components.v1 import html as st_html
st_html("""
<script>
(function() {
  const STYLE_ID = 'ar-toggle-style';

  function injectStyle() {
    if (document.getElementById(STYLE_ID)) return;
    const s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = `
      [data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: all !important;
        z-index: 99999 !important;
        position: fixed !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        background: #111 !important;
        border: 1px solid #2a2a2a !important;
        border-radius: 0 8px 8px 0 !important;
        width: 22px !important;
        height: 52px !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 2px 0 16px rgba(0,0,0,0.7) !important;
        transition: background 0.2s, border-color 0.2s !important;
        cursor: pointer !important;
      }
      [data-testid="collapsedControl"]:hover {
        background: #f97316 !important;
        border-color: #f97316 !important;
      }
      [data-testid="collapsedControl"] svg {
        fill: #888 !important;
        width: 12px !important;
        height: 12px !important;
        flex-shrink: 0 !important;
      }
      [data-testid="collapsedControl"]:hover svg {
        fill: #000 !important;
      }
    `;
    document.head.appendChild(s);
  }

  function forceVisible() {
    const btn = document.querySelector('[data-testid="collapsedControl"]');
    if (btn) {
      btn.style.setProperty('display', 'flex', 'important');
      btn.style.setProperty('visibility', 'visible', 'important');
      btn.style.setProperty('opacity', '1', 'important');
      btn.style.setProperty('pointer-events', 'all', 'important');
      btn.style.setProperty('z-index', '99999', 'important');
    }
    injectStyle();
  }

  // Run immediately
  forceVisible();

  // Run after DOM ready
  document.addEventListener('DOMContentLoaded', forceVisible);

  // MutationObserver: watch entire body for any DOM changes (Streamlit re-renders)
  const observer = new MutationObserver(function(mutations) {
    forceVisible();
  });

  function startObserver() {
    const target = document.body;
    if (target) {
      observer.observe(target, { childList: true, subtree: true });
    } else {
      setTimeout(startObserver, 100);
    }
  }
  startObserver();

  // Also poll every 500ms as safety net
  setInterval(forceVisible, 500);
})();
</script>
""", height=0)

# ── Session State ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    # Profile header
    st.markdown("""
    <div class="sb-header">
      <div class="sb-header-top">
        <div class="sb-avatar">🤖</div>
        <div class="sb-id">
          <div class="sb-name">Ashik Roshan I.</div>
          <div class="sb-role">Data &amp; AI Engineer — L2</div>
          <div class="sb-company">Optisol Business Solutions</div>
        </div>
      </div>

      <div class="sb-stats">
        <div class="sb-stat">
          <div class="sb-stat-num">14</div>
          <div class="sb-stat-label">Projects</div>
        </div>
        <div class="sb-stat">
          <div class="sb-stat-num">8</div>
          <div class="sb-stat-label">Awards</div>
        </div>
        <div class="sb-stat">
          <div class="sb-stat-num">2+</div>
          <div class="sb-stat-label">Years Exp.</div>
        </div>
        <div class="sb-stat">
          <div class="sb-stat-num">9</div>
          <div class="sb-stat-label">Certifications</div>
        </div>
      </div>

      <div class="sb-links">
        <a class="sb-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub ↗</a>
        <a class="sb-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn ↗</a>
        <a class="sb-link" href="https://medium.com/@ashikroshan261" target="_blank">Medium ↗</a>
        <a class="sb-link" href="https://arshowcase.streamlit.app" target="_blank">Portfolio ↗</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Body — tags + reset
    st.markdown("""
    <div class="sb-body">
      <div class="sb-divider"></div>
      <div class="sb-tags">
        <span class="sb-tag">Python</span>
        <span class="sb-tag">Azure</span>
        <span class="sb-tag">AWS</span>
        <span class="sb-tag">Snowflake</span>
        <span class="sb-tag">GenAI</span>
        <span class="sb-tag">LangChain</span>
        <span class="sb-tag">PySpark</span>
        <span class="sb-tag">dbt</span>
        <span class="sb-tag">Neo4j</span>
        <span class="sb-tag">RAG</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Reset button — centred, styled
    if st.button("↺  Reset Conversation", key="reset"):
        st.session_state.messages = []
        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

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

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

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

if not st.session_state.messages:
    st.markdown("""
    <div class="mrow">
      <div class="av av-ai">🤖</div>
      <div class="mcontent">
        <div class="msender">Assistant</div>
        <div class="bubble bai">
          Good day. I am Ashik Roshan's dedicated AI Assistant — your comprehensive resource
          for exploring his professional portfolio.<br><br>
          I can walk you through his <strong style="color:#edebe6">technical expertise</strong>,
          <strong style="color:#edebe6">14 delivered projects</strong>,
          <strong style="color:#edebe6">career milestones</strong>,
          <strong style="color:#edebe6">certifications</strong>, and
          <strong style="color:#edebe6">8 professional awards</strong>.<br><br>
          Type your question below to get started.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

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
