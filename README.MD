# ClassVision — AI-Powered Smart Attendance System

<p align="center">
  <strong>AI That Recognizes Your Class</strong><br>
  Face Recognition • Voice Recognition • Smart Attendance • Cloud Database
</p>

ClassVision is an AI-powered classroom attendance management application that helps teachers record attendance and helps students manage their class participation records. It combines facial recognition and voice verification with a role-based Streamlit interface and a cloud-backed database.

Teachers can create subjects, enroll students, share unique join codes or QR codes, capture classroom images to recognize students, and review attendance records. Students can join subjects and view their attendance history.

---

## Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Run Locally](#run-locally)
- [Application Workflow](#application-workflow)
- [Database](#database)
- [Security and Privacy](#security-and-privacy)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [Demo and Screenshots](#demo-and-screenshots)
- [License](#license)

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

## How It Works

### Face Recognition Attendance Flow

1. A teacher selects the attendance workflow and provides a classroom image.
2. The application detects faces in the image.
3. Facial landmarks and face encodings are extracted using the face-processing pipeline.
4. Detected encodings are compared against enrolled student face data.
5. Matching students are identified according to the recognition logic.
6. Attendance information is recorded for the relevant subject/session.

### Voice Verification Flow

1. A voice recording is provided to the voice-processing module.
2. Librosa loads and prepares the audio at the required sampling rate.
3. Resemblyzer converts the voice sample into a speaker embedding.
4. The generated embedding is compared with stored voice representations.
5. The similarity result is used by the voice verification logic.

### Enrollment Flow

1. A teacher creates a subject.
2. ClassVision generates a unique join code (and QR code where available).
3. Students use the join flow to enroll in the subject.
4. Enrollment records are stored in Supabase.
5. The teacher can manage the class and access attendance information.

## System Architecture

```text
                         ┌────────────────────────┐
                         │     Streamlit UI      │
                         │  Teacher / Student    │
                         └───────────┬──────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 │             App / Screens            │
                 │ Login • Dashboards • Subjects       │
                 │ Enrollment • Attendance             │
                 └───────────┬──────────────────────────┘
                             │
          ┌──────────────────┴───────────────────┐
          │                                      │
 ┌────────▼───────────┐                ┌─────────▼──────────┐
 │ Face Recognition  │                │ Voice Processing  │
 │ dlib / encodings │                │ Librosa          │
 │ Face embeddings   │                │ Resemblyzer      │
 └────────┬───────────┘                └─────────┬──────────┘
          │                                      │
          └──────────────────┬───────────────────┘
                             │
                    ┌────────▼─────────┐
                    │ Recognition Logic │
                    │ Matching / Verify│
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │    Supabase      │
                    │ Users • Subjects │
                    │ Enrollments      │
                    │ Attendance      │
                    └──────────────────┘
```

## Technology Stack

| Technology | Role in ClassVision |
|---|---|
| Python | Core programming language and application logic |
| Streamlit | Interactive UI, teacher/student screens, forms, and dashboards |
| NumPy | Numerical operations and embedding comparison |
| Pandas | Tabular attendance/data processing |
| dlib | Face detection-related processing, facial landmarks, and face feature extraction |
| face_recognition_models | Pretrained model assets used by the facial-recognition pipeline |
| scikit-learn | Machine-learning utilities, including recognition/classification components where used |
| Librosa | Audio loading and preprocessing |
| Resemblyzer | Speaker embeddings and voice similarity/verification |
| Supabase | Cloud database and data access |
| bcrypt | Password hashing and password verification |
| Segno | QR-code generation |
| Pillow | Image loading and image-related operations |
| setuptools | Build/install compatibility support for dependencies |

## Project Structure

The repository is organized around the Streamlit entry point and application modules under `src`.

```text
ClassVision-main/
├── .devcontainer/
├── src/
│   ├── Database/
│   │   ├── config.py
│   │   └── db.py
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   ├── componenets/
│   │   └── dialog_auto_enroll.py
│   ├── ...                    # Recognition, attendance, UI modules
├── app.py                    # Streamlit entry point
├── requirements.txt
├── README.MD
└── LICENSE
```

> The `src` tree above is illustrative rather than exhaustive; consult the repository for the current module names.

## Setup and Installation

### Prerequisites

- Python installed and available from the terminal.
- Git.
- A Supabase project and database credentials/configuration.
- A webcam or classroom image source for attendance capture.
- Microphone/audio sample if using voice recognition features.

### 1. Clone the repository

```bash
git clone https://github.com/asmit0227/ClassVision-main.git
cd ClassVision-main
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```bat
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some computer-vision/audio packages may require platform-specific wheels or additional system dependencies. If installation fails, check the package's installation notes for your Python version and operating system.

## Configuration

Configure Supabase connection details in the project's database configuration module or the configuration method used by your local copy.

**Do not commit credentials, service-role keys, passwords, or private biometric data to GitHub.** Use environment variables or a local secrets file excluded by `.gitignore` wherever possible.

Example environment-variable pattern (adapt the names to the application's actual configuration):

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

The variable names above are examples; use the names expected by the project's configuration code.

## Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will print a local URL, typically:

```text
http://localhost:8501
```

Open that address in a browser.

## Application Workflow

### Teacher

1. Register or log in as a teacher.
2. Open the teacher dashboard.
3. Create and manage subjects.
4. Enroll students or share subject join codes/QR codes.
5. Capture/upload a classroom image for recognition-based attendance.
6. Review and manage attendance records.

### Student

1. Register or log in as a student.
2. Join a subject using its join code or enrollment link/QR flow.
3. Open the student dashboard.
4. View enrolled subjects and attendance history.

## Database

Supabase is used for cloud-backed data storage. The project uses database records to manage application data such as:

- Teacher and student user profiles.
- Subjects.
- Subject enrollment relationships.
- Attendance records.
- Join-code related data.

The exact schema and table names should be checked in the Supabase setup and database module files for the deployed/current version.

## Security and Privacy

ClassVision works with facial and voice representations, which are sensitive biometric data. For a real institutional deployment, the following should be considered:

- Obtain informed consent before collecting biometric samples.
- Restrict database and application access by role.
- Avoid exposing database credentials or privileged keys in source code.
- Secure stored biometric data and limit retention.
- Provide a manual attendance correction/review path.
- Clearly explain recognition limitations and possible false matches.
- Follow applicable institutional policies and privacy laws.

Passwords should not be stored as plain text. ClassVision includes bcrypt-based password hashing/verification.

## Limitations

- Recognition can be affected by lighting, camera angle, image resolution, face occlusion, and pose.
- Voice verification can be affected by background noise, microphone quality, speaking distance, and variation in the speaker's voice.
- Similarity-based biometric recognition may produce false matches or missed matches.
- Performance may vary with hardware and the number of faces/audio samples processed.
- Attendance records should be reviewed in situations where recognition confidence is uncertain.
- The project is a prototype and requires additional validation before use in high-stakes attendance decisions.

## Future Improvements

- Add a robust manual review and attendance correction workflow.
- Add stronger role-based authorization and security auditing.
- Improve handling of duplicate attendance and session boundaries.
- Add attendance exports (CSV/PDF) and richer analytics.
- Improve recognition evaluation with documented precision/recall and threshold testing.
- Add configurable biometric-data retention and deletion controls.
- Add automated tests for database, recognition, enrollment, and attendance flows.
- Improve deployment, monitoring, and backup practices.

## Learning Outcomes

Working on ClassVision involves practical learning in:

- Python application development.
- Streamlit UI and session-state navigation.
- Database integration with Supabase.
- Authentication concepts and password hashing with bcrypt.
- Computer vision and face embeddings.
- Facial feature processing with dlib.
- Audio preprocessing and speaker embeddings.
- Voice similarity/verification with Resemblyzer.
- Attendance and enrollment workflows.
- QR-code generation.
- Modular application structure and debugging.
- Integrating multiple AI/data libraries into a single application.

## Demo and Screenshots

**Live demo / landing page:** https://cv-landing-page-sigma.vercel.app/

Add screenshots to the repository (for example, under a `screenshots/` directory) and update these placeholders:

| Screen | Screenshot |
|---|---|
| Home / Login | `screenshots/home.png` |
| Teacher Dashboard | `screenshots/teacher_dashboard.png` |
| Student Dashboard | `screenshots/student_dashboard.png` |
| Attendance | `screenshots/attendance.png` |
| Subject / QR Enrollment | `screenshots/enrollment.png` |

<!-- Example after adding screenshot files:
![ClassVision Home](screenshots/home.png)
-->

## Author

**Asmit**

AI / Machine Learning and Python project portfolio.

- GitHub: [@asmit0227](https://github.com/asmit0227)

## License

See the [`LICENSE`](LICENSE) file in this repository for the project's license and usage terms.
