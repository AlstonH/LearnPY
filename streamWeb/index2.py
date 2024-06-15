import streamlit as st
col1, col2 = st.columns([1,1])          #([3,1]) 3表示權重佔比3/4, 1/4

with col1:
    st.title("這是欄位1")
    st.header("欄位1header")
    st.subheader("欄位1subheader")

with col2:
    st.title("這是欄位2")
    st.header("欄位2header")
    st.subheader("欄位2subheader")