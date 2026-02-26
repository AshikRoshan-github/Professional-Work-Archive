import streamlit as st
import os

# ── google-genai import (with clear error if missing) ──────────────────────
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

# ══════════════════════════════════════════════════════════════════════════════
#  FULL SYSTEM PROMPT — ALL INFO ABOUT ASHIK
# ══════════════════════════════════════════════════════════════════════════════
ASHIK_SYSTEM_PROMPT = """
You are Ashik Roshan I's personal AI portfolio assistant. You have complete knowledge of Ashik's professional background, projects, skills, awards, education, and contact info. Answer all questions about Ashik in a confident, professional, and friendly tone. Use the sections below to answer accurately.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — PERSONAL INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Full Name      : Ashik Roshan I
Current Role   : Data Engineer & AI Engineer — Level 2 (L2)
Company        : Optisol Business Solutions
Location       : Chennai, India
Email          : ashikroshan261@gmail.com
GitHub         : https://github.com/AshikRoshan-github
LinkedIn       : https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium Blog    : https://medium.com/@ashikroshan261
Total Experience: 2+ years (since Jun 2023)
Summary        : Results-driven Data & AI Engineer delivering scalable ETL/ELT pipelines, enterprise cloud migrations, and production-grade AI automation. Specialises in Snowflake, Azure, AWS, LangChain, and GenAI agent design — from DWH migrations to self-healing AI agents and RAG-powered knowledge graphs. MVP award winner and 7x Spot Award recipient.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — PROFESSIONAL EXPERIENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Role 1: Data Engineer — L2
  Company   : Optisol Business Solutions
  Duration  : Apr 2025 – Present
  Key Work  :
    - Led cross-functional teams on enterprise cloud migrations
    - Architected Snowflake Data Warehouse with dbt ELT pipelines
    - Built production GenAI agents using Azure OpenAI and LangChain
    - Designed knowledge graphs with Neo4j and RAG query layers
    - Mentored junior engineers and conducted college tech sessions
    - Received CTO-recognized Spot Award for project excellence and leadership

Role 2: Data Engineer — L1
  Company   : Optisol Business Solutions
  Duration  : Aug 2024 – Mar 2025
  Key Work  :
    - Developed Python-based ETL pipelines for Azure SQL
    - Implemented AI-powered data profiling platforms with Azure OpenAI
    - Built automated web scraping systems with LangChain and Apify
    - Delivered Ontology Mapping tool with 40-50% manual effort reduction
    - Created self-healing AI Pandas code generation agent

Role 3: Data Engineer Intern — L0
  Company   : Optisol Business Solutions
  Duration  : Mar 2024 – Jul 2024
  Key Work  :
    - Automated web data extraction workflows using Selenium and PyAutoGUI
    - Built AI-driven scraping tools with LangChain and Apify cloud Actors
    - Developed internationalization HTML validation tools

Role 4: Trainee — Software Engineer
  Company   : Blue Cloud
  Duration  : Jun 2023 – Mar 2024
  Key Work  :
    - Developed full-stack web applications
    - Worked on automation and integration projects
    - Gained foundational skills in Python and databases

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — TECHNICAL SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Languages          : Python, SQL, JavaScript, HTML, CSS
Cloud — Azure      : Blob Storage, Data Lake, SQL Database, Azure OpenAI, Databricks, ADF (Azure Data Factory), Azure VM
Cloud — AWS        : S3, Lambda, Glue, Step Functions, EC2, CloudWatch, Textract, Bedrock
Data Engineering   : PySpark, DBT (data build tool), Informatica, Snowflake, Pandas, ADF
Databases          : SSMS, pgAdmin, MySQL, Oracle, SQL Server, Snowflake
BI & Analytics     : Power BI, ThoughtSpot, Plotly, Streamlit
AI & GenAI         : Azure OpenAI, Amazon Bedrock, Gemini 2.5 Pro, LangChain, Neo4j, RAG (Retrieval-Augmented Generation), Prompt Engineering, Azure Document Intelligence
Automation & Web   : Selenium, Web Scraping, FastAPI, PyAutoGUI, Apify, Flask
DevOps & Tools     : GitHub, Azure DevOps, CI/CD, PuTTY, ServiceNow, Rally
Python Libraries   : asyncio, PyVis, PyPDF2, pyodbc, Snowflake Connector, xmltodict, smtplib

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — DATA ENGINEERING PROJECTS (4 Projects)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project DE-1: Python-Based Data Migration — Google Sheets to Azure SQL
  Role      : Data Engineer
  Client    : Internal | Optisol
  Tech Stack: Python, Pandas, gspread, pyodbc, Azure SQL, Azure VM, Cron Jobs
  Description:
    Cost-effective ETL pipeline that extracts data from Google Sheets into Azure SQL Database.
    Implements both full-load and incremental-load logic. Uses Pandas for transformation,
    gspread for Google Sheets API integration, pyodbc for Azure SQL connectivity, and
    Cron Jobs on Azure VM for automated scheduling. Reduced manual data transfer effort to zero.

Project DE-2: On-Premises to Snowflake Data Warehouse Migration
  Role      : Data Engineer
  Client    : Republic Services | Optisol
  Tech Stack: Snowflake, Informatica, dbt, Oracle, SQL Server, AWS Step Functions, CloudWatch
  Description:
    Led the full migration of 6 on-premises source systems (Oracle, SQL Server) to Snowflake DWH.
    Used Informatica for ETL extraction, dbt for ELT transformations with GitHub CI/CD integration,
    AWS Step Functions for automated orchestration, and CloudWatch for monitoring and alerting.
    Delivered a production-grade data warehouse serving enterprise analytics.

Project DE-3: Enterprise DB Migration — Oracle to SQL Server (On-Premises)
  Role      : Data Engineer
  Client    : Republic Services | Optisol
  Tech Stack: Oracle, SQL Server, Autogen ETL framework, T-SQL, ServiceNow
  Description:
    Used the internal Autogen ETL framework to automate schema conversion across a 5-layer
    pipeline: RAW to Staging to Mirror to Test to Production. Managed change requests through
    ServiceNow for enterprise change management compliance. Ensured zero data loss across
    the migration layers.

Project DE-4: API-Driven Migration — Podio to Azure SQL Database
  Role      : Data Engineer
  Client    : Jiffy Cultural Exchange | Optisol
  Tech Stack: Python, REST API, Pandas, ADF, Azure SQL, Azure Blob, AzCopy
  Description:
    Full migration from Podio project management platform to Azure SQL. Extracted data
    via Podio REST API, transformed with Pandas, built ADF pipeline for orchestration,
    and loaded into Azure SQL using pyodbc fast_executemany for high-performance bulk inserts.
    Used AzCopy for document/attachment migration to Azure Blob Storage.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — AI & AUTOMATION PROJECTS (10 Projects)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project AI-1: Automated Web Data Extraction & Reporting Platform
  Role      : Automation Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Selenium, PyAutoGUI, smtplib, Azure DevOps
  Description:
    Browser automation system for fully unattended web data extraction. Automates login,
    navigation, file download, data processing, structured report generation, and
    automated SMTP email distribution. Fully scheduled with zero manual intervention.

Project AI-2: AI-Driven Web Scraping with LangChain & Apify
  Role      : Automation Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Python, LangChain, Apify, REST APIs
  Description:
    Integrated Apify cloud Actors with LangChain to build scalable AI-powered web crawlers.
    Transforms scraped web content into LLM-ready structured documents for downstream
    AI processing and analysis pipelines.

Project AI-3: AI-Powered Automated Data Profiling Platform
  Role      : Data & AI Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Azure OpenAI, Snowflake, Streamlit, Prompt Engineering
  Description:
    Multi-source data profiling platform that automatically generates AI-driven anomaly
    detection reports, data quality insights, and distribution analysis. Connects to
    Snowflake for data access and presents interactive Streamlit dashboards via
    Azure OpenAI GPT models with custom prompt engineering.

Project AI-4: AI Pandas Agent — Self-Healing Code Generation
  Role      : Data & AI Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Azure OpenAI, Pandas, Python
  Description:
    Natural language to Pandas code generator with a self-healing execution loop.
    User describes a data transformation in plain English, agent generates Pandas code,
    executes it, if runtime error occurs sends the exception context back to the LLM,
    LLM auto-regenerates corrected code. Eliminates manual debugging of AI-generated transformations.

Project AI-5: Ontology Kit — Data Mapping Agent
  Role      : Data & AI Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Gemini 2.5 Pro, Streamlit, Pandas, PyODBC
  Description:
    AI-driven ontology mapping tool that reduces manual mapping effort by 40-50%.
    Uses Gemini 2.5 Pro for protocol-based domain understanding, auto-generates metadata,
    integrates sample data, and provides an interactive Streamlit interface. Received
    client praise during an on-site presentation visit.

Project AI-6: AI Document Processing & Structured Data Extraction
  Role      : AI Engineer
  Client    : RS Hackathon | Optisol
  Tech Stack: AWS Textract, Amazon Bedrock, EC2, S3, Flask
  Description:
    End-to-end pipeline: scanned PDFs and images to structured JSON output.
    AWS Textract handles OCR and text extraction, Amazon Bedrock performs semantic
    structuring and entity recognition, Flask REST API on EC2 orchestrates the full
    pipeline and exposes endpoints for downstream consumption. S3 used for document storage.

Project AI-7: Internationalization HTML Validation Tool
  Role      : AI / Data Engineer
  Client    : Optisol (Internal)
  Tech Stack: Python, HTML Parsing, i18n, JSON
  Description:
    Analyzes HTML files for internationalization (i18n) readiness. Detects hard-coded
    strings that should be translated, flags missing translation keys, validates i18n
    attribute completeness, and generates structured JSON reports. Significantly cuts
    manual inspection time for multilingual web application audits.

Project AI-8: Automated Internationalization Workflow
  Role      : Automation Engineer
  Client    : IBEAM | Optisol
  Tech Stack: Python, i18n, Batch Processing, CI/CD
  Description:
    Framework for managing i18n locale files across multiple languages. Validates
    translation keys, syncs new translations, detects missing entries, and integrates
    into CI/CD pipelines for continuous multilingual quality assurance across deployments.

Project AI-9: Credit Risk Reporting & JSON Intelligence Platform
  Role      : Data & AI Engineer
  Client    : Atradius | Optisol
  Tech Stack: Gemini 2.5 Pro, asyncio, Plotly, JSON
  Description:
    Automated pipeline for processing credit risk reports. Maps 40+ credit risk data blocks,
    uses a token-bucket rate limiter with asyncio for async parallel LLM dispatch via
    asyncio.gather, applies section-based prompt engineering to Gemini 2.5 Pro, and
    generates interactive Plotly visualizations. Handles high-volume concurrent API calls
    without rate limit violations.

Project AI-10: Knowledge Graph Builder (KGB) with RAG
  Role      : Data & AI Engineer
  Client    : Internal | Optisol
  Tech Stack: LangChain, Azure OpenAI, Neo4j, PyVis, Streamlit, asyncio
  Description:
    Full-stack application that transforms multi-format documents (PDF, DOCX, JSON, XML, SQL)
    into interactive knowledge graphs. Uses LangChain for document parsing and entity extraction,
    Azure OpenAI for relationship inference, Neo4j for persistent graph storage, PyVis for
    physics-simulated interactive visualization, and a Streamlit front-end with RAG query
    layer for natural language graph querying.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — AWARDS & ACHIEVEMENTS (8 Awards)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Award 1: Most Valuable Person (MVP) Award — 2024-25
  This is the highest organizational award at Optisol. Granted for exceptional performance
  excellence, cross-functional leadership, and long-term business contribution. Ashik is one
  of the youngest recipients of this award.

Award 2: Spot Award — Project Excellence & Leadership — Jan 2026
  Awarded directly by the CTO for mature project handling, strong ownership, and fostering
  a culture of peer recognition within the team.

Award 3: Spot Award — RS ARP Project Go-Live — Nov 2025
  Exceptional contribution to the Beatty Go-Live rollout and the complex Delta Load
  feature delivery under tight enterprise timelines.

Award 4: Spot Award — AI Tool Innovation (NotebookLLM) — May 2025
  Evaluated, demonstrated, and drove team-wide adoption of NotebookLLM to significantly
  enhance project documentation and knowledge-sharing efficiency.

Award 5: Spot Award — Community Mentorship — Mar 2025
  Conducted technical sessions for college students on interview preparation, career
  guidance, and emerging technologies in Data & AI.

Award 6: OKR Top Contributor (Q4) — Oct–Dec 2024
  Pivotal role in achieving company-wide Objectives and Key Results (OKRs) for Q4 2024.

Award 7: Spot Award — Client Excellence (Ontology Mapping) — Dec 2024
  Received direct high praise from the client during an on-site visit for the Ontology
  Mapping platform presentation and live demo.

Award 8: Spot Award — Gen AI & Automation — Jul 2024
  Recognized for GenAI-based data inventory automation project and for serving as SME
  (Subject Matter Expert) to resolve critical DBT pipeline blockers for the team.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — CERTIFICATIONS (8 Certifications)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SnowPro Core Certification         — Snowflake
2. Azure Data Fundamentals (DP-900)   — Microsoft
3. Databricks Lakehouse Fundamentals  — Databricks
4. Generative AI Fundamentals         — Databricks
5. dbt Learn Fundamentals             — dbt Labs
6. SQL (Basic) Certificate            — HackerRank
7. 100 Days of Code: Python Pro Bootcamp — Udemy
8. Snowflake Masterclass              — Udemy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — EDUCATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Degree    : Bachelor of Engineering in Computer Science
College   : KLN College of Engineering
Duration  : 2019 – 2023
Grade     : A+ (Distinction)
Specialization: Computer Science & Engineering

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9 — KEY STATS & HIGHLIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- 2+ years of industry experience
- 14+ projects delivered across Data Engineering and AI/Automation
- 7 Spot Awards received
- 1 MVP Award (highest company honor) — 2024-25
- 8 professional certifications
- Expertise across 3 major clouds: Azure, AWS, Snowflake
- Worked with enterprise clients: Republic Services, Atradius, Jiffy Cultural Exchange, IBEAM
- Reduced manual effort by 40-50% in ontology mapping project
- Built self-healing AI agents, RAG systems, knowledge graphs, async LLM pipelines
- Youngest MVP award recipient at Optisol

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10 — CONTACT & LINKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Email     : ashikroshan261@gmail.com
GitHub    : https://github.com/AshikRoshan-github
LinkedIn  : https://www.linkedin.com/in/ashik-roshan-i-073897249
Medium    : https://medium.com/@ashikroshan261
Resume    : Available for download from the portfolio

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTRUCTIONS FOR YOU (AI Assistant)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Always answer based on the above data accurately.
- Be enthusiastic and professional when describing Ashik's work.
- If asked about a specific project, give full details including tech stack and impact.
- If asked about skills, list them clearly by category.
- If asked for contact info, provide it from Section 10.
- If asked something not in the data above, say you don't have that info but invite them to reach out via email.
- Keep responses well-structured with clear formatting when listing multiple items.
- Never make up data not present above.
"""

