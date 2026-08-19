"""
Local preview harness for the Kleos Georgia contractor guide.

The page is laid out for a fixed 1440px canvas matching the Figma frame, and the
stylesheet has no breakpoints. This harness pins that width so what you see is
what the design specifies, and reports the guard checks that matter when editing:
stylesheet integrity and the container budgets that clip silently.

    streamlit run streamlit_app.py
"""

import hashlib
import pathlib
import re

import streamlit as st
import streamlit.components.v1 as components

PAGE = pathlib.Path(__file__).parent / "index.html"

CANVAS_WIDTH = 1440
CANVAS_HEIGHT = 12000  # taller than the page; the iframe does not scroll itself

# Stylesheet fingerprint. The <style> block is never edited; if either of these
# fails, something has modified it and the Figma mapping is no longer reliable.
CSS_LEN = 34739
CSS_SHA256_PREFIX = "d90ba6727a31632d"


def load() -> str:
    if not PAGE.exists():
        st.error(f"index.html not found next to this script (looked in {PAGE.parent}).")
        st.stop()
    return PAGE.read_text(encoding="utf-8")


def stylesheet(html: str) -> str:
    try:
        return html.split("<style>")[1].split("</style>")[0]
    except IndexError:
        st.error("No <style> block found in index.html.")
        st.stop()


def checks(html: str) -> list[tuple[bool, str]]:
    css = stylesheet(html)
    digest = hashlib.sha256(css.encode()).hexdigest()

    visible = re.sub(r"<style.*?</style>", "", html, flags=re.S)
    visible = re.sub(r"<script.*?</script>", "", visible, flags=re.S)
    visible = re.sub(r"<!--.*?-->", "", visible, flags=re.S)

    # tag balance, ignoring void elements
    void = {"meta", "br", "rect", "path", "circle", "input", "img", "link", "hr"}
    counts: dict[str, int] = {}
    for closing, tag in re.findall(r"<(/?)([a-zA-Z][\w-]*)", visible):
        counts[tag] = counts.get(tag, 0) + (-1 if closing else 1)
    unbalanced = {t: n for t, n in counts.items() if n and t not in void}

    tabs = len(re.findall(r'class="calc__tab[" ]', html))
    beats = len(re.findall(r'class="tl"', html))
    signals = html.count('class="chk"')
    faqs = html.count('class="faq-item"')

    return [
        (len(css) == CSS_LEN, f"stylesheet length {len(css)} (expected {CSS_LEN})"),
        (digest.startswith(CSS_SHA256_PREFIX), f"stylesheet sha256 {digest[:16]}"),
        (not unbalanced, f"tag balance {unbalanced or 'ok'}"),
        (html.count("<section") == html.count("</section>"),
         f"sections {html.count('<section')} open / {html.count('</section>')} closed"),
        (tabs == 3, f"calculator tabs {tabs} (budget 3: 409px each in a 1260px inner)"),
        (beats == 4, f"timeline beats {beats} (budget 4: .yearlife is 1299px, overflow hidden)"),
        (signals == 10, f"checklist signals {signals} (count also appears 3x in the script)"),
        (faqs == 9, f"FAQ items {faqs}"),
        ("VAT" not in visible, "no VAT references in visible copy"),
        ("Armenia" not in html, "no Armenia references left"),
        ("\u20be" not in html and "&#8382;" not in html, "no lari glyphs (page displays USD)"),
    ]


st.set_page_config(page_title="Kleos — Georgia contractor guide", layout="wide")

html = load()

with st.sidebar:
    st.subheader("Guard checks")
    results = checks(html)
    for ok, label in results:
        st.write(("✅ " if ok else "❌ ") + label)

    failed = [label for ok, label in results if not ok]
    if failed:
        st.error(f"{len(failed)} check(s) failing. See README before committing.")
    else:
        st.success("All checks passing.")

    st.divider()
    st.caption(
        f"{PAGE.name} — {len(html):,} bytes\n\n"
        f"Rendered at a fixed {CANVAS_WIDTH}px. The stylesheet has no "
        f"breakpoints, so resizing the browser will not reflow the page."
    )
    st.caption("Status: pending legal sign-off. See README → Needs legal review.")

components.html(html, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, scrolling=True)
