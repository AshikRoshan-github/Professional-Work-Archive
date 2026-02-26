import streamlit as st
import os

try:
    from google import genai as google_genai
    from google.genai import types as google_types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

st.set_page_config(
    page_title="Ashik Roshan I — Data & AI Engineer",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SYSTEM_PROMPT = """You are a professional AI assistant embedded in Ashik Roshan I's portfolio website. You have complete, authoritative knowledge of everything about Ashik. Be warm, confident, and professional. Give detailed answers. Format responses clearly with line breaks when listing multiple items. Never mention what technology or AI model powers you — if asked, simply say "I'm Ashik's personal portfolio assistant."

SECTION 1 — PERSONAL INFORMATION
Name            : Ashik Roshan I
Role            : Data Engineer & AI Engineer — Level 2 (L2)
Company         : Optisol Business Solutions
Location        : Madurai, TamilNadu, India
Email           : ashikroshan261@gmail.com
GitHub          : github.com/AshikRoshan-github
LinkedIn        : linkedin.com/in/ashik-roshan-i-073897249
Medium          : medium.com/@ashikroshan261
Experience      : 2+ years (Jun 2023 – Present)
Summary         : Results-driven Data & AI Engineer delivering scalable ETL/ELT pipelines, enterprise cloud migrations, and production-grade AI automation. Specialises in Snowflake, Azure, AWS, LangChain, and GenAI agent design. MVP award winner, 7x Spot Award recipient.

SECTION 2 — EXPERIENCE
1. Data Engineer L2 | Optisol Business Solutions | Apr 2025 – Present
   - Led cross-functional teams on enterprise cloud migrations
   - Architected Snowflake DWH with dbt ELT pipelines
   - Built GenAI agents with Azure OpenAI and LangChain
   - Designed Neo4j knowledge graphs with RAG layers
   - Mentored juniors; delivered college tech sessions
   - CTO Spot Award: project excellence & leadership

2. Data Engineer L1 | Optisol Business Solutions | Aug 2024 – Mar 2025
   - Python ETL pipelines for Azure SQL
   - AI-powered data profiling platforms
   - Self-healing AI Pandas code generation agent
   - Ontology Mapping tool — 40–50% manual effort reduction

3. Data Engineer Intern L0 | Optisol Business Solutions | Mar 2024 – Jul 2024
   - Web extraction automation: Selenium, PyAutoGUI
   - AI scraping tools: LangChain, Apify

4. Trainee Software Engineer | Blue Cloud | Jun 2023 – Mar 2024
   - Full-stack web application development
   - Automation and integration projects

SECTION 3 — TECHNICAL SKILLS
Languages: Python, SQL, JavaScript, HTML, CSS
Cloud Azure: Blob Storage, Data Lake, SQL Database, Azure OpenAI, Databricks, ADF, Azure VM
Cloud AWS: S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock
Data Engineering: PySpark, dbt, Informatica, Snowflake, Pandas, ADF
Databases: SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics: Power BI, ThoughtSpot, Plotly, Streamlit
AI & GenAI: Azure OpenAI, Amazon Bedrock, Gemini 2.5 Pro, LangChain, Neo4j, RAG, Prompt Engineering, Azure Document Intelligence
Automation: Selenium, Web Scraping, FastAPI, PyAutoGUI, Apify, Flask
DevOps: GitHub, Azure DevOps, CI/CD, PuTTY, ServiceNow, Rally
Libraries: asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict, smtplib

SECTION 4 — DATA ENGINEERING PROJECTS
DE-1: Python-Based Data Migration — Google Sheets to Azure SQL
  Client: Internal Optisol | Stack: Python, Pandas, gspread, pyodbc, Azure SQL, Azure VM, Cron
  Full ETL with incremental/full load, Pandas transforms, Cron automation on Azure VM.

DE-2: On-Premises to Snowflake Data Warehouse Migration
  Client: Republic Services | Stack: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS Step Functions, CloudWatch
  Migrated 6 on-prem sources. dbt ELT via CI/CD, Step Functions orchestration, CloudWatch monitoring.

DE-3: Enterprise DB Migration — Oracle to SQL Server
  Client: Republic Services | Stack: Oracle, SQL Server, Autogen ETL, T-SQL, ServiceNow
  5-layer pipeline: RAW > Staging > Mirror > Test > Production. ServiceNow change management.

DE-4: API-Driven Migration — Podio to Azure SQL
  Client: Jiffy Cultural Exchange | Stack: Python, REST API, Pandas, ADF, Azure SQL, Azure Blob, AzCopy
  Podio REST API extraction, ADF pipeline, pyodbc fast_executemany bulk load, AzCopy migration.

SECTION 5 — AI & AUTOMATION PROJECTS
AI-1: Automated Web Data Extraction & Reporting | IBEAM | Selenium, PyAutoGUI, smtplib
  Fully unattended browser automation: extract, process, SMTP email reports.

AI-2: AI-Driven Web Scraping — LangChain & Apify | IBEAM | Python, LangChain, Apify
  Apify cloud Actors + LangChain for scalable AI-powered crawling.

AI-3: AI-Powered Data Profiling Platform | IBEAM | Azure OpenAI, Snowflake, Streamlit
  AI anomaly detection, data quality insights, interactive dashboards.

AI-4: AI Pandas Agent — Self-Healing Code Generation | IBEAM | Azure OpenAI, Pandas
  NL to Pandas code with self-healing: error > LLM context > auto-corrected code.

AI-5: Ontology Kit — Data Mapping Agent | IBEAM | Gemini 2.5 Pro, Streamlit, Pandas
  Reduces ontology mapping effort 40–50%. Client praised during on-site demo.

AI-6: AI Document Processing & Extraction | RS Hackathon | AWS Textract, Bedrock, Flask
  Scanned PDF to structured JSON: OCR, semantic structuring, Flask REST API.

AI-7: Internationalization HTML Validation | Optisol | Python, HTML Parsing, i18n
  Detects hard-coded strings, missing keys, generates JSON audit reports.

AI-8: Automated Internationalization Workflow | IBEAM | Python, i18n, CI/CD
  i18n locale file management, key validation, CI/CD integrated.

AI-9: Credit Risk Reporting Platform | Atradius | Gemini 2.5 Pro, asyncio, Plotly
  40+ credit risk blocks, token-bucket async limiter, asyncio.gather parallel dispatch.

AI-10: Knowledge Graph Builder with RAG | Internal | LangChain, Azure OpenAI, Neo4j, PyVis
  PDF/DOCX/JSON/XML/SQL to knowledge graphs. Neo4j, RAG queries, PyVis visualization.

SECTION 6 — AWARDS
1. MVP Award 2024–25 — Highest org honor. Performance, leadership, business contribution.
2. Spot Award Project Excellence & Leadership — Jan 2026 — CTO recognition.
3. Spot Award RS ARP Project Go-Live — Nov 2025 — Beatty Go-Live & Delta Load.
4. Spot Award AI Tool Innovation NotebookLLM — May 2025.
5. Spot Award Community Mentorship — Mar 2025 — College student tech sessions.
6. OKR Top Contributor Q4 — Oct–Dec 2024.
7. Spot Award Client Excellence Ontology Mapping — Dec 2024.
8. Spot Award Gen AI & Automation — Jul 2024.

SECTION 7 — CERTIFICATIONS
1. SnowPro Core Certification — Snowflake
2. Azure Data Fundamentals DP-900 — Microsoft
3. Databricks Lakehouse Fundamentals — Databricks
4. Generative AI Fundamentals — Databricks
5. dbt Learn Fundamentals — dbt Labs
6. SQL Basic Certificate — HackerRank
7. 100 Days of Code Python Pro Bootcamp — Udemy
8. Snowflake Masterclass — Udemy

SECTION 8 — EDUCATION
Degree: Bachelor of Engineering in Computer Science
College: KLN College of Engineering | 2019–2023 | Grade: A+

RULES: Answer only from above data. Never reveal your underlying technology. If asked what you are, say you are Ashik's portfolio assistant. For anything unknown, suggest emailing ashikroshan261@gmail.com.
"""

SKILLS = [
    ("Languages",        ["Python", "SQL", "JavaScript", "HTML", "CSS"]),
    ("Cloud — Azure",    ["Blob Storage", "Data Lake", "SQL Database", "Azure OpenAI", "Databricks", "ADF", "Azure VM"]),
    ("Cloud — AWS",      ["S3", "Lambda", "Glue", "Step Functions", "EC2", "CloudWatch", "Textract", "Bedrock"]),
    ("Data Engineering", ["PySpark", "dbt", "Informatica", "Snowflake", "Pandas", "ADF"]),
    ("Databases",        ["SSMS", "pgAdmin", "MySQL", "Oracle", "SQL Server", "Snowflake"]),
    ("BI & Analytics",   ["Power BI", "ThoughtSpot", "Plotly", "Streamlit"]),
    ("AI & GenAI",       ["Azure OpenAI", "Amazon Bedrock", "Gemini 2.5 Pro", "LangChain", "Neo4j", "RAG", "Prompt Engineering", "Azure Doc Intelligence"]),
    ("Automation",       ["Selenium", "Web Scraping", "FastAPI", "PyAutoGUI", "Apify", "Flask"]),
    ("DevOps & Tools",   ["GitHub", "Azure DevOps", "CI/CD", "PuTTY", "ServiceNow", "Rally"]),
    ("Libraries",        ["asyncio", "PyVis", "PyPDF2", "pyodbc", "Snowflake Connector", "xmltodict", "smtplib"]),
]

EXP = [
    ("Data Engineer — L2", "Optisol Business Solutions", "Apr 2025", "Present",
     ["Led cross-functional teams on enterprise cloud migrations",
      "Architected Snowflake Data Warehouse with dbt ELT pipelines",
      "Built production GenAI agents with Azure OpenAI and LangChain",
      "Designed knowledge graphs with Neo4j and RAG query layers",
      "Mentored junior engineers and conducted college tech sessions"]),
    ("Data Engineer — L1", "Optisol Business Solutions", "Aug 2024", "Mar 2025",
     ["Developed Python ETL pipelines for Azure SQL",
      "Implemented AI-powered data profiling platforms",
      "Built self-healing AI Pandas code generation agent",
      "Delivered Ontology Mapping tool — 40–50% effort reduction"]),
    ("Data Engineer Intern — L0", "Optisol Business Solutions", "Mar 2024", "Jul 2024",
     ["Automated web extraction with Selenium and PyAutoGUI",
      "Built AI scraping tools with LangChain and Apify"]),
    ("Trainee — Software Engineer", "Blue Cloud", "Jun 2023", "Mar 2024",
     ["Full-stack web application development",
      "Automation and integration projects"]),
]

DE_PROJ = [
    ("01","Python-Based Data Migration","Google Sheets to Azure SQL — full and incremental load ETL with Pandas transforms, gspread API integration, pyodbc connectivity, and Cron-scheduled automation on Azure VM.",
     "Data Engineer","Internal — Optisol",["Python","Pandas","gspread","pyodbc","Azure SQL","Azure VM","Cron"]),
    ("02","On-Premises to Snowflake Data Warehouse","Migrated 6 on-prem source systems to Snowflake DWH. dbt ELT via GitHub CI/CD, Informatica extraction, AWS Step Functions orchestration, CloudWatch monitoring.",
     "Data Engineer","Republic Services — Optisol",["Snowflake","Informatica","dbt","Oracle","SQL Server","AWS Step Functions","CloudWatch"]),
    ("03","Enterprise DB Migration — Oracle to SQL Server","Autogen ETL framework automating schema conversion across a 5-layer pipeline: RAW to Staging to Mirror to Test to Production with ServiceNow change management.",
     "Data Engineer","Republic Services — Optisol",["Oracle","SQL Server","Autogen ETL","T-SQL","ServiceNow"]),
    ("04","API-Driven Migration — Podio to Azure SQL","Podio REST API extraction, ADF pipeline transformation, high-performance bulk load into Azure SQL using pyodbc fast_executemany, AzCopy for document migration.",
     "Data Engineer","Jiffy Cultural Exchange — Optisol",["Python","REST API","Pandas","ADF","Azure SQL","Azure Blob","AzCopy"]),
]

AI_PROJ = [
    ("01","Automated Web Data Extraction & Reporting","Fully unattended browser automation: scheduled login, data extraction, file processing, structured report generation, and SMTP email distribution.",
     "Automation Engineer","IBEAM — Optisol",["Selenium","PyAutoGUI","smtplib","Azure DevOps"]),
    ("02","AI-Driven Web Scraping — LangChain & Apify","Apify cloud Actors integrated with LangChain for scalable AI-powered crawling. Transforms scraped content into LLM-ready structured documents for downstream pipelines.",
     "Automation Engineer","IBEAM — Optisol",["Python","LangChain","Apify","REST APIs"]),
    ("03","AI-Powered Automated Data Profiling","Multi-source profiling generating AI-driven anomaly detection reports, data quality insights, and distribution analysis via interactive dashboards.",
     "Data & AI Engineer","IBEAM — Optisol",["Azure OpenAI","Snowflake","Streamlit","Prompt Engineering"]),
    ("04","AI Pandas Agent — Self-Healing Code","Natural language to Pandas code with a self-healing loop. On runtime error, exception context is sent to the AI model which auto-generates corrected transformation code.",
     "Data & AI Engineer","IBEAM — Optisol",["Azure OpenAI","Pandas","Python"]),
    ("05","Ontology Kit — Data Mapping Agent","AI-driven ontology mapping reducing manual effort by 40–50%. Protocol-based domain understanding, auto-generated metadata, sample data integration. Praised by client on-site.",
     "Data & AI Engineer","IBEAM — Optisol",["Gemini 2.5 Pro","Streamlit","Pandas","PyODBC"]),
    ("06","AI Document Processing & Extraction","Scanned PDFs and images to structured JSON pipeline. OCR extraction, semantic structuring via AI, Flask REST API orchestrates the full pipeline with S3 document storage.",
     "AI Engineer","RS Hackathon — Optisol",["AWS Textract","Amazon Bedrock","EC2","S3","Flask"]),
    ("07","Internationalization HTML Validation","Analyzes HTML for i18n readiness: detects hard-coded strings, flags missing translation keys, validates i18n attributes, generates structured JSON audit reports.",
     "AI / Data Engineer","Optisol Internal",["Python","HTML Parsing","i18n","JSON"]),
    ("08","Automated Internationalization Workflow","Framework managing i18n locale files across multiple languages. Validates keys, syncs translations, detects missing entries, integrated into CI/CD pipelines.",
     "Automation Engineer","IBEAM — Optisol",["Python","i18n","Batch Processing","CI/CD"]),
    ("09","Credit Risk Reporting & JSON Intelligence","Automated pipeline for 40+ credit risk data blocks. Token-bucket async rate limiter, parallel AI dispatch, section-based prompting, interactive Plotly visualizations.",
     "Data & AI Engineer","Atradius — Optisol",["Gemini 2.5 Pro","asyncio","Plotly","JSON"]),
    ("10","Knowledge Graph Builder with RAG","Transforms PDF, DOCX, JSON, XML, and SQL into interactive knowledge graphs. Persistent graph storage, RAG query layer for natural language querying, physics-simulated visualization.",
     "Data & AI Engineer","Internal — Optisol",["LangChain","Azure OpenAI","Neo4j","PyVis","Streamlit","asyncio"]),
]

AWARDS = [
    ("Most Valuable Person — MVP Award","2024–25","Highest organizational honor at Optisol for performance excellence, cross-functional leadership, and long-term business contribution. One of the youngest recipients."),
    ("Spot Award — Project Excellence & Leadership","Jan 2026","Awarded by the CTO for mature project handling, strong ownership, and fostering a culture of peer recognition within the team."),
    ("Spot Award — RS ARP Project Go-Live","Nov 2025","Exceptional contribution to the Beatty Go-Live rollout and complex Delta Load feature delivery under tight enterprise timelines."),
    ("Spot Award — AI Tool Innovation","May 2025","Evaluated, demonstrated, and drove team-wide adoption of NotebookLLM to enhance project documentation and knowledge sharing."),
    ("Spot Award — Community Mentorship","Mar 2025","Conducted technical sessions for college students on interview preparation, career guidance, and emerging Data & AI technologies."),
    ("OKR Top Contributor — Q4","Oct–Dec 2024","Pivotal role in achieving company-wide Objectives and Key Results for Q4 2024."),
    ("Spot Award — Client Excellence","Dec 2024","Received direct high praise from the client during an on-site visit for the Ontology Mapping platform presentation and live demo."),
    ("Spot Award — Gen AI & Automation","Jul 2024","Recognized for GenAI-based data inventory automation and serving as Subject Matter Expert to resolve critical dbt pipeline blockers."),
]

CERTS = [
    ("SnowPro Core Certification","Snowflake"),
    ("Azure Data Fundamentals — DP-900","Microsoft"),
    ("Databricks Lakehouse Fundamentals","Databricks"),
    ("Generative AI Fundamentals","Databricks"),
    ("dbt Learn Fundamentals","dbt Labs"),
    ("SQL Basic Certificate","HackerRank"),
    ("100 Days of Code: Python Pro Bootcamp","Udemy"),
    ("Snowflake Masterclass","Udemy"),
]

RESUME_URL = "https://github.com/AshikRoshan-github/Professional-Work-Archive/raw/main/Resume_Center/Data%26AI_1360.docx"
PAGES = ["Home","Skills","Experience","Projects","Awards","Education","Assistant"]

# ══════════════════════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Manrope:wght@300;400;500;600;700;800&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
#MainMenu,footer,header,.stDeployButton,
[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
section[data-testid="stSidebar"]{display:none!important}

:root{
  --navy:#0D1B2E;
  --navy2:#152642;
  --navy3:#1E3A5F;
  --blue:#1A56DB;
  --blue2:#1347C0;
  --blue-lt:#EBF2FF;
  --blue-md:#DBEAFE;
  --white:#FFFFFF;
  --off:#F7F9FC;
  --off2:#EFF3F8;
  --silver:#D4DCE8;
  --silver2:#B8C6D8;
  --slate:#546E8A;
  --body:#1E3248;
  --dark:#0A1520;
}

.stApp{background:var(--white);font-family:'Manrope',system-ui,sans-serif;color:var(--body)}

@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
.rise{animation:rise .55s cubic-bezier(.22,.68,0,1.1) both}
.r1{animation-delay:.05s}.r2{animation-delay:.13s}.r3{animation-delay:.22s}.r4{animation-delay:.32s}.r5{animation-delay:.44s}

/* BRAND BAR */
.brand-bar{
  background:var(--navy);
  height:60px;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;
  position:sticky;top:0;z-index:600;
  box-shadow:0 1px 0 rgba(255,255,255,0.06);
}
.brand-name{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:21px;font-weight:700;color:white;letter-spacing:-.3px;
}
.brand-name em{font-style:italic;font-weight:400;color:#7EABD6}
.brand-links{display:flex;align-items:center;gap:6px}
.brand-link{
  font-family:'Manrope',sans-serif;
  font-size:13px;font-weight:600;color:rgba(255,255,255,0.6);
  text-decoration:none;padding:6px 14px;border-radius:4px;
  transition:color .15s,background .15s;
}
.brand-link:hover{color:white;background:rgba(255,255,255,0.08)}
.brand-divider{color:rgba(255,255,255,0.18);font-size:11px;margin:0 2px}
.brand-resume{
  font-family:'Manrope',sans-serif;
  font-size:12px;font-weight:700;color:var(--navy);
  background:white;padding:7px 18px;border-radius:4px;
  text-decoration:none;letter-spacing:.4px;text-transform:uppercase;
  transition:background .15s;margin-left:8px;
}
.brand-resume:hover{background:#E8F0FF}

/* NAV — st.radio */
div[data-testid="stRadio"]{
  background:var(--white);
  border-bottom:2px solid var(--silver);
  position:sticky;top:60px;z-index:500;
  box-shadow:0 2px 16px rgba(13,27,46,0.05);
}
div[data-testid="stRadio"]>label{display:none!important}
div[data-testid="stRadio"]>div{
  display:flex!important;flex-direction:row!important;
  gap:0!important;padding:0 64px!important;
  background:transparent!important;flex-wrap:nowrap!important;
  overflow-x:auto!important;
}
div[data-testid="stRadio"]>div>label{
  background:transparent!important;border:none!important;
  border-bottom:3px solid transparent!important;border-radius:0!important;
  padding:17px 22px 14px!important;
  font-family:'Manrope',sans-serif!important;
  font-size:14px!important;font-weight:500!important;
  color:var(--slate)!important;cursor:pointer!important;
  transition:color .15s,border-color .15s!important;white-space:nowrap!important;
}
div[data-testid="stRadio"]>div>label:hover{color:var(--navy)!important;background:var(--off)!important}
div[data-testid="stRadio"]>div>label:has(input:checked){
  color:var(--navy)!important;border-bottom:3px solid var(--blue)!important;
  font-weight:700!important;background:transparent!important;
}
div[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] p{
  font-size:14px!important;font-family:'Manrope',sans-serif!important;
}
div[data-testid="stRadio"] [data-baseweb="radio"]>div:first-child{display:none!important}

/* HERO */
.hero{
  background:var(--navy);
  padding:96px 64px 88px;
  position:relative;overflow:hidden;
}
.hero::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse 70% 90% at 75% 40%,rgba(26,86,219,0.16) 0%,transparent 65%),
             radial-gradient(ellipse 40% 50% at 10% 90%,rgba(26,86,219,0.07) 0%,transparent 60%);
}
.hero-grid{
  display:grid;grid-template-columns:1fr 400px;gap:80px;
  align-items:start;max-width:1280px;margin:0 auto;position:relative;z-index:2;
}
.hero-kicker{
  font-family:'Manrope',sans-serif;font-size:12px;font-weight:700;
  letter-spacing:3px;text-transform:uppercase;
  color:rgba(126,171,214,0.85);margin-bottom:22px;
}
.hero-name{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:clamp(56px,7vw,96px);font-weight:700;
  color:white;line-height:.93;letter-spacing:-3px;margin-bottom:8px;
}
.hero-name em{font-style:italic;font-weight:400;color:#7EABD6}
.hero-subtitle{
  font-family:'Manrope',sans-serif;font-size:17px;font-weight:400;
  color:rgba(255,255,255,0.45);letter-spacing:.3px;margin-bottom:40px;
}
.hero-rule{width:48px;height:2px;background:var(--blue);border-radius:1px;margin-bottom:28px}
.hero-bio{
  font-family:'Manrope',sans-serif;font-size:18px;line-height:1.85;
  color:rgba(255,255,255,0.7);font-weight:300;max-width:580px;
}
.hero-bio strong{color:white;font-weight:700}
.hero-stats{
  display:grid;grid-template-columns:repeat(4,1fr);gap:1px;
  background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.07);
  border-radius:8px;overflow:hidden;margin-top:44px;
}
.hstat{background:rgba(255,255,255,0.03);padding:24px 20px;transition:background .2s}
.hstat:hover{background:rgba(255,255,255,0.07)}
.hstat-n{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:40px;font-weight:700;color:white;
  letter-spacing:-1.5px;line-height:1;
}
.hstat-n em{color:#6B9FDB;font-style:normal}
.hstat-l{
  font-family:'Manrope',sans-serif;font-size:11px;font-weight:600;
  letter-spacing:1.5px;text-transform:uppercase;
  color:rgba(255,255,255,0.35);margin-top:6px;
}

/* Contact card */
.ccard{background:white;border-radius:10px;overflow:hidden;box-shadow:0 28px 72px rgba(0,0,0,0.32)}
.ccard-head{background:var(--blue);padding:24px 30px}
.ccard-ht{font-family:'Libre Baskerville',serif;font-size:18px;font-style:italic;color:white}
.ccard-hs{font-family:'Manrope',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-top:3px}
.ccard-body{padding:24px 30px}
.clink{
  display:flex;align-items:center;justify-content:space-between;
  padding:13px 0;border-bottom:1px solid var(--off2);text-decoration:none;
}
.clink:last-of-type{border-bottom:none}
.clink-l{display:flex;flex-direction:column;gap:2px}
.clink-pl{
  font-family:'Manrope',sans-serif;font-size:10px;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;color:var(--slate);
}
.clink-nm{
  font-family:'Manrope',sans-serif;font-size:15px;font-weight:600;
  color:var(--navy);transition:color .12s;
}
.clink:hover .clink-nm{color:var(--blue)}
.clink-ar{font-size:15px;color:var(--silver2);transition:color .12s,transform .15s}
.clink:hover .clink-ar{color:var(--blue);transform:translateX(4px)}
.ccard-dl{
  display:block;text-align:center;background:var(--navy);color:white;
  font-family:'Manrope',sans-serif;font-size:12px;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;
  padding:14px 20px;margin-top:18px;border-radius:6px;text-decoration:none;
  transition:background .15s,transform .15s;
}
.ccard-dl:hover{background:var(--navy2);transform:translateY(-1px)}

/* PAGE SHELL */
.pg{padding:80px 64px 88px;max-width:1280px;margin:0 auto}
.pg-kicker{
  font-family:'Manrope',sans-serif;font-size:11px;font-weight:700;
  letter-spacing:3px;text-transform:uppercase;color:var(--blue);
  margin-bottom:12px;display:flex;align-items:center;gap:14px;
}
.pg-kicker::before{content:'';width:32px;height:2px;background:var(--blue);flex-shrink:0}
.pg-title{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:clamp(38px,4.5vw,60px);font-weight:700;
  color:var(--navy);letter-spacing:-2px;line-height:1.05;margin-bottom:52px;
}
.pg-title em{font-style:italic;font-weight:400;color:var(--blue)}

/* SKILLS */
.skill-wrap{border:1px solid var(--silver);border-radius:8px;overflow:hidden}
.skill-row{
  display:grid;grid-template-columns:190px 1fr;
  border-bottom:1px solid var(--silver);transition:background .15s;
}
.skill-row:last-child{border-bottom:none}
.skill-row:hover{background:var(--blue-lt)}
.skill-cat{
  padding:18px 24px;font-family:'Manrope',sans-serif;
  font-size:12px;font-weight:700;letter-spacing:.5px;
  color:var(--navy);text-transform:uppercase;
  background:var(--off);border-right:1px solid var(--silver);
  display:flex;align-items:center;
}
.skill-vals{padding:16px 20px;display:flex;flex-wrap:wrap;gap:7px;align-items:center}
.sv{
  font-family:'Manrope',sans-serif;font-size:14px;font-weight:500;
  color:var(--navy3);background:white;
  border:1px solid var(--silver);padding:5px 13px;border-radius:4px;
  transition:all .15s;cursor:default;
}
.sv:hover{background:var(--blue);color:white;border-color:var(--blue)}

/* EXPERIENCE */
.exp-item{
  display:grid;grid-template-columns:210px 2px 1fr;
  gap:0 44px;padding:44px 0;border-bottom:1px solid var(--silver);align-items:start;
}
.exp-item:last-child{border-bottom:none}
.exp-date{text-align:right;font-family:'Manrope',sans-serif;font-size:14px;font-weight:600;color:var(--slate);line-height:1.7;padding-top:4px}
.exp-line{background:var(--silver);position:relative;align-self:stretch}
.exp-dot{position:absolute;top:7px;left:-6px;width:13px;height:13px;background:var(--blue);border-radius:50%;border:3px solid white;box-shadow:0 0 0 2px var(--blue)}
.exp-body{padding-left:0}
.exp-role{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:24px;font-weight:700;color:var(--navy);margin-bottom:5px;line-height:1.2;
}
.exp-company{
  font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;
  color:var(--blue);letter-spacing:.5px;margin-bottom:20px;text-transform:uppercase;
}
.exp-list{list-style:none;padding:0}
.exp-list li{
  font-family:'Manrope',sans-serif;font-size:16px;line-height:1.75;
  color:var(--body);padding-left:22px;position:relative;margin-bottom:7px;
}
.exp-list li::before{
  content:'';position:absolute;left:0;top:12px;
  width:6px;height:6px;background:var(--blue);border-radius:50%;
}

/* PROJECTS */
.proj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:22px}
.pcard{
  background:white;border:1px solid var(--silver);border-radius:10px;
  padding:30px;display:flex;flex-direction:column;gap:16px;
  transition:border-color .2s,box-shadow .2s,transform .2s;position:relative;overflow:hidden;
}
.pcard::before{
  content:'';position:absolute;top:0;left:0;width:100%;height:3px;
  background:var(--silver);transition:background .2s;
}
.pcard:hover{border-color:var(--blue);box-shadow:0 10px 36px rgba(26,86,219,0.11);transform:translateY(-3px)}
.pcard:hover::before{background:var(--blue)}
.pcard-num{font-family:'Manrope',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--slate)}
.pcard-title{font-family:'Libre Baskerville',Georgia,serif;font-size:19px;font-weight:700;color:var(--navy);line-height:1.3}
.pcard-desc{font-family:'Manrope',sans-serif;font-size:15px;line-height:1.75;color:var(--body);font-weight:400;flex:1}
.pcard-meta{display:flex;gap:24px;flex-wrap:wrap}
.pm-item{display:flex;flex-direction:column;gap:2px}
.pm-label{font-family:'Manrope',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--slate)}
.pm-val{font-family:'Manrope',sans-serif;font-size:14px;font-weight:600;color:var(--navy3)}
.pcard-tags{display:flex;flex-wrap:wrap;gap:6px;padding-top:12px;border-top:1px solid var(--off2)}
.ptag{font-family:'Manrope',sans-serif;font-size:12px;font-weight:600;color:var(--blue);background:var(--blue-md);padding:4px 10px;border-radius:4px}

