import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favoutrite color: ',
    ('Blue', 'Red', 'Green'))

st.write('Your favourite color is ', option)


