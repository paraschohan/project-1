# streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="✭")
st.title("🌳 Growth Mindest Challenge: Web App with Streamlit")

st.header("🤗Welcome to your Growth journey!")
st.write("Embrace challeges, learn from mistakes, and unlock your full potential. This AI-powered app help you build a growth mindset with reflection, challenges, and achievements!✤")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts._winston Churchill")

st.header("🧗What's Your challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f"you're facing: {user_input}. keep pushing forward towords your goal!🌱")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("write your reflection here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")


#acheivements
st.header("🏆Celerate Your Wins! ")
acheivment = st.text_input("share something you've recently accomplished:")



if acheivment:
    st.success(f"🎉Amazing! You achieved: {acheivment}")
else:
    st.info("Big or small , every acheivement counts! share one now 😊 ")

#footer
st.write("- - -")
st.write("Success begins where fear ends. Embrace challenges, learn from failures, and turn setbacks into comebacks! 🚀🔥")
st.write("⛔ created by Paras Kishan")