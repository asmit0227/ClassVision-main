from src.Database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode() 

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())


def username_exist(username):
    # Check for unique username, returns false when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0 


def create_teacher(username,name,password):
    data = {"username": username,
            "name"    : name,
            "password": hash_pass(password),
              
            }
    response= supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username,password):
    response=supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher["password"]):
            return teacher
    return None

    

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data


def create_student(new_name, image_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'image_embedding':image_embedding, "voice_embedding": voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data


def create_subject(subject_code, subject_name, section, teacher_id):
    data = {"subject_code": subject_code, "subject_name": subject_name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, student_subjects(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data


    for sub in subjects:
        sub['total_students'] = sub.get("student_subjects", [{}])[0].get('count', 0) if sub.get('student_subjects') else 0
        attendance = sub.get('attendance_logs', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions


        sub.pop('student_subjects', None)
        sub.pop('attendance_logs', None)

    return subjects


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('student_subjects').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('student_subjects').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('student_subjects').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()

    print( response.data)
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data

def delete_subject(subject_code):
    response = supabase.table('subjects').delete().eq("subject_code",subject_code).execute()
    return response.data