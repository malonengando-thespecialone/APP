import streamlit as st

# ---------- PAGE STYLING ----------
page_bg = """
<style>
body {
    background: radial-gradient(circle at top, #f5e6c8 0%, #c9a66b 35%, #5b4636 100%);
    color: #2b1b0f;
    font-family: 'Georgia', serif;
}
h1, h2, h3 {
    color: #2b1b0f;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1
if "score" not in st.session_state:
    st.session_state.score = 0

def next_page(points):
    st.session_state.score += points
    st.session_state.page += 1

def show_progress():
    st.markdown("""
        <style>
        .stProgress > div > div > div > div {
            background-color: #8b5a2b; /* warm brown, like wood frame */
        }
        </style>
    """, unsafe_allow_html=True)
    st.progress(min(st.session_state.score, 100))

# ---------- PAGE 1: INTRO ----------
if st.session_state.page == 1:
    st.title("Build Your Own Renaissance Painting")
    show_progress()

    st.image("images/canvas.jpg", caption="A blank canvas waiting for a Renaissance vision.")

    st.write("""
    You’re about to build a painting one choice at a time.

    At each step, you’ll pick between different visual options.
    Some are true to Renaissance style. Others break away from it.

    By the end, your choices will shape the final painting and your Renaissance score.
    """)

    if st.button("Start building the painting"):
        next_page(0)

# ---------- PAGE 2: COMPOSITION ----------
elif st.session_state.page == 2:
    st.title("Step 1: Composition")

    show_progress()

    st.image(
        ["images/perspective.jpg", "images/byzantine.jpg"],
        caption=["Structured space with linear perspective", "Flat, stacked medieval layout"],
        width=300
    )

    st.write("""
    How do you want to structure the space in your painting?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Use linear perspective to create depth"):
            next_page(20)
    with col2:
        if st.button("Keep everything flat and stacked"):
            next_page(5)

# ---------- PAGE 3: LIGHT ----------
elif st.session_state.page == 3:
    st.title("Step 2: Light and Shadow")

    show_progress()

    st.image(
        ["images/light.jpg", "images/flat.jpg"],
        caption=["Dramatic light and shadow (chiaroscuro)", "Even, flat lighting"],
        width=300
    )

    st.write("""
    How should the light fall across your scene?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Use strong light and shadow to shape the forms"):
            next_page(20)
    with col2:
        if st.button("Keep the lighting even and low-contrast"):
            next_page(5)

# ---------- PAGE 4: SUBJECT ----------
elif st.session_state.page == 4:
    st.title("Step 3: Subject Matter")

    show_progress()

    st.image(
        ["images/adam.png", "images/islam.png"],
        caption=["Human-centered scene", "Decorative pattern"],
        width=300
    )

    st.write("""
    What is at the heart of your painting?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Focus on people and their emotions"):
            next_page(20)
    with col2:
        if st.button("Focus on decorative shapes and patterns"):
            next_page(5)

# ---------- PAGE 5: COLOR ----------
elif st.session_state.page == 5:
    st.title("Step 4: Color Palette")

    show_progress()

    st.image(
        ["images/earth.png", "images/neon.png"],
        caption=["Earthy, natural pigments", "Neon, synthetic colors"],
        width=300
    )

    st.write("""
    What kind of colors do you want to use?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Use warm, natural earth tones"):
            next_page(15)
    with col2:
        if st.button("Use bright neon digital colors"):
            next_page(5)

# ---------- PAGE 6: GESTURE ----------
elif st.session_state.page == 6:
    st.title("Step 5: Gesture and Emotion")

    show_progress()

    st.image(
        ["images/flow.png", "images/stiff.jpg"],
        caption=["Natural, expressive gesture", "Stiff, symbolic pose"],
        width=300
    )

    st.write("""
    How should the figures move and feel in your painting?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Give them natural, expressive movement"):
            next_page(15)
    with col2:
        if st.button("Keep them stiff and symbolic"):
            next_page(5)

# ---------- PAGE 7: BACKGROUND ----------
elif st.session_state.page == 7:
    st.title("Step 6: Background and Space")

    show_progress()

    st.image(
        ["images/mona.png", "images/gold.jpeg"],
        caption=["Soft, atmospheric depth", "Flat, solid background"],
        width=300
    )

    st.write("""
    What kind of space do you want behind your figures?
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Use atmospheric perspective to fade into the distance"):
            next_page(15)
    with col2:
        if st.button("Use a flat, single-color background"):
            next_page(5)

# ---------- FINAL PAGE: RESULT ----------
elif st.session_state.page == 8:
    st.title("Your Renaissance Painting")

    show_progress()

    score = st.session_state.score

    
    if score >= 80:
        st.image("images/school.jpg", caption="Your painting leans strongly into Renaissance style.")
        st.success("You built a painting that uses core Renaissance ideas: humanism, perspective, chiaroscuro, and naturalism.")
    elif score >= 55:
        st.image("images/fra.jpg", caption="Your painting mixes Renaissance elements with more modern or non-traditional choices.")
        st.warning("You picked some strong Renaissance features, but also broke away from them in a few key places.")
    else:
        st.image("images/cima.jpg", caption="Your painting drifts away from Renaissance style.")
        st.error("You moved away from Renaissance visual logic and leaned more into non-Renaissance choices.")

    st.write(f"Renaissance Style Score: **{score}/100**")
    st.write("""
    Each choice you made shaped the final image.

    Perspective, light, subject, color, gesture, and space all work together
    to create a visual language. That’s the core of Renaissance painting,
    and now you’ve built your own version of it.
    """)
