import streamlit as st
import os

# ── google-genai import ────────────────────────────────────────────────────
try:
    from google import genai as google_genai
    from google.genai import types as google_types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

st.set_page_config(
    page_title="Ashik Roshan I — Data & AI Engineer",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  FULL SYSTEM PROMPT
# ══════════════════════════════════════════════════════════════════════════════
ASHIK_SYSTEM_PROMPT = """
You are Ashik Roshan I's personal AI portfolio assistant. You have complete knowledge of Ashik's professional background, projects, skills, awards, education, and contact info. Answer all questions about Ashik in a confident, professional, and friendly tone.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — PERSONAL INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Full Name      : Ashik Roshan I
Current Role   : Data Engineer & AI Engineer — Level 2 (L2)
Company        : Optisol Business Solutions
Location       : Madurai, TamilNadu, India
Email          : ashikroshan261@gmail.com
GitHub         : https://github.com/AshikRoshan-github
LinkedIn       : https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium Blog    : https://medium.com/@ashikroshan261
Total Experience: 2+ years (since Jun 2023)
Summary        : Results-driven Data & AI Engineer delivering scalable ETL/ELT pipelines, enterprise cloud migrations, and production-grade AI automation. Specialises in Snowflake, Azure, AWS, LangChain, and GenAI agent design. MVP award winner and 7x Spot Award recipient.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — PROFESSIONAL EXPERIENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Role 1: Data Engineer — L2 | Optisol Business Solutions | Apr 2025 – Present
  - Led cross-functional teams on enterprise cloud migrations
  - Architected Snowflake Data Warehouse with dbt ELT pipelines
  - Built production GenAI agents using Azure OpenAI and LangChain
  - Designed knowledge graphs with Neo4j and RAG query layers
  - Mentored junior engineers; conducted college tech sessions
  - CTO-recognized Spot Award for project excellence

Role 2: Data Engineer — L1 | Optisol Business Solutions | Aug 2024 – Mar 2025
  - Python-based ETL pipelines for Azure SQL
  - AI-powered data profiling platforms with Azure OpenAI
  - Automated web scraping with LangChain and Apify
  - Ontology Mapping tool — 40-50% manual effort reduction
  - Self-healing AI Pandas code generation agent

Role 3: Data Engineer Intern — L0 | Optisol Business Solutions | Mar 2024 – Jul 2024
  - Web data extraction automation (Selenium, PyAutoGUI)
  - AI scraping tools with LangChain and Apify cloud Actors
  - i18n HTML validation tools

Role 4: Trainee — Software Engineer | Blue Cloud | Jun 2023 – Mar 2024
  - Full-stack web applications
  - Automation and integration projects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — TECHNICAL SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Languages          : Python, SQL, JavaScript, HTML, CSS
Cloud — Azure      : Blob Storage, Data Lake, SQL Database, Azure OpenAI, Databricks, ADF, Azure VM
Cloud — AWS        : S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock
Data Engineering   : PySpark, DBT, Informatica, Snowflake, Pandas, ADF
Databases          : SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics     : Power BI, ThoughtSpot, Plotly, Streamlit
AI & GenAI         : Azure OpenAI, Amazon Bedrock, Gemini 2.5 Pro, LangChain, Neo4j, RAG, Prompt Engineering, Azure Doc Intelligence
Automation & Web   : Selenium, Web Scraping, FastAPI, PyAutoGUI, Apify, Flask
DevOps & Tools     : GitHub, Azure DevOps, CI/CD, PuTTY, ServiceNow, Rally
Python Libraries   : asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict, smtplib

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — DATA ENGINEERING PROJECTS (4 Projects)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DE-1: Python-Based Data Migration — Google Sheets to Azure SQL
  Client: Internal | Optisol | Tech: Python, Pandas, gspread, pyodbc, Azure SQL, Azure VM, Cron Jobs
  Full ETL pipeline: Google Sheets extraction, incremental/full load logic, Pandas transform, Cron automation.

DE-2: On-Premises to Snowflake Data Warehouse Migration
  Client: Republic Services | Optisol | Tech: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS Step Functions, CloudWatch
  Migrated 6 on-prem sources to Snowflake DWH. dbt ELT via CI/CD, AWS Step Functions orchestration, CloudWatch monitoring.

DE-3: Enterprise DB Migration — Oracle to SQL Server
  Client: Republic Services | Optisol | Tech: Oracle, SQL Server, Autogen ETL, T-SQL, ServiceNow
  Autogen ETL framework for 5-layer pipeline: RAW > Staging > Mirror > Test > Production. ServiceNow change management.

DE-4: API-Driven Migration — Podio to Azure SQL
  Client: Jiffy Cultural Exchange | Optisol | Tech: Python, REST API, Pandas, ADF, Azure SQL, Azure Blob, AzCopy
  Podio REST API extraction, ADF pipeline, pyodbc fast_executemany bulk load, AzCopy document migration.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — AI & AUTOMATION PROJECTS (10 Projects)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI-1: Automated Web Data Extraction & Reporting Platform
  Client: IBEAM | Optisol | Tech: Selenium, PyAutoGUI, smtplib, Azure DevOps
  Fully unattended browser automation: login, extract, process, report, email via SMTP.

AI-2: AI-Driven Web Scraping — LangChain & Apify
  Client: IBEAM | Optisol | Tech: Python, LangChain, Apify, REST APIs
  Apify cloud Actors + LangChain for AI-powered scalable crawling to LLM-ready documents.

AI-3: AI-Powered Automated Data Profiling Platform
  Client: IBEAM | Optisol | Tech: Azure OpenAI, Snowflake, Streamlit, Prompt Engineering
  Multi-source profiling: anomaly detection, data quality insights, interactive Streamlit dashboards.

AI-4: AI Pandas Agent — Self-Healing Code Generation
  Client: IBEAM | Optisol | Tech: Azure OpenAI, Pandas, Python
  NL to Pandas code with self-healing loop: runtime error -> LLM context -> auto-regenerated corrected code.

AI-5: Ontology Kit — Data Mapping Agent
  Client: IBEAM | Optisol | Tech: Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
  AI ontology mapping reducing manual effort 40-50%. Client praised during on-site visit.

AI-6: AI Document Processing & Structured Data Extraction
  Client: RS Hackathon | Optisol | Tech: AWS Textract, Amazon Bedrock, EC2, S3, Flask
  Scanned PDF/image to structured JSON: Textract OCR, Bedrock semantic structuring, Flask REST API.

AI-7: Internationalization HTML Validation Tool
  Client: Optisol Internal | Tech: Python, HTML Parsing, i18n, JSON
  Detects hard-coded strings, missing translation keys, generates JSON audit reports.

AI-8: Automated Internationalization Workflow
  Client: IBEAM | Optisol | Tech: Python, i18n, Batch Processing, CI/CD
  Manages i18n locale files, validates keys, syncs translations, CI/CD integrated.

AI-9: Credit Risk Reporting & JSON Intelligence Platform
  Client: Atradius | Optisol | Tech: Gemini 2.5 Pro, asyncio, Plotly, JSON
  40+ credit risk blocks, token-bucket async rate limiter, asyncio.gather parallel LLM dispatch, Plotly viz.

AI-10: Knowledge Graph Builder (KGB) with RAG
  Client: Internal | Optisol | Tech: LangChain, Azure OpenAI, Neo4j, PyVis, Streamlit, asyncio
  PDF/DOCX/JSON/XML/SQL to knowledge graph: Neo4j persistence, RAG query layer, physics-simulated PyVis viz.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — AWARDS (8 Awards)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. MVP Award 2024-25 — Highest org honor at Optisol. Performance excellence & leadership.
2. Spot Award — Project Excellence & Leadership — Jan 2026 — CTO recognition.
3. Spot Award — RS ARP Project Go-Live — Nov 2025 — Beatty Go-Live & Delta Load delivery.
4. Spot Award — AI Tool Innovation (NotebookLLM) — May 2025 — Team adoption driver.
5. Spot Award — Community Mentorship — Mar 2025 — College student tech sessions.
6. OKR Top Contributor Q4 — Oct-Dec 2024 — Company-wide OKR achievement.
7. Spot Award — Client Excellence (Ontology Mapping) — Dec 2024 — On-site client praise.
8. Spot Award — Gen AI & Automation — Jul 2024 — GenAI inventory automation + DBT SME.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — CERTIFICATIONS (8)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SnowPro Core Certification — Snowflake
2. Azure Data Fundamentals DP-900 — Microsoft
3. Databricks Lakehouse Fundamentals — Databricks
4. Generative AI Fundamentals — Databricks
5. dbt Learn Fundamentals — dbt Labs
6. SQL Basic Certificate — HackerRank
7. 100 Days of Code Python Pro Bootcamp — Udemy
8. Snowflake Masterclass — Udemy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — EDUCATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Degree: Bachelor of Engineering in Computer Science
College: KLN College of Engineering
Duration: 2019-2023 | Grade: A+

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9 — KEY STATS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 2+ years experience | 14+ projects | 7 Spot Awards | 1 MVP Award | 8 certifications
- Clients: Republic Services, Atradius, Jiffy Cultural Exchange, IBEAM
- Youngest MVP at Optisol

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10 — CONTACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Email: ashikroshan261@gmail.com
GitHub: https://github.com/AshikRoshan-github
LinkedIn: https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium: https://medium.com/@ashikroshan261

INSTRUCTIONS: Answer accurately from the above. Be enthusiastic. Give full project details when asked. Never invent data. If unknown, suggest contacting via email.
"""

# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════
SKILLS = [
    ("Languages",        ["Python", "SQL", "JavaScript", "HTML", "CSS"]),
    ("Cloud — Azure",    ["Blob Storage", "Data Lake", "SQL Database", "Azure OpenAI", "Databricks", "ADF", "Azure VM"]),
    ("Cloud — AWS",      ["S3", "Lambda", "Glue", "Step Functions", "EC2", "CloudWatch", "Textract", "Bedrock"]),
    ("Data Engineering", ["PySpark", "DBT", "Informatica", "Snowflake", "Pandas", "ADF"]),
    ("Databases",        ["SSMS", "pgAdmin", "MySQL", "Oracle", "SQL Server", "Snowflake"]),
    ("BI & Analytics",   ["Power BI", "ThoughtSpot", "Plotly", "Streamlit"]),
    ("AI & GenAI",       ["Azure OpenAI", "Amazon Bedrock", "Gemini 2.5 Pro", "LangChain", "Neo4j", "RAG", "Prompt Engineering", "Azure Doc Intelligence"]),
    ("Automation & Web", ["Selenium", "Web Scraping", "FastAPI", "PyAutoGUI", "Apify", "Flask"]),
    ("DevOps & Tools",   ["GitHub", "Azure DevOps", "CI/CD", "PuTTY", "ServiceNow", "Rally"]),
    ("Libraries",        ["asyncio", "PyVis", "PyPDF2", "pyodbc", "Snowflake Connector", "xmltodict", "smtplib"]),
]
EXP = [
    ("Data Engineer — L2",          "Optisol Business Solutions", "Apr 2025", "Present",
     ["Led cross-functional teams on enterprise cloud migrations","Architected Snowflake DWH with dbt ELT pipelines","Built GenAI agents with Azure OpenAI & LangChain","Mentored junior engineers; conducted college sessions"]),
    ("Data Engineer — L1",          "Optisol Business Solutions", "Aug 2024", "Mar 2025",
     ["Python ETL pipelines for Azure SQL","AI-powered data profiling platforms","Knowledge graph system using Neo4j and RAG","Self-healing AI Pandas code agent"]),
    ("Data Engineer Intern — L0",   "Optisol Business Solutions", "Mar 2024", "Jul 2024",
     ["Automated web extraction with Selenium & PyAutoGUI","AI scraping tools with LangChain and Apify"]),
    ("Trainee — Software Engineer", "Blue Cloud",                 "Jun 2023", "Mar 2024",
     ["Full-stack web application development","Automation and integration projects"]),
]
DE_PROJ = [
    ("#1","Python-Based Data Migration: Google Sheets → Azure SQL","Data Engineer","Internal | Optisol",
     ["Python","Pandas","gspread","pyodbc","Azure SQL","Azure VM","Cron Jobs"],
     "Cost-effective ETL: Google Sheets extraction, full & incremental load, Pandas transforms, Cron-scheduled automation on Azure VM."),
    ("#2","On-Premises → Snowflake Data Warehouse Migration","Data Engineer","Republic Services | Optisol",
     ["Snowflake","Informatica","dbt","Oracle","SQL Server","AWS Step Functions","CloudWatch"],
     "Migrated 6 on-prem sources to Snowflake DWH. dbt ELT via GitHub CI/CD, Step Functions orchestration, CloudWatch monitoring."),
    ("#3","Enterprise DB Migration: Oracle → SQL Server","Data Engineer","Republic Services | Optisol",
     ["Oracle","SQL Server","Autogen ETL","T-SQL","ServiceNow"],
     "Autogen ETL framework for 5-layer pipeline: RAW → Staging → Mirror → Test → Production with ServiceNow change management."),
    ("#4","API-Driven Migration: Podio → Azure SQL","Data Engineer","Jiffy Cultural Exchange | Optisol",
     ["Python","REST API","Pandas","ADF","Azure SQL","Azure Blob","AzCopy"],
     "Podio REST API extraction → ADF transform → Azure SQL bulk load via pyodbc fast_executemany. AzCopy for document migration."),
]
AI_PROJ = [
    ("#1","Automated Web Data Extraction & Reporting","Automation Eng.","IBEAM | Optisol",
     ["Selenium","PyAutoGUI","smtplib","Azure DevOps"],
     "Fully unattended browser automation: login, extract, process reports, SMTP email distribution on schedule."),
    ("#2","AI-Driven Web Scraping — LangChain & Apify","Automation Eng.","IBEAM | Optisol",
     ["Python","LangChain","Apify","REST APIs"],
     "Apify cloud Actors + LangChain for scalable AI-powered crawling. Converts web content to LLM-ready structured docs."),
    ("#3","AI-Powered Automated Data Profiling Platform","Data & AI Eng.","IBEAM | Optisol",
     ["Azure OpenAI","Snowflake","Streamlit","Prompt Engineering"],
     "Multi-source profiling platform: AI-driven anomaly detection, quality insights, interactive Streamlit dashboards."),
    ("#4","AI Pandas Agent — Self-Healing Code Generation","Data & AI Eng.","IBEAM | Optisol",
     ["Azure OpenAI","Pandas","Python"],
     "NL → Pandas code with self-healing loop: runtime error → LLM context → auto-regenerated corrected code."),
    ("#5","Ontology Kit — Data Mapping Agent","Data & AI Eng.","IBEAM | Optisol",
     ["Gemini 2.5 Pro","Streamlit","Pandas","PyODBC"],
     "AI ontology mapping reducing manual effort 40–50%. Protocol-based domain understanding, praised by client on-site."),
    ("#6","AI Document Processing & Structured Extraction","AI Engineer","RS Hackathon | Optisol",
     ["AWS Textract","Amazon Bedrock","EC2","S3","Flask"],
     "Scanned PDFs → structured JSON: Textract OCR, Bedrock semantic structuring, Flask REST API on EC2."),
    ("#7","Internationalization HTML Validation Tool","AI/Data Eng.","Optisol",
     ["Python","HTML Parsing","i18n","JSON"],
     "Detects hard-coded strings, flags missing translation keys, generates JSON audit reports for i18n readiness."),
    ("#8","Automated Internationalization Workflow","Automation Eng.","IBEAM | Optisol",
     ["Python","i18n","Batch Processing","CI/CD"],
     "Manages i18n locale files across languages, validates keys, syncs translations, fully CI/CD integrated."),
    ("#9","Credit Risk Reporting & JSON Intelligence Platform","Data & AI Eng.","Atradius | Optisol",
     ["Gemini 2.5 Pro","asyncio","Plotly","JSON"],
     "40+ credit risk blocks, token-bucket async limiter, asyncio.gather parallel LLM dispatch, Plotly visualizations."),
    ("#10","Knowledge Graph Builder (KGB) with RAG","Data & AI Eng.","Internal | Optisol",
     ["LangChain","Azure OpenAI","Neo4j","PyVis","Streamlit","asyncio"],
     "PDF/DOCX/JSON/XML/SQL → knowledge graphs. Neo4j persistence, RAG query layer, physics-simulated PyVis visualization."),
]
AWARDS = [
    ("🏆","Most Valuable Person (MVP) Award","2024–25","Highest organizational honor. Performance excellence, cross-functional leadership, long-term business contribution. One of the youngest recipients at Optisol."),
    ("🥇","Spot Award — Project Excellence & Leadership","Jan 2026","Awarded by the CTO for mature project handling and fostering a culture of peer recognition."),
    ("🥇","Spot Award — RS ARP Project Go-Live","Nov 2025","Exceptional contribution to Beatty Go-Live rollout and Delta Load delivery under tight enterprise timelines."),
    ("🥇","Spot Award — AI Tool Innovation (NotebookLLM)","May 2025","Evaluated, demonstrated, and drove team-wide adoption of NotebookLLM."),
    ("🥇","Spot Award — Community Mentorship","Mar 2025","Technical sessions for college students on interview prep and emerging Data & AI technologies."),
    ("🥇","OKR Top Contributor (Q4)","Oct–Dec 2024","Pivotal role in achieving company-wide Q4 Objectives and Key Results."),
    ("🥇","Spot Award — Client Excellence (Ontology Mapping)","Dec 2024","High praise from client during on-site Ontology Mapping platform demo."),
    ("🥇","Spot Award — Gen AI & Automation","Jul 2024","GenAI data inventory automation and SME for resolving critical DBT blockers."),
]
CERTS = [
    ("❄️","SnowPro Core Certification","Snowflake"),
    ("☁️","Azure Data Fundamentals (DP-900)","Microsoft"),
    ("🧱","Databricks Lakehouse Fundamentals","Databricks"),
    ("🤖","Generative AI Fundamentals","Databricks"),
    ("🔧","dbt Learn Fundamentals","dbt Labs"),
    ("💾","SQL (Basic) Certificate","HackerRank"),
    ("🐍","100 Days of Code: Python Pro Bootcamp","Udemy"),
    ("❄️","Snowflake Masterclass","Udemy"),
]
RESUME_URL = "https://github.com/AshikRoshan-github/Professional-Work-Archive/raw/main/Resume_Center/Data%26AI_1360.docx"
PAGES = ["🏠  Home", "⚡  Skills", "💼  Experience", "🚀  Projects", "🏆  Awards & Certs", "🎓  Education", "🤖  Chat with AI"]

# ══════════════════════════════════════════════════════════════════════════════
#  CSS — Snowflake White/Blue Theme
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Sora:wght@300;400;600;700;800&display=swap');

*, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
#MainMenu,footer,header,.stDeployButton,
[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"]{ display:none !important; }
.block-container { padding:0 !important; max-width:100% !important; }
section[data-testid="stSidebar"] { display:none !important; }

:root{
  --snow:    #FFFFFF;
  --ice:     #F0F6FF;
  --frost:   #E1EEFF;
  --mist:    #C8DCFF;
  --blue:    #0B66FF;
  --blue2:   #0052D4;
  --blue3:   #003EA6;
  --sky:     #EBF4FF;
  --ink:     #0A1628;
  --ink2:    #1E3A5F;
  --ink3:    #3D6091;
  --muted:   #7B9EC4;
  --border:  #D0E3FF;
  --border2: #B0CCFF;
}

.stApp { background:var(--snow); font-family:'Inter',sans-serif; color:var(--ink); }

@keyframes fadeUp { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }
.fade { animation:fadeUp 0.5s ease both; }
.d1{animation-delay:.05s} .d2{animation-delay:.12s} .d3{animation-delay:.2s} .d4{animation-delay:.3s}

/* ══ NAV BAR ══ */
.topnav {
  background:var(--snow);
  border-bottom: 2px solid var(--blue);
  display:flex; align-items:center; justify-content:space-between;
  padding:0 48px; height:62px;
  position:sticky; top:0; z-index:500;
  box-shadow: 0 2px 20px rgba(11,102,255,0.08);
}
.nav-brand {
  display:flex; align-items:center; gap:10px;
  font-family:'Sora',sans-serif; font-size:16px; font-weight:700; color:var(--ink);
}
.nav-logo {
  width:32px; height:32px; background:var(--blue);
  border-radius:6px; display:flex; align-items:center; justify-content:center;
  font-size:18px;
}
.nav-tagline { font-size:11px; font-weight:400; color:var(--muted); margin-left:4px; letter-spacing:.5px; }

/* ══ HERO ══ */
.hero-outer {
  background: linear-gradient(135deg, var(--ink) 0%, var(--ink2) 60%, var(--blue3) 100%);
  padding:72px 56px 64px; position:relative; overflow:hidden;
}
.hero-outer::before {
  content:'';
  position:absolute; inset:0;
  background-image:
    radial-gradient(circle at 20% 80%, rgba(11,102,255,0.25) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(11,102,255,0.2) 0%, transparent 50%);
}
.hero-grid { display:grid; grid-template-columns:1fr 340px; gap:64px; align-items:start; max-width:1200px; margin:0 auto; position:relative; z-index:2; }
.hero-eyebrow {
  font-size:11px; font-weight:600; letter-spacing:3px; text-transform:uppercase;
  color:var(--blue); background:rgba(11,102,255,0.15); border:1px solid rgba(11,102,255,0.3);
  display:inline-flex; align-items:center; gap:8px;
  padding:5px 14px; border-radius:100px; margin-bottom:24px;
}
.hero-name {
  font-family:'Sora',sans-serif;
  font-size:clamp(44px,6vw,80px); font-weight:800;
  line-height:1; letter-spacing:-2.5px; color:white; margin-bottom:8px;
}
.hero-name-sub {
  font-family:'Sora',sans-serif;
  font-size:clamp(16px,2.5vw,24px); font-weight:300;
  color:rgba(255,255,255,0.55); letter-spacing:-0.5px; margin-bottom:28px;
}
.hero-rule { width:48px; height:3px; background:var(--blue); border-radius:2px; margin-bottom:24px; }
.hero-bio { font-size:15px; line-height:1.85; color:rgba(255,255,255,0.75); font-weight:300; max-width:520px; }
.hero-bio strong { color:white; font-weight:600; }

/* Stats strip */
.hero-stats { display:grid; grid-template-columns:repeat(2,1fr); gap:12px; margin-top:32px; }
.hstat {
  background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12);
  border-radius:8px; padding:16px 18px; backdrop-filter:blur(4px);
}
.hstat-n { font-family:'Sora',sans-serif; font-size:28px; font-weight:700; color:white; letter-spacing:-1px; line-height:1; }
.hstat-n em { color:var(--blue); font-style:normal; }
.hstat-l { font-size:10px; font-weight:500; letter-spacing:1.5px; text-transform:uppercase; color:rgba(255,255,255,0.4); margin-top:3px; }

/* Contact card */
.contact-card {
  background:white; border-radius:12px; padding:28px 24px;
  box-shadow:0 8px 40px rgba(0,0,0,0.25);
  position:sticky; top:80px;
}
.cc-title { font-family:'Sora',sans-serif; font-size:14px; font-weight:700; color:var(--ink); margin-bottom:20px; padding-bottom:14px; border-bottom:2px solid var(--frost); display:flex; align-items:center; gap:8px; }
.cc-title::before { content:''; width:4px; height:16px; background:var(--blue); border-radius:2px; }
.cc-row { display:flex; align-items:center; gap:11px; margin-bottom:12px; text-decoration:none; padding:8px 10px; border-radius:6px; transition:background .15s; }
.cc-row:hover { background:var(--ice); }
.cc-icon { width:28px; height:28px; background:var(--frost); border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:13px; flex-shrink:0; color:var(--blue2); }
.cc-lbl { font-size:9px; font-weight:600; letter-spacing:1px; text-transform:uppercase; color:var(--muted); }
.cc-val { font-size:12px; color:var(--ink2); font-weight:500; }
.cc-resume {
  display:block; text-align:center; background:var(--blue); color:white;
  font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;
  padding:12px 16px; border-radius:8px; text-decoration:none; margin-top:16px;
  transition:background .15s, transform .15s; box-shadow:0 4px 14px rgba(11,102,255,0.35);
}
.cc-resume:hover { background:var(--blue2); transform:translateY(-1px); }

/* ══ SECTION WRAPPER ══ */
.sec { padding:56px 56px 64px; max-width:1200px; margin:0 auto; }
.sec-label {
  font-size:10px; font-weight:700; letter-spacing:3px; text-transform:uppercase;
  color:var(--blue); margin-bottom:8px;
  display:flex; align-items:center; gap:10px;
}
.sec-label::before { content:''; width:24px; height:2px; background:var(--blue); border-radius:1px; }
.sec-title { font-family:'Sora',sans-serif; font-size:clamp(28px,4vw,46px); font-weight:700; color:var(--ink); letter-spacing:-1.5px; margin-bottom:36px; line-height:1.1; }
.sec-title em { font-style:normal; color:var(--blue); }

/* ══ SKILLS ══ */
.skill-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:var(--border); border:1px solid var(--border); border-radius:10px; overflow:hidden; }
.skill-row { background:var(--snow); padding:14px 20px; display:flex; gap:16px; align-items:flex-start; transition:background .15s; }
.skill-row:hover { background:var(--ice); }
.skill-cat { font-size:9px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--blue); min-width:106px; padding-top:4px; flex-shrink:0; }
.skill-tags { display:flex; flex-wrap:wrap; gap:5px; }
.stag { font-size:11.5px; color:var(--ink2); background:var(--sky); padding:3px 9px; border-radius:4px; border:1px solid var(--border); font-weight:500; transition:all .15s; cursor:default; }
.stag:hover { background:var(--blue); color:white; border-color:var(--blue); }

