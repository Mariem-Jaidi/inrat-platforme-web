# -*- coding: utf-8 -*-
"""
Feuille de style de la plateforme SIG.

Direction visuelle : outil cartographique institutionnel (type SIG
ministériel), sobre et lisible. Palette ardoise/bleu pétrole avec un seul
accent terre cuite rappelant le contexte agricole. Pas d'effets décoratifs,
pas de dégradés gratuits : la hiérarchie vient de la typographie et de
l'espacement, pas de la couleur.
"""

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap');

:root {
    --ink:        #1B2430;
    --slate:      #3D4A5C;
    --slate-soft: #6B7686;
    --hairline:   #D8DCE2;
    --paper:      #FFFFFF;
    --paper-dim:  #F6F7F9;
    --petrol:     #1F4E5F;
    --petrol-dk:  #163945;
    --terracotta: #B5552E;
    --terracotta-soft: #F4E3D8;
    --ok:         #2E7D4F;
}

html, body, [class*="css"]  {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--ink);
}

/* ---------- Layout shell ---------- */
.block-container {
    padding-top: 1.6rem;
    padding-bottom: 2.5rem;
    max-width: 1320px;
}

/* Kill Streamlit's default top decoration bar color */
[data-testid="stDecoration"] { background-image: none; background-color: var(--petrol); height: 3px; }

/* ---------- Header band ---------- */
.platform-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--hairline);
    padding-bottom: 18px;
    margin-bottom: 6px;
}
.platform-header .eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11.5px;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--terracotta);
    margin-bottom: 6px;
    font-weight: 500;
}
.platform-header h1 {
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--ink);
    margin: 0;
    line-height: 1.25;
}
.platform-header .subtitle-ar {
    font-size: 15px;
    color: var(--slate-soft);
    margin-top: 4px;
    font-weight: 400;
}
.platform-header .header-meta {
    text-align: right;
    font-size: 12.5px;
    color: var(--slate-soft);
    line-height: 1.7;
}
.platform-header .header-meta .org {
    color: var(--ink);
    font-weight: 600;
    font-size: 13.5px;
}

/* ---------- Section labels ---------- */
.section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--petrol);
    font-weight: 500;
    margin: 0 0 10px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--hairline);
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background-color: var(--paper-dim);
    border-right: 1px solid var(--hairline);
}
section[data-testid="stSidebar"] .block-container { padding-top: 1.4rem; }
section[data-testid="stSidebar"] h3 {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--petrol);
    font-weight: 500;
    margin-top: 1.4rem;
    margin-bottom: 0.5rem;
}
.sidebar-brand {
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 17px;
    font-weight: 600;
    color: var(--ink);
    padding-bottom: 12px;
    border-bottom: 1px solid var(--hairline);
    margin-bottom: 4px;
}
.sidebar-brand small {
    display: block;
    font-family: 'Inter', sans-serif;
    font-size: 11.5px;
    font-weight: 400;
    color: var(--slate-soft);
    margin-top: 3px;
}

/* ---------- Cards / info panels ---------- */
.info-card {
    background: var(--paper);
    border: 1px solid var(--hairline);
    border-radius: 3px;
    padding: 14px 16px;
    margin-bottom: 12px;
}
.info-card .card-title {
    font-size: 12px;
    font-weight: 600;
    color: var(--slate);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 8px;
}
.region-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--paper-dim);
    border: 1px solid var(--hairline);
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 12.5px;
    color: var(--slate);
    font-weight: 500;
}
.region-pill.active {
    background: var(--petrol);
    border-color: var(--petrol);
    color: #fff;
}
.status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
}
.status-dot.ok { background: var(--ok); }
.status-dot.pending { background: var(--terracotta); }

.data-banner {
    border-left: 3px solid var(--terracotta);
    background: var(--terracotta-soft);
    padding: 10px 14px;
    font-size: 13px;
    color: #5C3A24;
    border-radius: 0 3px 3px 0;
    margin: 10px 0 16px 0;
    line-height: 1.5;
}
.data-banner b { color: #45290F; }

/* ---------- Legend ---------- */
.legend-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 5px 0;
    font-size: 13px;
    color: var(--slate);
}
.legend-swatch {
    width: 22px;
    height: 14px;
    border-radius: 2px;
    border: 1px solid rgba(0,0,0,0.08);
    flex-shrink: 0;
}

/* ---------- Metrics ---------- */
[data-testid="stMetric"] {
    background: var(--paper);
    border: 1px solid var(--hairline);
    border-radius: 3px;
    padding: 12px 14px 10px 14px;
}
[data-testid="stMetricLabel"] { font-size: 12px; color: var(--slate-soft); }
[data-testid="stMetricValue"] { font-family: 'IBM Plex Mono', monospace; font-size: 22px; color: var(--ink); }

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 22px; border-bottom: 1px solid var(--hairline); }
.stTabs [data-baseweb="tab"] {
    font-size: 13.5px;
    font-weight: 500;
    color: var(--slate-soft);
    padding: 8px 2px;
}
.stTabs [aria-selected="true"] { color: var(--petrol) !important; }
.stTabs [data-baseweb="tab-highlight"] { background-color: var(--petrol) !important; }

/* ---------- Buttons / selects ---------- */
.stSelectbox label, .stCheckbox label, .stRadio label { font-size: 13px; color: var(--slate); font-weight: 500; }

button[kind="primary"], button[kind="secondary"] {
    border-radius: 3px;
}

/* ---------- Text visibility fix (checkboxes, radios, selects, all sidebar text) ----------
   Streamlit wraps every widget's visible caption in a container with
   data-testid="stWidgetLabel" (confirmed from the installed Streamlit 1.58
   frontend bundle), with the text itself inside a nested <p>. That text
   inherits a light, dark-theme-only color which disappears on this light
   background. Target that testid directly rather than guessing at classes. */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
[data-testid="stWidgetLabel"] div,
[data-testid="stCheckbox"] [data-testid="stWidgetLabel"] p,
[data-testid="stRadio"] [data-testid="stWidgetLabel"] p,
[data-testid="stSelectbox"] [data-testid="stWidgetLabel"] p {
    color: var(--ink) !important;
}

/* Belt-and-suspenders: force readable text on every element inside the
   sidebar, regardless of which container Streamlit uses internally. */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: var(--ink) !important;
}
section[data-testid="stSidebar"] .section-label,
section[data-testid="stSidebar"] h3 {
    color: var(--petrol) !important;
}
section[data-testid="stSidebar"] .sidebar-brand small,
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: var(--slate-soft) !important;
}
section[data-testid="stSidebar"] .region-pill.active,
section[data-testid="stSidebar"] .region-pill.active * {
    color: #fff !important;
}

/* BaseWeb checkbox / radio tick marks: keep them readable against the light bg */
[data-testid="stCheckbox"] svg, [data-testid="stRadio"] svg {
    color: var(--petrol);
}

/* Selectbox closed-state value text and dropdown menu options */
[data-baseweb="select"] * {
    color: var(--ink) !important;
}
[data-baseweb="popover"] li, [data-baseweb="popover"] div {
    color: var(--ink) !important;
}

/* ---------- Footer ---------- */
.platform-footer {
    margin-top: 36px;
    padding-top: 14px;
    border-top: 1px solid var(--hairline);
    font-size: 11.5px;
    color: var(--slate-soft);
    display: flex;
    justify-content: space-between;
}

/* ---------- Misc tightening ---------- */
hr { border-color: var(--hairline); margin: 1.2rem 0; }
.streamlit-expanderHeader { font-size: 13px; font-weight: 500; color: var(--slate); }
</style>
"""