/* AWARDS */
.award-tbl{border:1px solid var(--silver);border-radius:8px;overflow:hidden}
.award-row{
  display:grid;grid-template-columns:1fr 120px;gap:0;
  padding:26px 30px;border-bottom:1px solid var(--silver);
  transition:background .15s;align-items:start;
}
.award-row:last-child{border-bottom:none}
.award-row:hover{background:var(--blue-lt)}
.award-title{font-family:'Libre Baskerville',Georgia,serif;font-size:18px;font-weight:700;color:var(--navy);margin-bottom:7px;line-height:1.3}
.award-desc{font-family:'Manrope',sans-serif;font-size:15px;line-height:1.7;color:var(--body);font-weight:400}
.award-yr{font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:var(--blue);text-align:right;padding-top:3px}

/* CERTS */
.cert-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px}
.cert-row{
  display:flex;align-items:center;justify-content:space-between;
  background:white;border:1px solid var(--silver);border-radius:6px;
  padding:17px 22px;transition:border-color .15s,background .15s;
}
.cert-row:hover{border-color:var(--blue);background:var(--blue-lt)}
.cert-name{font-family:'Manrope',sans-serif;font-size:15px;font-weight:600;color:var(--navy);margin-bottom:2px}
.cert-by{font-family:'Manrope',sans-serif;font-size:13px;font-weight:500;color:var(--slate)}
.cert-badge{
  font-family:'Manrope',sans-serif;font-size:11px;font-weight:700;
  color:var(--blue);background:var(--blue-md);padding:4px 11px;border-radius:3px;
  letter-spacing:.3px;white-space:nowrap;flex-shrink:0;margin-left:12px;
}