/* ══ TIMELINE ══ */
.tl-item { display:grid; grid-template-columns:160px 3px 1fr; gap:0 28px; padding:28px 0; border-bottom:1px solid var(--frost); align-items:start; }
.tl-item:last-child { border-bottom:none; }
.tl-date { text-align:right; font-size:11px; color:var(--muted); line-height:1.7; padding-top:5px; font-weight:500; }
.tl-line { background:var(--border); position:relative; align-self:stretch; }
.tl-dot { position:absolute; top:5px; left:-5px; width:13px; height:13px; background:var(--blue); border-radius:50%; border:2px solid white; box-shadow:0 0 0 2px var(--blue); }
.tl-body { padding-left:4px; }
.tl-role { font-family:'Sora',sans-serif; font-size:18px; font-weight:700; color:var(--ink); margin-bottom:4px; }
.tl-company { font-size:11.5px; color:var(--blue); font-weight:600; letter-spacing:.5px; margin-bottom:14px; }
.tl-bullets { list-style:none; }
.tl-bullets li { font-size:13.5px; color:var(--ink3); line-height:1.75; padding-left:16px; position:relative; margin-bottom:4px; }
.tl-bullets li::before { content:'▸'; position:absolute; left:0; color:var(--blue); font-size:10px; top:3px; }

