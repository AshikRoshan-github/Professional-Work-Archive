import streamlit as st

st.set_page_config(
    page_title="Ashik Roshan I — Data & AI Engineer",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

:root {
  --bg:         #0E0E0E;
  --bg1:        #141414;
  --bg2:        #1A1A1A;
  --bg3:        #222222;
  --border:     #2C2C2C;
  --border2:    #383838;
  --white:      #F4F0EB;
  --white2:     #C8C0B8;
  --muted:      #787060;
  --orange:     #FF5C00;
  --orange2:    #FF8040;
  --orange-dim: rgba(255,92,0,0.12);
  --orange-glow:rgba(255,92,0,0.06);
}

.stApp {
  background: var(--bg);
  font-family: 'Outfit', sans-serif;
  color: var(--white);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.fade { animation: fadeUp 0.6s ease both; }
.fade-1 { animation-delay: 0.05s; }
.fade-2 { animation-delay: 0.15s; }
.fade-3 { animation-delay: 0.25s; }
.fade-4 { animation-delay: 0.35s; }

/* ══ NAV ══ */
.nav {
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 72px;
  height: 62px;
  position: sticky;
  top: 0;
  z-index: 200;
}
.nav-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 13px;
  font-weight: 500;
  color: var(--white);
  letter-spacing: 0.5px;
}
.nav-logo-mark {
  width: 28px; height: 28px;
  background: var(--orange);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 700;
  color: white;
  border-radius: 4px;
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
}
.nav-right { display: flex; align-items: center; gap: 0; }
.nav-right a {
  font-size: 11.5px;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  letter-spacing: 1px;
  text-transform: uppercase;
  padding: 0 18px;
  height: 62px;
  display: flex;
  align-items: center;
  border-left: 1px solid var(--border);
  transition: color 0.15s, background 0.15s;
}
.nav-right a:hover { color: var(--orange); background: var(--orange-glow); }
.nav-resume {
  font-size: 11.5px !important;
  font-weight: 600 !important;
  color: var(--orange) !important;
  gap: 5px;
}
.nav-resume:hover { background: var(--orange-dim) !important; }

/* ══ HERO ══ */
.hero {
  background: var(--bg1);
  padding: 96px 72px 80px;
  border-bottom: 1px solid var(--border);
  position: relative;
  overflow: hidden;
}
.hero::after {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 480px; height: 480px;
  background: conic-gradient(from 200deg at 100% 0%, var(--orange-dim) 0deg, transparent 80deg);
  pointer-events: none;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, var(--border) 1px, transparent 1px);
  background-size: 36px 36px;
  opacity: 0.35;
  pointer-events: none;
}
.hero-inner { position: relative; z-index: 2; max-width: 1160px; }
.hero-label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 32px;
}
.hero-label::before { content: ''; width: 32px; height: 1px; background: var(--orange); display: inline-block; }
.hero-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(64px, 8vw, 112px);
  font-weight: 300;
  line-height: 0.92;
  letter-spacing: -3px;
  color: var(--white);
  margin-bottom: 6px;
}
.hero-name-last { font-style: italic; color: var(--orange); }
.hero-name-sub {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(20px, 3vw, 34px);
  font-weight: 300;
  font-style: italic;
  color: var(--muted);
  letter-spacing: -0.5px;
  margin-bottom: 36px;
}
.hero-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, var(--orange) 0%, var(--border) 40%, transparent 100%);
  margin-bottom: 36px;
}
.hero-bottom { display: grid; grid-template-columns: 1fr auto; gap: 48px; align-items: end; }
.hero-bio { font-size: 16px; line-height: 1.85; color: var(--white2); font-weight: 300; max-width: 600px; }
.hero-bio strong { color: var(--white); font-weight: 600; }
.hero-meta { text-align: right; }
.hero-meta-item {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.5px;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: flex-end;
}
.hero-meta-item a { color: var(--white2); text-decoration: none; transition: color 0.15s; }
.hero-meta-item a:hover { color: var(--orange); }
.hero-dot { color: var(--orange); }