# ══════════════════════════════════════════════════════════════════════════════
#  PORTFOLIO DATA
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
    ("Data Engineer — L2", "Optisol Business Solutions", "Apr 2025", "Present",
     ["Led cross-functional teams on enterprise cloud migrations", "Architected Snowflake DWH with dbt ELT pipelines", "Built production GenAI agents with Azure OpenAI & LangChain", "Mentored junior engineers and conducted technical sessions"]),
    ("Data Engineer — L1", "Optisol Business Solutions", "Aug 2024", "Mar 2025",
     ["Developed Python-based ETL pipelines for Azure SQL", "Implemented AI-powered data profiling platforms", "Built knowledge graph system using Neo4j and RAG"]),
    ("Data Engineer Intern — L0", "Optisol Business Solutions", "Mar 2024", "Jul 2024",
     ["Automated web data extraction workflows with Selenium", "Built AI scraping tools with LangChain and Apify"]),
    ("Trainee — Software Engineer", "Blue Cloud", "Jun 2023", "Mar 2024",
     ["Developed full-stack web applications", "Worked on automation and integration projects"]),
]

DE_PROJ = [
    ("#1", "Python-Based Data Migration: Google Sheets to Azure SQL",
     "Data Engineer", "Internal | Optisol",
     ["Python", "Pandas", "gspread", "pyodbc", "Azure SQL", "Azure VM", "Cron Jobs"],
     "Cost-effective ETL extracting Google Sheets data into Azure SQL Database with full & incremental load logic, Pandas transformation, and Cron-scheduled automation."),
    ("#2", "On-Premises to Snowflake Data Warehouse Migration",
     "Data Engineer", "Republic Services | Optisol",
     ["Snowflake", "Informatica", "dbt", "Oracle", "SQL Server", "AWS Step Functions", "CloudWatch"],
     "Led migration of 6 on-premises source systems to Snowflake DWH with automated AWS orchestration, CloudWatch monitoring, and dbt ELT transformations via GitHub CI/CD."),
    ("#3", "Enterprise DB Migration: Oracle to SQL Server (On-Prem)",
     "Data Engineer", "Republic Services | Optisol",
     ["Oracle", "SQL Server", "Autogen ETL", "T-SQL", "ServiceNow"],
     "Used the internal Autogen ETL framework to automate schema conversion across RAW > Staging > Mirror > Test > Production with ServiceNow change management."),
    ("#4", "API-Driven Migration: Podio to Azure SQL Database",
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
     "AI-driven ontology mapping tool reducing manual effort 40-50% with protocol-based domain understanding, auto-generated metadata, and sample data integration."),
    ("#6", "AI Document Processing & Structured Data Extraction",
     "AI Engineer", "RS Hackathon | Optisol",
     ["AWS Textract", "Amazon Bedrock", "EC2", "S3", "Flask"],
     "Scanned PDFs/images to structured JSON pipeline: Textract for extraction, Bedrock for semantic structuring, Flask REST API on EC2 for orchestration."),
    ("#7", "Internationalization HTML Validation Tool",
     "AI/Data Eng.", "Optisol",
     ["Python", "HTML Parsing", "i18n", "JSON"],
     "Analyzes HTML for i18n readiness, detects hard-coded strings, flags missing translations, generates JSON reports."),
    ("#8", "Automated Internationalization Workflow",
     "Automation Eng.", "IBEAM | Optisol",
     ["Python", "i18n", "Batch Processing", "CI/CD"],
     "Framework managing i18n locale files across languages — validates keys, syncs translations, integrates into CI/CD for continuous multilingual quality."),
    ("#9", "Credit Risk Reporting & JSON Intelligence Platform",
     "Data & AI Eng.", "Atradius | Optisol",
     ["Gemini 2.5 Pro", "asyncio", "Plotly", "JSON"],
     "Automated pipeline mapping 40+ credit risk blocks with async rate limiter (token-bucket), section-based LLM prompting, and asyncio.gather parallel dispatch."),
    ("#10", "Knowledge Graph Builder (KGB) with RAG",
     "Data & AI Eng.", "Internal | Optisol",
     ["LangChain", "Azure OpenAI", "Neo4j", "PyVis", "Streamlit", "asyncio"],
     "Full-stack app transforming PDFs, DOCX, JSON, XML & SQL into interactive knowledge graphs with Neo4j persistence, RAG query layer, and physics-simulated PyVis viz."),
]