/* ══ PROJECT CARDS ══ */
.proj-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:16px; }
.pcard {
  background:var(--snow); padding:22px 22px; display:flex; flex-direction:column; gap:11px;
  border:1px solid var(--border); border-radius:10px;
  transition:border-color .2s, box-shadow .2s, transform .2s;
}
.pcard:hover { border-color:var(--blue); box-shadow:0 6px 24px rgba(11,102,255,0.12); transform:translateY(-2px); }
.pcard-header { display:flex; align-items:flex-start; gap:10px; }
.pcard-num { font-size:10px; font-weight:700; color:var(--blue); background:var(--frost); padding:2px 8px; border-radius:4px; flex-shrink:0; border:1px solid var(--border2); }
.pcard-title { font-size:13.5px; font-weight:700; color:var(--ink); line-height:1.45; flex:1; }
.pcard-meta { display:flex; gap:12px; flex-wrap:wrap; }
.pmeta { font-size:10px; color:var(--muted); font-weight:500; }
.pmeta span { color:var(--ink2); font-weight:600; }
.pcard-desc { font-size:12.5px; line-height:1.75; color:var(--ink3); flex:1; }
.pcard-tags { display:flex; flex-wrap:wrap; gap:4px; padding-top:8px; border-top:1px solid var(--frost); }
.ptag { font-size:10px; color:var(--blue2); background:var(--sky); padding:2px 7px; border-radius:4px; font-weight:500; }

