import streamlit as st
import google.generativeai as genai

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan – AI Assistant",
    page_icon="🤖",
    layout="centered",
)

# ── Custom CSS (dark-blue + orange theme) ────────────────────────────────────
st.markdown("""
<style>
/* Background */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #0d1b2a;
    color: #f0f4f8;
}
[data-testid="stHeader"] { background-color: #0d1b2a; }
[data-testid="stSidebar"] { background-color: #112233; border-right: 1px solid #1e3a5f; }

/* Input box */
[data-testid="stChatInput"] textarea {
    background-color: #1a2e45 !important;
    color: #f0f4f8 !important;
    border: 1px solid #ff6b35 !important;
    border-radius: 12px !important;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    border-radius: 14px;
    padding: 4px 8px;
    margin-bottom: 6px;
}
/* User bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: #1e3a5f;
    border-left: 4px solid #ff6b35;
}
/* Assistant bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background-color: #112233;
    border-left: 4px solid #00a8e8;
}

/* Headings & accent text */
h1, h2, h3 { color: #ff6b35 !important; }
a { color: #ff9a5c !important; }

/* Buttons */
.stButton > button {
    background-color: #ff6b35;
    color: #0d1b2a;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    width: 100%;
    text-align: left;
    margin-bottom: 4px;
}
.stButton > button:hover {
    background-color: #ff9a5c;
    color: #0d1b2a;
}

/* Spinner */
.stSpinner > div { border-top-color: #ff6b35 !important; }

/* Divider */
hr { border-color: #1e3a5f; }
</style>
""", unsafe_allow_html=True)

# ── Resume knowledge base ─────────────────────────────────────────────────────
RESUME_CONTEXT = """
RESUME OF ASHIK ROSHAN I
========================
Role: Data & AI Engineer – L2
Email: ashikroshan261@gmail.com
GitHub: https://github.com/AshikRoshan-github
LinkedIn: https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium: https://medium.com/@ashikroshan261
Website: https://arshowcase.streamlit.app

--- TECHNICAL SKILLS ---
Languages: Python, SQL, JavaScript, HTML, CSS

Cloud – Azure: Blob Storage, Data Lake, SQL Database, Azure OpenAI, Databricks, ADF, Azure VM,
  Azure Document Intelligence, Function App
Cloud – AWS: S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock

Data Engineering: PySpark, DBT, Informatica, Snowflake, Pandas, ADF
Databases: SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics: Power BI, ThoughtSpot, Plotly, Streamlit
AI & GenAI: Azure OpenAI, Amazon Bedrock, Gemini, LangChain, Neo4j, RAG, Prompt Engineering,
  Azure Document Intelligence
Automation & Web: Selenium, Web Scraping, Web Crawling, FastAPI, PyAutoGUI, Apify, Flask
DevOps & Tools: GitHub, Azure DevOps, CI/CD, PuTTY, ServiceNow, Rally, SharePoint
Libraries & Frameworks: asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict,
  smtplib, oracledb, pywin, pytesseract, dotenv

--- PROFESSIONAL EXPERIENCE ---
1. Data Engineer – L2 | Optisol Business Solutions | April 2025 – Present
2. Data Engineer – L1 | Optisol Business Solutions | August 2024 – March 2025
3. Data Engineer Intern – L0 | Optisol Business Solutions | March 2024 – July 2024
4. Trainee – Software Engineer | Blue Cloud | June 2023 – March 2024

--- EDUCATION ---
Bachelor of Engineering in Computer Science (Grade: A+)
KLN College of Engineering | 2019 – 2023

--- CERTIFICATIONS ---
Cloud & Data Engineering:
  - SnowPro Core Certification – Snowflake
  - Microsoft Certified: Azure Data Fundamentals – Microsoft
  - Databricks Lakehouse Fundamentals – Databricks

Data Tools & Engineering:
  - dbt Learn Fundamentals – dbt Labs
  - SQL (Basic) Certificate – HackerRank

AI & Programming:
  - Academy Accreditation: Generative AI Fundamentals – Databricks
  - 100 Days of Code: Python Pro Bootcamp – Udemy
  - Snowflake Masterclass – Udemy

--- AWARDS & RECOGNITION (Optisol Business Solutions 2024–Present) ---
• Most Valuable Person (MVP) Award | 2024–2025
  Highest organizational honor for consistent performance excellence and leadership.
• Spot Award – Project Excellence & Leadership | Jan 2026
  Awarded by the CTO for mature professional handling of project success.
• Spot Award – RS ARP Project Go-Live | Nov 2025
  Recognized for exceptional contribution to the "Beatty Go-Live" rollout.
• Spot Award – AI Tool Innovation (NotebookLLM) | May 2025
  Drove team adoption of NotebookLLM to enhance project efficiency.
• Spot Award – Community Mentorship | Mar 2025
  Delivered technical sessions for college students on interview prep and emerging tech.
• OKR Top Contributor (Q4) | Oct–Dec 2024
• Spot Award – Client Excellence (Ontology Mapping) | Dec 2024
• Spot Award – Gen AI & Automation | July 2024

--- DATA ENGINEERING PROJECTS ---
#1. Python-Based Data Migration: Google Sheets to Azure SQL Database
  Tech: Python (Pandas, gspread, pyodbc), SQL, Azure SQL Database, Azure VM, Cron Jobs, GitHub

#2. On-Premises to Snowflake Data Warehouse Migration
  Client: Republic Services (Waste Disposal)
  Tech: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS (EC2, Step Functions, CloudWatch)

#3. Enterprise Database Migration: Oracle to SQL Server (On-Premises)
  Client: Republic Services (Waste Disposal)
  Tech: Oracle, SQL Server, Python, Autogen ETL Framework, T-SQL, ServiceNow

#4. API-Driven Data Migration: Podio to Azure SQL Database
  Client: Jiffy – Cultural Exchange Agencies
  Tech: Python, REST API, Pandas, Azure Data Factory, Azure SQL Database, Blob Storage, AzCopy

--- AI & AUTOMATION ENGINEERING PROJECTS ---
#1. Automated Web Data Extraction & Reporting Platform
  Tech: Python (Selenium, PyAutoGUI, smtplib), Chrome WebDriver, Email Automation

#2. AI-Driven Web Scraping with LangChain & Apify Integration
  Tech: Python, LangChain, Apify (Actors & API), REST APIs

#3. AI-Powered Automated Data Profiling Platform
  Tech: Python (pyodbc), Snowflake Connector, Azure OpenAI, Streamlit, Prompt Engineering

#4. AI-Powered Pandas Code Generation & Self-Healing Data Transformation Agent
  Tech: Python, Azure OpenAI, Pandas, Prompt Engineering

#5. Ontology Kit – Data Mapping Agent
  Tech: Python, Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
  Reduced manual mapping effort by 40–50%.

#6. AI-Powered Document Processing & Structured Data Extraction Tool
  Client: Republic Services Hackathon
  Tech: Python, AWS Textract, Amazon Bedrock, EC2, S3, Flask

#7. Internationalization HTML Validation & Automation Tool
  Tech: Python, HTML Parsing, i18n, JSON, CLI Automation

#8. Automated Internationalization Workflow
  Tech: Python, i18n Automation Scripts, JSON, Batch Processing

#9. Credit Risk Reporting & JSON Data Intelligence Platform
  Client: Atradius – Trade Credit Insurance
  Tech: Python, Google Gemini 2.5 Pro, asyncio, Plotly, JSON
  Built async rate limiter (token bucket) and section-based LLM prompting for 40+ credit blocks.

#10. Knowledge Graph Builder (KGB) with RAG
  Tech: Python, Streamlit, LangChain, Azure OpenAI, Neo4j, PyVis, PyPDF2, asyncio
  Transforms unstructured documents into interactive, queryable knowledge graphs with RAG.
"""

