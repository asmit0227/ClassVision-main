import streamlit as st
from src.componenets.header_home import header_dashboard
from src.UI.base_layout import style_base_all , style_base_layout
from src.componenets.footer import footer_dashboard 
from src.Database.db import username_exist,create_teacher,teacher_login,get_teacher_subjects,get_attendance_for_teacher,delete_subject
from src.Database.config import supabase
from datetime import datetime
import numpy as np
from src.componenets.dialog_add_photo import add_photos_dialog
from src.componenets.dialog_attendance_result import attendance_result_dialog
from src.componenets.dialog_voice_attendance import voice_attendance_dialog
from src.componenets.create_subject_dialoge  import create_subject_dialog  
from src.componenets.dialog_share_subject    import share_subject_dialog 
from src.componenets.subject_card import subject_card                      
from src.pipelines.face_pipelines import predict_attendance
import pandas as pd
def teacher_screen():
     style_base_layout()
     style_base_all()

     if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "LogIn"
     if "teacher_data" in st.session_state:
        teacher_dashboard()
     elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="LogIn":
         teacher_login_screen()
     elif st.session_state.teacher_login_type=="Register":
         teacher_register_screen()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']}""")


    c1,c2=st.columns(2, gap="xxlarge",vertical_alignment="center")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Logout",type="secondary",key="loginback",shortcut="control+backspace"):
            st.session_state.teacher_login_type=="LogIn"
            del st.session_state.teacher_data   
            st.rerun() 

    st.space() 
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab ='take_attendance'
    tab1,tab2,tab3=st.columns(3) 

    with tab1:
        type1="primary" if st.session_state.current_teacher_tab=="take_attendance" else "tertiary"
        if st.button("Take attendance ",type=type1,width="stretch",icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab="take_attendance"
            st.rerun()
    with tab2:
        type2="primary" if st.session_state.current_teacher_tab=="Manage_Subjects" else "tertiary"
        if st.button("Manage Subjects ",type=type2,width="stretch",icon=':material/book_ribbon:'):
            st.session_state.current_teacher_tab="Manage_Subjects"
            st.rerun()
    with tab3:
        type3="primary" if st.session_state.current_teacher_tab=="Attendance_Records" else "tertiary"
        if st.button("Attendance Records",type=type3,width="stretch",icon=':material/cards_stack:'):
            st.session_state.current_teacher_tab="Attendance_Records"
            st.rerun()  

    st.divider()

    if st.session_state.current_teacher_tab=="take_attendance":
            take_attendance_tab() 
    if st.session_state.current_teacher_tab=="Manage_Subjects":
            Manage_Subjects_tab() 
    if st.session_state.current_teacher_tab=="Attendance_Records":
            Attendance_Records_tab()
                      

def take_attendance_tab():
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.header('Take AI Attendance')


    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You havent created any subjects yet! Please create one to begin!')
        return
    
    subject_options = {f"{s['subject_name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3,1], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:
        if st.button('Add Photos', type='primary', icon=':material/photo_prints:', width='stretch'):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4 ]:
                st.image(img, width='stretch', caption=f'Photo {idx+1}')
    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Clear all photos', width='stretch', type='tertiary', icon=':material/delete:', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()


    with c2:
        
        if st.button('Run Face Analysis', width='stretch', type='secondary', icon=':material/analytics:', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids = {}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _ = predict_attendance(img_np)


                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)

                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                enrolled_res = supabase.table('student_subjects').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:

                    results, attendance_to_log  = [], []

                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present= len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('Use Voice Attendance', type='primary', width='stretch', icon=':material/mic:'):
            voice_attendance_dialog(selected_subject_id)


def Manage_Subjects_tab():
    teacher_id = st.session_state.teacher_data['teacher_id']
    c1=st.columns(1,width="stretch")[0]
    with c1:
                   if st.button("Create New Subject",width="stretch",key='createsubject'):
                         create_subject_dialog(teacher_id)
      
   
    subjects = get_teacher_subjects(teacher_id)
    if not subjects:
        if not subjects:
            st.warning('You havent created any subjects yet! Please create one to begin!')
            return
    
    
  

    select_subject = {f"{s['subject_name']} - {s['total_students']} - {s['total_classes']}": s for s in subjects}

    col1=st.columns(1 , width="stretch",gap="small",vertical_alignment='bottom')[0]
    with col1:
        selected_subject = st.selectbox("Edit Subject",options=list(select_subject),width="stretch")
   
    current_subject=select_subject[selected_subject]

  
    stats = [
         ("🫂","Students",current_subject['total_students']),
         ("🕰️","Classes",current_subject['total_classes']),
             ]  
    def share_btn():
        if st.button(f"Share Code: {current_subject['subject_name']}", key=f"share_{current_subject['subject_code']}", icon=":material/share:"):
             share_subject_dialog(current_subject['subject_name'], current_subject['subject_code'])
             st.space()

    subject_card(
    
             name = current_subject['subject_name'],
             code = current_subject['subject_code'],
             section = current_subject['section'],
             stats=stats,
             footer_callback=share_btn
         )
    c1= st.columns(4)[0]    
    with c1:
        if st.button("!Delete",width="stretch",type="tertiary"):
            delete_subject(current_subject['subject_code'])       


def Attendance_Records_tab():
    st.header('Attendance Records')

    teacher_id = st.session_state.teacher_data['teacher_id']

    records = get_attendance_for_teacher(teacher_id)

    if not records:
        return
    
    data = []

    for r in records:
        ts = r.get('timestamp')

        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
            "Subject": r['subjects']['subject_name'],
            "Subject Code":r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })


    df = pd.DataFrame(data)



    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_Count = ('is_present', 'sum'),
            Total_Count =('is_present', 'count')
        ).reset_index()

    )

    summary['Attendance Stats'] = (
        "✅ " + summary['Present_Count'].astype(str) + " /"
        + summary['Total_Count'].astype(str) + ' Students'
    )

    display_df = ( summary.sort_values(by='ts_group' ,ascending=False)
                  [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
                  )
    
    st.dataframe(display_df, width='stretch', hide_index=True)
  



def login_teacher(username,password):
    if not username or not password:
        return False
    teacher=teacher_login(username,password)
    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True
    
    return False


              


def teacher_login_screen():
     style_base_layout()
     style_base_all()

    
     
     cl1 , cl2 =st.columns(2, vertical_alignment="center",gap="xxlarge")
     with cl1:
      header_dashboard()

     with cl2:
       if st.button("Go Back To Home",type="secondary",key="loginbackbtn",shortcut="backspace") :
           st.session_state['login_type']=None
           st.rerun()


     st.header("Login Your Teacher Profile",text_alignment="center") 
     st.space()
     st.space()
     teacher_username= st.text_input("Enter Your Username",placeholder="username")
     teacher_pass= st.text_input("Enter Your Password",placeholder="Enter Password",type="password")
     st.divider()
     btnc1,btnc2=st.columns(2)
     with btnc1:
        if st.button("LogIn",width="stretch",icon=':material/passkey:',shortcut="enter"):
            if login_teacher(teacher_username,teacher_pass):
              st.toast("welcome Back" ,icon= "👋")
              import time
              time.sleep(1)
              st.rerun()
            else:
             st.error("Invalid Username and Password")    
     with btnc2:
         if st.button("Register Instead",width="stretch",icon=':material/passkey:',type="primary",shortcut="control+space"):
             st.session_state.teacher_login_type="Register"

     footer_dashboard()

def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_confirm_pass):
    if not teacher_username or not teacher_name or not teacher_pass or not teacher_confirm_pass:
        return False,"All fields are required"
    if username_exist(teacher_username):
        return False, "Username already taken"
    if teacher_pass!=teacher_confirm_pass:
        return False,"Password not match"   
    try:
        create_teacher(teacher_username,teacher_name,teacher_pass)  
        return True,"Created Successfully"
    except Exception as e:
        return False,str(e)
    





