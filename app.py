import streamlit as st

st.set_page_config(
    page_title="Ashik Roshan I — Data & AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Sora:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ─── RESET ─────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── STREAMLIT OVERRIDES ────────────────────────────────────────── */
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }
.stApp { background: #FAFAF8; font-family: 'Plus Jakarta Sans', sans-serif; }

/* ─── CSS VARIABLES ──────────────────────────────────────────────── */
:root {
  --orange:      #F05A00;
  --orange-lt:   #FF7A20;
  --orange-pale: #FEF0E7;
  --orange-mid:  #FDDCC8;
  --black:       #0F0F0F;
  --dark:        #1C1C1C;
  --body:        #3A3A3A;
  --muted:       #7A7A7A;
  --border:      #E8E4DF;
  --white:       #FFFFFF;
  --bg:          #FAFAF8;
  --bg2:         #F5F1EC;
}

/* ─── NAV ────────────────────────────────────────────────────────── */
.nav {
    background: var(--white);
    border-bottom: 1.5px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 64px;
    height: 60px;
    position: sticky;
    top: 0;
    z-index: 100;
}
.nav-brand {
    font-family: 'Sora', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -0.5px;
}
.nav-brand em {
    color: var(--orange);
    font-style: normal;
    display: inline-block;
    width: 8px; height: 8px;
    background: var(--orange);
    border-radius: 50%;
    vertical-align: middle;
    margin-left: 3px;
    margin-bottom: 3px;
}
.nav-links { display: flex; gap: 36px; align-items: center; }
.nav-links a {
    font-size: 12.5px;
    font-weight: 600;
    color: var(--muted);
    text-decoration: none;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    transition: color 0.15s;
}
.nav-links a:hover { color: var(--orange); }

/* ─── HERO ───────────────────────────────────────────────────────── */
.hero-wrap {
    background: var(--white);
    padding: 80px 64px 72px;
    border-bottom: 1.5px solid var(--border);
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--orange-pale);
    color: var(--orange);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 28px;
    border: 1px solid var(--orange-mid);
}
.hero-badge::before { content: ''; width: 7px; height: 7px; background: var(--orange); border-radius: 50%; display: inline-block; animation: pulse 2s infinite; }
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.5; transform: scale(0.8); }
}
.hero-name {
    font-family: 'Sora', sans-serif;
    font-size: clamp(44px, 5.5vw, 72px);
    font-weight: 800;
    color: var(--black);
    line-height: 1.08;
    letter-spacing: -2.5px;
    margin-bottom: 18px;
}
.hero-name span { color: var(--orange); }
.hero-role {
    font-size: 17px;
    font-weight: 400;
    color: var(--muted);
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}
.hero-role strong { color: var(--dark); font-weight: 600; }
.hero-sep { color: var(--orange-mid); }
.hero-bio {
    max-width: 620px;
    font-size: 15.5px;
    line-height: 1.85;
    color: var(--body);
    margin-bottom: 40px;
    font-weight: 400;
}
.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 60px; }
.btn-p {
    background: var(--orange);
    color: white;
    padding: 12px 28px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 700;
    text-decoration: none;
    transition: background 0.15s, transform 0.15s;
    letter-spacing: 0.2px;
}
.btn-p:hover { background: #D94F00; transform: translateY(-1px); }
.btn-s {
    background: transparent;
    color: var(--dark);
    padding: 12px 24px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 600;
    text-decoration: none;
    border: 1.5px solid var(--border);
    transition: border-color 0.15s, color 0.15s;
}
.btn-s:hover { border-color: var(--orange); color: var(--orange); }

/* ─── STATS ROW ──────────────────────────────────────────────────── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    border: 1.5px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    max-width: 760px;
}
.stat-box {
    padding: 20px 24px;
    border-right: 1px solid var(--border);
    text-align: center;
}
.stat-box:last-child { border-right: none; }
.stat-n {
    font-family: 'Sora', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: var(--orange);
    line-height: 1;
    margin-bottom: 4px;
}
.stat-l {
    font-size: 11px;
    color: var(--muted);
    font-weight: 500;
    letter-spacing: 0.3px;
    line-height: 1.3;
}

/* ─── CONTACT BAND ───────────────────────────────────────────────── */
.contact-band {
    background: var(--dark);
    padding: 14px 64px;
    display: flex;
    gap: 0;
    align-items: center;
    flex-wrap: wrap;
}
.c-link {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #AAA;
    font-size: 12.5px;
    text-decoration: none;
    font-weight: 500;
    padding: 6px 20px;
    border-right: 1px solid #333;
    transition: color 0.15s;
    font-family: 'JetBrains Mono', monospace;
}
.c-link:first-child { padding-left: 0; }
.c-link:last-child { border-right: none; }
.c-link:hover { color: var(--orange); }
.c-icon { color: var(--orange); font-size: 13px; }

/* ─── SECTION WRAPPER ────────────────────────────────────────────── */
.sec { padding: 72px 64px; max-width: 1280px; margin: 0 auto; }
.sec-alt { background: var(--bg2); padding: 72px 0; }
.sec-alt .sec { margin: 0 auto; }

.sec-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--orange);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sec-eyebrow::before {
    content: '';
    width: 20px; height: 2px;
    background: var(--orange);
    display: inline-block;
}
.sec-title {
    font-family: 'Sora', sans-serif;
    font-size: clamp(26px, 3vw, 38px);
    font-weight: 800;
    color: var(--black);
    letter-spacing: -1px;
    margin-bottom: 40px;
    line-height: 1.15;
}

