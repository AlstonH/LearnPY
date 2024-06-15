import streamlit as st

st.title("計數器範例")
if 'count' not in st.session_state:             #一開始檢查cookies裡面有沒有, 沒有則給定值0
    st.session_state.count = 0

#利用session_state的寫法
increment = st.button("Increment", key='Increment')      #如若未給key值, 程式會自動給定一個值
st.session_state                                         #顯示出值
if increment:
    st.session_state.count += 1                 #每次都加1, 會存入cookies裡面
    
st.write("Count=", st.session_state.count)