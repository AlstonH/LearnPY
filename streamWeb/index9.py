#sidebar一次只能有一個, 與index10.py不同的是, 這邊沒有form, 所以更改數值之後程式碼就會直接從頭到尾執行

import streamlit as st

# object notation
selected_value = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

#with notation
with st.sidebar:
    radio_value = st.radio(
        "Choose a shipping method",
        ("Standard(5-15 days)","Express (2-3 days)")
            )
    
st.write(selected_value, radio_value)