/* ─── SKILLS GRID ────────────────────────────────────────────────── */
.skill-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
}
.skill-box {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 20px 22px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.skill-box:hover {
    border-color: var(--orange);
    box-shadow: 0 4px 20px rgba(240,90,0,0.08);
}
.skill-box-label {
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--orange);
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.stag {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--body);
    font-size: 12px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    transition: background 0.15s, color 0.15s, border-color 0.15s;
}
.stag:hover { background: var(--orange-pale); color: var(--orange); border-color: var(--orange-mid); }

/* ─── TIMELINE ───────────────────────────────────────────────────── */
.timeline { display: flex; flex-direction: column; gap: 0; }
.tl-item {
    display: flex;
    gap: 28px;
    padding: 28px 0;
    border-bottom: 1px solid var(--border);
    align-items: flex-start;
}
.tl-item:last-child { border-bottom: none; }
.tl-left {
    flex-shrink: 0;
    width: 160px;
    text-align: right;
}
.tl-date {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    font-weight: 500;
    color: var(--muted);
    background: var(--bg2);
    padding: 5px 10px;
    border-radius: 4px;
    display: inline-block;
    line-height: 1.4;
}
.tl-dot-col {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 6px;
}
.tl-dot {
    width: 12px; height: 12px;
    background: var(--orange);
    border-radius: 50%;
    border: 3px solid var(--white);
    outline: 2px solid var(--orange);
    flex-shrink: 0;
}
.tl-line {
    width: 2px;
    flex: 1;
    background: var(--border);
    margin-top: 6px;
    min-height: 30px;
}
.tl-content { flex: 1; padding-top: 2px; }
.tl-role {
    font-size: 17px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 4px;
}
.tl-company {
    font-size: 13.5px;
    font-weight: 600;
    color: var(--orange);
}

/* ─── PROJECT CARD ───────────────────────────────────────────────── */
.proj-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 20px;
}
.proj-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 10px;
    padding: 26px 28px;
    transition: all 0.2s;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.proj-card:hover {
    border-color: var(--orange);
    box-shadow: 0 8px 32px rgba(240,90,0,0.1);
    transform: translateY(-2px);
}
.proj-header { display: flex; align-items: flex-start; gap: 14px; }
.proj-num-badge {
    background: var(--orange-pale);
    color: var(--orange);
    font-family: 'Sora', sans-serif;
    font-size: 13px;
    font-weight: 800;
    padding: 6px 10px;
    border-radius: 6px;
    flex-shrink: 0;
    border: 1px solid var(--orange-mid);
}
.proj-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--dark);
    line-height: 1.4;
    padding-top: 2px;
}
.proj-meta-row {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.proj-meta-item {
    font-size: 12px;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 4px;
}
.proj-meta-item strong { color: var(--dark); font-weight: 600; }
.proj-desc {
    font-size: 13px;
    line-height: 1.75;
    color: var(--body);
    flex: 1;
}
.proj-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 4px; }
.ptag {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', monospace;
}

