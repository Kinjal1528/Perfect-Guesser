
import streamlit as st
import random
import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image filename
set_bg_from_local("Bg_duck.jpeg")  # Change to your actual image name

# 🎯 Page Settings
st.set_page_config(
    page_title="🎯 Perfect Guesser",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "Made with ❤️ by Kinjal",
        "Report a Bug": "mailto:kkinjal_be23@thapar.edu",
        "Get Help": "https://github.com/Kinjal1528"
    }
)

# 🎮 Game State
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.won = False
    st.session_state.games_played = 0
    st.session_state.best_score = None

# 📝 UI
st.markdown("<h1 style='text-align: center; color:gold;'>🎯 Perfect Guesser</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #A0AEC0;'>I'm thinking of a number between <b>1 and 100</b>. Can you guess it?</p>", unsafe_allow_html=True)

# 📊 Scoreboard
st.markdown(f"""
<div style='text-align: center; background-color: #1F2937; padding: 12px; border-radius: 12px; border: 1px solid #4B5563; margin-top: 15px;'>
    <h4 style='color:white;'>📊 Scoreboard</h4>
    <p>🕹️ Games Played: <b>{st.session_state.games_played}</b></p>
    <p>🏆 Best Score: <b>{st.session_state.best_score if st.session_state.best_score is not None else '–'}</b> attempts</p>
    <p>🎯 Current Attempts: <b>{st.session_state.guesses}</b></p>
</div>
""", unsafe_allow_html=True)

# 🧠 Input Area
input_box = st.empty()
with input_box:
    guess = st.text_input("🔢 Your Guess (1–100):", placeholder="Enter a number...")

# 🧠 Logic
if guess:
    try:
        guess_int = int(guess)

        if 1 <= guess_int <= 100:
            st.session_state.guesses += 1

            if guess_int < st.session_state.number:
                st.info(f"❌ You guessed {guess_int}. Try a bigger number!")
            elif guess_int > st.session_state.number:
                st.info(f"❌ You guessed {guess_int}. Try a smaller number!")
            else:
                st.success(f"🎉 Correct! The number was {st.session_state.number}.")
                st.balloons()
                st.session_state.won = True
                st.session_state.games_played += 1
                if (st.session_state.best_score is None) or (st.session_state.guesses < st.session_state.best_score):
                    st.session_state.best_score = st.session_state.guesses
                st.write(f"✅ You guessed it in {st.session_state.guesses} attempts.")
        else:
            st.warning("⚠️ Your guess must be between 1 and 100.")

    except ValueError:
        st.error("🚫 Please enter a valid number between 1 and 100.")


# 🔁 Restart
if st.session_state.won:
    if st.button("🔁 Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.guesses = 0
        st.session_state.won = False
        st.session_state["guess_input"] = ""
        st.session_state["last_guess"] = ""
        st.rerun()  # Optional: ensures clean UI reload


# 🌙 Dark Theme Styles
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #E0E0E0;
    }
    .stApp {
        background-color: #121212;
        font-family: 'Segoe UI', sans-serif;
    }
    input, .stTextInput>div>div>input {
        background-color: #1E1E1E !important;
        color: #F8F8F2 !important;
        border-radius: 8px;
        border: 1px solid #44475a !important;
    }
    .stButton>button {
        background-color: #03DAC5 !important;
        color: #000000 !important;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.6em 1.2em;
        margin-top: 10px;
    }
    .stMarkdown h1 {
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
""", unsafe_allow_html=True)

# 📌 Sidebar
with st.sidebar:
    st.header("📌 How to Play")
    st.markdown("""
    - I'm thinking of a number between **1 and 100**.
    - Type your guess and hit **Enter**.
    - I'll guide you if it's **too high** or **too low**.
    - Try to beat your **best score**!
    """)
    st.caption("💻 Made by Kinjal • v1.2")