/* EDUCATION */
.edu-block{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--silver);border-radius:10px;overflow:hidden;max-width:820px}
.edu-left{background:var(--navy);padding:52px 48px}
.edu-yr{font-family:'Libre Baskerville',serif;font-size:88px;font-weight:700;color:rgba(255,255,255,0.06);line-height:1;letter-spacing:-5px}
.edu-deg{font-family:'Libre Baskerville',serif;font-size:27px;font-weight:700;color:white;line-height:1.2;margin-top:-22px;margin-bottom:12px;position:relative;z-index:1}
.edu-school{font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:rgba(255,255,255,0.45);letter-spacing:1px;text-transform:uppercase}
.edu-right{background:var(--off);padding:52px 48px;display:flex;flex-direction:column;justify-content:center;gap:28px}
.edu-item{display:flex;flex-direction:column;gap:4px}
.edu-lbl{font-family:'Manrope',sans-serif;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--slate)}
.edu-val{font-family:'Manrope',sans-serif;font-size:18px;font-weight:700;color:var(--navy)}

/* CHAT */
.chat-pg{padding:80px 64px 88px;max-width:900px;margin:0 auto}
.chat-title{
  font-family:'Libre Baskerville',Georgia,serif;
  font-size:clamp(36px,4.5vw,56px);font-weight:700;
  color:var(--navy);letter-spacing:-2px;line-height:1.05;margin-bottom:10px;
}
.chat-title em{font-style:italic;font-weight:400;color:var(--blue)}
.chat-sub{font-family:'Manrope',sans-serif;font-size:17px;color:var(--slate);font-weight:400;margin-bottom:36px;line-height:1.6}
.chat-window{
  background:var(--off);border:1.5px solid var(--silver);border-radius:14px;
  padding:30px;min-height:380px;max-height:540px;overflow-y:auto;
  margin-bottom:16px;display:flex;flex-direction:column;gap:22px;scroll-behavior:smooth;
}
.chat-empty{
  flex:1;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  text-align:center;padding:48px 24px;gap:14px;
}
.chat-empty-mark{
  font-family:'Libre Baskerville',serif;font-size:52px;
  font-style:italic;color:var(--silver2);font-weight:700;
}
.chat-empty-title{
  font-family:'Libre Baskerville',serif;font-size:24px;
  font-weight:700;color:var(--navy);letter-spacing:-.5px;
}
.chat-empty-sub{
  font-family:'Manrope',sans-serif;font-size:15px;color:var(--slate);
  max-width:380px;line-height:1.65;
}
.chat-pills{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-top:10px}
.chat-pill{
  font-family:'Manrope',sans-serif;font-size:14px;font-weight:600;
  color:var(--blue);background:var(--blue-md);border:1px solid rgba(26,86,219,0.25);
  padding:8px 16px;border-radius:100px;cursor:default;
}
.msg-user{display:flex;justify-content:flex-end}
.msg-ai{display:flex;justify-content:flex-start;align-items:flex-end;gap:12px}
.ai-avatar{
  width:34px;height:34px;background:var(--navy);border-radius:50%;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  font-family:'Libre Baskerville',serif;font-size:14px;font-style:italic;
  color:white;font-weight:700;margin-bottom:2px;
}
.bubble{max-width:78%;padding:15px 20px;border-radius:18px;font-family:'Manrope',sans-serif;font-size:16px;line-height:1.7;font-weight:400}
.bubble-user{background:var(--blue);color:white;border-bottom-right-radius:4px}
.bubble-ai{background:white;color:var(--navy);border:1.5px solid var(--silver);border-bottom-left-radius:4px;box-shadow:0 3px 12px rgba(13,27,46,0.06)}