AWARDS = [
    ("🏆", "Most Valuable Person (MVP) Award", "2024-25",
     "Highest organizational honor for performance excellence, cross-functional leadership, and long-term business contribution."),
    ("◆", "Spot Award — Project Excellence & Leadership", "Jan 2026",
     "Awarded by the CTO for mature project handling and fostering a culture of peer recognition."),
    ("◆", "Spot Award — RS ARP Project Go-Live", "Nov 2025",
     "Exceptional contribution to the Beatty Go-Live rollout and complex Delta Load delivery under tight timelines."),
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
    ("❄️", "SnowPro Core Certification",           "Snowflake"),
    ("☁️", "Azure Data Fundamentals (DP-900)",      "Microsoft"),
    ("🧱", "Databricks Lakehouse Fundamentals",     "Databricks"),
    ("🤖", "Generative AI Fundamentals",            "Databricks"),
    ("🔧", "dbt Learn Fundamentals",                "dbt Labs"),
    ("💾", "SQL (Basic) Certificate",               "HackerRank"),
    ("🐍", "100 Days of Code: Python Pro Bootcamp", "Udemy"),
    ("❄️", "Snowflake Masterclass",                 "Udemy"),
]

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

:root {
  --bg:#FFFFFF; --bg1:#F8F8F8; --bg2:#F0F0F0; --bg3:#E8E8E8;
  --ink:#0A0A0A; --ink2:#2A2A2A; --ink3:#4A4A4A;
  --muted:#8A8A8A; --border:#D8D8D8; --border2:#B0B0B0;
}