def teacher_register_screen():
    style_base_layout()
    style_base_all()
   
    cl1 , cl2 =st.columns(2, vertical_alignment="center",gap="xxlarge")
    with cl1:
         header_dashboard()
   
    with cl2:
        if st.button("Go Back To Home",type="secondary",key="loginbackbtn",shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()
             
   
   
    st.header("Register Your Teacher Profile") 
    st.space()
    st.space()
    teacher_name= st.text_input("enter your name",placeholder="name")
    teacher_username=st.text_input("enter your username",placeholder="username")
    teacher_pass= st.text_input("Enter Your Password",placeholder="Enter Password",type="password")
    teacher_confirm_pass= st.text_input("Confirm Password ",placeholder="Confirm Password",type="password")
    st.divider()
    btnc1,btnc2=st.columns(2)
    with btnc1:
       if st.button("Register",width="stretch",icon=':material/passkey:',type="primary"):
           success,message =register_teacher(teacher_username,teacher_name,teacher_pass,teacher_confirm_pass)
           if success:
               st.success(message)
               import time
               time.sleep(2)
               st.session_state.teacher_login_type="LogIn"
               st.rerun()
           else:  
               st.error(message)  
       
    with btnc2:
        if st.button("Login Instead",width="stretch",icon=':material/passkey:',shortcut="control+enter"):
              st.session_state.teacher_login_type="LogIn"
        
    
    footer_dashboard()
   
    