/* Input overrides */
div[data-testid="stTextInput"] input{
  background:white!important;border:2px solid var(--silver)!important;
  border-radius:12px!important;color:var(--navy)!important;
  font-family:'Manrope',sans-serif!important;font-size:16px!important;
  font-weight:400!important;padding:15px 20px!important;height:54px!important;
}
div[data-testid="stTextInput"] input:focus{
  border-color:var(--blue)!important;
  box-shadow:0 0 0 3px rgba(26,86,219,0.12)!important;outline:none!important;
}
div[data-testid="stTextInput"] input::placeholder{color:var(--silver2)!important;font-weight:400!important}
div[data-testid="stButton"] button{
  background:var(--navy)!important;color:white!important;border:none!important;
  border-radius:12px!important;font-family:'Manrope',sans-serif!important;
  font-size:15px!important;font-weight:700!important;
  padding:15px 28px!important;height:54px!important;
  transition:background .15s,transform .15s!important;letter-spacing:.3px!important;
}
div[data-testid="stButton"] button:hover{background:var(--navy2)!important;transform:translateY(-1px)!important}

/* FOOTER */
.footer{background:var(--navy);padding:52px 64px;display:flex;align-items:center;justify-content:space-between}
.footer-name{font-family:'Libre Baskerville',serif;font-size:24px;font-weight:700;color:white;letter-spacing:-.3px}
.footer-name em{font-style:italic;font-weight:400;color:#7EABD6}
.footer-sub{font-family:'Manrope',sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.3);letter-spacing:1px;text-transform:uppercase;margin-top:5px}
.footer-copy{font-family:'Manrope',sans-serif;font-size:13px;color:rgba(255,255,255,0.28);text-align:right;line-height:2}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "chat" not in st.session_state:
    st.session_state.chat = []

