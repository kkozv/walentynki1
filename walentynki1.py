import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💘", page_icon="💘", layout="centered")

# Jasnoróżowe tło całej aplikacji
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

# Możesz podmienić na własny obrazek/gif (np. z serduszkami)
FINAL_IMAGE_URL = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"

html = f"""
<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root {{
    --pink-bg: #ffe4ef;
    --title: #8b1d2c;
    --yes: #2e7d32;
    --no: #b71c1c;
    --card: rgba(255,255,255,0.0);
  }}

  body {{
    margin: 0;
    background: transparent;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
    color: #111;
  }}

  .wrap {{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 560px;
    padding: 10px 0;
  }}

  .stage {{
    width: min(860px, 96vw);
    text-align: center;
    background: var(--card);
  }}

  /* Rysunek "misiów" + serduszka (CSS, bez plików) */
  .art {{
    position: relative;
    height: 180px;
    margin-bottom: 10px;
  }}

  .heart {{
    position: absolute;
    width: 14px;
    height: 14px;
    border: 2px solid #d45a73;
    border-radius: 4px;
    transform: rotate(45deg);
    opacity: 0.85;
  }}
  .heart:before, .heart:after {{
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    border: 2px solid #d45a73;
    border-radius: 50%;
  }}
  .heart:before {{ left: -9px; top: 0px; }}
  .heart:after  {{ left: 0px;  top: -9px; }}

  .bear {{
    position: absolute;
    top: 35px;
    left: 50%;
    transform: translateX(-50%);
    width: 220px;
    height: 120px;
  }}

  .b {{
    position: absolute;
    width: 80px;
    height: 80px;
    border: 3px solid #1b1b1b;
    border-radius: 24px;
    background: #fff;
  }}
  .b.left {{ left: 35px; top: 20px; }}
  .b.right {{ right: 35px; top: 20px; transform: rotate(10deg); }}

  .b .eye {{
    position: absolute;
    width: 7px;
    height: 7px;
    background: #1b1b1b;
    border-radius: 50%;
    top: 28px;
  }}
  .b.left .eye.e1 {{ left: 24px; }}
  .b.left .eye.e2 {{ left: 46px; }}
  .b.right .eye.e1 {{ left: 24px; }}
  .b.right .eye.e2 {{ left: 46px; }}

  .b .blush {{
    position: absolute;
    width: 10px; height: 6px;
    background: #ff9fb5;
    border-radius: 6px;
    top: 40px;
  }}
  .b.left .blush.b1 {{ left: 14px; }}
  .b.left .blush.b2 {{ left: 56px; }}
  .b.right .blush.b1 {{ left: 14px; }}
  .b.right .blush.b2 {{ left: 56px; }}

  .nose {{
    position: absolute;
    left: 50%;
    top: 44px;
    width: 12px; height: 10px;
    background: #1b1b1b;
    transform: translateX(-50%);
    border-radius: 0 0 8px 8px;
  }}

  .kiss {{
    position: absolute;
    left: 50%;
    top: 55px;
    width: 44px; height: 28px;
    transform: translateX(-50%);
    border: 3px solid #1b1b1b;
    border-top: 0;
    border-left: 0;
    border-radius: 0 0 18px 0;
    opacity: 0.85;
  }}

  h1 {{
    margin: 0 0 18px 0;
    font-size: clamp(26px, 3.2vw, 38px);
    color: var(--title);
    font-weight: 800;
  }}

  .btnRow {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin-top: 10px;
    flex-wrap: wrap;
  }}

  button {{
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 700;
  }}

  /* Startowe rozmiary jak na screenie */
  #yesBtn {{
    background: var(--yes);
    color: #fff;
    padding: 10px 26px;
    font-size: 16px;
    transform-origin: center;
  }}

  #noBtn {{
    background: var(--no);
    color: #fff;
    padding: 10px 26px;
    font-size: 16px;
  }}

  /* Ekran końcowy */
  .final {{
    display: none;
    margin-top: 10px;
  }}
  .final h2 {{
    margin: 0 0 10px 0;
    font-size: clamp(26px, 3.2vw, 40px);
    color: var(--title);
    font-weight: 900;
  }}
  .final img {{
    width: min(520px, 92vw);
    border-radius: 14px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.18);
  }}

  /* Ukrywanie sekcji pytania po wyborze */
  .question {{
    display: block;
  }}
</style>
</head>
<body>
<div class="wrap">
  <div class="stage">
    <div class="question" id="questionBox">

      <div class="art">
        <!-- serduszka dookoła -->
        <div class="heart" style="left: 40%; top: 15px;"></div>
        <div class="heart" style="left: 60%; top: 20px;"></div>
        <div class="heart" style="left: 30%; top: 65px;"></div>
        <div class="heart" style="left: 70%; top: 70px;"></div>
        <div class="heart" style="left: 45%; top: 105px;"></div>
        <div class="heart" style="left: 58%; top: 115px;"></div>

        <!-- „misie” (prosty rysunek CSS) -->
        <div class="bear">
          <div class="b left">
            <div class="eye e1"></div><div class="eye e2"></div>
            <div class="blush b1"></div><div class="blush b2"></div>
            <div class="nose"></div>
          </div>
          <div class="b right">
            <div class="eye e1"></div><div class="eye e2"></div>
            <div class="blush b1"></div><div class="blush b2"></div>
            <div class="nose"></div>
          </div>
          <div class="kiss"></div>
        </div>
      </div>

      <h1>Kochanie, zostaniesz moją walentynką?</h1>

      <div class="btnRow" id="btnRow">
        <button id="yesBtn" type="button">Tak</button>
        <button id="noBtn" type="button">Nie</button>
      </div>
    </div>

    <div class="final" id="finalBox">
      <h2>Wiedziałam, że się zgodzisz!! 💖</h2>
      <img src="{FINAL_IMAGE_URL}" alt="serduszka" />
    </div>
  </div>
</div>

<script>
  const yesBtn = document.getElementById("yesBtn");
  const noBtn = document.getElementById("noBtn");
  const finalBox = document.getElementById("finalBox");
  const questionBox = document.getElementById("questionBox");
  const btnRow = document.getElementById("btnRow");

  // Teksty które będą się pojawiać na "Nie"
  const noTexts = [
    "Nie",
    "Jesteś pewny?",
    "Na pewno??",
    "Będzie mi przykro...",
    "Ostatnia szansa 😳",
    "Serio wybierasz NIE?",
    "Dobra, już kliknij TAK 💖"
  ];

  let noClicks = 0;
  let scale = 1.0;

  function growYesButton() {
    // rośnij stopniowo, a później agresywniej
    if (scale < 2.2) scale += 0.25;
    else if (scale < 3.2) scale += 0.35;
    else scale += 0.5;

    yesBtn.style.transform = `scale(${scale})`;

    // Gdy bardzo duży - zrób z niego praktycznie cały ekran (jak na trendach)
    if (scale >= 4.2) {
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

      // schowaj "Nie"
      noBtn.style.display = "none";
    }
  }

  noBtn.addEventListener("click", () => {
    noClicks += 1;
    growYesButton();

    // Zmieniaj tekst "Nie"
    const idx = Math.min(noClicks, noTexts.length - 1);
    noBtn.textContent = noTexts[idx];
  });

  yesBtn.addEventListener("click", () => {
    // Pokaż ekran końcowy
    questionBox.style.display = "none";
    finalBox.style.display = "block";

    // jeśli YES jest już fullscreen, to zwolnij go żeby zobaczyć final
    yesBtn.style.position = "static";
    yesBtn.style.width = "";
    yesBtn.style.height = "";
    yesBtn.style.borderRadius = "6px";
    yesBtn.style.fontSize = "16px";
    yesBtn.style.transform = "scale(1)";
    yesBtn.style.zIndex = "";
  });
</script>
</body>
</html>
"""

components.html(html, height=650)
