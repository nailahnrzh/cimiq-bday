import streamlit as st
import random
st.set_page_config(page_title="🎉 Tebak Angka Ultah!", page_icon="🎂")
st.title("🎂お誕生日おめでとうございます！ ")
st.subheader("ゲームを始めましょう！")   
###
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = 23
    st.session_state.attempts = 0
    st.session_state.found = False
guess = st.number_input("Age you are turning in today: ", min_value=1, step=1)
if st.button("COC SEASON 23 DIMULAI! 🎯") and not st.session_state.found:
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("Mangsud km su tua")
    elif guess > st.session_state.secret_number:
        st.warning("Tabe kak belum")
    else:
        st.success(f"Alhamdulillah masyaAllah ismi su {st.session_state.secret_number} tahun")
        st.balloons()
        st.markdown("### 💌誕生日のメッセージ:")
        st.markdown("""
Happiest birthday beautiful soul!
Mmamahhh hbddd huhuhuhuhuhuhuhuhuhu youre doing great until tudei
love you and always proud of every what you did
our mmamah is so lovely
semoga panjang umur dan sehat selalu
semoga dapat cowo
semoga dapat kerja ya Allah allahumma aamiin
semoga banyak doa baik yang terkabull semoga semua yang dicitakan tercapai
semoga jadi orang kaya
selamat memasuki babak baruu, ismi
tentunya di umur yang sudah tidak muda lagi ini banyak sekali tantangan baru yang akan dihadapi
insyaAllah diberi kemudahan untuk segala perjalanannya ismii
jangan capek-capek dulu yaa HAHAHAHA panjanh perjalanan banh
bukanka orang yangg words of affirmation sekalii
tapi semoga kehangatanku selalu dirasa sama ismiii
WE LOVE ISMI
MIHU MIHU I LOVE YOU
MIHU MIHU
yeayers hepi 23
we sorry nda ada spasinya kta beru pake beginian se nda tau kenapa nda terbaca prompt enternya
""")