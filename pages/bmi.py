import streamlit as st
from streamlit import session_state as sst
import time as t

st.set_page_config('BMI Eval()', page_icon='🏃‍♂️', layout='wide', initial_sidebar_state='collapsed')

with open('./Styles/bmiStyles.css', 'r') as file:
    styling = file.read()
st.markdown('<style>'+styling+'</style>', unsafe_allow_html=True)

st.title('🧮 :orange[BMI] Calculator -- Know Your :red[Health] Status 🏥')
st.subheader('Basic BMI Evaluator📊⚗️')

leftCol, rightCol = st.columns([2, 1.2], gap='medium')

with leftCol:
    
    with st.form(key='bmiForm', border=True, clear_on_submit=True, enter_to_submit=False):

        sst.name = st.text_input('Name', value=None, placeholder="What's your name😍", max_chars=50)
        sst.age = st.number_input('Age', min_value=1, max_value=100, key='tempx', placeholder='Enter your Age')
        sst.gender = st.selectbox("Gender",('Male', 'Female', 'Prefer Not to Say'),placeholder='Choose from Below',)
        
        weight = st.slider('Weight (kg)', min_value=1, max_value=250, value=20, key='x')
        height = st.slider('Height (cm)', min_value=1, max_value=250, value=120, key='xx')
        height_m = height / 100
        
        is_Valid = (sst.name and sst.age and sst.gender and weight and height>0 )  #basic validation
        formSubmit = st.form_submit_button(label='Evaluate⚒️', use_container_width=True, type='secondary',)

def calculateBmi():
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        status = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
        color = "green"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
        color = "orange"
    else:
        status = "Obese"
        color = "red"

    return bmi, status, color

with rightCol:

    if formSubmit:

        if is_Valid :  
            cont = st.container(border=True)
            with cont:
                st.success('Form Submitted⚡')
                with st.spinner('Evaluating ...', show_time=True):
                    t.sleep(1)
                
                sst.bmiScore, status, color = calculateBmi()
                st.header(f':blue[{sst.name}] 👋')
                st.subheader(f'BMI Score ➡️:{color}[{sst.bmiScore:.2f}]')
                st.subheader(f'Status ➡️ :{color}[{status}]')

            if status == 'Normal weight':
                    st.balloons()
        else:
            st.warning('Missing Fields! Fill the Form.⚠️')
    
    if st.button('<- Back To 🏡', key='xcv', type='secondary'):
        st.switch_page('home.py') 

