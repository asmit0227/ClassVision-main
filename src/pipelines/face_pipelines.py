import dlib
import face_recognition_models
import streamlit as st
import numpy as np
from sklearn.svm import SVC
from src.Database.db import get_all_students


def load_dlib_models():
    detector=dlib.get_frontal_face_detector()

    sp=dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )


    face_rec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector,sp,face_rec


def get_all_embeddings(images_np):
    detector,sp,face_rec=load_dlib_models()
    faces=detector(images_np,1)
    encoding=[]

    for face in faces:
        shape=sp(images_np,face)
        descriptor=face_rec.compute_face_descriptor(images_np,shape,1)
        encoding.append(np.array(descriptor))
    return encoding  


@st.cache_resource
def get_trained_model():
    X=[]
    Y=[]

    students=get_all_students()

    for student in students:
        embedding=student.get('image_embedding')
        if embedding:
          X.append(np.array(embedding))
          Y.append(student.get('student_id'))


    if len(X)==0:
        return 0

    clf=SVC(kernel='linear',probability=True,class_weight='balanced' )
    try:
        clf.fit(X,Y)  
    except ValueError:
        pass
    return {'clf': clf, 'X':X, "Y":Y}


def train_classifier():
        st.cache_resource.clear()
        model_data=get_trained_model()
        return bool(model_data)


def predict_attendance(class_image_np):
    encodings = get_all_embeddings(class_image_np)

    detected_student = {}


    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['Y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students)>= 2:
            predicted_id= int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
    return detected_student, all_students, len(encodings)