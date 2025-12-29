##File: app.py
##Project: Fun project 1 
##Description: fun-project-1-quiz
##how to run: streamlit run app.py
##Created / modified by: Christian Rohanda Wiyoto
##Day Date/time: Mon 29-Dec-2025 / 16:00
##how to run: streamlit run app.py

import streamlit as st

st.title("🧠 Siapakah Kamu? - Mini Personality Quiz")

score_programmer = 0
score_designer = 0
score_datascientist = 0

# Soal 1
st.header("1. Kamu paling suka ngapain?")
q1 = st.radio("1. Pilih satu:", [
    "Ngoding sampai lupa waktu",
    "Bikin layout & warna yang estetik",
    "Main data dan analisa tren"
], key="q1")

# Soal 2
st.header("2. Kamu lebih suka alat yang mana?")
q2 = st.radio("Pilih satu:", [
    "VS Code",
    "Figma",
    "Google Colab"
], key="q2")

# Soal 3
st.header("3. Motto kamu?")
q3 = st.radio("Pilih satu:", [
    "Keep calm and debug the code",
    "Design is thinking made visual",
    "In data we trust"
], key="q3")

if st.button("Lihat Hasil"):
    # Skoring berdasarkan jawaban
    if q1 == "Ngoding sampai lupa waktu":
        score_programmer += 1
    elif q1 == "Bikin layout & warna yang estetik":
        score_designer += 1
    else:
        score_datascientist += 1

    if q2 == "VS Code":
        score_programmer += 1
    elif q2 == "Figma":
        score_designer += 1
    else:
        score_datascientist += 1

    if q3 == "Keep calm and debug the code":
        score_programmer += 1
    elif q3 == "Design is thinking made visual":
        score_designer += 1
    else:
        score_datascientist += 1

    # Hasil akhir
    st.subheader("🧾 Hasil Kamu:")
    if score_programmer > score_designer and score_programmer > score_datascientist:
        st.success("💻 Kamu cocok jadi PROGRAMMER sejati!")
        ##st.image("https://media.giphy.com/media/26tPghhb3709o2F9u/giphy.gif")
        ##st.image("https://tenor.com/view/gamerx-funplay-opice-gif-19974887")
        st.image("assets/programmer_1.gif")

    elif score_designer > score_programmer and score_designer > score_datascientist:
        st.success("🎨 Kamu cocok jadi UI/UX DESIGNER kreatif!")
        st.image("https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif")
    else:
        st.success("📊 Kamu cocok jadi DATA SCIENTIST masa depan!")
        ##st.image("https://media.giphy.com/media/3o7aD0MhFszXG5Z8rO/giphy.gif")
        ##st.image("https://tenor.com/view/but-here's-the-coder-cat-gif-12160274951477317047")
        st.image("assets/data_scientes-3b.gif")
        