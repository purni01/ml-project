import streamlit as st
import random

# EmoBuddy – Emotional and Mental Health Chatbot
st.set_page_config(page_title="EmoBuddy – Your Emotional and Mental Health Companion", page_icon="💙")
st.title("💙 Welcome to EmoBuddy – Your Emotional and Mental Health Companion")
st.markdown("_Hi, I'm here to listen. How are you feeling today?_ 💬")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Quotes, jokes, greetings, resources
quotes = [
    "“This too shall pass.”",
    "“One step at a time is still progress.”",
    "“You are worthy, even when you feel broken.”",
    "“You are not a burden. You are loved.”"
]

jokes = [
    "Why don’t eggs tell jokes? Because they’d crack each other up! 🥚😄",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
    "What did one ocean say to the other? Nothing, they just waved. 🌊",
    "Feeling low? Just remember you're someone's favorite notification. 🔔"
]

resources = {
    "urgent": "[📞 National Helpline (India) – 9152987821](https://www.mohfw.gov.in/)",
    "breathing": "[🧘 Try this breathing exercise](https://www.youtube.com/watch?v=nmFUDkj1Aq0)",
    "journal": "[📝 Write your feelings here](https://www.penzu.com/)",
    "student_help": "[📘 Student support line: 1800-599-0019](https://manodarpan.education.gov.in/)"
}

greetings = [
    "Hello! 😊 How are you feeling today?",
    "Hi there! I'm here to listen to you. 💬",
    "Hey! How can I support you today?",
    "Welcome 🤗 You're safe to share here."
]

# Response logic
def get_response(msg):
    msg = msg.lower()

    if msg in ["hi", "hello", "hey", "good morning", "good evening"]:
        return random.choice(greetings)

    elif any(word in msg for word in ["i'm in love", "in love", "i have a crush", "i like someone", "dating"]):
        return (
            "💘 That’s so lovely to hear! Love is such a beautiful feeling.\n\n"
            "Take your time and enjoy the little moments — they matter the most. 💞"
        )

    elif "broke up" in msg or "breakup" in msg or "boyfriend" in msg or "girlfriend" in msg:
        return (
            "💔 I'm really sorry you're going through that. It hurts, but this isn’t the end.\n\n"
            "You deserve someone who values you deeply. Heal gently — you matter. 💞"
        )

    elif "death" in msg or "passed away" in msg or "lost someone" in msg or "funeral" in msg:
        return (
            "🕊️ I’m so sorry for your loss. Grieving takes time, and that’s okay.\n\n"
            "You are not alone — I'm here with you. 💐"
        )

    elif "exam" in msg or "failed" in msg or "marks" in msg or "didn't do well" in msg:
        return (
            "📚 It’s okay to struggle sometimes. One test doesn’t define your worth.\n\n"
            "Take it one step at a time — your effort still matters.\n\n"
            + resources["student_help"]
        )

    elif "student" in msg or "college" in msg or "pressure" in msg or "tired of studies" in msg:
        return (
            "🎓 Being a student is tough. It’s okay to feel pressure, but don’t forget to rest too.\n\n"
            "You’re doing better than you think. 🌈"
        )

    elif any(word in msg for word in ["sad", "depressed", "cry", "hopeless"]):
        return (
            "💛 I'm so sorry you're feeling this way. You're not alone.\n\n"
            + random.choice(quotes)
            + "\n\nHere’s something to cheer you up:\n" + random.choice(jokes)
        )

    elif any(word in msg for word in ["anxious", "panic", "nervous", "overthinking", "worried"]):
        return (
            "🌿 Let's breathe together. You're safe, and you’re not alone in this.\n\n"
            + resources["breathing"]
        )

    elif any(word in msg for word in ["angry", "frustrated", "annoyed", "irritated"]):
        return (
            "😤 Your emotions are valid. It’s okay to feel what you feel.\n\n"
            "Would writing help?\n" + resources["journal"]
        )

    elif any(word in msg for word in ["alone", "lonely", "isolated", "no one cares"]):
        return (
            "🫂 I'm here with you. You matter more than you realize.\n\n"
            + resources["urgent"]
        )

    elif any(word in msg for word in ["happy", "joyful", "excited", "great", "feeling good"]):
        return (
            "😊 That’s amazing to hear! Keep shining — you deserve this joy. 🌟"
        )

    elif "joke" in msg:
        return "😄 Here's a joke for you:\n\n" + random.choice(jokes)

    elif msg.strip() == "":
        return "🤗 I'm listening. Type anything you're feeling."

    else:
        return (
            "💙 Thank you for sharing that. Whatever you're feeling is valid.\n\n"
            + random.choice(quotes)
            + "\n\nHere’s something light to make you smile:\n" + random.choice(jokes)
        )

# Input form first
user_input = ""
with st.form(key="unique_chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type something...")
    submitted = st.form_submit_button("Send")

# Show latest chat first after submission
if submitted and user_input:
    bot_reply = get_response(user_input)
    st.session_state.history.insert(0, (user_input, bot_reply))  # Insert at top
    st.rerun()

# Show conversation history (latest on top)
if st.session_state.history:
    st.markdown("---")
    st.subheader("🗨️ Conversation History")
    for user_msg, bot_msg in st.session_state.history:
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**EmoBuddy:** {bot_msg}")