/* Buttons */
.btn-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 36px; }
.btn-a {
  background: var(--orange); color: white;
  font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 600;
  padding: 11px 26px; border-radius: 3px; text-decoration: none; letter-spacing: 0.3px;
  transition: background 0.15s, transform 0.15s; display: inline-block;
}
.btn-a:hover { background: #E04D00; transform: translateY(-1px); }
.btn-b {
  background: transparent; color: var(--white2);
  font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 500;
  padding: 10px 22px; border-radius: 3px; text-decoration: none;
  border: 1px solid var(--border2); transition: border-color 0.15s, color 0.15s; display: inline-block;
}
.btn-b:hover { border-color: var(--orange); color: var(--orange); }
.btn-resume {
  background: var(--orange-dim); color: var(--orange);
  font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 600;
  padding: 10px 22px; border-radius: 3px; text-decoration: none;
  border: 1px solid rgba(255,92,0,0.3);
  transition: background 0.15s, transform 0.15s;
  display: inline-flex; align-items: center; gap: 6px;
}
.btn-resume:hover { background: rgba(255,92,0,0.2); transform: translateY(-1px); }

/* Stats strip */
.stats-strip {
  background: var(--bg2); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
  display: grid; grid-template-columns: repeat(5, 1fr);
}
.stat-cell { padding: 24px 28px; border-right: 1px solid var(--border); display: flex; flex-direction: column; gap: 4px; }
.stat-cell:last-child { border-right: none; }
.stat-val { font-family: 'Cormorant Garamond', serif; font-size: 42px; font-weight: 600; color: var(--white); line-height: 1; letter-spacing: -1px; }
.stat-val em { color: var(--orange); font-style: normal; }
.stat-key { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); }

/* Sections */
.section { padding: 80px 72px; max-width: 1300px; margin: 0 auto; }
.section-dark { background: var(--bg1); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.section-dark .section { margin: 0 auto; }
.s-label { font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; font-weight: 500; letter-spacing: 2.5px; text-transform: uppercase; color: var(--orange); margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
.s-label::after { content: ''; flex: 0 0 24px; height: 1px; background: var(--orange); }
.s-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 4vw, 52px); font-weight: 300; color: var(--white); letter-spacing: -1.5px; margin-bottom: 48px; line-height: 1.1; }
.s-title em { font-style: italic; color: var(--orange); }

/* Skills */
.skill-table { display: grid; grid-template-columns: repeat(2, 1fr); border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
.skill-cell { padding: 18px 24px; border-bottom: 1px solid var(--border); border-right: 1px solid var(--border); display: flex; gap: 14px; align-items: flex-start; transition: background 0.2s; }
.skill-cell:hover { background: var(--orange-glow); }
.skill-cell:nth-child(even) { border-right: none; }
.skill-cell:nth-last-child(-n+2) { border-bottom: none; }
.skill-label { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--orange); min-width: 110px; padding-top: 4px; flex-shrink: 0; }
.skill-vals { display: flex; flex-wrap: wrap; gap: 5px; }
.sv { background: var(--bg3); color: var(--white2); font-size: 12px; font-weight: 400; padding: 3px 9px; border-radius: 3px; font-family: 'IBM Plex Mono', monospace; border: 1px solid var(--border2); transition: border-color 0.15s, color 0.15s; }
.sv:hover { border-color: var(--orange); color: var(--white); }

/* Experience */
.exp-list { display: flex; flex-direction: column; }
.exp-item { display: grid; grid-template-columns: 200px 1px 1fr; gap: 0 32px; padding: 32px 0; border-bottom: 1px solid var(--border); align-items: start; }
.exp-item:last-child { border-bottom: none; }
.exp-date-col { text-align: right; padding-top: 4px; }
.exp-date { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--muted); line-height: 1.6; }
.exp-line { background: var(--border2); width: 1px; align-self: stretch; position: relative; }
.exp-line::before { content: ''; position: absolute; top: 6px; left: -4px; width: 9px; height: 9px; background: var(--orange); border-radius: 50%; }
.exp-body { padding-left: 8px; }
.exp-role { font-size: 19px; font-weight: 600; color: var(--white); margin-bottom: 4px; line-height: 1.3; }
.exp-company { font-size: 13px; color: var(--orange); font-weight: 500; font-family: 'IBM Plex Mono', monospace; }

