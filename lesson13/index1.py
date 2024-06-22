import streamlit as st
st.image("https://miro.medium.com/v2/resize:fit:1400/1*_rSIVyAo3uD_ncHXrMstAw@2x.jpeg")
st.subheader("BMI計算")
st.divider()
st.latex('BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)')
st.latex('例如：一個52公斤的人，身高是155公分，則BMI為 :')
st.markdown('<h6 style="color:blue;text-align:center">52 (公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>',
            unsafe_allow_html=True)

st.markdown('<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>', 
            unsafe_allow_html=True)

st.markdown('<hr style="border:0;margin:0 auto;width:100%;border-top:2px dotted blue">',
            unsafe_allow_html=True)

st.markdown('<h6 style="color:purple;text-align:center">快看看自己的BMI是否在理想範圍吧!</h6>', 
            unsafe_allow_html=True)

if 'bmi_result' not in st.session_state:
    st.session_state.bmi_result = 0

def clear_result():
    st.session_state.height=0
    st.session_state.weight=0
    st.session_state.bmi_result=0

with st.form('bmi form', border=False):
    height = st.slider(":green[請選擇身高(cm)]",max_value=300,min_value=0,key="height") 
    weight = st.number_input(":blue[請選擇體重(kg)]",max_value=300,min_value=0,key="weight")
    txt=''         #建立文件變數(不會被消滅, 除非文件被關掉), 另一個則是區域變數執行完會被消滅掉
    if st.form_submit_button("BMI計算"):  
        st.session_state.bmi_result = round(weight / (height/100) ** 2,1)
        if st.session_state.bmi_result < 18.5:
            txt = "您的BMI為體重過輕, 你需要再吃營養些，讓自己重一些！"
        elif st.session_state.bmi_result >= 18.5 and st.session_state.bmi_result < 24:
            txt = "您的BMI為健康體位, 很不錯喔，很標準，請您繼續保持！"
        elif st.session_state.bmi_result >= 24 and st.session_state.bmi_result < 27:
            txt = "您的BMI為過重, 您得控制一下飲食了，請加油！"
        elif st.session_state.bmi_result >= 27 and st.session_state.bmi_result < 30:
            txt = "您的BMI為輕度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"
        elif st.session_state.bmi_result >= 30 and st.session_state.bmi_result < 35:
            txt = "您的BMI為中度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"
        else:
            txt = "您的BMI為重度肥胖, 肥胖容易引起疾病，您得要多多注意自己的健康囉！"
            
    st.form_submit_button("清除內容",on_click=clear_result)
                
st.markdown(f'### :orange[{st.session_state.bmi_result}]')
st.markdown(f'#### :black[{txt}]')

st.session_state

