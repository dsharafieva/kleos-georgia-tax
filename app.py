import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Kleos — Hiring a contractor in Georgia",
    page_icon="🇬🇪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide default Streamlit chrome so the page renders full-bleed
st.markdown("""
<style>
  #MainMenu, header, footer {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
  [data-testid="stHeader"] {display: none;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

# Height must comfortably exceed the tallest rendered state (all sections
# expanded, RU strings, checklist ticked). Georgia mirrors Serbia's layout —
# a six-flag checklist under the "Keeping the 1%" section.
components.html(html, height=6300, scrolling=True)