/* Project cards */
.proj-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(380px, 1fr)); gap: 1px; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; background: var(--border); }
.pcard { background: var(--bg1); padding: 28px 30px; display: flex; flex-direction: column; gap: 14px; transition: background 0.2s; cursor: default; }
.pcard:hover { background: var(--bg2); }
.pcard-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.pcard-num { font-family: 'Cormorant Garamond', serif; font-size: 13px; font-weight: 600; color: var(--orange); background: var(--orange-dim); padding: 3px 8px; border-radius: 3px; border: 1px solid rgba(255,92,0,0.25); flex-shrink: 0; font-style: italic; }
.pcard-title { font-size: 14.5px; font-weight: 600; color: var(--white); line-height: 1.45; flex: 1; }
.pcard-meta { display: flex; flex-wrap: wrap; gap: 14px; }
.pcard-meta-item { font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; color: var(--muted); display: flex; gap: 5px; }
.pcard-meta-item span { color: var(--white2); }
.pcard-desc { font-size: 13px; line-height: 1.75; color: var(--white2); font-weight: 300; flex: 1; }
.pcard-tags { display: flex; flex-wrap: wrap; gap: 5px; padding-top: 6px; border-top: 1px solid var(--border); }
.ptag { font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; color: var(--muted); background: var(--bg3); padding: 3px 7px; border-radius: 2px; }

/* Awards */
.award-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
.acard { background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 24px 26px; display: flex; flex-direction: column; gap: 10px; transition: border-color 0.2s, background 0.2s; position: relative; overflow: hidden; }
.acard::before { content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%; background: var(--border2); transition: background 0.2s; }
.acard:hover { border-color: var(--border2); background: var(--bg3); }
.acard:hover::before { background: var(--orange); }
.acard-top { display: flex; align-items: center; justify-content: space-between; }
.acard-icon { font-size: 20px; line-height: 1; }
.acard-year { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 1px; color: var(--orange); background: var(--orange-dim); padding: 3px 8px; border-radius: 100px; border: 1px solid rgba(255,92,0,0.2); }
.acard-title { font-size: 14px; font-weight: 600; color: var(--white); line-height: 1.4; }
.acard-desc { font-size: 12.5px; color: var(--muted); line-height: 1.65; font-weight: 300; }

/* Certs */
.cert-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }
.ccard { background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; transition: border-color 0.2s; }
.ccard:hover { border-color: var(--orange); }
.ccard-icon { width: 40px; height: 40px; background: var(--bg3); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; border: 1px solid var(--border2); }
.ccard-name { font-size: 13px; font-weight: 600; color: var(--white); margin-bottom: 3px; line-height: 1.35; }
.ccard-by { font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; color: var(--orange); }

/* Education */
.edu-wrap { display: flex; gap: 48px; align-items: stretch; max-width: 700px; }
.edu-year-col { display: flex; flex-direction: column; align-items: center; gap: 8px; padding-top: 6px; }
.edu-year-label { font-family: 'Cormorant Garamond', serif; font-size: 52px; font-weight: 300; color: var(--border2); line-height: 1; letter-spacing: -2px; }
.edu-year-line { flex: 1; width: 1px; background: var(--border); }
.edu-card-body { flex: 1; background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 28px 30px; }
.edu-degree { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 600; color: var(--white); line-height: 1.25; margin-bottom: 8px; }
.edu-school { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: var(--orange); margin-bottom: 18px; letter-spacing: 0.5px; }
.edu-chips { display: flex; gap: 8px; }
.edu-chip { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: var(--white2); background: var(--bg3); border: 1px solid var(--border2); padding: 4px 10px; border-radius: 3px; }