/* ══ AWARDS ══ */
.award-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:14px; }
.acard {
  background:var(--snow); border:1px solid var(--border); border-radius:10px;
  padding:20px 22px; display:flex; flex-direction:column; gap:8px;
  transition:all .2s; position:relative; overflow:hidden;
}
.acard::after { content:''; position:absolute; top:0; left:0; width:3px; height:100%; background:var(--border2); transition:background .2s; }
.acard:hover { border-color:var(--blue); box-shadow:0 4px 20px rgba(11,102,255,0.1); }
.acard:hover::after { background:var(--blue); }
.acard-top { display:flex; align-items:center; justify-content:space-between; }
.acard-icon { font-size:18px; }
.acard-year { font-size:9.5px; font-weight:600; letter-spacing:1px; color:var(--blue); background:var(--sky); padding:3px 9px; border-radius:100px; border:1px solid var(--border2); }
.acard-title { font-size:13px; font-weight:700; color:var(--ink); line-height:1.4; }
.acard-desc { font-size:12px; color:var(--muted); line-height:1.65; }

/* ══ CERTS ══ */
.cert-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(255px,1fr)); gap:10px; }
.ccard {
  background:var(--snow); border:1px solid var(--border); border-radius:8px;
  padding:13px 16px; display:flex; align-items:center; gap:12px; transition:all .2s;
}
.ccard:hover { border-color:var(--blue); background:var(--ice); }
.ccard-icon { width:36px; height:36px; background:var(--sky); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0; border:1px solid var(--border2); }
.ccard-name { font-size:12.5px; font-weight:700; color:var(--ink); margin-bottom:2px; line-height:1.35; }
.ccard-by { font-size:10.5px; color:var(--blue); font-weight:600; }

