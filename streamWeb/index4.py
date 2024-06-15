import streamlit as st
import time

placehoder = st.empty()

with placehoder:
    for seconds in range(60):        #list 0~59不含60
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)                #每執行一次停一秒
        
    st.write("😆 1 minute over!")
    
time.sleep(5)
placehoder.empty()
