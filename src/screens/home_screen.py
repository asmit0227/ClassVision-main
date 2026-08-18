import streamlit as st
from  src.componenets.header_home import header_home
from  src.UI.base_layout import style_base_background,style_base_layout
from  src.componenets.footer import footer


def home_screen(): 
    style_base_layout()
    style_base_background()
    
    header_home()
    col_1,col_2= st.columns(2)

    with col_1:

     st.header("I am Student")
     st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
     if st.button("student-portal",icon=':material/arrow_outward:',icon_position='right'):
        st.session_state.login_type="teacher"
        st.rerun()     
      

    with col_2:
       st.header("I am Teacher")
       st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
       if  st.button("teacher-portal",icon=':material/arrow_outward:',icon_position='right'):
         st.session_state.login_type="student"
         st.rerun()

    footer()    