/* Footer — simplified, no repeated social links */
.footer {
  background: var(--bg1);
  border-top: 1px solid var(--border);
  padding: 48px 72px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: center;
}
.footer-name { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 300; font-style: italic; color: var(--white); margin-bottom: 6px; }
.footer-sub { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: var(--muted); letter-spacing: 1.5px; text-transform: uppercase; }
.footer-copy { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: var(--muted); line-height: 1.8; text-align: right; }
.footer-copy span { color: var(--orange); }
</style>
""", unsafe_allow_html=True)

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
    ("Data Engineer — L2",           "Optisol Business Solutions", "Apr 2025\n— Present"),
    ("Data Engineer — L1",           "Optisol Business Solutions", "Aug 2024\n— Mar 2025"),
    ("Data Engineer Intern — L0",    "Optisol Business Solutions", "Mar 2024\n— Jul 2024"),
    ("Trainee — Software Engineer",  "Blue Cloud",                 "Jun 2023\n— Mar 2024"),
]

DE_PROJ = [
    ("#1", "Python-Based Data Migration: Google Sheets → Azure SQL",
     "Data Engineer", "Internal | Optisol",
     ["Python", "Pandas", "gspread", "pyodbc", "Azure SQL", "Azure VM", "Cron Jobs"],
     "Cost-effective ETL extracting Google Sheets data into Azure SQL Database with full & incremental load logic, Pandas transformation, and Cron-scheduled automation."),
    ("#2", "On-Premises → Snowflake Data Warehouse Migration",
     "Data Engineer", "Republic Services | Optisol",
     ["Snowflake", "Informatica", "dbt", "Oracle", "SQL Server", "AWS Step Functions", "CloudWatch"],
     "Led migration of 6 on-premises source systems to Snowflake DWH with automated AWS orchestration, CloudWatch monitoring, and dbt ELT transformations via GitHub CI/CD."),
    ("#3", "Enterprise DB Migration: Oracle → SQL Server (On-Prem)",
     "Data Engineer", "Republic Services | Optisol",
     ["Oracle", "SQL Server", "Autogen ETL", "T-SQL", "ServiceNow"],
     "Used the internal Autogen ETL framework to automate schema conversion across RAW → Staging → Mirror → Test → Production with ServiceNow change management."),
    ("#4", "API-Driven Migration: Podio → Azure SQL Database",
     "Data Engineer", "Jiffy — Cultural Exchange | Optisol",
     ["Python", "REST API", "Pandas", "ADF", "Azure SQL", "Azure Blob", "AzCopy"],
     "REST API extraction from Podio, ADF pipeline transformation, and high-performance bulk-load into Azure SQL using pyodbc fast_executemany with AzCopy document migration."),
]

AI_PROJ = [
    ("#1", "Automated Web Data Extraction & Reporting Platform",
     "Automation Eng.", "IBEAM | Optisol",
     ["Selenium", "PyAutoGUI", "smtplib", "Azure DevOps"],
     "Browser automation for web extraction, file processing, structured report generation, and automated SMTP distribution — fully unattended scheduled execution."),
    ("#2", "AI-Driven Web Scraping — LangChain & Apify",
     "Automation Eng.", "IBEAM | Optisol",
     ["Python", "LangChain", "Apify", "REST APIs"],
     "Apify cloud Actors integrated with LangChain to enable scalable AI-powered crawling, transforming scraped content into LLM-ready structured documents."),
    ("#3", "AI-Powered Automated Data Profiling Platform",
     "Data & AI Eng.", "IBEAM | Optisol",
     ["Azure OpenAI", "Snowflake", "Streamlit", "Prompt Engineering"],
     "Multi-source profiling platform generating AI-driven anomaly detection, quality insights, and interactive Streamlit dashboards via Azure OpenAI."),
    ("#4", "AI Pandas Agent — Self-Healing Code Generation",
     "Data & AI Eng.", "IBEAM | Optisol",
     ["Azure OpenAI", "Pandas", "Python"],
     "Natural-language-to-Pandas-code agent with self-healing loop: catches runtime errors, sends exception context to LLM, auto-regenerates corrected transformation code."),
    ("#5", "Ontology Kit — Data Mapping Agent",
     "Data & AI Eng.", "IBEAM | Optisol",
     ["Gemini 2.5 Pro", "Streamlit", "Pandas", "PyODBC"],
     "AI-driven ontology mapping tool reducing manual effort 40–50% with protocol-based domain understanding, auto-generated metadata, and sample data integration."),
    ("#6", "AI Document Processing & Structured Data Extraction",
     "AI Engineer", "RS Hackathon | Optisol",
     ["AWS Textract", "Amazon Bedrock", "EC2", "S3", "Flask"],
     "Scanned PDFs/images → structured JSON pipeline: Textract for extraction, Bedrock for semantic structuring, Flask REST API on EC2 for orchestration."),
    ("#7", "Internationalization HTML Validation Tool",
     "AI/Data Eng.", "Optisol",
     ["Python", "HTML Parsing", "i18n", "JSON"],
     "Analyzes HTML for i18n readiness, detects hard-coded strings, flags missing translations, generates JSON reports — cutting manual inspection effort significantly."),
    ("#8", "Automated Internationalization Workflow",
     "Automation Eng.", "IBEAM | Optisol",
     ["Python", "i18n", "Batch Processing", "CI/CD"],
     "Framework managing i18n locale files across languages — validates keys, syncs translations, integrates into CI/CD for continuous multilingual quality."),
    ("#9", "Credit Risk Reporting & JSON Intelligence Platform",
     "Data & AI Eng.", "Atradius | Optisol",
     ["Gemini 2.5 Pro", "asyncio", "Plotly", "JSON"],
     "Automated pipeline mapping 40+ credit risk blocks with async rate limiter (token-bucket algorithm), section-based LLM prompting, and asyncio.gather parallel dispatch."),
    ("#10", "Knowledge Graph Builder (KGB) with RAG",
     "Data & AI Eng.", "Internal | Optisol",
     ["LangChain", "Azure OpenAI", "Neo4j", "PyVis", "Streamlit", "asyncio"],
     "Full-stack app transforming PDFs, DOCX, JSON, XML & SQL into interactive knowledge graphs with Neo4j persistence, RAG query layer, and physics-simulated PyVis viz."),
]

AWARDS = [
    ("🏆", "Most Valuable Person (MVP) Award", "2024–25",
     "Highest organizational honor for performance excellence, cross-functional leadership, and long-term business contribution."),
    ("◆", "Spot Award — Project Excellence & Leadership", "Jan 2026",
     "Awarded by the CTO for mature project handling and fostering a culture of peer recognition."),
    ("◆", "Spot Award — RS ARP Project Go-Live", "Nov 2025",
     "Exceptional contribution to the 'Beatty Go-Live' rollout and complex 'Delta Load' delivery under tight timelines."),
    ("◆", "Spot Award — AI Tool Innovation (NotebookLLM)", "May 2025",
     "Evaluated, demoed, and drove team adoption of NotebookLLM to enhance project efficiency."),
    ("◆", "Spot Award — Community Mentorship", "Mar 2025",
     "Technical sessions for college students on interview preparation and emerging technologies."),
    ("◆", "OKR Top Contributor (Q4)", "Oct–Dec 2024",
     "Pivotal role in attaining company-wide Objectives and Key Results (OKRs)."),
    ("◆", "Spot Award — Client Excellence (Ontology Mapping)", "Dec 2024",
     "High praise from client for Ontology Mapping presentation during an on-site visit."),
    ("◆", "Spot Award — Gen AI & Automation", "Jul 2024",
     "GenAI-based data inventory automation and SME for resolving DBT blockers."),
]

CERTS = [
    ("❄️", "SnowPro Core Certification",             "Snowflake"),
    ("☁️", "Azure Data Fundamentals (DP-900)",        "Microsoft"),
    ("🧱", "Databricks Lakehouse Fundamentals",       "Databricks"),
    ("🤖", "Generative AI Fundamentals",              "Databricks"),
    ("🔧", "dbt Learn Fundamentals",                  "dbt Labs"),
    ("💾", "SQL (Basic) Certificate",                 "HackerRank"),
    ("🐍", "100 Days of Code: Python Pro Bootcamp",   "Udemy"),
    ("❄️", "Snowflake Masterclass",                   "Udemy"),
]

RESUME_URL = "https://github.com/AshikRoshan-github/Professional-Work-Archive/raw/main/Resume_Center/Data%26AI_1360.docx"

# ══════════════════════════════════════════════════════════════════════════════
#  RENDER
# ══════════════════════════════════════════════════════════════════════════════

# ── NAV — resume download added, no social links here ─────────────────────
st.markdown(f"""
<div class="nav">
  <div class="nav-logo">
    <div class="nav-logo-mark">A</div>
    ashik-roshan.dev
  </div>
  <div class="nav-right">
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#awards">Awards</a>
    <a href="#certs">Certs</a>
    <a href="#education">Education</a>
    <a href="{RESUME_URL}" target="_blank" class="nav-resume"> ⬇️ Resume</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── HERO — social links live HERE only ────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div class="hero-inner">
    <div class="hero-label fade fade-1">Data Engineer &amp; AI Engineer — L2</div>
    <h1 class="hero-name fade fade-2">
      Ashik<br>
      <span class="hero-name-last">Roshan I</span>
    </h1>
    <p class="hero-name-sub fade fade-2">Building data pipelines &amp; intelligent systems</p>
    <div class="hero-divider"></div>
    <div class="hero-bottom fade fade-3">
      <div>
        <p class="hero-bio">
          Results-driven engineer with <strong>2+ years</strong> delivering scalable ETL/ELT pipelines,
          enterprise cloud migrations, and production-grade AI automation at
          <strong>Optisol Business Solutions</strong>. Specialising in Snowflake, Azure, AWS,
          LangChain, and GenAI agent design — from data warehouse migrations to
          self-healing AI code agents and RAG-powered knowledge graphs.
        </p>
        <div class="btn-row">
          <a href="mailto:ashikroshan261@gmail.com" class="btn-a">Get in Touch</a>
          <a href="{RESUME_URL}" target="_blank" class="btn-resume">⬇ Download Resume</a>
          <a href="https://github.com/AshikRoshan-github" target="_blank" class="btn-b">GitHub ↗</a>
          <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank" class="btn-b">LinkedIn ↗</a>
          <a href="https://medium.com/@ashikroshan261" target="_blank" class="btn-b">Medium ↗</a>
        </div>
      </div>
      <div class="hero-meta fade fade-4">
       
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STATS STRIP ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-strip">
  <div class="stat-cell"><div class="stat-val">2<em>+</em></div><div class="stat-key">Years Experience</div></div>
  <div class="stat-cell"><div class="stat-val">14<em>+</em></div><div class="stat-key">Projects Delivered</div></div>
  <div class="stat-cell"><div class="stat-val">7</div><div class="stat-key">Spot Awards</div></div>
  <div class="stat-cell"><div class="stat-val"><em>MVP</em></div><div class="stat-key">Award 2024–25</div></div>
  <div class="stat-cell"><div class="stat-val">8</div><div class="stat-key">Certifications</div></div>
