import streamlit as st

def header_home():
    logo ="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
      <div style="display : flex; flex-direction : column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
       <img src='{logo}' style= 'height:100px'>
       <h1 style = "text-align:center; color:white">SNAP<br/>CLASS</h1>
     </div>


     """,
     unsafe_allow_html=True

    )