.stApp { background:var(--bg); font-family:'DM Sans',sans-serif; color:var(--ink); }

@keyframes fadeIn { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.fade{animation:fadeIn 0.45s ease both}
.d1{animation-delay:.04s} .d2{animation-delay:.1s} .d3{animation-delay:.18s} .d4{animation-delay:.26s}

/* ══ NAV ══ */
.topnav {
  background:var(--bg); border-bottom:2px solid var(--ink);
  display:flex; align-items:center; justify-content:space-between;
  padding:0 56px; height:58px; position:sticky; top:0; z-index:500;
}
.nav-brand { font-family:'Playfair Display',serif; font-size:17px; font-weight:700; font-style:italic; color:var(--ink); }
.nav-brand span { font-style:normal; font-weight:400; font-size:11px; color:var(--muted); margin-left:10px; font-family:'JetBrains Mono',monospace; letter-spacing:1px; }

/* ══ PAGE ══ */
.page { padding:56px 56px 72px; max-width:1200px; margin:0 auto; }
.page-label {
  font-family:'JetBrains Mono',monospace; font-size:10px; font-weight:600;
  letter-spacing:3px; text-transform:uppercase; color:var(--muted); margin-bottom:10px;
  display:flex; align-items:center; gap:12px;
}
.page-label::before { content:''; width:28px; height:1px; background:var(--ink); }
.page-title {
  font-family:'Playfair Display',serif; font-size:clamp(34px,5vw,58px);
  font-weight:700; color:var(--ink); line-height:1.05; letter-spacing:-2px; margin-bottom:44px;
}
.page-title em { font-style:italic; font-weight:400; }

/* ══ HERO ══ */
.hero-wrap {
  display:grid; grid-template-columns:1fr 360px; gap:72px; align-items:start;
  padding:64px 56px; border-bottom:1px solid var(--border); max-width:1200px; margin:0 auto;
}
.hero-name { font-family:'Playfair Display',serif; font-size:clamp(48px,7vw,92px); font-weight:700; line-height:0.95; letter-spacing:-4px; color:var(--ink); margin-bottom:8px; }
.hero-name em { font-style:italic; font-weight:400; }
.hero-role { font-family:'JetBrains Mono',monospace; font-size:11.5px; font-weight:500; letter-spacing:2px; text-transform:uppercase; color:var(--muted); margin-bottom:28px; }
.hero-rule { width:56px; height:2px; background:var(--ink); margin-bottom:24px; }
.hero-bio { font-size:15px; line-height:1.9; color:var(--ink3); font-weight:300; max-width:540px; margin-bottom:28px; }
.hero-bio strong { color:var(--ink); font-weight:600; }
.stats-row { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--border); border:1px solid var(--border); border-radius:4px; overflow:hidden; }
.stat-box { background:var(--bg); padding:18px 14px; text-align:center; }
.stat-n { font-family:'Playfair Display',serif; font-size:30px; font-weight:700; color:var(--ink); line-height:1; letter-spacing:-1px; }
.stat-l { font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:500; letter-spacing:1.5px; text-transform:uppercase; color:var(--muted); margin-top:4px; }

