import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘", page_icon="💘", layout="centered")

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        background: #ffe4ef !important;
      }
      .block-container { padding-top: 0.8rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# GIF z misiami (podmień na dowolny, jeśli chcesz inny)
BEARS_GIF_URL = "https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif"
# Ekran końcowy (może być ten sam albo inny)
FINAL_GIF_URL = "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"

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

  /* CENTROWANIE CAŁEJ ZAWARTOŚCI */
  .wrap {{
    min-height: 85vh;
    display: grid;
    place-items: center;
    padding: 18px 0 28px;
  }}

  .panel {{
    width: min(860px, 96vw);
    text-align: center;
    position: relative;
  }}

  /* Animowane serduszka w tle */
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
    100% {{ transform: translateY(-240px); opacity: 0; }}
  }}

  .bears {{
    margin: 0 auto 14px;
    width: min(320px, 70vw);
    border-radius: 18px;
  }}

  h1 {{
    margin: 0 0 18px 0;
    font-size: clamp(26px, 3.1vw, 40px);
    color: var(--title);
    font-weight: 900;
  }}

  /* Przestrzeń nad przyciskami żeby YES mógł rosnąć w dół */
  .spacer {{
    height: 8px;
  }}

  .btnRow {{
    display: flex;
    justify-content: center;
    gap: 14px;
    align-items: center;
    margin-top: 6px;
    /* ważne: pozwala rosnąć bez wchodzenia na tytuł */
    padding-top: 10px;
  }}

  button {{
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 800;
    box-shadow: 0 8px 18px rgba(0,0,0,0.12);
  }}

  #yesBtn {{
    background: var(--yes);
    color: #fff;
    padding: 12px 30px;
    font-size: 18px;
    transform-origin: top center; /* rośnie w dół */
    transition: transform 120ms ease;
  }}

  #noBtn {{
    background: var(--no);
    color: #fff;
    padding: 12px 30px;
    font-size: 18px;
  }}

  .hint {{
    margin-top: 12px;
    color: rgba(0,0,0,0.55);
    font-size: 13px;
    font-weight: 600;
  }}

  .final {{
    display: none;
    text-align: center;
  }}

  .final h2 {{
    margin: 0 0 12px 0;
    font-size: clamp(26px, 3.2vw, 42px);
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
      <!-- SERDUSZKA (wygenerujemy też dodatkowe w JS) -->
      <div class="float-heart" style="left: 8%; top: 240px; animation-delay: 0s;">💗</div>
      <div class="float-heart" style="left: 22%; top: 260px; animation-delay: 1s;">💖</div>
      <div class="float-heart" style="left: 78%; top: 250px; animation-delay: 0.6s;">💗</div>
      <div class="float-heart" style="left: 90%; top: 270px; animation-delay: 1.4s;">💖</div>

      <div class="question" id="questionBox">
        <img class="bears" src="{BEARS_GIF_URL}" alt="misie z serduszkami" />
        <h1>Kochanie, zostaniesz moją walentynką?</h1>

        <div class="spacer"></div>

        <div class="btnRow" id="btnRow">
          <button id="yesBtn" type="button">Tak</button>
          <button id="noBtn" type="button">Nie</button>
        </div>

        <div class="hint" id="hint">Kliknij… tylko dobrze wybierz 😈</div>
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
  const finalBox = document.getElementById("finalBox");
  const questionBox = document.getElementById("questionBox");
  const hint = document.getElementById("hint");

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
  let scale = 1.0;

  function maybeFullscreen() {{
    if (scale >= 4.0) {{
      // fullscreen dopiero na końcu
      yesBtn.style.position = "fixed";
      yesBtn.style.left = "0";
      yesBtn.style.top = "0";
      yesBtn.style.width = "100vw";
      yesBtn.style.height = "100vh";
      yesBtn.style.borderRadius = "0";
      yesBtn.style.fontSize = "min(22vw, 220px)";
      yesBtn.style.zIndex = "9999";
      yesBtn.style.display = "flex";
      yesBtn.style.alignItems = "center";
      yesBtn.style.justifyContent = "center";
      noBtn.style.display = "none";
      hint.textContent = "No weź… 😌";
    }}
  }}

  noBtn.addEventListener("click", () => {{
    clicks += 1;

    // rośnij, ale nie zasłaniaj tytułu (origin ustawiony na top)
    if (scale < 2.2) scale += 0.22;
    else if (scale < 3.2) scale += 0.32;
    else scale += 0.45;

    yesBtn.style.transform = `scale(${{scale}})`;

    const idx = Math.min(clicks, noTexts.length - 1);
    noBtn.textContent = noTexts[idx];

    maybeFullscreen();
  }});

  yesBtn.addEventListener("click", () => {{
    // pokaż finał
    questionBox.style.display = "none";
    finalBox.style.display = "block";

    // zwolnij fullscreen jeśli był
    yesBtn.style.position = "static";
    yesBtn.style.width = "";
    yesBtn.style.height = "";
    yesBtn.style.borderRadius = "8px";
    yesBtn.style.fontSize = "18px";
    yesBtn.style.transform = "scale(1)";
    yesBtn.style.zIndex = "";
  }});

  // Dodatkowe pływające serduszka (losowo)
  const panel = document.getElementById("panel");
  function spawnHeart() {{
    const h = document.createElement("div");
    h.className = "float-heart";
    h.textContent = Math.random() > 0.5 ? "💗" : "💖";
    h.style.left = Math.floor(Math.random() * 95) + "%";
    h.style.top = "330px";
    h.style.animationDuration = (4 + Math.random() * 3) + "s";
    h.style.opacity = 0.4 + Math.random() * 0.35;
    panel.appendChild(h);
    setTimeout(() => h.remove(), 7000);
  }}
  setInterval(spawnHeart, 700);
</script>
</body>
</html>
"""

components.html(html, height=720)
