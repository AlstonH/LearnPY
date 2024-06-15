#與index6.py不同的是, 只要使用者有更改過設定, 程式碼即會馬上從頭開始讀寫

import streamlit as st


st.write("Inside the form")
slider_val = st.slider("Form slider")
checkbox_val = st.checkbox("Form checkbox")

st.write("slider", slider_val, "checkbox", checkbox_val)
        