/* Contact Card */
.contact-card { background:var(--ink); border-radius:6px; padding:28px 24px; position:sticky; top:76px; }
.contact-card-title { font-family:'Playfair Display',serif; font-size:17px; font-style:italic; color:white; margin-bottom:22px; padding-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.12); }
.contact-row { display:flex; align-items:center; gap:12px; margin-bottom:14px; text-decoration:none; }
.contact-icon { width:30px; height:30px; background:rgba(255,255,255,0.1); border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:12px; flex-shrink:0; color:white; }
.contact-lbl { font-family:'JetBrains Mono',monospace; font-size:8.5px; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:1px; }
.contact-val { font-size:12px; color:rgba(255,255,255,0.8); }
.resume-btn { display:block; text-align:center; background:white; color:var(--ink); font-family:'JetBrains Mono',monospace; font-size:10.5px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; padding:12px 18px; border-radius:4px; text-decoration:none; margin-top:20px; }

/* ══ SKILLS ══ */
.skill-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:var(--border); border:1px solid var(--border); border-radius:6px; overflow:hidden; }
.skill-row { background:var(--bg); padding:14px 18px; display:flex; gap:14px; align-items:flex-start; }
.skill-row:hover { background:var(--bg1); }
.skill-cat { font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; color:var(--muted); min-width:100px; padding-top:3px; flex-shrink:0; }
.skill-tags { display:flex; flex-wrap:wrap; gap:5px; }
.stag { font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--ink2); background:var(--bg2); padding:3px 8px; border-radius:2px; border:1px solid var(--border); transition:all 0.15s; cursor:default; }
.stag:hover { background:var(--ink); color:white; border-color:var(--ink); }

/* ══ TIMELINE ══ */
.tl-item { display:grid; grid-template-columns:150px 2px 1fr; gap:0 28px; padding:28px 0; border-bottom:1px solid var(--border); align-items:start; }
.tl-item:last-child { border-bottom:none; }
.tl-date { text-align:right; font-family:'JetBrains Mono',monospace; font-size:10.5px; color:var(--muted); line-height:1.7; padding-top:4px; }
.tl-line { background:var(--border2); position:relative; align-self:stretch; }
.tl-dot { position:absolute; top:5px; left:-4px; width:10px; height:10px; background:var(--ink); border-radius:50%; }
.tl-body { padding-left:4px; }
.tl-role { font-family:'Playfair Display',serif; font-size:19px; font-weight:600; color:var(--ink); margin-bottom:4px; }
.tl-company { font-family:'JetBrains Mono',monospace; font-size:10.5px; color:var(--muted); letter-spacing:0.5px; margin-bottom:14px; }
.tl-bullets { list-style:none; }
.tl-bullets li { font-size:13px; color:var(--ink3); line-height:1.75; padding-left:16px; position:relative; margin-bottom:3px; }
.tl-bullets li::before { content:'—'; position:absolute; left:0; color:var(--border2); }

