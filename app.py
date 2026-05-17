import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="🎮 Mini-Game Arcade", page_icon="🕹️")
st.title("🕹️ Mini-Game Arcade")
st.markdown("Welcome to the ultimate game zone! Choose a game to play:")

# Score tracking
if "score" not in st.session_state:
    st.session_state.score = 0

# Game selection
games = [
    "Rock Paper Scissors", "Guess the Number", "Word Scramble", "Emoji Quiz",
    "Math Quiz", "Dice Roller", "Hangman Lite", "Memory Test",
    "Odd or Even", "Typing Speed Game"
]

selected_game = st.selectbox("🎮 Select a Game", games)

# Reset utility
def reset_game_state(keys):
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]

# ------------------ 1. Rock Paper Scissors ------------------
if selected_game == "Rock Paper Scissors":
    st.subheader("✊🖐✌ Rock Paper Scissors")
    user_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])
    if st.button("Play"):
        st.session_state.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        combo = (user_choice, st.session_state.computer_choice)
        if user_choice == st.session_state.computer_choice:
            result = "It's a tie!"
        elif combo in [("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")]:
            result = "You win!"
            st.session_state.score += 1
        else:
            result = "You lose!"
        st.success(f"Computer chose: {st.session_state.computer_choice} \n {result}")

# ------------------ 2. Guess the Number ------------------
elif selected_game == "Guess the Number":
    st.subheader("🔢 Guess the Number (1–20)")
    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(1, 20)
    guess = st.number_input("Your Guess:", 1, 20)
    if st.button("Check"):
        if guess == st.session_state.target_number:
            st.success("🎯 Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! It was {st.session_state.target_number}")
    if st.button("Next Round"):
        reset_game_state(["target_number"])

# ------------------ 3. Word Scramble ------------------
elif selected_game == "Word Scramble":
    st.subheader("🔀 Word Scramble")
    words = ["streamlit", "python", "arcade", "project", "school"]
    if "scramble_word" not in st.session_state:
        word = random.choice(words)
        st.session_state.scramble_answer = word
        st.session_state.scramble_word = ''.join(random.sample(word, len(word)))
    st.write(f"Unscramble: **{st.session_state.scramble_word}**")
    user_word = st.text_input("Your answer:")
    if st.button("Submit"):
        if user_word.lower() == st.session_state.scramble_answer:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Nope! The word was **{st.session_state.scramble_answer}**")
    if st.button("Next Word"):
        reset_game_state(["scramble_word", "scramble_answer"])

# ------------------ 4. Emoji Quiz ------------------
elif selected_game == "Emoji Quiz":
    st.subheader("😊 Emoji Quiz")
    emoji_dict = {
        "🎓📚💡": "study", "🍕🍟🍔": "fast food",
        "🦁🐯🐻": "animals", "🎵🎤🎸": "music"
    }
    if "emoji" not in st.session_state:
        emoji, answer = random.choice(list(emoji_dict.items()))
        st.session_state.emoji = emoji
        st.session_state.emoji_answer = answer
    st.write(f"What do these emojis mean? {st.session_state.emoji}")
    guess = st.text_input("Your answer:")
    if st.button("Guess"):
        if guess.lower() == st.session_state.emoji_answer:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ It was **{st.session_state.emoji_answer}**")
    if st.button("Next Emoji"):
        reset_game_state(["emoji", "emoji_answer"])

# ------------------ 5. Math Quiz ------------------
elif selected_game == "Math Quiz":
    st.subheader("➕➖ Math Challenge")
    if "math_question" not in st.session_state:
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        st.session_state.math_question = f"{a} {op} {b}"
        st.session_state.math_answer = eval(st.session_state.math_question)
    st.write(f"Solve: **{st.session_state.math_question}**")
    answer = st.number_input("Your answer:", step=1)
    if st.button("Submit"):
        if answer == st.session_state.math_answer:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ It's {st.session_state.math_answer}")
    if st.button("Next Question"):
        reset_game_state(["math_question", "math_answer"])

# ------------------ 6. Dice Roller ------------------
elif selected_game == "Dice Roller":
    st.subheader("🎲 Roll the Dice")
    if st.button("Roll"):
        dice = random.randint(1, 6)
        st.write(f"You rolled: 🎲 **{dice}**")
        if dice == 6:
            st.success("Lucky 6!")
            st.session_state.score += 1

# ------------------ 7. Hangman Lite ------------------
elif selected_game == "Hangman Lite":
    st.subheader("🪓 Hangman (1 Guess Only)")
    if "hangman_word" not in st.session_state:
        word = random.choice(["apple", "stream", "coder"])
        st.session_state.hangman_word = word
        st.session_state.hangman_clue = word[0] + "_" * (len(word)-1)
    st.write(f"Guess the word: **{st.session_state.hangman_clue}**")
    guess = st.text_input("Your guess:")
    if st.button("Try"):
        if guess.lower() == st.session_state.hangman_word:
            st.success("🎉 Well done!")
            st.session_state.score += 1
        else:
            st.error(f"❌ It was **{st.session_state.hangman_word}**")
    if st.button("Next Word"):
        reset_game_state(["hangman_word", "hangman_clue"])

# ------------------ 8. Memory Test ------------------
elif selected_game == "Memory Test":
    st.subheader("🧠 Memory Test")
    if "memory_numbers" not in st.session_state:
        st.session_state.memory_numbers = [random.randint(1, 9) for _ in range(3)]
    st.write("Memorize this:")
    st.code(st.session_state.memory_numbers)
    time.sleep(3)
    user_input = st.text_input("Now enter them back (e.g. 1,2,3):")
    if st.button("Check Memory"):
        try:
            if list(map(int, user_input.split(","))) == st.session_state.memory_numbers:
                st.success("🧠 Great memory!")
                st.session_state.score += 1
            else:
                st.error("❌ Incorrect sequence")
        except:
            st.error("⚠️ Invalid input")
    if st.button("Next Test"):
        reset_game_state(["memory_numbers"])

# ------------------ 9. Odd or Even ------------------
elif selected_game == "Odd or Even":
    st.subheader("➗ Odd or Even")
    if "odd_even_num" not in st.session_state:
        st.session_state.odd_even_num = random.randint(1, 99)
    st.write(f"Is **{st.session_state.odd_even_num}** Odd or Even?")
    choice = st.radio("Your answer:", ["Odd", "Even"])
    if st.button("Check"):
        correct = "Even" if st.session_state.odd_even_num % 2 == 0 else "Odd"
        if choice == correct:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ It was {correct}")
    if st.button("Next Number"):
        reset_game_state(["odd_even_num"])

# ------------------ 10. Typing Speed Game ------------------
elif selected_game == "Typing Speed Game":
    st.subheader("⌨️ Typing Challenge")
    sentence = "Streamlit is awesome"
    st.write(f"Type this exactly: `{sentence}`")
    typed = st.text_input("Start typing:")
    if st.button("Check Typing"):
        if typed.strip() == sentence:
            st.success("Perfect typing!")
            st.session_state.score += 1
        else:
            st.error("Mismatch! Try again.")

# ------------------ Scoreboard ------------------
st.markdown("---")
st.markdown(f"🏆 **Your Score:** `{st.session_state.score}`")
if st.button("🔁 Reset Score"):
    st.session_state.score = 0
