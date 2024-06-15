import streamlit as st

if 'alston' not in st.session_state:                #session_state像是一個dict, 但不是dict
    st.session_state['alston'] = 30                 #如果沒有則給定一個值
    
st.session_state['alston']                          #讀出裡面的值
st.session_state.alston = 50                        #更改裡面的值
st.session_state.alston                             #.運算值將裡面的值讀出
