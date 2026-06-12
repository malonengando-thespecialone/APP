
import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# Function to go to next page
def next_page(points):
    st.session_state.score += points
    st.session_state.page += 1

# Progress bar function
def show_progress():
    st.progress(min(st.session_state.score, 100))

# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:
    st.title("The User in Distress")
    show_progress()

    st.write("""
    A user reports that your app deleted an important file.
    They are stressed, upset, and need help immediately.
    """)

    if st.button("Respond with empathy"):
        next_page(18)
    if st.button("Respond dismissively"):
        next_page(7)

# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:
    st.title("Understanding the Situation")
    show_progress()

    st.write("""
    The user explains more details. They feel unheard by past support teams.
    """)

    if st.button("Ask clarifying questions"):
        next_page(22)
    if st.button("Offer a quick fix without details"):
        next_page(10)

# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:
    st.title("The Ethical Moment")
    show_progress()

    st.write("""
    You discover the bug affects more users than expected.
    """)

    if st.button("Report the issue immediately"):
        next_page(20)
    if st.button("Ignore it to avoid extra work"):
        next_page(5)

# ---------------- PAGE 4 ----------------
elif st.session_state.page == 4:
    st.title("The Emotional Tension")
    show_progress()

    st.write("""
    The user sends a frustrated message asking why this happened.
    """)

    if st.button("Acknowledge their frustration"):
        next_page(15)
    if st.button("Tell them to calm down"):
        next_page(3)

# ---------------- PAGE 5 ----------------
elif st.session_state.page == 5:
    st.title("High-Stakes Decision")
    show_progress()

    st.write("""
    You must decide whether to escalate the issue to leadership.
    """)

    if st.button("Escalate with a detailed report"):
        next_page(18)
    if st.button("Handle it quietly on your own"):
        next_page(6)

# ---------------- PAGE 6 ----------------
elif st.session_state.page == 6:
    st.title("Final Interaction")
    show_progress()

    st.write("""
    The user asks if this will happen again.
    """)

    if st.button("Reassure them with transparency"):
        next_page(12)
    if st.button("Give a vague non-answer"):
        next_page(4)

# ---------------- FINAL PAGE ----------------
elif st.session_state.page == 7:
    st.title("Your Final Results")
    show_progress()

    score = st.session_state.score

    if score >= 85:
        st.success("Your decisions reflect strong empathy and human-centered thinking.")
    elif score >= 60:
        st.warning("You balanced efficiency and empathy, but some choices lacked human focus.")
    else:
        st.error("Your decisions reveal gaps in empathy and ethical awareness.")

    st.write(f"Final Score: **{score}/100**")
