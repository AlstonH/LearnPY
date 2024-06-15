import streamlit as st

tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.header("A Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    
with tab2:
    st.header("B Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

with tab3:
    st.header("C Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=300)