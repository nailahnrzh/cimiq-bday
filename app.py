import streamlit as st
import random
st.set_page_config(page_title="🎉 Tebak Angka Ultah!", page_icon="🎂")
st.title("🎂お誕生日おめでとうございます！ ")
st.subheader("ゲームを始めましょう！")   
###
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = 23
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'found' not in st.session_state:
    st.session_state.found = False
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
if "special_done" not in st.session_state:
    st.session_state.special_done = False
if "score" not in st.session_state:
    st.session_state.score = 0
guess = st.number_input("Age you are turning in today: ", min_value=1, step=1)
if st.button("COC SEASON 23 DIMULAI! 🎯") and not st.session_state.found:
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("Mangsud km su tua")
    elif guess > st.session_state.secret_number:
        st.warning("Tabe kak belum")
    else:
        st.success(f"Alhamdulillah masyaAllah ismi su {st.session_state.secret_number} tahun. Ngkeh kta lanjut ke babak berikutnyh")
        st.session_state.found = True
        st.session_state.quiz_started = True
st.markdown("---")       
if st.session_state.quiz_started and not st.session_state.quiz_finished:
    st.header("COC Season 23 Deathmatch Quiz")
    questions =[
        {
            "questions": "Jika x + 1/x = 3, maka nilai dari x^2 + 1/x^2 adalah", 
            "answer": "7"
        },
        {
            "questions": "2, 6, 12, 20, 30, ?",
            "answer": "42"
        },
        {
            "questions": "A=1 B=2 ... Z= 26 Maka berapa nilai dari kata: ISMI?",
            "answer": "50"
        },
        {
            "questions": "Digit terakhir dari 7^2025";
            "answer": "3"
        }
    ]
    for idx, (q, a) in enumerate(questions.items()):
        user_answer = st.text_input(f"Q{idx+1}: {q}", key=f"q{idx}")
        if user_answer:
            if user_answer.lower() == a.lower():
                st.success("benul")
                st.session_state.score += 1
            else:
                st.error("tet tot salah")
    all_answered = all(st.session_state.get(f"q{idx}") not in [None, ""] for idx in range(len(questions)))
    if st.button("mensubmit"):
        if all_answered:
            score = 0
            for idx, q in enumerate(questions):
                if st.session_state.get(f"q{idx}", "").strip() == q['answer']:
                    score += 1

            if score == len(questions):
                st.success("bnul smwah! champions msup babak brikutnyh")
                st.session_state.quiz_finished = True
                st.balloons()
            else:
                st.warning("ckckckck. coba lagi kakak")
        else:
            st.info("diisi dlu yh kak")
if st.session_state.quiz_finished and not st.session_state.special_done:
    st.markdown("---") 
    st.header("special episode")
    questions = [
        {
            "questions": "Bagaimana film SORE?",
            "options": ["ya Allah, bagus", "BAGUSNYO", "BGUS BANGADH"],
        },
    ]   

    user_answer = []

    for idx, q in enumerate(questions):
        st.subheader(f"nyoal: {q['questions']}")
        answer = st.radio("jawabannyh adlh:", q['options'], key=f"questions_{1}")
        user_answer.append(answer)
       
    if st.button("mensubmit"):
        st.success("selamat anda adalah buzzer film SORE")
        st.balloons()
        st.markdown("---")
        st.markdown("### 💌誕生日のメッセージ:")
        st.markdown("Happiest birthday, beautiful soul!")
        st.markdown("You're doing great until today. Love you and always proud of everything you did.")
        st.markdown("Our mmamah is so lovely ❤️")

        st.markdown("Semoga panjang umur dan sehat selalu ingyh. Semoga dapat cowo smga dpt kerja.")
        st.markdown("Semoga banyak doa baik yang terkabul. Semua cita-cita tercapai. Jadi orang kaya alhamdulillah masyaAllah aamiin")

        st.markdown("Selamat memasuki babak baru di usia 23 ini ingyh.")
        st.markdown("Tentunya banyak tantangan baru, tapi insyaAllah dimudahkan jalannya.")

        st.markdown("Jangan capek-capek dulu yaa 🤭 Panjanh perjalanan banh")
        st.markdown("Bukanka word of affirmation skl maksudku palla pko, tapi semoga mantap.")

        st.markdown("**WE LOVE ISMI** 💕")
        st.markdown("**MIHU MIHU I LOVE YOU** 🎉🎉")
        st.markdown("**Yeayers hepi 23!!!**")
