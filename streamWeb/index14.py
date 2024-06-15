import streamlit as st

st.title("計數器範例")
if 'count' not in st.session_state:             #一開始檢查cookies裡面有沒有, 沒有則給定值0
    st.session_state.count = 0

increment = st.button("Increment")      
if increment:
    st.session_state.count += 1                 #每次都加1, 會存入cookies裡面
    
st.write("Count=", st.session_state.count)