/* ─── AWARD CARD ─────────────────────────────────────────────────── */
.award-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
    gap: 16px;
}
.award-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    transition: all 0.2s;
}
.award-card:hover {
    border-color: var(--orange);
    box-shadow: 0 4px 20px rgba(240,90,0,0.07);
}
.award-top { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
.award-icon-wrap {
    font-size: 22px;
    line-height: 1;
    flex-shrink: 0;
}
.award-year-badge {
    background: var(--orange);
    color: white;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    padding: 3px 9px;
    border-radius: 100px;
    white-space: nowrap;
}
.award-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--dark);
    line-height: 1.35;
}
.award-desc {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.65;
}

/* ─── CERT CARD ──────────────────────────────────────────────────── */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
    gap: 14px;
}
.cert-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all 0.2s;
}
.cert-card:hover {
    border-color: var(--orange);
    box-shadow: 0 4px 16px rgba(240,90,0,0.07);
}
.cert-icon-box {
    width: 42px; height: 42px;
    background: var(--orange-pale);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
    border: 1px solid var(--orange-mid);
}
.cert-name {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 3px;
    line-height: 1.3;
}
.cert-by {
    font-size: 11.5px;
    color: var(--orange);
    font-weight: 600;
}

/* ─── EDU CARD ───────────────────────────────────────────────────── */
.edu-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 10px;
    padding: 32px 36px;
    max-width: 560px;
    display: flex;
    gap: 24px;
    align-items: flex-start;
}
.edu-accent {
    width: 4px;
    height: 72px;
    background: linear-gradient(180deg, var(--orange) 0%, var(--orange-mid) 100%);
    border-radius: 4px;
    flex-shrink: 0;
    margin-top: 4px;
}
.edu-degree {
    font-size: 18px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 6px;
    line-height: 1.3;
}
.edu-school {
    font-size: 14px;
    color: var(--orange);
    font-weight: 600;
    margin-bottom: 12px;
}
.edu-chips { display: flex; gap: 8px; flex-wrap: wrap; }
.edu-chip {
    background: var(--orange-pale);
    color: var(--orange);
    font-size: 12px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid var(--orange-mid);
}

