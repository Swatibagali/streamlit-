import streamlit as st

st.title("somme basic commands like slider button etc")

age = st.slider("Select your age:", 1 ,100)
city = st.selectbox("choose your city ",["delhi","mumbai","banglore"])

if st.button("submit"):
    st.write("show the details")
    st.write("Your age is ", age)
    
    st.write("You live in ", city)