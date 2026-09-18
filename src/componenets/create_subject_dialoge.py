import streamlit as st
from src.Database.db import create_subject


@st.dialog("create new subject")
def create_subject_dialog(teacher_id):
    st.write("Enter Your Subject Details")
    sub_id=st.text_input("Subject Code",placeholder="CS101")
    sub_name=st.text_input("Subject Name",placeholder="Advanced Programming")
    sub_section= st.text_input("Subject Section",placeholder="A")

    if  st.button("Submit",type="primary",width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("subject created successfully")
                st.rerun()
            except Exception as e:
                st.error(f""" error : {str(e)}""")    
    else:
            st.warning("Please fill all the fields")            