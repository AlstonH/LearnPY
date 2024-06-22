import streamlit as st

st.image("https://health99.hpa.gov.tw/storage/images/materials/21752.jpg")
st.header("計算您的BMI:")
st.markdown("BMI計算公式: 體重(kg) / (身高(m)^2)")

with st.form("data"):
    name_val = st.text_input("請輸入您的姓名:")
    height_val = st.text_input("請輸入您的身高(cm):")
    weight_val = st.text_input("請輸入您的體重(kg):")
    
    submit = st.form_submit_button("送出")
    
def cal_bmi(bmi):
    if bmi < 18.5:
        return "您的BMI為體重過輕, 你需要再吃營養些，讓自己重一些！"
    elif bmi >= 18.5 and bmi < 24:
        return "您的BMI為健康體位, 很不錯喔，很標準，請您繼續保持！"
    elif bmi >= 24 and bmi < 27:
        return "您的BMI為過重, 您得控制一下飲食了，請加油！"
    elif bmi >= 27 and bmi < 30:
        return "您的BMI為輕度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"
    elif bmi >= 30 and bmi < 35:
        return "您的BMI為中度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"
    else:
        return "您的BMI為重度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"

if submit:
    try:
        height = float(height_val) / 100
        weight = float(weight_val)
        bmi = round(weight/height**2,ndigits=2)
        result = cal_bmi(bmi)
        st.write("您的姓名:",name_val, f"您的身高:{height_val}公分", f"您的體重:{weight_val}公斤", "您的BMI:", bmi)
        st.write(result)
    except ValueError:
        st.error("請確保您輸入的資料是否正確")
        



