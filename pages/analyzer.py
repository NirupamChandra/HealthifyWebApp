import streamlit as st
from streamlit import session_state as sst
import time as t
import pickle
import numpy as np

# load Model pickle file

with open('./backendML/IOMP_model.pkl', 'rb') as file:
    sleep_model = pickle.load(file)

st.set_page_config('SleepSense', page_icon='😴', layout='wide', initial_sidebar_state='collapsed')

with open('./Styles/analyzerStyles.css', 'r') as file:
    styling = file.read()
st.markdown('<style>' + styling + '</style>', unsafe_allow_html=True)

def calcResult():   #linking model with frontend!!!

    ##use sleep_model.feature_names_in_ for knowing the order of input feature...

    #need to perform gender conversion into Numerical representation!! i.e during training we used labelEncoder
    # i.e female = 0, male = 1, other = 2 i,e labelEncoder gives values acc. to alphabet order wise!

    Gender_map = {
        'Female'            : 0,
        'Male'              : 1,
        'Prefer Not to Say' : 2,    
    }
    genderNumeric = Gender_map.get(sst.gender)  #returns numeric value corresponding to gender from Gender_Map

    X_input = np.array([[sst.age, genderNumeric, sst.sleepHours, sst.sleepQuality, sst.exercise, sst.caffeine, sst.scrnTime, sst.workHours]])

    prod, mood, stress = sleep_model.predict(X_input)[0]

    sst.productivity = round(prod, 2)/10*100       #in percentage
    sst.mood = int(round(mood, 0))              #in integer
    sst.stress = int(round(stress, 0))          #rounded to 0 decimal plac
    # print(sst.productivity, sst.mood, sst.stress)
    # print(sleep_model.feature_names_in_)
    
    
st.title(':green[SleepSense] -- Analyze & :blue[Optimize] Your Rest⚡')

st.subheader('From Sleep😴 to Success🥇: Predict Your Day with :red[Healthify]⚡:green[SleepSense]')
st.write('Let Your Sleep Data Tell the Story of Your Mental and Work Health.')

colLeft, colRight = st.columns([2, 1], gap='medium', vertical_alignment='center')

with colLeft:

    with st.form(key='tempxxx', clear_on_submit=False, border=True, enter_to_submit=False):
        
        sst.name = st.text_input('Name', value=None, placeholder="What's your name😍", max_chars=50)
        sst.age = st.number_input('Age', min_value=1, max_value=100, key='tempx', placeholder='Enter your Age')
        sst.gender = st.selectbox("Gender",('Male', 'Female', 'Prefer Not to Say'),placeholder='Choose from Below',)

        sst.sleepHours = st.slider('Sleep-Hours', max_value=24, min_value=0, value=8)
        sst.exercise = st.number_input('Exercise (mins/day)🤸💪', max_value=500, min_value=0, value=30)
        sst.caffeine = st.number_input('Caffeine (mg)🍵', min_value=0, max_value=400, value=4)
        sst.scrnTime = st.slider('Screen Time Before Bed(min)🛌', min_value=0, max_value=500, value=65)
        sst.workHours = st.number_input('Work Hours/day 💼🛄💰', min_value=0, max_value=24, value=5)
        sst.sleepQuality = st.slider('Sleep Quality you Felt💤', min_value=1, max_value=10, value=6)

        isValid = sst.name and sst.age and sst.gender and sst.sleepHours and sst.sleepQuality>0
        submitForm = st.form_submit_button('Analyze⚒️🚀', type='secondary', use_container_width=True)

with colRight:

    if submitForm:

        if isValid:

            calcResult()
            cont = st.container(border=True)
            with cont:
                st.success('Form Submitted⚡')
                with st.spinner('Processing ...', show_time=True):
                    t.sleep(2)
                with st.spinner('Redirecting to Results🚀', show_time=True):
                    t.sleep(1)

            sst.allowResults = True
            st.switch_page('./pages/results.py')

        else:
            st.warning("Fill all fields. ⚠️")
    
    if st.button('<- Back To 🏡', key='fsfsd', type='secondary'):
        st.switch_page('home.py') 
                