SYSTEM_PROMPT = f"""You are an intelligent AI assistant for Ashik Roshan I's professional portfolio.
Your job is to answer questions about Ashik's skills, experience, projects, education, certifications,
and achievements in a friendly, professional, and concise manner.

Use ONLY the resume information below. If a question is not covered, say so politely.

{RESUME_CONTEXT}

Guidelines:
- Be conversational and enthusiastic about Ashik's accomplishments.
- Use bullet points for lists when appropriate.
- Highlight specific technologies, clients, and impact metrics when relevant.
- Keep responses focused and well-structured.
"""

# ── Load API key from Streamlit secrets ───────────────────────────────────────
try:
    api_key = st.secrets["credentials"]["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠️ API key not found. Please configure `GEMINI_API_KEY` in your Streamlit secrets.")
    st.stop()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 10px 0 6px 0;'>
        <div style='font-size:3rem;'>👨‍💻</div>
        <h2 style='color:#ff6b35; margin:6px 0 2px 0;'>Ashik Roshan I</h2>
        <p style='color:#a0b4c8; font-size:0.85rem; margin:0;'>Data & AI Engineer – L2</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='text-align:center; line-height:2;'>
        <a href='https://github.com/AshikRoshan-github' target='_blank'>🐙 GitHub</a>&nbsp;&nbsp;
        <a href='https://www.linkedin.com/in/ashik-roshan-i-073897249' target='_blank'>💼 LinkedIn</a>&nbsp;&nbsp;
        <a href='https://arshowcase.streamlit.app' target='_blank'>🌐 Website</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Quick Questions")

    suggestions = [
        "What are Ashik's top skills?",
        "Tell me about his AI projects",
        "What certifications does he hold?",
        "What awards has he won?",
        "Describe his work experience",
        "What is the Knowledge Graph project?",
        "Tell me about his education",
    ]
    for s in suggestions:
        if st.button(s, key=s):
            st.session_state.pending_question = s

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ── Main header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 24px 0 8px 0;'>
  <h1 style='font-size:2.1rem; margin-bottom:6px;'>🤖 AI Assistant</h1>
  <p style='color:#a0b4c8; font-size:1rem; margin:0;'>
    Ask me anything about <span style='color:#ff6b35; font-weight:700;'>Ashik Roshan's</span> experience, skills & projects
  </p>
</div>
<hr style='border-color:#1e3a5f; margin: 10px 0 20px 0;'>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Welcome message (first load) ──────────────────────────────────────────────
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("""
👋 Hi there! I'm Ashik's **AI Assistant**.

I can help you learn about:
- 🛠️ **Skills** — Python, Cloud (Azure/AWS), Data Engineering, AI/GenAI
- 💼 **Work Experience** — roles at Optisol Business Solutions & Blue Cloud
- 🚀 **Projects** — 14 data & AI engineering projects
- 🏆 **Awards** — MVP, multiple Spot Awards
- 📜 **Certifications** — Snowflake, Azure, Databricks & more

What would you like to know?
        """)

# ── Render chat history ───────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Handle sidebar suggestion or chat input ───────────────────────────────────
user_input = st.chat_input("Ask about skills, projects, experience…")
if st.session_state.pending_question:
    user_input = st.session_state.pending_question
    st.session_state.pending_question = None

# ── Generate response ─────────────────────────────────────────────────────────
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
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
                answer = f"❌ Something went wrong. Please try again.\n\n`{e}`"

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
