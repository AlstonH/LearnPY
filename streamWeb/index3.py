import streamlit as st
import numpy as np

with st.container(border=True):
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50,3))       #np是變數, 在numpy底下所以要import, random(module)底下randn隨機50筆資料的3種數值
    
st.write("This is outside the container")