/* ══ PROJECT CARDS ══ */
.proj-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:1px; background:var(--border); border:1px solid var(--border); border-radius:6px; overflow:hidden; }
.pcard { background:var(--bg); padding:22px 24px; display:flex; flex-direction:column; gap:11px; }
.pcard:hover { background:var(--bg1); }
.pcard-header { display:flex; align-items:flex-start; gap:10px; }
.pcard-num { font-family:'Playfair Display',serif; font-style:italic; font-size:11px; color:var(--muted); background:var(--bg2); padding:2px 7px; border-radius:2px; flex-shrink:0; border:1px solid var(--border); }
.pcard-title { font-size:13.5px; font-weight:600; color:var(--ink); line-height:1.45; flex:1; }
.pcard-meta { display:flex; gap:14px; flex-wrap:wrap; }
.pmeta { font-family:'JetBrains Mono',monospace; font-size:9.5px; color:var(--muted); }
.pmeta span { color:var(--ink2); }
.pcard-desc { font-size:12.5px; line-height:1.75; color:var(--ink3); font-weight:300; flex:1; }
.pcard-tags { display:flex; flex-wrap:wrap; gap:4px; padding-top:8px; border-top:1px solid var(--border); }
.ptag { font-family:'JetBrains Mono',monospace; font-size:9.5px; color:var(--muted); background:var(--bg2); padding:2px 6px; border-radius:2px; }

/* ══ AWARDS ══ */
.award-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:14px; }
.acard { background:var(--bg); border:1px solid var(--border); border-radius:6px; padding:20px 22px; display:flex; flex-direction:column; gap:9px; transition:all 0.2s; }
.acard:hover { border-color:var(--ink); box-shadow:3px 3px 0 var(--ink); transform:translate(-1px,-1px); }
.acard-top { display:flex; align-items:center; justify-content:space-between; }
.acard-icon { font-size:17px; }
.acard-year { font-family:'JetBrains Mono',monospace; font-size:9px; letter-spacing:1px; color:var(--muted); background:var(--bg2); padding:3px 8px; border-radius:100px; border:1px solid var(--border); }
.acard-title { font-size:13px; font-weight:600; color:var(--ink); line-height:1.4; }
.acard-desc { font-size:12px; color:var(--muted); line-height:1.65; font-weight:300; }

/* ══ CERTS ══ */
.cert-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(255px,1fr)); gap:10px; }
.ccard { background:var(--bg); border:1px solid var(--border); border-radius:6px; padding:13px 16px; display:flex; align-items:center; gap:12px; transition:all 0.2s; }
.ccard:hover { border-color:var(--ink); box-shadow:2px 2px 0 var(--ink); transform:translate(-1px,-1px); }
.ccard-icon { width:36px; height:36px; background:var(--bg2); border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0; border:1px solid var(--border); }
.ccard-name { font-size:12.5px; font-weight:600; color:var(--ink); margin-bottom:2px; line-height:1.35; }
.ccard-by { font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--muted); }

/* ══ EDU ══ */
.edu-card { background:var(--bg); border:2px solid var(--ink); border-radius:6px; padding:32px 36px; max-width:560px; box-shadow:6px 6px 0 var(--ink); }
.edu-degree { font-family:'Playfair Display',serif; font-size:24px; font-weight:700; color:var(--ink); line-height:1.2; margin-bottom:8px; }
.edu-school { font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--muted); letter-spacing:1px; text-transform:uppercase; margin-bottom:18px; }
.edu-pills { display:flex; gap:8px; flex-wrap:wrap; }
.edu-pill { font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--ink2); background:var(--bg2); border:1px solid var(--border2); padding:4px 12px; border-radius:3px; }

/* ══ CHAT ══ */
.chat-page { padding:56px 56px 72px; max-width:860px; margin:0 auto; }
.chat-info { font-size:13.5px; color:var(--muted); font-weight:300; margin-top:6px; margin-bottom:28px; }
.chat-box {
  background:var(--bg1); border:1px solid var(--border2); border-radius:8px;
  padding:24px; min-height:340px; max-height:500px; overflow-y:auto;
  margin-bottom:14px; display:flex; flex-direction:column; gap:14px;
}
.msg-user { display:flex; justify-content:flex-end; }
.msg-ai { display:flex; justify-content:flex-start; align-items:flex-start; gap:10px; }
.ai-avatar { width:28px; height:28px; background:var(--ink); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:11px; color:white; flex-shrink:0; font-family:'Playfair Display',serif; font-style:italic; }
.bubble { max-width:82%; padding:11px 15px; border-radius:6px; font-size:13.5px; line-height:1.65; }
.bubble-user { background:var(--ink); color:white; border-bottom-right-radius:2px; }
.bubble-ai { background:white; color:var(--ink); border:1px solid var(--border); border-bottom-left-radius:2px; }
.chat-welcome { text-align:center; padding:40px 20px; color:var(--muted); font-size:13px; }
.chat-welcome .wi { font-size:36px; margin-bottom:12px; }
.chat-welcome strong { display:block; font-size:16px; color:var(--ink); margin-bottom:8px; font-family:'Playfair Display',serif; }

