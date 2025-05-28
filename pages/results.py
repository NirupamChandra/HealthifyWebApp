import streamlit as st
import plotly.graph_objects as pgo
from streamlit import session_state as sst
import time as t

st.set_page_config('Results', page_icon='🚀', layout='wide', initial_sidebar_state='collapsed')

if 'allowResults' not in sst or not sst.allowResults :
    st.warning('Not Authorised!', icon="⚠️")
    with st.spinner("Redirecting To 🏠 Page...", show_time=True):
        t.sleep(1.6)
    st.switch_page('home.py')

with open('./Styles/resultStyle.css', 'r') as file:
    styling = file.read()
st.markdown('<style>' + styling+ '</style>', unsafe_allow_html=True)

st.balloons()

def setGauge(val:float, myTitle:str, myRange:list, myColor:str):
    
    fig = pgo.Figure(pgo.Indicator(
            mode = 'gauge+number',
            value = val,
            title = {'text' : myTitle},
            gauge = {
                'axis': {'range': myRange},
                'bar': {'color': myColor},
            }
    ))
    fig.update_layout(
        height=350,
        width = 300,
        margin = dict(t=40, b=10, l=30, r=30)
    )

    return fig

def getFeedBack(mood, stress, productivity):
    feedback = {}   #empty dictionary!

    # Mood-based feedback
    if mood <= 3:
        feedback['Mood'] = "😞 Your mood levels are quite low. Prioritize quality sleep and reduce stressors. Regular physical activity can also help improve emotional well-being."
    elif mood <= 6:
        feedback['Mood'] = "😐 Mood is moderate. Consider improving sleep hygiene and balancing screen time and caffeine intake."
    elif mood <= 8:
        feedback['Mood'] = "🙂 Good mood! You’re likely managing your routine fairly well. Keep up the healthy sleep and exercise habits."
    else:
        feedback['Mood'] = "😄 Excellent mood score! Your sleep and lifestyle choices are benefiting your emotional wellness."

    # Stress-based feedback
    if stress <= 3:
        feedback['Stress'] = "🧘 Very low stress — great job managing your workload and self-care practices!"
    elif stress <= 6:
        feedback['Stress'] = "😌 Moderate stress. You're doing okay, but some relaxation techniques or better time management may help."
    elif stress <= 8:
        feedback['Stress'] = "😣 Elevated stress levels. Try reducing screen time, getting regular exercise, and sleeping more soundly."
    else:
        feedback['Stress'] = "⚠️ High stress! Consider reassessing your work-life balance and reducing caffeine or screen exposure at night."

    # Productivity-based feedback
    if productivity <= 40:
        feedback['Productivity'] = "📉 Low productivity. Poor sleep or stress might be affecting your output. Improve consistency in sleep and reduce distractions."
    elif productivity <= 70:
        feedback['Productivity'] = "📈 Average productivity. You're doing fine, but optimizing sleep quality and exercise could help boost this further."
    elif productivity <= 89:
        feedback['Productivity'] = "💼 Strong productivity! Your lifestyle is well-aligned with good mental and physical health."
    else:
        feedback['Productivity'] = "🚀 Excellent productivity! Your sleep pattern and daily habits are optimized for peak performance."

    return feedback

fdBack = getFeedBack(sst.mood, sst.stress, sst.productivity)

st.title(f'Helloooo!! :blue[{sst.name}] 🤗')
st.subheader('Here are your results from :red[Healthify]-:orange[Sleep]Sense')
st.subheader('Find below for scores!🏆')
st.divider()



col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment='center', gap='medium')
with col1:
    c1 = st.container(border=True)
    fig1 = setGauge(sst.mood, 'Mood-Score', [0, 10], 'magenta')
    c1.plotly_chart(fig1)
    c2 = st.container(border=True)
    c2.write(fdBack.get('Mood'))

with col2:
    c1 = st.container(border=True)
    fig2 = setGauge(sst.productivity, 'Productivity(%)', [0, 100], 'orange')
    c1.plotly_chart(fig2)
    c2 = st.container(border=True)
    c2.write(fdBack.get('Productivity'))

with col3:
    c1 = st.container(border=True)
    fig3 = setGauge(sst.stress, 'Stress-Levels', [0, 10], 'limegreen')
    c1.plotly_chart(fig3)
    c2 = st.container(border=True)
    c2.write(fdBack.get('Stress'))



l, m, r = st.columns([1, 2, 3], gap='large')
with l:
    if st.button('<- Back To 🏡', key='xcv', type='primary', use_container_width=True):
        st.switch_page('home.py') 
with m:
    if st.button('<- Back to Analyzer', key='xzc', type='secondary', use_container_width=True):
        st.switch_page('./pages/analyzer.py')
with r:
    if st.button('BMI eval()🚀', key='asd', use_container_width=True):
        st.switch_page('./pages/bmi.py')