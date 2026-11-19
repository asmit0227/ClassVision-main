# ClassVision - AI That Recognize Your Class

ClassVision is an AI-powered smart attendance management system designed to make classroom attendance faster, easier, and more reliable.

Instead of relying on traditional roll calls or manual attendance sheets, ClassVision uses Face and voice Recognition technology to identify students and automate the attendance process.

The platform provides separate interfaces for Teachers and Students. Teachers can create and manage subjects, enroll students using unique join codes and QR codes, capture classroom images for attendance, and monitor attendance records. Students can securely access the system using facial recognition, join subjects, and view their attendance history.

ClassVision combines Artificial Intelligence, Computer Vision, and modern web technologies to create a practical solution for smarter classroom management.

## Overview

Manual attendance is often repetitive and takes time away from classroom activities. ClassVision aims to streamline this process by using biometric recognition to identify enrolled students from classroom images, while providing a structured attendance platform for both teachers and students.

The application has two primary roles:

- **Teacher:** Manage subjects, enrollments, attendance, and class information.
- **Student:** Join subjects and view their attendance records.

ClassVision uses face embeddings for facial matching and voice embeddings for speaker verification. User, subject, enrollment, and attendance information is stored using Supabase.

> ClassVision is a portfolio/learning project. Recognition performance depends on image quality, lighting, camera position, audio quality, and enrollment samples. Attendance records should be reviewed when needed.

## Problem Statement

Traditional attendance processes can be slow and prone to manual mistakes. They can also make it difficult for students and teachers to access organized attendance records.

ClassVision addresses these challenges by:

- Automating student recognition from classroom images.
- Providing teacher and student dashboards.
- Organizing subjects and student enrollments.
- Using join codes and QR codes to simplify enrollment.
- Maintaining attendance records in a cloud database.
- Providing students with access to their attendance history.

 ## Key Features

### AI-Based Face Recognition
- Detects and processes faces from images.
- Extracts facial features and converts them into numerical face embeddings.
- Compares a detected face against enrolled student representations.
- Supports identifying multiple enrolled students in a classroom image.
- Uses recognition results to support attendance marking.

### Voice Recognition / Verification
- Processes audio samples for speaker recognition.
- Prepares audio using Librosa.
- Generates voice embeddings with Resemblyzer.
- Compares voice representations for speaker verification.

### Teacher Dashboard
- Teacher-focused interface and workflow.
- Subject creation and management.
- Student enrollment management.
- Attendance capture and record review.
- Join-code and QR-code generation for enrollment.

### Student Dashboard
- Student-focused interface.
- Join subjects using enrollment codes or QR-based flows.
- View enrolled subjects and attendance records.

### Subject Enrollment
- Generates unique join codes for subjects.
- QR codes make joining a subject easier.
- Enrollment data is managed centrally.

### Cloud Database
- Supabase stores application records such as users, subjects, enrollments, and attendance.
- Database operations are handled through the Supabase client.

### Streamlit Interface
- Interactive Python-based interface.
- Login, registration, forms, dashboards, image upload, and attendance views.
- Session state manages navigation and login state.




 ## Project Screenshots
<p align="center">
    <img src="src/assets/student_login2.png" width="850"
</p>
<p align="center"> 
    <img src="src/assets/teacher_dashboard.png" width="850">
</p>
<p align="center">
    <img src="src/assets/attendance_tab.png" width="850">  
</p>
<p align="center"> 
    <img src="src/assets/student_dashboard.png" width="850">
</p>
<p align="center"> 
    <img src="src/assets/enrollment_subject.png" width="850">
</p> 
<p align="center"> 
    <img src="src/assets/voice_atte.png" width="850">
</p>


## Tech Stack & Technologies Used

ClassVision combines Artificial Intelligence, Computer Vision, Voice Processing, Cloud Database, and Web Technologies to build a complete smart attendance management system.

### 🎨 Streamlit

Streamlit is used to build the interactive web interface of ClassVision.

#### Key Features Used:

Interactive Teacher and Student dashboards
Forms for login, registration, and subject creation
Image uploading and classroom attendance capture
Attendance tables and records visualization
Session-based navigation and authentication flow
Fast deployment of the AI-powered web application

### ☁️ Supabase
Supabase is used as the cloud backend and database platform for storing and managing application data.

#### Key Features Used:

User data storage
Teacher and student records
Subject and classroom management
Student enrollment records
Attendance data storage
Join code management
Cloud-based database access
Secure data retrieval and updates
### 🧠 dlib

dlib is used for computer vision and facial feature processing.

#### Key Features Used:

Face detection
Facial landmark detection
Face feature extraction
Generation of facial embeddings
Support for accurate face comparison and recognition

dlib provides the underlying face-processing capabilities used by the facial recognition system.

### 🤖 Face Recognition

Face Recognition technology is the core AI component responsible for identifying students through their facial features.

#### Key Features Used:

Student face detection
Face encoding generation
Comparison of facial embeddings
Student identity matching
Recognition of multiple students from classroom images
Automated attendance marking
Reduction of manual attendance effort

The system compares detected student faces with stored facial encodings to identify students and mark their attendance.

### 🎙️ Librosa

Librosa is used for audio processing and feature extraction.

#### Key Features Used:

Audio file processing
Voice signal analysis
Audio normalization
Feature extraction from speech recordings
Preprocessing voice samples before speaker verification

Librosa helps prepare and analyze voice recordings used by the voice authentication system.

### 🗣️ Resemblyzer

Resemblyzer is used for AI-based speaker recognition and voice verification.

#### Key Features Used:

Voice embedding generation
Speaker identity representation
Voice similarity comparison
Student voice verification
Additional biometric authentication support

Resemblyzer converts a person's voice into numerical embeddings that can be compared with previously stored voice samples.

### 🌐 Flask

Flask is used to create lightweight backend services and APIs for AI-related operations.

#### Key Features Used:

REST API development
Communication between application components
AI model integration
Handling prediction and recognition requests
Sending JSON responses
Connecting frontend applications with backend AI services

Flask helps separate AI processing logic from the user interface and makes the system easier to scale and integrate.


## 🔄 Technology Flow
Streamlit provides the user interface for Teachers and Students.
Supabase stores users, subjects, enrollment data, and attendance records.
dlib and Face Recognition process facial images and generate face embeddings.
Classroom images are analyzed to automatically recognize students and mark attendance.
Librosa processes and prepares voice recordings.
Resemblyzer generates voice embeddings and performs speaker verification.
Flask provides backend API services for AI and recognition-related operations.
All components work together to create a secure and intelligent attendance management system.


## 🎯 Project Goal

The goal of ClassVision is to reduce the time teachers spend taking attendance while providing a simple, scalable, and AI-driven attendance management system for educational institutions.

### License
Copyright © 2026 Asmit. All Rights Reserved.

This project is publicly available for viewing and portfolio evaluation only. Copying, modifying, redistributing, publishing, or using this project's source code without prior permission is prohibited.

See the LICENSE file for details.