/* ══ FOOTER ══ */
.footer { background:var(--ink); padding:36px 56px; display:flex; align-items:center; justify-content:space-between; }
.footer-name { font-family:'Playfair Display',serif; font-size:20px; font-style:italic; color:white; }
.footer-copy { font-family:'JetBrains Mono',monospace; font-size:10px; color:rgba(255,255,255,0.35); text-align:right; line-height:1.9; }

/* Streamlit widget overrides */
div[data-testid="stTextInput"] input {
  background:var(--bg) !important; border:1.5px solid var(--border2) !important;
  border-radius:4px !important; color:var(--ink) !important;
  font-family:'DM Sans',sans-serif !important; font-size:14px !important; padding:11px 14px !important;
}
div[data-testid="stTextInput"] input:focus { border-color:var(--ink) !important; box-shadow:none !important; }
div[data-testid="stButton"] button {
  background:var(--ink) !important; color:white !important; border:none !important;
  border-radius:4px !important; font-family:'JetBrains Mono',monospace !important;
  font-size:10.5px !important; font-weight:600 !important; letter-spacing:1px !important;
  text-transform:uppercase !important; padding:11px 20px !important;
}
div[data-testid="stButton"] button:hover { opacity:0.88 !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

PAGES = ["Home", "Skills", "Experience", "Projects", "Awards & Certs", "Education", "Chat"]

# ══════════════════════════════════════════════════════════════════════════════
#  NAV
# ══════════════════════════════════════════════════════════════════════════════
tabs_html = ""
for p in PAGES:
    active_style = "font-weight:600;color:#0A0A0A;border-bottom:2px solid #0A0A0A;margin-bottom:-2px;" if st.session_state.page == p else "color:#8A8A8A;"
    tabs_html += (
        f'<span style="font-family:JetBrains Mono,monospace;font-size:10.5px;letter-spacing:1.5px;'
        f'text-transform:uppercase;padding:0 16px;height:58px;display:inline-flex;align-items:center;'
        f'border-left:1px solid #D8D8D8;{active_style}">{p}</span>'
    )

st.markdown(f"""
<div class="topnav">
  <div class="nav-brand">Ashik Roshan <em>I</em><span>DATA &amp; AI ENGINEER</span></div>
  <div style="display:flex;">{tabs_html}</div>
</div>
""", unsafe_allow_html=True)

# Functional nav buttons (visually hidden, still clickable)
st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] { position:fixed; bottom:0; left:0; width:1px; height:1px; overflow:hidden; opacity:0; pointer-events:none; z-index:-1; }
</style>
""", unsafe_allow_html=True)

nav_cols = st.columns(len(PAGES))
for col, p in zip(nav_cols, PAGES):
    with col:
        if st.button(p, key=f"nav_{p}"):
            st.session_state.page = p
            st.rerun()

page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════════════════

# ── HOME ─────────────────────────────────────────────────────────────────────
if page == "Home":
    st.markdown("""
    <div class="hero-wrap fade">
      <div>
        <div class="page-label d1">Data Engineer & AI Engineer — L2</div>
        <h1 class="hero-name d2">Ashik<br><em>Roshan I</em></h1>
        <div class="hero-role d2">Optisol Business Solutions · Chennai, India</div>
        <div class="hero-rule d3"></div>
        <p class="hero-bio d3">
          Results-driven engineer with <strong>2+ years</strong> delivering scalable ETL/ELT pipelines,
          enterprise cloud migrations, and production-grade AI automation. Specialising in
          <strong>Snowflake, Azure, AWS, LangChain,</strong> and GenAI agent design — from data warehouse
          migrations to self-healing AI code agents and RAG-powered knowledge graphs.
        </p>
        <div class="stats-row d4">
          <div class="stat-box"><div class="stat-n">2+</div><div class="stat-l">Years Exp.</div></div>
          <div class="stat-box"><div class="stat-n">14+</div><div class="stat-l">Projects</div></div>
          <div class="stat-box"><div class="stat-n">7</div><div class="stat-l">Spot Awards</div></div>
          <div class="stat-box"><div class="stat-n">8</div><div class="stat-l">Certifications</div></div>
        </div>
      </div>
      <div class="fade d3">
        <div class="contact-card">
          <div class="contact-card-title">Get in Touch</div>
          <a class="contact-row" href="mailto:ashikroshan261@gmail.com">
            <div class="contact-icon">✉</div>
            <div><div class="contact-lbl">Email</div><div class="contact-val">ashikroshan261@gmail.com</div></div>
          </a>
          <a class="contact-row" href="https://github.com/AshikRoshan-github" target="_blank">
            <div class="contact-icon">⌥</div>
            <div><div class="contact-lbl">GitHub</div><div class="contact-val">AshikRoshan-github</div></div>
          </a>
          <a class="contact-row" href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank">
            <div class="contact-icon">in</div>
            <div><div class="contact-lbl">LinkedIn</div><div class="contact-val">ashik-roshan-i</div></div>
          </a>
          <a class="contact-row" href="https://medium.com/@ashikroshan261" target="_blank">
            <div class="contact-icon">✍</div>
            <div><div class="contact-lbl">Medium</div><div class="contact-val">@ashikroshan261</div></div>
          </a>
          <a class="resume-btn" href="https://github.com/AshikRoshan-github/Professional-Work-Archive/raw/main/Resume_Center/Data%26AI_1360.docx" target="_blank">
            ⬇ Download Resume
          </a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────────────────
