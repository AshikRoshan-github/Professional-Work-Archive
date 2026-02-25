import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashik Roshan I – Data & AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.stApp {
    background: #FFFFFF;
    font-family: 'DM Sans', sans-serif;
    color: #1A1A1A;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── NAV ── */
.nav-bar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255,255,255,0.96);
    backdrop-filter: blur(12px);
    border-bottom: 2px solid #FF6B00;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    height: 64px;
    box-shadow: 0 2px 20px rgba(255,107,0,0.08);
}
.nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 900;
    color: #1A1A1A;
    letter-spacing: -0.5px;
}
.nav-logo span { color: #FF6B00; }
.nav-links { display: flex; gap: 32px; }
.nav-links a {
    font-size: 13px;
    font-weight: 500;
    color: #444;
    text-decoration: none;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    transition: color 0.2s;
}
.nav-links a:hover { color: #FF6B00; }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #FFF8F3 0%, #FFFFFF 50%, #FFF3E8 100%);
    padding: 80px 48px 60px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(255,107,0,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 10%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,107,0,0.06) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-inner { position: relative; z-index: 2; max-width: 1200px; margin: 0 auto; }
.hero-tag {
    display: inline-block;
    background: #FF6B00;
    color: white;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 2px;
    margin-bottom: 24px;
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(48px, 6vw, 80px);
    font-weight: 900;
    line-height: 1.05;
    color: #1A1A1A;
    margin-bottom: 16px;
    letter-spacing: -2px;
}
.hero-name span { color: #FF6B00; }
.hero-title {
    font-size: 20px;
    font-weight: 300;
    color: #555;
    margin-bottom: 28px;
    letter-spacing: 0.3px;
}
.hero-title strong { color: #FF6B00; font-weight: 600; }
.hero-summary {
    max-width: 680px;
    font-size: 16px;
    line-height: 1.8;
    color: #444;
    margin-bottom: 36px;
}
.hero-btns { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 48px; }
.btn-primary {
    background: #FF6B00;
    color: white;
    padding: 14px 32px;
    border-radius: 3px;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: 0.3px;
    transition: all 0.2s;
    box-shadow: 0 4px 16px rgba(255,107,0,0.3);
}
.btn-primary:hover { background: #E05E00; transform: translateY(-1px); }
.btn-outline {
    background: transparent;
    color: #FF6B00;
    padding: 14px 32px;
    border-radius: 3px;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    border: 2px solid #FF6B00;
    transition: all 0.2s;
}
.btn-outline:hover { background: #FFF3E8; }
.hero-stats {
    display: flex;
    gap: 48px;
    padding-top: 32px;
    border-top: 1px solid rgba(255,107,0,0.2);
    flex-wrap: wrap;
}
.stat-item { display: flex; flex-direction: column; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 900;
    color: #FF6B00;
    line-height: 1;
    margin-bottom: 4px;
}
.stat-label { font-size: 12px; color: #888; letter-spacing: 0.5px; text-transform: uppercase; }

/* ── CONTACT STRIP ── */
.contact-strip {
    background: #1A1A1A;
    padding: 16px 48px;
    display: flex;
    gap: 32px;
    flex-wrap: wrap;
    align-items: center;
}
.contact-item {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #CCC;
    font-size: 13px;
    text-decoration: none;
}
.contact-item:hover { color: #FF6B00; }
.contact-dot { width: 6px; height: 6px; background: #FF6B00; border-radius: 50%; flex-shrink: 0; }

/* ── SECTION ── */
.section {
    padding: 72px 48px;
    max-width: 1200px;
    margin: 0 auto;
}
.section-alt { background: #FFF8F3; padding: 72px 48px; }
.section-alt .section-inner { max-width: 1200px; margin: 0 auto; }

.section-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #FF6B00;
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 8px;
    letter-spacing: -1px;
    line-height: 1.2;
}
.section-divider {
    width: 48px; height: 4px;
    background: #FF6B00;
    border-radius: 2px;
    margin-bottom: 40px;
}

/* ── SKILLS ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 20px;
}
.skill-card {
    background: white;
    border: 1px solid #F0E8E0;
    border-radius: 8px;
    padding: 24px;
    border-left: 4px solid #FF6B00;
    transition: all 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.skill-card:hover {
    box-shadow: 0 8px 24px rgba(255,107,0,0.12);
    transform: translateY(-2px);
    border-left-color: #E05E00;
}
.skill-cat {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #FF6B00;
    margin-bottom: 10px;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.skill-tag {
    background: #FFF3E8;
    color: #CC5500;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 2px;
    font-family: 'DM Mono', monospace;
}

/* ── EXPERIENCE ── */
.timeline { position: relative; padding-left: 32px; }
.timeline::before {
    content: '';
    position: absolute;
    left: 7px; top: 8px; bottom: 8px;
    width: 2px;
    background: linear-gradient(to bottom, #FF6B00, rgba(255,107,0,0.1));
}
.timeline-item { position: relative; margin-bottom: 40px; }
.timeline-dot {
    position: absolute;
    left: -29px; top: 6px;
    width: 14px; height: 14px;
    background: #FF6B00;
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 0 0 2px #FF6B00;
}
.timeline-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 4px;
}
.timeline-role {
    font-size: 18px;
    font-weight: 600;
    color: #1A1A1A;
    line-height: 1.3;
}
.timeline-date {
    background: #FFF3E8;
    color: #CC5500;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 20px;
    white-space: nowrap;
    font-family: 'DM Mono', monospace;
}
.timeline-company {
    font-size: 14px;
    font-weight: 500;
    color: #FF6B00;
    margin-bottom: 4px;
}

/* ── PROJECT CARDS ── */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 24px;
}
.project-card {
    background: white;
    border: 1px solid #F0E8E0;
    border-radius: 10px;
    padding: 28px;
    transition: all 0.25s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    position: relative;
    overflow: hidden;
}
.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #FF6B00, #FFB347);
}
.project-card:hover {
    box-shadow: 0 16px 40px rgba(255,107,0,0.14);
    transform: translateY(-4px);
}
.project-num {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 900;
    color: rgba(255,107,0,0.1);
    line-height: 1;
    margin-bottom: -8px;
}
.project-title {
    font-size: 16px;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 8px;
    line-height: 1.4;
}
.project-meta {
    font-size: 12px;
    color: #888;
    margin-bottom: 6px;
    display: flex;
    gap: 6px;
    align-items: center;
}
.project-meta span { color: #FF6B00; font-weight: 600; }
.project-tech {
    margin-top: 14px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}
.tech-tag {
    background: #F8F8F8;
    color: #555;
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 2px;
    font-family: 'DM Mono', monospace;
    border: 1px solid #EEE;
}

/* ── AWARDS ── */
.awards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}
.award-card {
    background: white;
    border-radius: 8px;
    padding: 24px;
    border: 1px solid #F0E8E0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: all 0.2s;
}
.award-card:hover {
    box-shadow: 0 8px 24px rgba(255,107,0,0.1);
    transform: translateY(-2px);
}
.award-icon {
    font-size: 28px;
    margin-bottom: 10px;
    display: block;
}
.award-title {
    font-size: 15px;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 6px;
    line-height: 1.3;
}
.award-year {
    display: inline-block;
    background: #FF6B00;
    color: white;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 2px;
    margin-bottom: 10px;
    font-family: 'DM Mono', monospace;
}
.award-desc {
    font-size: 13px;
    color: #666;
    line-height: 1.6;
}

/* ── CERTIFICATIONS ── */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
}
.cert-card {
    background: white;
    border-radius: 8px;
    padding: 20px 24px;
    border: 1px solid #F0E8E0;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    transition: all 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.cert-card:hover {
    box-shadow: 0 6px 20px rgba(255,107,0,0.1);
    border-color: rgba(255,107,0,0.3);
}
.cert-icon {
    width: 40px; height: 40px;
    background: #FFF3E8;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
}
.cert-name {
    font-size: 14px;
    font-weight: 600;
    color: #1A1A1A;
    margin-bottom: 3px;
    line-height: 1.3;
}
.cert-issuer {
    font-size: 12px;
    color: #FF6B00;
    font-weight: 500;
}

/* ── EDUCATION ── */
.edu-card {
    background: white;
    border-radius: 10px;
    padding: 32px 36px;
    border: 1px solid #F0E8E0;
    border-left: 5px solid #FF6B00;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    max-width: 600px;
}
.edu-degree {
    font-size: 20px;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 6px;
}
.edu-school {
    font-size: 15px;
    color: #FF6B00;
    font-weight: 600;
    margin-bottom: 8px;
}
.edu-meta {
    font-size: 13px;
    color: #888;
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.edu-meta span {
    background: #FFF3E8;
    color: #CC5500;
    padding: 3px 10px;
    border-radius: 2px;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
}

/* ── FOOTER ── */
.footer {
    background: #1A1A1A;
    color: #888;
    text-align: center;
    padding: 32px 48px;
    font-size: 13px;
}
.footer strong { color: #FF6B00; }

</style>
""", unsafe_allow_html=True)

# ── NAV ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">Ashik<span>.</span></div>
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

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <div class="hero-tag">⚡ Open to Opportunities</div>
    <h1 class="hero-name">Ashik Roshan <span>I</span></h1>
    <p class="hero-title"><strong>Data Engineer – L2</strong> &nbsp;·&nbsp; AI Engineer &nbsp;·&nbsp; Optisol Business Solutions</p>
    <p class="hero-summary">
      Results-driven Data & AI Engineer with 2+ years of experience designing scalable ETL/ELT pipelines, 
      enterprise cloud migrations, and AI-powered automation solutions. Building at the intersection of 
      data engineering and generative AI — from Snowflake pipelines to self-healing AI agents.
    </p>
    <div class="hero-btns">
      <a href="mailto:ashikroshan261@gmail.com" class="btn-primary">✉ Get in Touch</a>
      <a href="https://github.com/AshikRoshan-github" target="_blank" class="btn-outline">⌥ GitHub</a>
      <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank" class="btn-outline">in LinkedIn</a>
      <a href="https://medium.com/@ashikroshan261" target="_blank" class="btn-outline">✍ Medium</a>
    </div>
    <div class="hero-stats">
      <div class="stat-item"><span class="stat-num">2+</span><span class="stat-label">Years Experience</span></div>
      <div class="stat-item"><span class="stat-num">14+</span><span class="stat-label">Projects Delivered</span></div>
      <div class="stat-item"><span class="stat-num">7</span><span class="stat-label">Spot Awards</span></div>
      <div class="stat-item"><span class="stat-num">MVP</span><span class="stat-label">2024–25 Award</span></div>
      <div class="stat-item"><span class="stat-num">9</span><span class="stat-label">Certifications</span></div>
    </div>
  </div>
</div>

<div class="contact-strip">
  <a href="mailto:ashikroshan261@gmail.com" class="contact-item">
    <span class="contact-dot"></span> ashikroshan261@gmail.com
  </a>
  <a href="https://github.com/AshikRoshan-github" target="_blank" class="contact-item">
    <span class="contact-dot"></span> github.com/AshikRoshan-github
  </a>
  <a href="https://www.linkedin.com/in/ashik-roshan-i-073897249" target="_blank" class="contact-item">
    <span class="contact-dot"></span> linkedin.com/in/ashik-roshan-i
  </a>
  <a href="https://medium.com/@ashikroshan261" target="_blank" class="contact-item">
    <span class="contact-dot"></span> medium.com/@ashikroshan261
  </a>
</div>
""", unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-alt"><div class="section-inner" id="skills">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">What I Work With</div>
<div class="section-title">Technical Skills</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

skills = [
    ("Languages", ["Python", "SQL", "JavaScript", "HTML", "CSS"]),
    ("Cloud – Azure", ["Azure Blob Storage", "Data Lake", "SQL Database", "Azure OpenAI", "Databricks", "ADF", "Azure VM"]),
    ("Cloud – AWS", ["S3", "Lambda", "Glue", "Step Functions", "EC2", "CloudWatch", "Textract", "Bedrock"]),
    ("Data Engineering", ["PySpark", "DBT", "Informatica", "Snowflake", "Pandas", "ADF"]),
    ("Databases & Admin", ["SSMS", "pgAdmin", "MySQL", "Oracle", "SQL Server", "Snowflake"]),
    ("BI & Analytics", ["Power BI", "ThoughtSpot", "Plotly", "Streamlit"]),
    ("AI & GenAI", ["Azure OpenAI", "Amazon Bedrock", "Gemini 2.5 Pro", "LangChain", "Neo4j", "RAG", "Prompt Engineering", "Azure Document Intelligence"]),
    ("Automation & Web", ["Selenium", "Web Scraping", "Web Crawling", "FastAPI", "PyAutoGUI", "Apify", "Flask"]),
    ("DevOps & Tools", ["GitHub", "Azure DevOps", "CI/CD", "PuTTY", "ServiceNow", "Rally", "SharePoint"]),
    ("Libs & Frameworks", ["asyncio", "PyVis", "PyPDF2", "pyodbc", "Snowflake Connector", "xmltodict", "smtplib"]),
]

cards_html = '<div class="skills-grid">'
for cat, tags in skills:
    tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in tags)
    cards_html += f"""
    <div class="skill-card">
        <div class="skill-cat">{cat}</div>
        <div class="skill-tags">{tags_html}</div>
    </div>"""
cards_html += "</div>"
st.markdown(cards_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
st.markdown('<div class="section" id="experience">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">Career Journey</div>
<div class="section-title">Professional Experience</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

experience = [
    ("Data Engineer – L2", "Optisol Business Solutions", "April 2025 – Present"),
    ("Data Engineer – L1", "Optisol Business Solutions", "August 2024 – March 2025"),
    ("Data Engineer Intern – L0", "Optisol Business Solutions", "March 2024 – July 2024"),
    ("Trainee – Software Engineer", "Blue Cloud", "June 2023 – March 2024"),
]

timeline_html = '<div class="timeline">'
for role, company, date in experience:
    timeline_html += f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-header">
            <div class="timeline-role">{role}</div>
            <div class="timeline-date">{date}</div>
        </div>
        <div class="timeline-company">{company}</div>
    </div>"""
timeline_html += "</div>"
st.markdown(timeline_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── DATA ENGINEERING PROJECTS ─────────────────────────────────────────────────
st.markdown('<div class="section-alt"><div class="section-inner" id="projects">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">What I've Built</div>
<div class="section-title">Data Engineering Projects</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

de_projects = [
    ("#1", "Python-Based Data Migration: Google Sheets → Azure SQL Database",
     "Data Engineer", "Internal Business Team | Optisol",
     ["Python", "Pandas", "gspread", "pyodbc", "Azure SQL", "Azure VM", "Cron Jobs", "GitHub"],
     "Designed and implemented a lightweight, cost-effective ETL solution extracting structured datasets from Google Sheets and loading into Azure SQL Database with full & incremental load logic."),
    ("#2", "On-Premises to Snowflake Data Warehouse Migration",
     "Data Engineer", "Republic Services | Optisol",
     ["Snowflake", "Informatica", "dbt", "Oracle", "SQL Server", "AWS Step Functions", "CloudWatch", "SSMS", "PuTTY"],
     "Led migration of 6 on-premises source systems to Snowflake cloud data warehouse with automated workflow orchestration and real-time monitoring on AWS."),
    ("#3", "Enterprise Database Migration: Oracle → SQL Server (On-Premises)",
     "Data Engineer", "Republic Services | Optisol",
     ["Oracle", "SQL Server", "Python", "Autogen ETL", "T-SQL", "SharePoint", "ServiceNow", "GitHub"],
     "Delivered structured enterprise migration using internally developed Autogen ETL framework, ensuring accurate schema conversion across Test and Production environments."),
    ("#4", "API-Driven Data Migration: Podio → Azure SQL Database",
     "Data Engineer", "Jiffy – Cultural Exchange | Optisol",
     ["Python", "REST API", "Pandas", "ADF", "Azure SQL", "Azure Blob", "AzCopy", "GitHub"],
     "API-driven migration solution extracting Podio data via REST APIs, transforming with ADF pipelines, and bulk-loading into Azure SQL with fast_executemany optimization."),
]

grid_html = '<div class="projects-grid">'
for num, title, role, client, tech, desc in de_projects:
    tags = "".join(f'<span class="tech-tag">{t}</span>' for t in tech)
    grid_html += f"""
    <div class="project-card">
        <div class="project-num">{num}</div>
        <div class="project-title">{title}</div>
        <div class="project-meta">Role: <span>{role}</span></div>
        <div class="project-meta">Client: <span>{client}</span></div>
        <p style="font-size:13px;color:#555;line-height:1.6;margin-top:10px;">{desc}</p>
        <div class="project-tech">{tags}</div>
    </div>"""
grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── AI & AUTOMATION PROJECTS ──────────────────────────────────────────────────
st.markdown('<div class="section" id="ai-projects">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">AI Engineering</div>
<div class="section-title">AI & Automation Projects</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

ai_projects = [
    ("#1", "Automated Web Data Extraction & Reporting Platform",
     "Automation Engineer", "IBEAM – Internal | Optisol",
     ["Selenium", "PyAutoGUI", "smtplib", "Chrome WebDriver", "Azure DevOps"],
     "End-to-end browser automation for data extraction, report generation, and automated email distribution — reducing manual effort with scheduled unattended execution."),
    ("#2", "AI-Driven Web Scraping with LangChain & Apify",
     "Automation Engineer", "IBEAM – Internal | Optisol",
     ["Python", "LangChain", "Apify", "REST APIs", "GitHub"],
     "AI-enabled web scraping integrating Apify cloud Actors with LangChain, transforming scraped content into LLM-ready format with automated orchestration."),
    ("#3", "AI-Powered Automated Data Profiling Platform",
     "Data & AI Engineer", "IBEAM – Internal | Optisol",
     ["Python", "Azure OpenAI", "Snowflake", "Streamlit", "Prompt Engineering"],
     "AI platform analyzing datasets across heterogeneous sources, generating intelligent summaries and anomaly detection insights via Azure OpenAI and interactive Streamlit dashboards."),
    ("#4", "AI Pandas Code Generation & Self-Healing Transformation Agent",
     "Data & AI Engineer", "IBEAM – Internal | Optisol",
     ["Python", "Azure OpenAI", "Pandas", "JSON", "Prompt Engineering"],
     "AI-driven agent generating Python transformation scripts from natural language with a self-healing loop — detects runtime errors, re-prompts the LLM, and auto-regenerates corrected code."),
    ("#5", "Ontology Kit – Data Mapping Agent",
     "Data & AI Engineer", "IBEAM – Internal | Optisol",
     ["Python", "Gemini 2.5 Pro", "Streamlit", "Pandas", "PyODBC"],
     "AI-driven ontology mapping tool reducing manual mapping effort by 40–50% with protocol-based mapping, domain understanding, and automatic metadata generation."),
    ("#6", "AI-Powered Document Processing & Data Extraction Tool",
     "AI Engineer", "Republic Services Hackathon | Optisol",
     ["AWS Textract", "Amazon Bedrock", "EC2", "S3", "Flask", "Prompt Engineering"],
     "Automated document processing converting scanned PDFs/images to structured JSON using Textract for extraction and Bedrock for semantic structuring via foundation models."),
    ("#7", "Internationalization HTML Validation & Automation Tool",
     "AI / Data Engineer", "Optisol Business Solutions",
     ["Python", "HTML Parsing", "i18n", "JSON", "CLI Automation"],
     "Tool analyzing HTML files for i18n readiness, detecting hard-coded strings, and generating structured JSON reports for localization gaps — cutting manual inspection effort significantly."),
    ("#8", "Automated Internationalization Workflow",
     "Automation Engineer", "IBEAM – Internal | Optisol",
     ["Python", "i18n", "Automation Scripts", "JSON", "Batch Processing"],
     "Automation framework managing and validating i18n files across multiple languages with batch processing and CI/CD integration for synchronized translation management."),
    ("#9", "Credit Risk Reporting & JSON Data Intelligence Platform",
     "Data & AI Engineer", "Atradius – Trade Credit Insurance | Optisol",
     ["Python", "Gemini 2.5 Pro", "asyncio", "Plotly", "JSON", "CLI Automation"],
     "End-to-end JSON pipeline mapping 40+ credit risk blocks with custom async rate limiter, section-based LLM prompting, and parallel requests via asyncio.gather for high throughput."),
    ("#10", "Knowledge Graph Builder (KGB) with RAG",
     "Data & AI Engineer", "Internal Platform | Optisol",
     ["Python", "LangChain", "Azure OpenAI", "Neo4j", "PyVis", "Streamlit", "asyncio"],
     "Full-stack Streamlit app transforming unstructured data into interactive knowledge graphs with Neo4j storage, RAG query layer, and physics-simulated PyVis visualizations."),
]

grid_html = '<div class="projects-grid">'
for num, title, role, client, tech, desc in ai_projects:
    tags = "".join(f'<span class="tech-tag">{t}</span>' for t in tech)
    grid_html += f"""
    <div class="project-card">
        <div class="project-num">{num}</div>
        <div class="project-title">{title}</div>
        <div class="project-meta">Role: <span>{role}</span></div>
        <div class="project-meta">Client: <span>{client}</span></div>
        <p style="font-size:13px;color:#555;line-height:1.6;margin-top:10px;">{desc}</p>
        <div class="project-tech">{tags}</div>
    </div>"""
grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── AWARDS ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-alt"><div class="section-inner" id="awards">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">Recognition</div>
<div class="section-title">Awards & Achievements</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

awards = [
    ("🏆", "Most Valuable Person (MVP) Award", "2024–2025",
     "Highest organizational honor for consistent performance excellence, cross-functional leadership, and significant contributions toward the company's long-term vision and project success."),
    ("⭐", "Spot Award – Project Excellence & Leadership", "Jan 2026",
     "Awarded by the CTO for mature professional handling of project success and fostering a culture of colleague recognition."),
    ("⭐", "Spot Award – RS ARP Project Go-Live", "Nov 2025",
     "Recognized for exceptional contribution to the 'Beatty Go-Live' rollout and managing complex 'Delta Load' activities under tight timelines."),
    ("⭐", "Spot Award – AI Tool Innovation (NotebookLLM)", "May 2025",
     "Took initiative to evaluate, demo, and drive team adoption of NotebookLLM to enhance project efficiency."),
    ("⭐", "Spot Award – Community Mentorship", "Mar 2025",
     "Delivered technical sessions for college students on interview preparation and emerging technologies."),
    ("⭐", "OKR Top Contributor (Q4)", "Oct–Dec 2024",
     "Honored for playing a pivotal role in attaining company-wide Objectives and Key Results (OKRs)."),
    ("⭐", "Spot Award – Client Excellence (Ontology Mapping)", "Dec 2024",
     "Received high praise from client for solution-oriented presentation on Ontology Mapping during an on-site visit."),
    ("⭐", "Spot Award – Gen AI & Automation", "July 2024",
     "Implemented Generative AI solution to automate data inventory and served as SME resolving DBT blockers."),
]

grid_html = '<div class="awards-grid">'
for icon, title, year, desc in awards:
    grid_html += f"""
    <div class="award-card">
        <span class="award-icon">{icon}</span>
        <div class="award-title">{title}</div>
        <span class="award-year">{year}</span>
        <div class="award-desc">{desc}</div>
    </div>"""
grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
st.markdown('<div class="section" id="certifications">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">Credentials</div>
<div class="section-title">Certifications</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

certs = [
    ("❄️", "SnowPro Core Certification", "Snowflake"),
    ("☁️", "Microsoft Certified: Azure Data Fundamentals", "Microsoft"),
    ("🧱", "Databricks Lakehouse Fundamentals", "Databricks"),
    ("🔧", "dbt Learn Fundamentals", "dbt Labs"),
    ("💾", "SQL (Basic) Certificate", "HackerRank"),
    ("🤖", "Generative AI Fundamentals Accreditation", "Databricks"),
    ("🐍", "100 Days of Code: Python Pro Bootcamp", "Udemy"),
    ("❄️", "Snowflake Masterclass", "Udemy"),
]

cert_html = '<div class="cert-grid">'
for icon, name, issuer in certs:
    cert_html += f"""
    <div class="cert-card">
        <div class="cert-icon">{icon}</div>
        <div>
            <div class="cert-name">{name}</div>
            <div class="cert-issuer">{issuer}</div>
        </div>
    </div>"""
cert_html += "</div>"
st.markdown(cert_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-alt"><div class="section-inner" id="education">', unsafe_allow_html=True)
st.markdown("""
<div class="section-label">Academic Background</div>
<div class="section-title">Education</div>
<div class="section-divider"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="edu-card">
    <div class="edu-degree">Bachelor of Engineering in Computer Science</div>
    <div class="edu-school">KLN College of Engineering</div>
    <div class="edu-meta">
        <span>2019 – 2023</span>
        <span>Grade: A+</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>Ashik Roshan I</strong> &nbsp;·&nbsp; Data Engineer – L2 &nbsp;·&nbsp; AI Engineer<br>
    <span style="margin-top:8px;display:inline-block;">
        ashikroshan261@gmail.com &nbsp;·&nbsp; 
        github.com/AshikRoshan-github &nbsp;·&nbsp; 
        medium.com/@ashikroshan261
    </span><br>
    <span style="margin-top:8px;display:inline-block;font-size:11px;color:#555;">
        Built with ❤️ using Streamlit &nbsp;·&nbsp; © 2025 Ashik Roshan I
    </span>
</div>
""", unsafe_allow_html=True)
