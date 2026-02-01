import streamlit as st

st.set_page_config(page_title="💘", page_icon="💘", layout="centered")

TOP_GIF_URL = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTV1cG9vamdvcWtucm9jYjM2YXY4d2ZkODRvaXR5cmpxODJpaWVmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SxdT4XwbwAAL5byUyq/giphy.gif"
FINAL_GIF_URL = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExem1hNnFyaHM4dzhxbXp5c3VvZzNrZTFtcXRiczh5dXdtOGo0YXlyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ifB1v1W3Db0GIW7uTA/giphy.gif"

START_BG = "#fffec8"   # żółte na start
FINAL_BG = "#ffb6c1"   # róż jak tło gifa po "Tak"

NO_TEXTS = [
    "Nie",
    "Jesteś pewny?",
    "Na pewno??",
    "Będzie mi przykro…",
    "Ostatnia szansa 😳",
    "Nie rób mi tego 🥺",
    "Dobra, kliknij TAK 💖",
]

# --- stan aplikacji ---
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "stage" not in st.session_state:
    st.session_state.stage = "ask"  # ask | final

# --- obsługa klików przez query params (Python widzi klik, więc może zmienić tło całej strony) ---
# Streamlit >= 1.30: st.query_params
try:
    params = st.query_params
    ans = params.get("ans")
except Exception:
    # fallback dla starszych
    ans = st.experimental_get_query_params().get("ans", [None])[0]

if ans:
    if ans == "no" and st.session_state.stage == "ask":
        st.session_state.no_clicks += 1
    elif ans == "yes":
        st.session_state.stage = "final"

    # wyczyść query params, żeby po odświeżeniu nie klikało ponownie
    try:
        st.query_params.clear()
    except Exception:
        st.experimental_set_query_params()

# --- tło globalne (tu znika "ramka") ---
bg = FINAL_BG if st.session_state.stage == "final" else START_BG
st.markdown(
    f"""
    <style>
      html, body, [data-testid="stAppViewContainer"] {{
        background: {bg} !important;
      }}
      .block-container {{
        padding-top: 1.2rem;
        max-width: 900px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- parametry wzrostu przycisku "Tak" ---
n = st.session_state.no_clicks
# rośnięcie: font + padding + szerokość
yes_font = 20 + n * 10
yes_pad_y = 12 + n * 6
yes_pad_x = 34 + n * 14

# po ilu kliknięciach "Nie" robić mega-TAK
mega = n >= 6

no_label = NO_TEXTS[min(n, len(NO_TEXTS) - 1)]

# --- render ---
if st.session_state.stage == "final":
    st.markdown(
        f"""
        <div style="text-align:center;">
          <h2 style="margin:0 0 16px 0; color:#8b1d2c; font-weight:950; font-size: clamp(28px, 3.2vw, 44px);">
            Wiedziałam, że się zgodzisz!! 💖
          </h2>

          <div style="
            background:{FINAL_BG};
            padding: 18px;
            border-radius: 22px;
            display: inline-block;
          ">
            <img src="{FINAL_GIF_URL}" style="
              width: min(560px, 92vw);
              border-radius: 18px;
              box-shadow: 0 14px 30px rgba(0,0,0,0.18);
              display:block;
            "/>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # ekran pytania
    st.markdown(
        f"""
        <div style="text-align:center; position:relative;">
          <img src="{TOP_GIF_URL}" style="
            width: min(340px, 78vw);
            border-radius: 18px;
            margin: 0 auto 12px;
            display:block;
          " />

          <h1 style="
            margin: 0 0 18px 0;
            font-size: clamp(26px, 3.2vw, 40px);
            color: #8b1d2c;
            font-weight: 950;
          ">
            Kochanie, zostaniesz moją walentynką?
          </h1>

          <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap; align-items:center;">

            <!-- TAK (rośnie) -->
            <a href="?ans=yes" style="
              text-decoration:none;
              background:#2e7d32;
              color:white;
              font-weight:900;
              border-radius: 10px;
              box-shadow: 0 10px 20px rgba(0,0,0,0.14);
              display: inline-flex;
              align-items:center;
              justify-content:center;
              font-size: {yes_font}px;
              padding: {yes_pad_y}px {yes_pad_x}px;
              min-width: 140px;
              min-height: 48px;
              {'width: min(900px, 96vw); height: 55vh; font-size: min(18vw, 180px); border-radius: 18px;' if mega else ''}
            ">
              Tak
            </a>

            <!-- NIE -->
            <a href="?ans=no" style="
              text-decoration:none;
              background:#b71c1c;
              color:white;
              font-weight:900;
              border-radius: 10px;
              box-shadow: 0 10px 20px rgba(0,0,0,0.14);
              display: inline-flex;
              align-items:center;
              justify-content:center;
              font-size: 18px;
              padding: 12px 26px;
              min-width: 120px;
              min-height: 48px;
              {'display:none;' if mega else ''}
            ">
              {no_label}
            </a>
          </div>

          <div style="margin-top: 12px; color: rgba(0,0,0,0.55); font-weight:700; font-size:13px;">
            Kliknij… tylko dobrze wybierz 😈
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