/* ══ EDU ══ */
.edu-card {
  background:linear-gradient(135deg,var(--ink) 0%,var(--blue3) 100%);
  border-radius:12px; padding:36px 40px; max-width:580px;
  box-shadow:0 12px 40px rgba(11,102,255,0.3);
}
.edu-year { font-size:64px; font-weight:800; color:rgba(255,255,255,0.06); line-height:1; font-family:'Sora',sans-serif; margin-bottom:4px; letter-spacing:-3px; }
.edu-degree { font-family:'Sora',sans-serif; font-size:22px; font-weight:700; color:white; line-height:1.25; margin-bottom:8px; }
.edu-school { font-size:12px; color:rgba(255,255,255,0.55); font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:20px; }
.edu-pills { display:flex; gap:8px; flex-wrap:wrap; }
.edu-pill { font-size:11px; font-weight:600; color:white; background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); padding:4px 12px; border-radius:4px; }

/* ══ CHAT ══ */
.chat-wrap { padding:56px 56px 64px; max-width:820px; margin:0 auto; }
.chat-info { font-size:14px; color:var(--muted); font-weight:400; margin-top:8px; margin-bottom:28px; }
.chat-box {
  background:var(--ice); border:1px solid var(--border2); border-radius:12px;
  padding:24px; min-height:340px; max-height:500px; overflow-y:auto;
  margin-bottom:14px; display:flex; flex-direction:column; gap:14px;
}
.msg-user { display:flex; justify-content:flex-end; }
.msg-ai { display:flex; justify-content:flex-start; align-items:flex-start; gap:10px; }
.ai-avatar { width:30px; height:30px; background:var(--blue); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; flex-shrink:0; }
.bubble { max-width:80%; padding:12px 16px; border-radius:10px; font-size:13.5px; line-height:1.7; }
.bubble-user { background:var(--blue); color:white; border-bottom-right-radius:3px; }
.bubble-ai { background:white; color:var(--ink); border:1px solid var(--border); border-bottom-left-radius:3px; box-shadow:0 2px 8px rgba(11,102,255,0.06); }
.chat-welcome { text-align:center; padding:36px 20px; color:var(--muted); font-size:13px; }
.chat-welcome .wi { font-size:40px; margin-bottom:12px; }
.chat-welcome strong { display:block; font-size:16px; color:var(--ink); margin-bottom:8px; font-family:'Sora',sans-serif; font-weight:700; }

