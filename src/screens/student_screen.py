import streamlit as st
from src.componenets.header_home import header_dashboard
from src.UI.base_layout import style_base_all , style_base_layout,style_base_background
from src.componenets.footer import footer_dashboard
from src.componenets.dialog_enroll  import enroll_dialog 
from src.componenets.subject_card import subject_card
from PIL import Image
import numpy as np
from src.pipelines.face_pipelines import predict_attendance
from src.Database.db import get_all_students,create_student,get_student_subjects,get_student_attendance,unenroll_student_to_subject
from src.pipelines.face_pipelines import get_all_embeddings , train_classifier
import time
from src.pipelines.voice_pipelines import get_voice_embedding


def student_dashboard():
    
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data 
            st.rerun()


    st.space()

    c1, c2 =st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()


    st.divider()


    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']


        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        def unenroll_button():
                if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:',key=f"unenroll_{sub['subject_id']}"):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub['subject_name']} successfully!')
                    st.rerun()

        with cols[i % 2]:

            subject_card(
                name = sub['subject_name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()



def student_screen():
     style_base_all()
     style_base_layout()
     st.markdown("""
    <style>
    div[data-testid="stCameraInput"] label p {
        font-weight: 700 !important;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)



     if "student_data" in st.session_state:
        student_dashboard()
        return
     show_registration=False
    
     cl1 , cl2 =st.columns(2, vertical_alignment="center",gap="xxlarge")
     with cl1:
          header_dashboard()
    
     with cl2:
           if st.button("Go Back To Home",type="secondary",key="loginbackbtn",shortcut="control+backspace") :
               st.session_state['login_type']=None
               st.rerun()

     st.header("Login Your Profile Using FaceId",text_alignment="center") 
     st.space()
     st.space()          
     




     photo_source = st.camera_input("Position Your Face In The Camera")
     if photo_source:
       img = np.array(Image.open(photo_source))
       with st.spinner("AI is scanning ...."):
           
         detected,all_ids,num_faces=predict_attendance(img)

         if num_faces == 0:
                st.warning('Face not found!')
         elif num_faces >1:
                st.warning('Multiple faces found')
         else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student['name']}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True

     if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input("Enter your name", placeholder='E.g.  Asmit')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your for voice only attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings= get_all_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, image_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')


    
                 




     footer_dashboard()
