import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘", page_icon="💘", layout="centered")

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        background: #ffe4ef !important;
      }
      .block-container { padding-top: 2.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

FINAL_IMAGE_URL = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"

html = f"""
<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8" />
<style>
body {{
  margin: 0;
  background: transparent;
  font-family: system-ui, sans-serif;
  text-align: center;
}}

h1 {{
  color: #8b1d2c;
}}

#yesBtn {{
  background: #2e7d32;
  color: white;
  padding: 10px 26px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}}

#noBtn {{
  background: #b71c1c;
  color: white;
  padding: 10px 26px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}}

.final {{
  display: none;
}}

img {{
  width: min(400px, 90vw);
  margin-top: 20px;
}}
</style>
</head>
<body>

<h1>Kochanie, zostaniesz moją walentynką?</h1>

<div id="buttons">
  <button id="yesBtn">Tak</button>
  <button id="noBtn">Nie</button>
</div>

<div class="final" id="finalBox">
  <h2>Wiedziałam, że się zgodzisz!! 💖</h2>
  <img src="{FINAL_IMAGE_URL}">
</div>

<script>
const yesBtn = document.getElementById("yesBtn");
const noBtn = document.getElementById("noBtn");
const finalBox = document.getElementById("finalBox");
const buttons = document.getElementById("buttons");

const noTexts = [
  "Nie",
  "Jesteś pewny?",
  "Na pewno??",
  "Będzie mi przykro...",
  "Ostatnia szansa 😳",
  "Kliknij TAK 💖"
];

let clicks = 0;
let scale = 1;

noBtn.addEventListener("click", () => {{
  clicks += 1;
  scale += 0.4;
  yesBtn.style.transform = `scale(${{scale}})`;

  const idx = Math.min(clicks, noTexts.length - 1);
  noBtn.textContent = noTexts[idx];

  if (scale > 3) {{
    yesBtn.style.position = "fixed";
    yesBtn.style.top = "0";
    yesBtn.style.left = "0";
    yesBtn.style.width = "100vw";
    yesBtn.style.height = "100vh";
    yesBtn.style.fontSize = "20vw";
    noBtn.style.display = "none";
  }}
}});

yesBtn.addEventListener("click", () => {{
  buttons.style.display = "none";
  finalBox.style.display = "block";
}});
</script>

</body>
</html>
"""

components.html(html, height=600)