/* ══ FOOTER ══ */
.footer {
  background:var(--ink);
  padding:36px 56px; display:flex; align-items:center; justify-content:space-between;
}
.footer-name { font-family:'Sora',sans-serif; font-size:18px; font-weight:700; color:white; }
.footer-sub { font-size:11px; color:rgba(255,255,255,0.35); margin-top:3px; letter-spacing:.5px; }
.footer-copy { font-size:11px; color:rgba(255,255,255,0.3); text-align:right; line-height:1.9; }

/* ══ STREAMLIT NAV RADIO OVERRIDE ══ */
div[data-testid="stHorizontalBlock"] { display:none !important; }

/* Style st.radio as nav pills */
div[data-testid="stRadio"] > div {
  display:flex !important; flex-direction:row !important;
  gap:4px !important; flex-wrap:wrap !important;
  background:var(--snow) !important;
  border-bottom:2px solid var(--blue) !important;
  padding:10px 48px !important;
  position:sticky !important; top:62px !important;
  z-index:400 !important;
  box-shadow:0 2px 12px rgba(11,102,255,0.06) !important;
}
div[data-testid="stRadio"] > div > label {
  background:transparent !important;
  border:none !important;
  border-radius:6px !important;
  padding:7px 14px !important;
  font-size:12px !important;
  font-weight:500 !important;
  color:var(--ink3) !important;
  cursor:pointer !important;
  transition:all .15s !important;
  white-space:nowrap !important;
}
div[data-testid="stRadio"] > div > label:hover {
  background:var(--sky) !important; color:var(--blue) !important;
}
div[data-testid="stRadio"] > div > label[data-baseweb="radio"] input:checked ~ div,
div[data-testid="stRadio"] > div > label:has(input:checked) {
  background:var(--blue) !important; color:white !important;
  border-radius:6px !important;
}
div[data-testid="stRadio"] > label { display:none !important; }
div[data-testid="stRadio"] p { font-size:12px !important; }
div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { font-size:12px !important; }

