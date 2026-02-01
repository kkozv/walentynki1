import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘", page_icon="💘", layout="centered")

st.markdown(
    """
    <style>
     html, body, [data-testid="stAppViewContainer"] { background: #fffec8 !important; }
      .block-container { padding-top: 0.6rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

TOP_GIF_URL = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTV1cG9vamdvcWtucm9jYjM2YXY4d2ZkODRvaXR5cmpxODJpaWVmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SxdT4XwbwAAL5byUyq/giphy.gif"

FINAL_GIF_URL = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExem1hNnFyaHM4dzhxbXp5c3VvZzNrZTFtcXRiczh5dXdtOGo0YXlyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ifB1v1W3Db0GIW7uTA/giphy.gif"

html = f"""
<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root {{
    --bg: #ffe4ef;
    --title: #8b1d2c;
    --yes: #2e7d32;
    --no: #b71c1c;
  }}

  body {{
    margin: 0;
    background: transparent;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }}

  .wrap {{
    min-height: 82vh;
    display: grid;
    place-items: center;
    padding: 12px 0 24px;
  }}

  .panel {{
    width: min(820px, 96vw);
    position: relative;
    text-align: center;
  }}

  .float-heart {{
    position: absolute;
    font-size: 18px;
    opacity: 0.55;
    animation: floatUp 6s linear infinite;
    user-select: none;
    pointer-events: none;
  }}

  @keyframes floatUp {{
    0%   {{ transform: translateY(40px); opacity: 0; }}
    10%  {{ opacity: 0.55; }}
    100% {{ transform: translateY(-260px); opacity: 0; }}
  }}

  img.top {{
    width: min(320px, 75vw);
    border-radius: 18px;
    margin: 0 auto 12px;
    display: block;
  }}

  h1 {{
    margin: 0 0 18px 0;
    font-size: clamp(26px, 3.2vw, 40px);
    color: var(--title);
    font-weight: 950;
  }}

  .controls {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    margin-top: 8px;
  }}

  .btnRow {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
  }}

  button {{
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 900;
    box-shadow: 0 10px 20px rgba(0,0,0,0.14);
  }}

  #yesBtn {{
    background: var(--yes);
    color: #fff;
    padding: 12px 34px;
    font-size: 20px;
    min-width: 140px;
    min-height: 48px;
  }}

  #noBtn {{
    background: var(--no);
    color: #fff;
    padding: 12px 26px;
    font-size: 18px;
    min-width: 120px;
    min-height: 48px;
  }}

  .hint {{
    color: rgba(0,0,0,0.55);
    font-size: 13px;
    font-weight: 700;
  }}

  .overlay {{
    position: absolute;
    inset: 0;
    background: var(--yes);
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    border-radius: 18px;
    padding: 22px;
  }}

  .overlay .bigYes {{
    color: white;
    font-weight: 1000;
    font-size: clamp(72px, 16vw, 180px);
  }}

  .overlay .sub {{
    color: rgba(255,255,255,0.9);
    font-weight: 800;
    margin-bottom: 14px;
  }}

  .final {{
    display: none;
    margin-top: 12px;
    background: #ffb6c1;
    padding: 20px;
    border-radius: 20px;
  }}

  .final h2 {{
    margin: 0 0 12px 0;
    font-size: clamp(26px, 3.1vw, 42px);
    color: var(--title);
    font-weight: 950;
  }}

  .final img {{
    width: min(520px, 92vw);
    border-radius: 16px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.18);
  }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="panel" id="panel">

      <div class="float-heart" style="left: 10%; top: 320px;">💗</div>
      <div class="float-heart" style="left: 22%; top: 340px;">💖</div>
      <div class="float-heart" style="left: 78%; top: 330px;">💗</div>
      <div class="float-heart" style="left: 90%; top: 350px;">💖</div>

      <div id="questionBox">
        <img class="top" src="{TOP_GIF_URL}" alt="gif" />
        <h1>Kochanie, zostaniesz moją walentynką?</h1>

        <div class="controls">
          <div class="btnRow" id="btnRow">
            <button id="yesBtn" type="button">Tak</button>
            <button id="noBtn" type="button">Nie</button>
          </div>
          <div class="hint" id="hint">Kliknij… tylko dobrze wybierz 😈</div>
        </div>
      </div>

      <div class="overlay" id="overlay">
        <div class="bigYes">TAK</div>
        <div class="sub">No i elegancko 💖</div>
        <button id="overlayYes" type="button"
                style="background:#fff;color:#1b1b1b;padding:12px 18px;border-radius:10px;font-weight:900;">
          Kliknij tu 💘
        </button>
      </div>

      <div class="final" id="finalBox">
        <h2>Wiedziałam, że się zgodzisz!! 💖</h2>
        <img src="{FINAL_GIF_URL}" alt="final" />
      </div>
    </div>
  </div>

<script>
  const yesBtn = document.getElementById("yesBtn");
  const noBtn = document.getElementById("noBtn");
  const hint = document.getElementById("hint");

  const questionBox = document.getElementById("questionBox");
  const finalBox = document.getElementById("finalBox");

  const overlay = document.getElementById("overlay");
  const overlayYes = document.getElementById("overlayYes");

  const noTexts = [
    "Nie",
    "Jesteś pewny?",
    "Na pewno??",
    "Będzie mi przykro…",
    "Ostatnia szansa 😳",
    "Nie rób mi tego 🥺",
    "Dobra, kliknij TAK 💖"
  ];

  let clicks = 0;

  function growYes() {{
    const baseFont = 20;
    const basePadY = 12;
    const basePadX = 34;
    const baseMinW = 140;
    const baseMinH = 48;

    const step = clicks;
    const font = baseFont + step * 10;
    const padY = basePadY + step * 6;
    const padX = basePadX + step * 14;
    const minW = baseMinW + step * 60;
    const minH = baseMinH + step * 20;

    yesBtn.style.fontSize = font + "px";
    yesBtn.style.padding = padY + "px " + padX + "px";
    yesBtn.style.minWidth = minW + "px";
    yesBtn.style.minHeight = minH + "px";

    if (step >= 6) {{
      overlay.style.display = "flex";
      document.getElementById("btnRow").style.display = "none";
      hint.textContent = "Dobra… już wiadomo 😌";
    }}
  }}

  noBtn.addEventListener("click", () => {{
    clicks += 1;
    const idx = Math.min(clicks, noTexts.length - 1);
    noBtn.textContent = noTexts[idx];
    growYes();
  }});
function showFinal() {{
    questionBox.style.display = "none";
    overlay.style.display = "none";
    finalBox.style.display = "block";

    // zmiana tła strony PO kliknięciu "Tak"
    document.body.style.background = "#ffb6c1";
}}



  yesBtn.addEventListener("click", showFinal);
  overlayYes.addEventListener("click", showFinal);
</script>
</body>
</html>
"""

components.html(html, height=820)