elif page == "Skills":
    st.markdown('<div class="page fade">', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Arsenal</div><h2 class="page-title">Technical <em>Skills</em></h2>', unsafe_allow_html=True)
    rows = ""
    for cat, tags in SKILLS:
        tag_html = "".join(f'<span class="stag">{t}</span>' for t in tags)
        rows += f'<div class="skill-row"><div class="skill-cat">{cat}</div><div class="skill-tags">{tag_html}</div></div>'
    st.markdown(f'<div class="skill-grid">{rows}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
elif page == "Experience":
    st.markdown('<div class="page fade">', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Career</div><h2 class="page-title">Professional <em>Experience</em></h2>', unsafe_allow_html=True)
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
elif page == "Projects":
    def make_proj_grid(projects):
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

    st.markdown('<div class="page fade">', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Data Engineering</div><h2 class="page-title">Data Engineering <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(make_proj_grid(DE_PROJ), unsafe_allow_html=True)
    st.markdown('<div style="height:60px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-label">AI & Automation</div><h2 class="page-title">AI & Automation <em>Projects</em></h2>', unsafe_allow_html=True)
    st.markdown(make_proj_grid(AI_PROJ), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── AWARDS & CERTS ───────────────────────────────────────────────────────────
elif page == "Awards & Certs":
    st.markdown('<div class="page fade">', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Recognition</div><h2 class="page-title">Awards & <em>Achievements</em></h2>', unsafe_allow_html=True)
    aw = "".join(f"""<div class="acard">
      <div class="acard-top"><span class="acard-icon">{icon}</span><span class="acard-year">{year}</span></div>
      <div class="acard-title">{title}</div>
      <div class="acard-desc">{desc}</div>
    </div>""" for icon, title, year, desc in AWARDS)
    st.markdown(f'<div class="award-grid">{aw}</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:56px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Credentials</div><h2 class="page-title"><em>Certifications</em></h2>', unsafe_allow_html=True)
    ce = "".join(f"""<div class="ccard">
      <div class="ccard-icon">{icon}</div>
      <div><div class="ccard-name">{name}</div><div class="ccard-by">{issuer}</div></div>
    </div>""" for icon, name, issuer in CERTS)
    st.markdown(f'<div class="cert-grid">{ce}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ────────────────────────────────────────────────────────────────
elif page == "Education":
    st.markdown('<div class="page fade">', unsafe_allow_html=True)
    st.markdown('<div class="page-label">Academic</div><h2 class="page-title"><em>Education</em></h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-card">
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
elif page == "Chat":
    st.markdown('<div class="chat-page fade">', unsafe_allow_html=True)
    st.markdown("""
    <div class="page-label">AI Assistant</div>
    <h2 class="page-title" style="margin-bottom:6px;">Ask <em>Ashik's AI</em></h2>
    <p class="chat-info">Powered by Gemini 2.5 Pro · Knows everything about Ashik's background, projects & skills</p>
    """, unsafe_allow_html=True)

    # Render chat messages
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="chat-box">
          <div class="chat-welcome">
            <div class="wi">◈</div>
            <strong>Hi! I'm Ashik's AI Assistant</strong>
            Ask me anything — his projects, skills, experience, awards, certifications, or how to contact him.
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
                bubbles += f'<div class="msg-ai"><div class="ai-avatar">A</div><div class="bubble bubble-ai">{content}</div></div>'
        st.markdown(f'<div class="chat-box">{bubbles}</div>', unsafe_allow_html=True)

    # Input row
    col_in, col_send = st.columns([5, 1])
    with col_in:
        user_input = st.text_input("", placeholder="Ask about projects, skills, experience, awards...", label_visibility="collapsed", key="chat_input")
    with col_send:
        send_clicked = st.button("Send →", key="send_btn", use_container_width=True)

    col_clr, _ = st.columns([1, 6])
    with col_clr:
        if st.button("Clear", key="clear_btn"):
            st.session_state.chat_history = []
            st.rerun()

    # Package check
    if not GENAI_AVAILABLE:
        st.error("""
        ⚠️ **google-genai package not installed!**
        Add this to your `requirements.txt`:
        ```
        google-genai
        ```
        Then redeploy on Streamlit Cloud.
        """)

    elif send_clicked and user_input.strip():
        # Read key from Streamlit secrets: [GOOGLE] → Gemini_api_key
        gemini_key = None
        try:
            gemini_key = st.secrets["GOOGLE"]["Gemini_api_key"]
        except Exception:
            pass
        if not gemini_key:
            gemini_key = os.environ.get("GEMINI_API_KEY", "")

        if not gemini_key:
            st.error("""
            ⚠️ **API key not found.**
            In Streamlit Cloud → App Settings → Secrets, add:
            ```toml
            [GOOGLE]
            Gemini_api_key = "your-key-here"
            ```
            """)
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            with st.spinner("Thinking..."):
                try:
                    client = google_genai.Client(api_key=gemini_key)

                    contents = []
                    for msg in st.session_state.chat_history:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append(
                            google_types.Content(
                                role=role,
                                parts=[google_types.Part.from_text(text=msg["content"])]
                            )
                        )

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
                        "role": "assistant",
                        "content": response.text
                    })
                    st.rerun()

                except Exception as e:
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": f"⚠️ Error calling Gemini API: {str(e)}"
                    })
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  <div class="footer-name">Ashik Roshan I</div>
  <div class="footer-copy">
    Built with Streamlit · Powered by Gemini 2.5 Pro<br>
    © 2025 Ashik Roshan I · All rights reserved
  </div>
</div>
""", unsafe_allow_html=True)
