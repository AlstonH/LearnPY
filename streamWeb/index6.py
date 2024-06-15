#按下Submit Button程式碼才會從頭到尾讀寫更改設定

import streamlit as st

with st.form('my_form'):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    
    #每一個form必須要有一個submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
        
st.write("Outside the form")