import streamlit as st

st.title("Karachi Official")
st.header("Welcome to Karachi")
st.subheader("The City of Lights")
name= st.text_input("Enter your Name :")
f_Name= st.text_input("Enter your Fathers Name: ")
Age= st.number_input("Enter your Age: ")
address= st.text_area("Enter your location: ")
classdata= st.selectbox("Enter your class:",(1,2,3,4,5,6,7))
button=st.button("Submit")
if button:
    st.markdown(f"""
    Name={name}
    Father Name={f_Name}
    Age={Age}
    Address={address}
    Class={classdata}
    """)
st.balloons()