/* Input overrides */
div[data-testid="stTextInput"] input {
  background:var(--snow) !important; border:1.5px solid var(--border2) !important;
  border-radius:8px !important; color:var(--ink) !important;
  font-family:'Inter',sans-serif !important; font-size:14px !important; padding:11px 14px !important;
}
div[data-testid="stTextInput"] input:focus { border-color:var(--blue) !important; box-shadow:0 0 0 3px rgba(11,102,255,0.1) !important; }
div[data-testid="stButton"] button {
  background:var(--blue) !important; color:white !important; border:none !important;
  border-radius:8px !important; font-family:'Inter',sans-serif !important;
  font-size:12px !important; font-weight:600 !important; letter-spacing:.5px !important;
  padding:11px 20px !important; box-shadow:0 4px 12px rgba(11,102,255,0.3) !important;
}
div[data-testid="stButton"] button:hover { background:var(--blue2) !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ══════════════════════════════════════════════════════════════════════════════
#  TOP BRAND BAR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="topnav">
  <div class="nav-brand">
    <div class="nav-logo">❄️</div>
    Ashik Roshan I
    <span class="nav-tagline">DATA &amp; AI ENGINEER</span>
  </div>
  <div style="font-size:11px;color:#7B9EC4;font-weight:500;letter-spacing:.5px;">Madurai, TamilNadu, India · Optisol Business Solutions</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  NAVIGATION — using st.radio (THIS ACTUALLY WORKS in Streamlit)
# ══════════════════════════════════════════════════════════════════════════════
page = st.radio(
    "nav",
    PAGES,
    horizontal=True,
    label_visibility="collapsed",
    key="main_nav"
)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════════════════

# ── HOME ─────────────────────────────────────────────────────────────────────
if page == PAGES[0]:
    st.markdown("""
    <div class="hero-outer">
      <div class="hero-grid">
        <div>
          <div class="hero-eyebrow fade d1">❄️ Data Engineer & AI Engineer — L2</div>
          <h1 class="hero-name fade d2">Ashik<br>Roshan I</h1>
          <p class="hero-name-sub fade d2">Building data pipelines & intelligent systems</p>
          <div class="hero-rule fade d3"></div>
          <p class="hero-bio fade d3">
            Results-driven engineer with <strong>2+ years</strong> delivering scalable ETL/ELT pipelines,
            enterprise cloud migrations, and production-grade AI automation at
            <strong>Optisol Business Solutions</strong>. Specialising in
            <strong>Snowflake, Azure, AWS, LangChain,</strong> and GenAI agent design.
          </p>
          <div class="hero-stats fade d4">
            <div class="hstat"><div class="hstat-n">2<em>+</em></div><div class="hstat-l">Years Experience</div></div>
            <div class="hstat"><div class="hstat-n">14<em>+</em></div><div class="hstat-l">Projects Delivered</div></div>
            <div class="hstat"><div class="hstat-n">7</div><div class="hstat-l">Spot Awards</div></div>
            <div class="hstat"><div class="hstat-n"><em>MVP</em></div><div class="hstat-l">Award 2024–25</div></div>
          </div>
        </div>
        <div class="fade d3">
          <div class="contact-card">
            <div class="cc-title">Get in Touch</div>
            <a class="cc-row" href="mailto:ashikroshan261@gmail.com">
              <div class="cc-icon">✉</div>
              <div><div class="cc-lbl">Email</div><div class="cc-val">ashikroshan261@gmail.com</div></div>
            </a>
            <a class="cc-row" href="https://github.com/AshikRoshan-github" target="_blank">
              <div class="cc-icon">⌥</div>
              <div><div class="cc-lbl">GitHub</div><div class="cc-val">AshikRoshan-github</div></div>
            </a>
            <a class="cc-row" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">
              <div class="cc-icon">in</div>
              <div><div class="cc-lbl">LinkedIn</div><div class="cc-val">ashik-roshan-i</div></div>
            </a>
            <a class="cc-row" href="https://medium.com/@ashikroshan261" target="_blank">
              <div class="cc-icon">✍</div>
              <div><div class="cc-lbl">Medium</div><div class="cc-val">@ashikroshan261</div></div>
            </a>
            <a class="cc-resume" href="https://github.com/AshikRoshan-github/Professional-Work-Archive/raw/main/Resume_Center/Data%26AI_1360.docx" target="_blank">
              ⬇ Download Resume
            </a>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────────────────
elif page == PAGES[1]:
    st.markdown('<div class="sec fade">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Arsenal</div><h2 class="sec-title">Technical <em>Skills</em></h2>', unsafe_allow_html=True)
    rows = ""
    for cat, tags in SKILLS:
        tag_html = "".join(f'<span class="stag">{t}</span>' for t in tags)
        rows += f'<div class="skill-row"><div class="skill-cat">{cat}</div><div class="skill-tags">{tag_html}</div></div>'
    st.markdown(f'<div class="skill-grid">{rows}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
elif page == PAGES[2]:
    st.markdown('<div class="sec fade">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Career</div><h2 class="sec-title">Professional <em>Experience</em></h2>', unsafe_allow_html=True)
    tl = ""
    for role, company, start, end, bullets in EXP:
        bl = "".join(f"<li>{b}</li>" for b in bullets)
        tl += f"""<div class="tl-item">
          <div class="tl-date">{start}<br>—<br>{end}</div>
          <div class="tl-line"><div class="tl-dot"></div></div>
          <div class="tl-body">
            <div class="tl-role">{role}</div>
            <div class="tl-company">{company}</div>
            <ul class="tl-bullets">{bl}</ul>
          </div>
        </div>"""
    st.markdown(f'<div>{tl}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── PROJECTS ─────────────────────────────────────────────────────────────────
elif page == PAGES[3]:
    def make_grid(projects):
        html = '<div class="proj-grid">'
        for num, title, role, client, tech, desc in projects:
            tags = "".join(f'<span class="ptag">{t}</span>' for t in tech)
            html += f"""<div class="pcard">
              <div class="pcard-header"><div class="pcard-num">{num}</div><div class="pcard-title">{title}</div></div>
              <div class="pcard-meta"><div class="pmeta">ROLE <span>{role}</span></div><div class="pmeta">CLIENT <span>{client}</span></div></div>
              <div class="pcard-desc">{desc}</div>
              <div class="pcard-tags">{tags}</div>
            </div>"""
        return html + "</div>"

    st.markdown('<div class="sec fade">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Data Engineering</div><h2 class="sec-title">Data Engineering <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(make_grid(DE_PROJ), unsafe_allow_html=True)
    st.markdown('<div style="height:52px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">AI & Automation</div><h2 class="sec-title">AI & Automation <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(make_grid(AI_PROJ), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── AWARDS & CERTS ───────────────────────────────────────────────────────────
elif page == PAGES[4]:
    st.markdown('<div class="sec fade">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Recognition</div><h2 class="sec-title">Awards & <em>Achievements</em></h2>', unsafe_allow_html=True)
    aw = "".join(f"""<div class="acard">
      <div class="acard-top"><span class="acard-icon">{icon}</span><span class="acard-year">{year}</span></div>
      <div class="acard-title">{title}</div>
      <div class="acard-desc">{desc}</div>
    </div>""" for icon, title, year, desc in AWARDS)
    st.markdown(f'<div class="award-grid">{aw}</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:52px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Credentials</div><h2 class="sec-title"><em>Certifications</em></h2>', unsafe_allow_html=True)
    ce = "".join(f"""<div class="ccard">
      <div class="ccard-icon">{icon}</div>
      <div><div class="ccard-name">{name}</div><div class="ccard-by">{issuer}</div></div>
    </div>""" for icon, name, issuer in CERTS)
    st.markdown(f'<div class="cert-grid">{ce}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ────────────────────────────────────────────────────────────────
elif page == PAGES[5]:
    st.markdown('<div class="sec fade">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Academic</div><h2 class="sec-title"><em>Education</em></h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-card">
      <div class="edu-year">2023</div>
      <div class="edu-degree">Bachelor of Engineering<br>in Computer Science</div>
      <div class="edu-school">KLN College of Engineering</div>
      <div class="edu-pills">
        <span class="edu-pill">2019 – 2023</span>
        <span class="edu-pill">Grade: A+</span>
        <span class="edu-pill">Computer Science & Engineering</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── CHAT ─────────────────────────────────────────────────────────────────────
elif page == PAGES[6]:
    st.markdown('<div class="chat-wrap fade">', unsafe_allow_html=True)
    st.markdown("""
    <div class="sec-label">AI Assistant</div>
    <h2 class="sec-title">Ask <em>Ashik's AI</em></h2>
    <p class="chat-info">❄️ Powered by Gemini 2.5 Pro · Knows everything about Ashik's projects, skills & background</p>
    """, unsafe_allow_html=True)

    # Render messages
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="chat-box">
          <div class="chat-welcome">
            <div class="wi">❄️</div>
            <strong>Hi! I'm Ashik's AI Assistant</strong>
            Ask me about his projects, skills, experience, awards, certifications, or how to contact him.
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        bubbles = ""
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                bubbles += f'<div class="msg-user"><div class="bubble bubble-user">{msg["content"]}</div></div>'
            else:
                content = msg["content"].replace("\n", "<br>")
                bubbles += f'<div class="msg-ai"><div class="ai-avatar">❄️</div><div class="bubble bubble-ai">{content}</div></div>'
        st.markdown(f'<div class="chat-box">{bubbles}</div>', unsafe_allow_html=True)

    # Input row
    col_in, col_send = st.columns([5, 1])
    with col_in:
        user_input = st.text_input(
            "", placeholder="Ask about Ashik's projects, skills, awards...",
            label_visibility="collapsed", key="chat_input"
        )
    with col_send:
        send_clicked = st.button("Send ❄️", key="send_btn", use_container_width=True)

    col_clr, _ = st.columns([1, 6])
    with col_clr:
        if st.button("🗑 Clear", key="clear_btn"):
            st.session_state.chat_history = []
            st.rerun()

    # Missing package warning
    if not GENAI_AVAILABLE:
        st.error("⚠️ **google-genai not installed.** Add `google-genai` to requirements.txt and redeploy.")

    elif send_clicked and user_input.strip():
        # Read key: st.secrets["GOOGLE"]["Gemini_api_key"]
        gemini_key = None
        try:
            gemini_key = st.secrets["GOOGLE"]["Gemini_api_key"]
        except Exception:
            pass
        if not gemini_key:
            gemini_key = os.environ.get("GEMINI_API_KEY", "")

        if not gemini_key:
            st.error("""⚠️ API key not found. In Streamlit Cloud Secrets add:
```toml
[GOOGLE]
Gemini_api_key = "your-key-here"
```""")
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            with st.spinner("❄️ Thinking..."):
                try:
                    client = google_genai.Client(api_key=gemini_key)
                    contents = []
                    for msg in st.session_state.chat_history:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append(google_types.Content(
                            role=role,
                            parts=[google_types.Part.from_text(text=msg["content"])]
                        ))
                    config = google_types.GenerateContentConfig(
                        system_instruction=ASHIK_SYSTEM_PROMPT,
                        max_output_tokens=1024,
                    )
                    response = client.models.generate_content(
                        model="gemini-2.5-pro",
                        contents=contents,
                        config=config,
                    )
                    st.session_state.chat_history.append({
                        "role": "assistant", "content": response.text
                    })
                    st.rerun()
                except Exception as e:
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": f"⚠️ Gemini API error: {str(e)}"
                    })
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-name">Ashik Roshan I</div>
    <div class="footer-sub">DATA ENGINEER · AI ENGINEER · L2 · OPTISOL</div>
  </div>
  <div class="footer-copy">
    Built with Streamlit · Powered by Gemini 2.5 Pro<br>
    © 2025 Ashik Roshan I · All rights reserved
  </div>
</div>
""", unsafe_allow_html=True)
