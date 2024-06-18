import streamlit as st

st.image("https://health99.hpa.gov.tw/storage/images/materials/21752.jpg")
st.header("計算您的BMI:")
st.subheader("BMI計算公式: 體重(kg)/身高平方(cm)")


with st.form("data"):
    name = st.text_input("請輸入您的姓名:")
    height = st.text_input("請輸入您的身高(cm):")
    weight = st.text_input("請輸入您的體重(kg):")
    
    st.form_submit_button("送出")
st.write("您的姓名:",name,"您的身高:",height,"您的體重:",weight)