</div>
""", unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────────────────
st.markdown('<div id="skills" class="section-dark"><div class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Arsenal</div><h2 class="s-title">Technical <em>Skills</em></h2>', unsafe_allow_html=True)
skill_html = '<div class="skill-table">'
for cat, tags in SKILLS:
    tag_str = "".join(f'<span class="sv">{t}</span>' for t in tags)
    skill_html += f'<div class="skill-cell"><div class="skill-label">{cat}</div><div class="skill-vals">{tag_str}</div></div>'
skill_html += "</div>"
st.markdown(skill_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Career</div><h2 class="s-title">Professional <em>Experience</em></h2>', unsafe_allow_html=True)
exp_html = '<div class="exp-list">'
for role, company, date in EXP:
    date_display = date.replace('\n', '<br>')
    exp_html += f"""
    <div class="exp-item">
      <div class="exp-date-col"><div class="exp-date">{date_display}</div></div>
      <div class="exp-line"></div>
      <div class="exp-body">
        <div class="exp-role">{role}</div>
        <div class="exp-company">{company}</div>
      </div>
    </div>"""
exp_html += "</div>"
st.markdown(exp_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── DATA ENG PROJECTS ────────────────────────────────────────────────────────
st.markdown('<div id="projects" class="section-dark"><div class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Data Engineering</div><h2 class="s-title">Data Engineering <em>Projects</em></h2>', unsafe_allow_html=True)

def proj_grid_html(projects):
    html = '<div class="proj-grid">'
    for num, title, role, client, tech, desc in projects:
        tags = "".join(f'<span class="ptag">{t}</span>' for t in tech)
        html += f"""
        <div class="pcard">
          <div class="pcard-top">
            <div class="pcard-num">{num}</div>
            <div class="pcard-title">{title}</div>
          </div>
          <div class="pcard-meta">
            <div class="pcard-meta-item">ROLE <span>{role}</span></div>
            <div class="pcard-meta-item">CLIENT <span>{client}</span></div>
          </div>
          <div class="pcard-desc">{desc}</div>
          <div class="pcard-tags">{tags}</div>
        </div>"""
    html += "</div>"
    return html

st.markdown(proj_grid_html(DE_PROJ), unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── AI PROJECTS ──────────────────────────────────────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">AI & Automation</div><h2 class="s-title">AI & Automation <em>Projects</em></h2>', unsafe_allow_html=True)
st.markdown(proj_grid_html(AI_PROJ), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── AWARDS ───────────────────────────────────────────────────────────────────
st.markdown('<div id="awards" class="section-dark"><div class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Recognition</div><h2 class="s-title">Awards & <em>Achievements</em></h2>', unsafe_allow_html=True)
award_html = '<div class="award-grid">'
for icon, title, year, desc in AWARDS:
    award_html += f"""
    <div class="acard">
      <div class="acard-top">
        <span class="acard-icon">{icon}</span>
        <span class="acard-year">{year}</span>
      </div>
      <div class="acard-title">{title}</div>
      <div class="acard-desc">{desc}</div>
    </div>"""
award_html += "</div>"
st.markdown(award_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── CERTIFICATIONS ───────────────────────────────────────────────────────────
st.markdown('<div id="certs" class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Credentials</div><h2 class="s-title"><em>Certifications</em></h2>', unsafe_allow_html=True)
cert_html = '<div class="cert-grid">'
for icon, name, issuer in CERTS:
    cert_html += f"""
    <div class="ccard">
      <div class="ccard-icon">{icon}</div>
      <div>
        <div class="ccard-name">{name}</div>
        <div class="ccard-by">{issuer}</div>
      </div>
    </div>"""
cert_html += "</div>"
st.markdown(cert_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ────────────────────────────────────────────────────────────────
st.markdown('<div id="education" class="section-dark"><div class="section">', unsafe_allow_html=True)
st.markdown('<div class="s-label">Academic</div><h2 class="s-title"><em>Education</em></h2>', unsafe_allow_html=True)
st.markdown("""
<div class="edu-wrap">
  <div class="edu-year-col">
    <div class="edu-year-label">2019</div>
    <div class="edu-year-line"></div>
    <div class="edu-year-label">2023</div>
  </div>
  <div class="edu-card-body">
    <div class="edu-degree">Bachelor of Engineering<br>in Computer Science</div>
    <div class="edu-school">KLN COLLEGE OF ENGINEERING</div>
    <div class="edu-chips">
      <span class="edu-chip">2019 – 2023</span>
      <span class="edu-chip">Grade: A+</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── FOOTER — simplified, social links NOT repeated here ─────────────────────
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-name">Ashik Roshan I</div>
    <div class="footer-sub">Data Engineer · AI Engineer · L2</div>
  </div>
  <div class="footer-copy">
    Built with <span>Streamlit</span><br>
    © 2025 Ashik Roshan I<br>
    All rights reserved
  </div>
</div>
""", unsafe_allow_html=True)
