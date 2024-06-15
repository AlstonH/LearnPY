import streamlit as st

st.bar_chart({"data":[1, 5, 2, 6, 2, 1]})

with st.expander(':orange-background[See Godzilla]', expanded=True):         #markdown也重視語法, 如果間隔打錯則會錯誤, expander可看說明
    st.markdown('''       
## Chart above
- The chart above shows some numbers I picked for you.
- I rolled actual dice for these, so they're *guaranteed*

> to be random.
''')
    st.image("https://www.specfictionshop.com/cdn/shop/files/MAINATOMICCHARGE_2000x.jpg?v=1682376161")