# ══════════════════════════════════════════════════════════════════════════════
#  BRAND BAR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="brand-bar">
  <div class="brand-name">Ashik <em>Roshan I</em></div>
  <div class="brand-links">
    <a class="brand-link" href="https://github.com/AshikRoshan-github" target="_blank">GitHub</a>
    <span class="brand-divider">·</span>
    <a class="brand-link" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn</a>
    <span class="brand-divider">·</span>
    <a class="brand-link" href="https://medium.com/@ashikroshan261" target="_blank">Medium</a>
    <span class="brand-divider">·</span>
    <a class="brand-link" href="mailto:ashikroshan261@gmail.com">Email</a>
    <a class="brand-resume" href="{RESUME_URL}" target="_blank">Resume</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  NAVIGATION — st.radio (WORKING)
# ══════════════════════════════════════════════════════════════════════════════
page = st.radio("", PAGES, horizontal=True, label_visibility="collapsed", key="nav")

# ══════════════════════════════════════════════════════════════════════════════
#  HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    st.markdown(f"""
    <div class="hero">
      <div class="hero-grid">
        <div>
          <p class="hero-kicker rise r1">Data Engineer &amp; AI Engineer — Level 2</p>
          <h1 class="hero-name rise r2">Ashik<br><em>Roshan I</em></h1>
          <p class="hero-subtitle rise r2">Optisol Business Solutions &nbsp;·&nbsp; Madurai, TamilNadu, India</p>
          <div class="hero-rule rise r3"></div>
          <p class="hero-bio rise r3">
            Results-driven engineer with <strong>2+ years</strong> delivering scalable ETL/ELT pipelines,
            enterprise cloud migrations, and production-grade AI automation. Specialising in
            <strong>Snowflake, Azure, AWS, LangChain,</strong> and GenAI agent design — from data warehouse
            migrations to self-healing AI agents and RAG-powered knowledge graphs.
          </p>
          <div class="hero-stats rise r4">
            <div class="hstat"><div class="hstat-n">2<em>+</em></div><div class="hstat-l">Years Experience</div></div>
            <div class="hstat"><div class="hstat-n">14<em>+</em></div><div class="hstat-l">Projects Delivered</div></div>
            <div class="hstat"><div class="hstat-n">7</div><div class="hstat-l">Spot Awards</div></div>
            <div class="hstat"><div class="hstat-n"><em>MVP</em></div><div class="hstat-l">Award 2024–25</div></div>
          </div>
        </div>
        <div class="rise r4">
          <div class="ccard">
            <div class="ccard-head">
              <div class="ccard-ht">Get in Touch</div>
              <div class="ccard-hs">Open to opportunities</div>
            </div>
            <div class="ccard-body">
              <a class="clink" href="mailto:ashikroshan261@gmail.com">
                <div class="clink-l"><span class="clink-pl">Email</span><span class="clink-nm">ashikroshan261@gmail.com</span></div>
                <span class="clink-ar">→</span>
              </a>
              <a class="clink" href="https://github.com/AshikRoshan-github" target="_blank">
                <div class="clink-l"><span class="clink-pl">GitHub</span><span class="clink-nm">AshikRoshan-github</span></div>
                <span class="clink-ar">→</span>
              </a>
              <a class="clink" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">
                <div class="clink-l"><span class="clink-pl">LinkedIn</span><span class="clink-nm">ashik-roshan-i</span></div>
                <span class="clink-ar">→</span>
              </a>
              <a class="clink" href="https://medium.com/@ashikroshan261" target="_blank">
                <div class="clink-l"><span class="clink-pl">Medium</span><span class="clink-nm">@ashikroshan261</span></div>
                <span class="clink-ar">→</span>
              </a>
              <a class="ccard-dl" href="{RESUME_URL}" target="_blank">Download Resume</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SKILLS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Skills":
    st.markdown('<div class="pg rise">', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Arsenal</div><h2 class="pg-title">Technical <em>Skills</em></h2>', unsafe_allow_html=True)
    h = '<div class="skill-wrap">'
    for cat, tags in SKILLS:
        th = "".join(f'<span class="sv">{t}</span>' for t in tags)
        h += f'<div class="skill-row"><div class="skill-cat">{cat}</div><div class="skill-vals">{th}</div></div>'
    st.markdown(h + '</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Experience":
    st.markdown('<div class="pg rise">', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Career</div><h2 class="pg-title">Professional <em>Experience</em></h2>', unsafe_allow_html=True)
    h = ""
    for role, company, start, end, bullets in EXP:
        bl = "".join(f"<li>{b}</li>" for b in bullets)
        h += f"""<div class="exp-item">
          <div class="exp-date">{start}<br>— {end}</div>
          <div class="exp-line"><div class="exp-dot"></div></div>
          <div class="exp-body">
            <div class="exp-role">{role}</div>
            <div class="exp-company">{company}</div>
            <ul class="exp-list">{bl}</ul>
          </div>
        </div>"""
    st.markdown(h, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Projects":
    def proj_grid(projs):
        g = '<div class="proj-grid">'
        for num, title, desc, role, client, tags in projs:
            th = "".join(f'<span class="ptag">{t}</span>' for t in tags)
            g += f"""<div class="pcard">
              <div class="pcard-num">Project {num}</div>
              <div class="pcard-title">{title}</div>
              <div class="pcard-desc">{desc}</div>
              <div class="pcard-meta">
                <div class="pm-item"><span class="pm-label">Role</span><span class="pm-val">{role}</span></div>
                <div class="pm-item"><span class="pm-label">Client</span><span class="pm-val">{client}</span></div>
              </div>
              <div class="pcard-tags">{th}</div>
            </div>"""
        return g + '</div>'

    st.markdown('<div class="pg rise">', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Data Engineering</div><h2 class="pg-title">Data Engineering <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(proj_grid(DE_PROJ), unsafe_allow_html=True)
    st.markdown('<div style="height:68px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">AI &amp; Automation</div><h2 class="pg-title">AI &amp; Automation <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(proj_grid(AI_PROJ), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  AWARDS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Awards":
    st.markdown('<div class="pg rise">', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Recognition</div><h2 class="pg-title">Awards &amp; <em>Achievements</em></h2>', unsafe_allow_html=True)
    h = '<div class="award-tbl">'
    for title, year, desc in AWARDS:
        h += f"""<div class="award-row">
          <div><div class="award-title">{title}</div><div class="award-desc">{desc}</div></div>
          <div class="award-yr">{year}</div>
        </div>"""
    st.markdown(h + '</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:68px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Credentials</div><h2 class="pg-title"><em>Certifications</em></h2>', unsafe_allow_html=True)
    h = '<div class="cert-grid">'
    for name, issuer in CERTS:
        h += f"""<div class="cert-row">
          <div><div class="cert-name">{name}</div><div class="cert-by">{issuer}</div></div>
          <span class="cert-badge">{issuer}</span>
        </div>"""
    st.markdown(h + '</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Education":
    st.markdown('<div class="pg rise">', unsafe_allow_html=True)
    st.markdown('<div class="pg-kicker">Academic Background</div><h2 class="pg-title"><em>Education</em></h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-block">
      <div class="edu-left">
        <div class="edu-yr">2023</div>
        <div class="edu-deg">Bachelor of Engineering in Computer Science</div>
        <div class="edu-school">KLN College of Engineering</div>
      </div>
      <div class="edu-right">
        <div class="edu-item"><span class="edu-lbl">Duration</span><span class="edu-val">2019 – 2023</span></div>
        <div class="edu-item"><span class="edu-lbl">Grade</span><span class="edu-val">A+ — Distinction</span></div>
        <div class="edu-item"><span class="edu-lbl">Specialisation</span><span class="edu-val">Computer Science &amp; Engineering</span></div>
        <div class="edu-item"><span class="edu-lbl">Location</span><span class="edu-val">Tamil Nadu, India</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ASSISTANT (ChatGPT-style)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Assistant":
    st.markdown('<div class="chat-pg rise">', unsafe_allow_html=True)
    st.markdown("""
    <div class="pg-kicker">Portfolio Assistant</div>
    <h2 class="chat-title">Ask me <em>anything</em></h2>
    <p class="chat-sub">I know everything about Ashik — his projects, skills, experience, awards, and more. Try asking a question below.</p>
    """, unsafe_allow_html=True)

    # Chat window
    if not st.session_state.chat:
        st.markdown("""
        <div class="chat-window">
          <div class="chat-empty">
            <div class="chat-empty-mark">A</div>
            <div class="chat-empty-title">Portfolio Assistant</div>
            <div class="chat-empty-sub">Ask me about Ashik's data engineering projects, AI work, skills, certifications, awards, or how to contact him.</div>
            <div class="chat-pills">
              <span class="chat-pill">What projects has Ashik built?</span>
              <span class="chat-pill">What are his top skills?</span>
              <span class="chat-pill">Tell me about the MVP award</span>
              <span class="chat-pill">How can I contact Ashik?</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        bubbles = ""
        for m in st.session_state.chat:
            if m["role"] == "user":
                bubbles += f'<div class="msg-user"><div class="bubble bubble-user">{m["content"]}</div></div>'
            else:
                content = m["content"].replace("\n", "<br>")
                bubbles += f'<div class="msg-ai"><div class="ai-avatar">A</div><div class="bubble bubble-ai">{content}</div></div>'
        st.markdown(f'<div class="chat-window">{bubbles}</div>', unsafe_allow_html=True)

    # Input row
    c1, c2, c3 = st.columns([7, 1, 1])
    with c1:
        user_input = st.text_input("", key="ci", placeholder="Ask about projects, skills, experience, awards…", label_visibility="collapsed")
    with c2:
        send = st.button("Send", key="send", use_container_width=True)
    with c3:
        if st.button("Clear", key="clr", use_container_width=True):
            st.session_state.chat = []
            st.rerun()

    if send and user_input.strip():
        if not GENAI_AVAILABLE:
            st.error("Package `google-genai` is missing. Add it to requirements.txt.")
        else:
            key = None
            try:
                key = st.secrets["GOOGLE"]["Gemini_api_key"]
            except Exception:
                pass
            if not key:
                key = os.environ.get("GEMINI_API_KEY", "")
            if not key:
                st.error("API key not configured. Add `[GOOGLE] Gemini_api_key` to Streamlit Secrets.")
            else:
                st.session_state.chat.append({"role": "user", "content": user_input})
                with st.spinner(""):
                    try:
                        client = google_genai.Client(api_key=key)
                        contents = []
                        for m in st.session_state.chat:
                            r = "user" if m["role"] == "user" else "model"
                            contents.append(google_types.Content(role=r, parts=[google_types.Part.from_text(text=m["content"])]))
                        cfg = google_types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, max_output_tokens=1200)
                        resp = client.models.generate_content(model="gemini-2.5-pro", contents=contents, config=cfg)
                        st.session_state.chat.append({"role": "assistant", "content": resp.text})
                        st.rerun()
                    except Exception as e:
                        st.session_state.chat.append({"role": "assistant", "content": f"I'm having trouble connecting right now. Please try again in a moment."})
                        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-name">Ashik <em>Roshan I</em></div>
    <div class="footer-sub">Data Engineer · AI Engineer · L2</div>
  </div>
  <div class="footer-copy">© 2025 Ashik Roshan I<br>All rights reserved</div>
</div>
""", unsafe_allow_html=True)