/* ─── FOOTER ─────────────────────────────────────────────────────── */
.footer-wrap {
    background: #111;
    padding: 40px 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    border-top: 2px solid var(--orange);
}
.footer-brand {
    font-family: 'Sora', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: white;
}
.footer-brand span { color: var(--orange); }
.footer-links { display: flex; gap: 20px; flex-wrap: wrap; }
.footer-links a {
    color: #888;
    font-size: 12.5px;
    text-decoration: none;
    font-family: 'JetBrains Mono', monospace;
    transition: color 0.15s;
}
.footer-links a:hover { color: var(--orange); }
.footer-copy { color: #555; font-size: 12px; width: 100%; text-align: center; padding-top: 16px; border-top: 1px solid #222; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════
SKILLS = [
    ("Languages",         ["Python", "SQL", "JavaScript", "HTML", "CSS"]),
    ("Cloud – Azure",     ["Blob Storage", "Data Lake", "SQL Database", "Azure OpenAI", "Databricks", "ADF", "Azure VM"]),
    ("Cloud – AWS",       ["S3", "Lambda", "Glue", "Step Functions", "EC2", "CloudWatch", "Textract", "Bedrock"]),
    ("Data Engineering",  ["PySpark", "DBT", "Informatica", "Snowflake", "Pandas", "ADF"]),
    ("Databases",         ["SSMS", "pgAdmin", "MySQL", "Oracle", "SQL Server", "Snowflake"]),
    ("BI & Analytics",    ["Power BI", "ThoughtSpot", "Plotly", "Streamlit"]),
    ("AI & GenAI",        ["Azure OpenAI", "Amazon Bedrock", "Gemini 2.5 Pro", "LangChain", "Neo4j", "RAG", "Prompt Engineering", "Azure Document Intelligence"]),
    ("Automation & Web",  ["Selenium", "Web Scraping", "FastAPI", "PyAutoGUI", "Apify", "Flask"]),
    ("DevOps & Tools",    ["GitHub", "Azure DevOps", "CI/CD", "PuTTY", "ServiceNow", "Rally", "SharePoint"]),
    ("Libraries",         ["asyncio", "PyVis", "PyPDF2", "pyodbc", "Snowflake Connector", "xmltodict", "smtplib"]),
]

EXPERIENCE = [
    ("Data Engineer – L2",          "Optisol Business Solutions", "Apr 2025 – Present"),
    ("Data Engineer – L1",          "Optisol Business Solutions", "Aug 2024 – Mar 2025"),
    ("Data Engineer Intern – L0",   "Optisol Business Solutions", "Mar 2024 – Jul 2024"),
    ("Trainee – Software Engineer", "Blue Cloud",                 "Jun 2023 – Mar 2024"),
]

DE_PROJECTS = [
    ("#1", "Python-Based Data Migration: Google Sheets → Azure SQL",
     "Data Engineer", "Internal Team | Optisol",
     ["Python", "Pandas", "gspread", "pyodbc", "Azure SQL", "Azure VM", "Cron Jobs"],
     "Built a cost-effective ETL solution to extract structured data from Google Sheets and load into Azure SQL Database with full and incremental load logic, data validation, and automated scheduling."),
    ("#2", "On-Premises to Snowflake Data Warehouse Migration",
     "Data Engineer", "Republic Services | Optisol",
     ["Snowflake", "Informatica", "dbt", "Oracle", "SQL Server", "AWS Step Functions", "CloudWatch"],
     "Led migration of 6 on-premises source systems to Snowflake cloud DWH with automated AWS Step Functions orchestration, CloudWatch monitoring, and GitHub CI/CD for dbt pipelines."),
    ("#3", "Enterprise DB Migration: Oracle → SQL Server (On-Prem)",
     "Data Engineer", "Republic Services | Optisol",
     ["Oracle", "SQL Server", "Python", "Autogen", "T-SQL", "ServiceNow", "GitHub"],
     "Used the internal Autogen ETL framework to automate schema conversion and data migration from Oracle to SQL Server across RAW → Staging → Mirror → Test → Production environments."),
    ("#4", "API-Driven Data Migration: Podio → Azure SQL Database",
     "Data Engineer", "Jiffy – Cultural Exchange | Optisol",
     ["Python", "REST API", "Pandas", "ADF", "Azure SQL", "Azure Blob", "AzCopy"],
     "Extracted Podio data via REST API, transformed with ADF pipelines, and high-performance bulk-loaded into Azure SQL with pyodbc fast_executemany and AzCopy for document migration."),
]

AI_PROJECTS = [
    ("#1", "Automated Web Data Extraction & Reporting Platform",
     "Automation Engineer", "IBEAM | Optisol",
     ["Selenium", "PyAutoGUI", "smtplib", "Azure DevOps"],
     "End-to-end browser automation for web data extraction, file processing, report generation, and automated SMTP email distribution with scheduled unattended execution."),
    ("#2", "AI-Driven Web Scraping with LangChain & Apify",
     "Automation Engineer", "IBEAM | Optisol",
     ["Python", "LangChain", "Apify", "REST APIs"],
     "Integrated Apify cloud Actors with LangChain to enable scalable AI-powered web crawling, transforming scraped content into structured LLM-ready documents."),
    ("#3", "AI-Powered Automated Data Profiling Platform",
     "Data & AI Engineer", "IBEAM | Optisol",
     ["Azure OpenAI", "Snowflake", "Streamlit", "Prompt Engineering"],
     "Multi-source data profiling platform generating AI-driven anomaly detection, quality insights, and visual dashboards via Azure OpenAI and Streamlit."),
    ("#4", "AI Pandas Agent — Self-Healing Code Generation",
     "Data & AI Engineer", "IBEAM | Optisol",
     ["Azure OpenAI", "Pandas", "Python", "Prompt Engineering"],
     "Natural-language-to-Pandas-code agent with a self-healing loop: detects runtime errors, re-prompts the LLM with the exception context, and auto-regenerates corrected code."),
    ("#5", "Ontology Kit – Data Mapping Agent",
     "Data & AI Engineer", "IBEAM | Optisol",
     ["Gemini 2.5 Pro", "Streamlit", "Pandas", "PyODBC"],
     "AI-driven ontology tool automating source-to-destination data mapping with 40–50% reduction in manual effort, including auto-generated metadata and sample data integration."),
    ("#6", "AI Document Processing & Structured Data Extraction",
     "AI Engineer", "Republic Services Hackathon | Optisol",
     ["AWS Textract", "Amazon Bedrock", "EC2", "S3", "Flask"],
     "Converted scanned PDFs and images to structured JSON using Textract for extraction and Bedrock for semantic structuring; REST API on EC2 for orchestration."),
    ("#7", "Internationalization HTML Validation Tool",
     "AI / Data Engineer", "Optisol",
     ["Python", "HTML Parsing", "i18n", "JSON", "CLI"],
     "Analyzed HTML files for i18n readiness, flagged hard-coded strings and missing translation keys, and generated structured JSON reports to streamline multilingual UI workflows."),
    ("#8", "Automated Internationalization Workflow",
     "Automation Engineer", "IBEAM | Optisol",
     ["Python", "i18n", "JSON", "Batch Processing", "CI/CD"],
     "Automation framework for managing i18n locale files across languages — validates keys, syncs translations, and integrates into CI/CD pipelines for continuous quality."),
    ("#9", "Credit Risk Reporting & JSON Intelligence Platform",
     "Data & AI Engineer", "Atradius – Trade Credit | Optisol",
     ["Gemini 2.5 Pro", "asyncio", "Plotly", "JSON", "CLI"],
     "Automated JSON pipeline mapping 40+ credit risk blocks with custom async rate limiter, token-bucket algorithm, section-based LLM prompting, and asyncio.gather for high throughput."),
    ("#10", "Knowledge Graph Builder (KGB) with RAG",
     "Data & AI Engineer", "Internal Platform | Optisol",
     ["LangChain", "Azure OpenAI", "Neo4j", "PyVis", "Streamlit", "asyncio"],
     "Full-stack app transforming PDFs, DOCX, JSON, XML, and SQL data into interactive knowledge graphs with Neo4j persistence, GraphCypherQAChain, RAG query layer, and PyVis visualisation."),
]

AWARDS = [
    ("🏆", "Most Valuable Person (MVP) Award", "2024–2025",
     "Highest organizational honor for consistent performance excellence, cross-functional leadership, and long-term business contribution."),
    ("⭐", "Spot Award – Project Excellence & Leadership", "Jan 2026",
     "Awarded by the CTO for mature project handling and fostering a culture of colleague recognition."),
    ("⭐", "Spot Award – RS ARP Project Go-Live", "Nov 2025",
     "Exceptional contribution to the 'Beatty Go-Live' rollout and complex 'Delta Load' activities under tight timelines."),
    ("⭐", "Spot Award – AI Tool Innovation (NotebookLLM)", "May 2025",
     "Evaluated, demoed, and drove team adoption of NotebookLLM to enhance project efficiency."),
    ("⭐", "Spot Award – Community Mentorship", "Mar 2025",
     "Delivered technical sessions for college students on interview preparation and emerging technologies."),
    ("⭐", "OKR Top Contributor (Q4)", "Oct–Dec 2024",
     "Pivotal role in attaining company-wide Objectives and Key Results (OKRs)."),
    ("⭐", "Spot Award – Client Excellence (Ontology Mapping)", "Dec 2024",
     "High praise from client for a solution-oriented Ontology Mapping presentation during an on-site visit."),
    ("⭐", "Spot Award – Gen AI & Automation", "Jul 2024",
     "Implemented GenAI-based data inventory automation and served as SME resolving DBT blockers."),
]

CERTS = [
    ("❄️", "SnowPro Core Certification",                    "Snowflake"),
    ("☁️", "Azure Data Fundamentals (DP-900)",               "Microsoft"),
    ("🧱", "Databricks Lakehouse Fundamentals",              "Databricks"),
    ("🤖", "Generative AI Fundamentals Accreditation",       "Databricks"),
    ("🔧", "dbt Learn Fundamentals",                         "dbt Labs"),
    ("💾", "SQL (Basic) Certificate",                        "HackerRank"),
    ("🐍", "100 Days of Code: Python Pro Bootcamp",          "Udemy"),
    ("❄️", "Snowflake Masterclass",                          "Udemy"),
]


# ══════════════════════════════════════════════════════════════════════════════
#  RENDER HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def skill_grid():
    cards = ""
    for cat, tags in SKILLS:
        tag_html = "".join(f'<span class="stag">{t}</span>' for t in tags)
        cards += f'<div class="skill-box"><div class="skill-box-label">{cat}</div><div class="skill-tags">{tag_html}</div></div>'
    return f'<div class="skill-grid">{cards}</div>'

def project_grid(projects):
    cards = ""
    for num, title, role, client, tech, desc in projects:
        tags = "".join(f'<span class="ptag">{t}</span>' for t in tech)
        cards += f"""
        <div class="proj-card">
          <div class="proj-header">
            <div class="proj-num-badge">{num}</div>
            <div class="proj-title">{title}</div>
          </div>
          <div class="proj-meta-row">
            <div class="proj-meta-item"><strong>Role:</strong> {role}</div>
            <div class="proj-meta-item"><strong>Client:</strong> {client}</div>
          </div>
          <div class="proj-desc">{desc}</div>
          <div class="proj-tags">{tags}</div>
        </div>"""
    return f'<div class="proj-grid">{cards}</div>'


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE RENDER
# ══════════════════════════════════════════════════════════════════════════════

# ── NAV
st.markdown("""
<div class="nav">
  <div class="nav-brand">Ashik Roshan<em></em></div>
  <div class="nav-links">
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#awards">Awards</a>
    <a href="#certifications">Certifications</a>
    <a href="#education">Education</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── HERO
st.markdown("""
<div class="hero-wrap">
  <div class="sec" style="padding-bottom:0;">
    <div class="hero-badge">🟢 &nbsp; Open to Opportunities</div>
    <h1 class="hero-name">Ashik Roshan <span>I</span></h1>
    <p class="hero-role">
      <strong>Data Engineer – L2</strong>
      <span class="hero-sep">·</span>
      AI Engineer
      <span class="hero-sep">·</span>
      Optisol Business Solutions
    </p>
    <p class="hero-bio">
      Results-driven Data & AI Engineer with 2+ years delivering scalable ETL/ELT pipelines, 
      enterprise cloud migrations, and production-grade AI automation. 
      I work at the intersection of data engineering and generative AI — 
      from Snowflake migrations to self-healing AI agents and RAG-powered knowledge graphs.
    </p>
    <div class="hero-actions">
      <a href="mailto:ashikroshan261@gmail.com" class="btn-p">✉&nbsp; Get in Touch</a>
      <a href="https://github.com/AshikRoshan-github" target="_blank" class="btn-s">GitHub ↗</a>
      <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank" class="btn-s">LinkedIn ↗</a>
      <a href="https://medium.com/@ashikroshan261" target="_blank" class="btn-s">Medium ↗</a>
    </div>
    <div class="stats-row">
      <div class="stat-box"><div class="stat-n">2+</div><div class="stat-l">Years Exp.</div></div>
      <div class="stat-box"><div class="stat-n">14+</div><div class="stat-l">Projects</div></div>
      <div class="stat-box"><div class="stat-n">7</div><div class="stat-l">Spot Awards</div></div>
      <div class="stat-box"><div class="stat-n">MVP</div><div class="stat-l">2024–25</div></div>
      <div class="stat-box"><div class="stat-n">8</div><div class="stat-l">Certs</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT BAND
st.markdown("""
<div class="contact-band">
  <a href="mailto:ashikroshan261@gmail.com" class="c-link"><span class="c-icon">✉</span>ashikroshan261@gmail.com</a>
  <a href="https://github.com/AshikRoshan-github" target="_blank" class="c-link"><span class="c-icon">⌥</span>github.com/AshikRoshan-github</a>
  <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank" class="c-link"><span class="c-icon">in</span>linkedin.com/in/ashik-roshan-i</a>
  <a href="https://medium.com/@ashikroshan261" target="_blank" class="c-link"><span class="c-icon">✍</span>medium.com/@ashikroshan261</a>
</div>
""", unsafe_allow_html=True)

# ── SKILLS
st.markdown('<div id="skills" class="sec-alt"><div class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">What I Work With</div><h2 class="sec-title">Technical Skills</h2>', unsafe_allow_html=True)
st.markdown(skill_grid(), unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── EXPERIENCE
st.markdown('<div id="experience" class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Career Journey</div><h2 class="sec-title">Professional Experience</h2>', unsafe_allow_html=True)
tl = '<div class="timeline">'
for i, (role, company, date) in enumerate(EXPERIENCE):
    tl += f"""
    <div class="tl-item">
      <div class="tl-left"><span class="tl-date">{date}</span></div>
      <div class="tl-dot-col">
        <div class="tl-dot"></div>
        {'<div class="tl-line"></div>' if i < len(EXPERIENCE)-1 else ''}
      </div>
      <div class="tl-content">
        <div class="tl-role">{role}</div>
        <div class="tl-company">{company}</div>
      </div>
    </div>"""
tl += '</div>'
st.markdown(tl, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── DATA ENGINEERING PROJECTS
st.markdown('<div id="projects" class="sec-alt"><div class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Data Engineering</div><h2 class="sec-title">Data Engineering Projects</h2>', unsafe_allow_html=True)
st.markdown(project_grid(DE_PROJECTS), unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── AI & AUTOMATION PROJECTS
st.markdown('<div class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">AI & Automation</div><h2 class="sec-title">AI & Automation Projects</h2>', unsafe_allow_html=True)
st.markdown(project_grid(AI_PROJECTS), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── AWARDS
st.markdown('<div id="awards" class="sec-alt"><div class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Recognition</div><h2 class="sec-title">Awards & Achievements</h2>', unsafe_allow_html=True)
award_html = '<div class="award-grid">'
for icon, title, year, desc in AWARDS:
    award_html += f"""
    <div class="award-card">
      <div class="award-top">
        <div style="display:flex;align-items:center;gap:10px;">
          <span class="award-icon-wrap">{icon}</span>
          <span class="award-year-badge">{year}</span>
        </div>
      </div>
      <div class="award-title">{title}</div>
      <div class="award-desc">{desc}</div>
    </div>"""
award_html += "</div>"
st.markdown(award_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── CERTIFICATIONS
st.markdown('<div id="certifications" class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Credentials</div><h2 class="sec-title">Certifications</h2>', unsafe_allow_html=True)
cert_html = '<div class="cert-grid">'
for icon, name, issuer in CERTS:
    cert_html += f"""
    <div class="cert-card">
      <div class="cert-icon-box">{icon}</div>
      <div>
        <div class="cert-name">{name}</div>
        <div class="cert-by">{issuer}</div>
      </div>
    </div>"""
cert_html += "</div>"
st.markdown(cert_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION
st.markdown('<div id="education" class="sec-alt"><div class="sec">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">Academic Background</div><h2 class="sec-title">Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="edu-card">
  <div class="edu-accent"></div>
  <div>
    <div class="edu-degree">Bachelor of Engineering<br>in Computer Science</div>
    <div class="edu-school">KLN College of Engineering</div>
    <div class="edu-chips">
      <span class="edu-chip">2019 – 2023</span>
      <span class="edu-chip">Grade: A+</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── FOOTER
st.markdown("""
<div class="footer-wrap">
  <div class="footer-brand">Ashik Roshan <span>I</span></div>
  <div class="footer-links">
    <a href="mailto:ashikroshan261@gmail.com">ashikroshan261@gmail.com</a>
    <a href="https://github.com/AshikRoshan-github" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">LinkedIn</a>
    <a href="https://medium.com/@ashikroshan261" target="_blank">Medium</a>
  </div>
  <div class="footer-copy">Built with Streamlit &nbsp;·&nbsp; © 2025 Ashik Roshan I &nbsp;·&nbsp; Data Engineer & AI Engineer</div>
</div>
""", unsafe_allow_html=True)
