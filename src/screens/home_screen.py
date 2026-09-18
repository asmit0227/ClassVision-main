import streamlit as st
from  src.componenets.header_home import header_homes
from  src.UI.base_layout import style_base_background,style_base_layout
from  src.componenets.footer import footer




def home_screen(): 
    style_base_layout()
    style_base_background()
    
    header_homes()
    col_1,col_2= st.columns(2)

    with col_1:

      st.header("STUDENT")
      st.image("https://i.postimg.cc/tgRQGjSk/8a21a877-584d-429d-bd80-e4898cc110bc.png", width=145)
      if st.button("Student-Portal",icon=':material/arrow_outward:',icon_position='right',width="stretch"):
        st.session_state.login_type="student"
        st.rerun()     
      
    
    with col_2:
       st.header("TEACHER")
       st.image("https://i.postimg.cc/Jhx6NHQ6/b074ed4d-f3cc-4ceb-803e-4f1c2ac7506f.png", width=115)
       if  st.button("Teacher-Portal",icon=':material/arrow_outward:',icon_position='right',width="stretch"):
         st.session_state.login_type="teacher"
         st.rerun()

    footer()    