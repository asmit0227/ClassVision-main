import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_register_screen,teacher_screen
from src.componenets.header_home import header_home 
from src.componenets.dialog_auto_enroll import auto_enroll_dialog
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
     .stAppDeployButton {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.set_page_config(
        page_title='ClassVision - AI That Recognizes Your Class',
        page_icon= "https://i.postimg.cc/7hXS2Kk1/172f2e60-b338-44b8-a68a-9d020d4a4cfc.png"
    )
    if "login_type" not in st.session_state:
        st.session_state.login_type = None
    

    match st.session_state.login_type:
        case "student":
            student_screen()
        case "teacher":
            teacher_screen()
        case None:
            home_screen()    

    join_code= st.query_params.get("join-code")  
    if join_code:
        if st.session_state.login_type!="student":
            st.session_state.login_type="student"
            st.rerun()
        if   st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
            st.rerun()

main()

