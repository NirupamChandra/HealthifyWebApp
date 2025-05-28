
import streamlit as st
from streamlit import session_state as sst
import time as t
import plotly.graph_objects as pgo


st.set_page_config("Healthify", '🧠', layout='wide', initial_sidebar_state='collapsed')

def declareSessionStateVariables():
    sst.allowResults = False
    sst.name = "temp"
    sst.age = 0
    sst.gender = ""
    sst.bmiScore = 0

declareSessionStateVariables()

with open('./Styles/homeStyles.css', 'r') as file:
    styling = file.read()

st.markdown('<style>' + styling+ '</style>', unsafe_allow_html=True)    #adding external css file...

Left, Right = st.columns([2, 1], gap='large')

with Left:

    st.title("Welcome to :red[Healthify] 🩺👩🏼‍⚕️")
    st.write("One stop :blue[Analyzer] for all Lifestyle Needs!")

    inLeftl, inLeftr = st.columns([1, 0.7], gap='medium')

    with inLeftl:

        cont1b = st.container(border=True)
        with cont1b:
            st.subheader(":orange[Sleep] Analyzer  👇🏼")
            conGap = st.container(height=10, border=False)      #just for creating gap...
            st.image('./public/sleep.jpg',use_container_width=True)
            if st.button('Go to Analyzer 🚀', use_container_width=True, key='tempb'):
                st.switch_page('./pages/analyzer.py')

    with inLeftr:

        cont1a = st.container(border=True)
        with cont1a:
            st.subheader(":orange[BMI] score 👇🏼")
            conGap = st.container(height=10, border=False)
            st.image('https://www.shutterstock.com/image-vector/bmi-body-mass-index-meter-600nw-2313911113.jpg',)
            if st.button('Go to BMI ✈️', use_container_width=True, key='tempa'):
                st.switch_page('./pages/bmi.py')

    cont1c = st.container(height=170, border=True)
    with cont1c:
        st.subheader('"😂A good laugh and a long sleep 💤 are the best cures in the doctor’s book."')
        st.write('— Irish Proverb')
        
with Right:

    Right.image('public/health2.jpg', use_container_width=True)
    cont2a = st.container()
    with cont2a:
        st.page_link(label='Harvard Health Publishing↗️', page='https://www.health.harvard.edu/blog/healthy-lifestyle-5-keys-to-a-longer-life-2018070514186', use_container_width=True)

    Right.image('public/health1.jpg', use_container_width=True, caption='Sleep Routines')
    cont2b = st.container()
    with cont2b:
        st.page_link(label='Sleep cycle Routines↗️', page='https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-science-of-sleep-understanding-what-happens-when-you-sleep', use_container_width=True)

bottom = st.container(height=200, border=True)
with bottom:
    st.header('👋 Hang Tight!  ')
    st.subheader('Extra features ⚒️ and updates are on the way.🚧  ')
    st.write("We can’t wait to share them with you.🤘")