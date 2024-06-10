import streamlit as st
st.title("Harsh Profile")
st.header("What you want to know about me?")
option=st.selectbox("Enter your option",("Age","standard","Contact","Parent detail"))
if option=="Age":
    st.header("My age is 13.")
elif option=="standard":
    st.header("I study in class 8")
elif option=="Contact":
    st.header("Contact me at +919874561230")
elif option=="Parent detail":
    st.header("Mother Name: Sonia")
    st.header("Father Name: Ashwani kumar")
