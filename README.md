# 🏋️ AI-Powered Real-Time Gym Trainer



# 🔗 Live Demo: https://ai-gym-coach-u3qtnlbfgrcoaxhxu5kpr2.streamlit.app



# 📖 Overview

The **AI-Powered Real-Time Gym Trainer** is an end-to-end Computer Vision application that functions as a virtual fitness coach by providing real-time exercise recognition, posture correction, repetition counting, workout analytics, and AI-powered voice coaching.

Unlike traditional workout applications that only count repetitions or display prerecorded exercise videos, this system continuously evaluates user posture using **MediaPipe Pose**, analyzes movement through **joint-angle calculations**, and generates personalized exercise recommendations using a **Large Language Model (GPT-OSS via Groq API)**.

The application is fully browser-based and enables users to perform guided workouts without installing additional software.

---

# 🎯 Problem Statement

Most online workout applications suffer from several limitations:

- No real-time posture correction
- Manual repetition counting
- Generic exercise recommendations
- No personalized workout feedback
- Lack of progress tracking
- High dependence on human trainers

Incorrect exercise form not only reduces workout effectiveness but also increases the risk of injuries.

This project addresses these challenges by combining **Computer Vision**, **Pose Estimation**, and **Generative AI** to deliver an intelligent real-time fitness coaching experience.

---

# ⭐ Key Features

## 🧠 Computer Vision

- Real-Time Pose Estimation
- Human Landmark Detection
- Joint Angle Calculation
- Live Exercise Recognition
- Motion Analysis
- Real-Time Frame Processing

---

## 💪 Exercise Tracking

Supports:

- Squats
- Push-ups
- Biceps Curls
- Lunges

Provides:

- Automatic Rep Counting
- Exercise Stage Detection
- Joint Angle Monitoring
- Workout Duration
- Estimated Calories Burned

---

## 📐 Form Validation

The system evaluates posture throughout the workout.

Features include:

- Elbow Drift Detection
- Torso Swing Detection
- Balance Analysis
- Knee Alignment
- Hip Angle Monitoring
- Back Posture Analysis

---

## 🤖 Artificial Intelligence

- AI Workout Coach
- Personalized Exercise Recommendations
- Dynamic Workout Feedback
- GPT-OSS Integration through Groq API
- Voice Coaching using Google Text-to-Speech

---

## 👤 User Management

- User Authentication
- Workout History
- Exercise Statistics
- SQLite Database
- Progress Tracking

---


# 🏗 System Architecture

```text
                                    USER

                                      │
                                      ▼

                         Streamlit Web Application

        ┌──────────────────────────────────────────────────────────────┐
        │ Login │ Dashboard │ Exercise Selection │ History │ AI Coach │
        └──────────────────────────────────────────────────────────────┘

                                      │
                                      ▼

                         Streamlit-WebRTC Camera Stream

                                      │
                                      ▼

                          VideoProcessor (OpenCV)

                                      │
                                      ▼

                           Frame Preprocessing

                                      │
                                      ▼

                         MediaPipe Pose Estimation

                                      │
                                      ▼

                      33 Human Body Landmark Detection

                                      │
                                      ▼

                  Exercise Detection & Angle Calculation

          ┌──────────────┬──────────────┬──────────────┬──────────────┐
          ▼              ▼              ▼              ▼
       Squats        Push-ups      Biceps Curl      Lunges
          │              │              │              │
          └──────────────┴──────────────┴──────────────┘

                                      │
                                      ▼

                 Finite State Machine (Rep Counting Engine)

                                      │
                                      ▼

                     Form Validation & Workout Analytics

                                      │
                      ┌───────────────┴───────────────┐
                      ▼                               ▼

                 SQLite Database                Groq GPT-OSS

                      │                               │
                      └───────────────┬───────────────┘
                                      ▼

                         AI Voice Feedback (gTTS)

                                      │
                                      ▼

                              Personalized Coaching
```

---

# ⚙️ How the Application Works

The application follows an end-to-end real-time computer vision pipeline.

### Step 1 — User Login

Users authenticate through the Streamlit interface. User profiles and workout history are securely stored in a SQLite database.

---

### Step 2 — Exercise Selection

The user selects one of the supported exercises:

- Squats
- Push-ups
- Biceps Curls
- Lunges

Based on the selected exercise, the corresponding detector module is initialized.

---

### Step 3 — Real-Time Video Streaming

The webcam is accessed using **Streamlit-WebRTC**, enabling low-latency browser-based video streaming.

Unlike OpenCV's `VideoCapture`, Streamlit-WebRTC works seamlessly in cloud deployments and supports real-time communication through WebRTC.

---

### Step 4 — Frame Processing

Each incoming video frame is processed using **OpenCV**.

The processing pipeline includes:

- Frame resizing
- RGB conversion
- Image preprocessing
- Landmark visualization
- Annotation rendering

---

### Step 5 — Pose Estimation

The processed frame is passed to **MediaPipe Pose**, which detects **33 human body landmarks** in real time.

Each landmark contains:

- X Coordinate
- Y Coordinate
- Z Coordinate
- Visibility Score

Important landmarks include:

- Nose
- Shoulders
- Elbows
- Wrists
- Hips
- Knees
- Ankles

These landmarks are used to estimate body posture and movement.

---

### Step 6 — Joint Angle Calculation

The application calculates multiple joint angles using vector mathematics.

Examples include:

- Shoulder Angle
- Elbow Angle
- Hip Angle
- Knee Angle

These joint angles form the basis for exercise recognition and posture analysis.

---

### Step 7 — Exercise Recognition

Dedicated detector classes analyze joint angles to recognize the selected exercise.

Each detector is responsible for:

- Stage Detection
- Rep Counting
- Form Validation
- Feedback Generation

Supported exercises:

- Squats
- Push-ups
- Biceps Curls
- Lunges

---

### Step 8 — Finite State Machine

Instead of simply checking joint angles, the application uses a **Finite State Machine (FSM)** to accurately count repetitions.

Typical state transitions:

```
START
   ↓
DOWN
   ↓
UP
   ↓
Rep +1
```

This approach prevents duplicate counting and improves accuracy.

---

### Step 9 — Form Validation

The system continuously evaluates the quality of each repetition.

Examples include:

#### Squats

- Knee Angle
- Hip Depth
- Back Alignment

#### Push-ups

- Elbow Extension
- Body Alignment

#### Biceps Curl

- Elbow Drift
- Torso Swing

#### Lunges

- Front Knee Angle
- Balance
- Torso Position

Incorrect posture immediately generates corrective feedback.

---

### Step 10 — Workout Analytics

During each workout the dashboard displays:

- Exercise Name
- Current Stage
- Repetition Count
- Joint Angles
- Workout Duration
- Estimated Calories Burned
- Posture Status
- AI Coaching Messages

The metrics are continuously updated in real time.

---

# 📊 Exercise Processing Pipeline

```text
Webcam

   │

   ▼

Streamlit-WebRTC

   │

   ▼

OpenCV Frame Processing

   │

   ▼

MediaPipe Pose

   │

   ▼

33 Human Landmarks

   │

   ▼

Joint Angle Calculation

   │

   ▼

Exercise Detector

   │

   ▼

Finite State Machine

   │

   ▼

Rep Counter

   │

   ▼

Form Validation

   │

   ▼

Workout Metrics

   │

   ▼

SQLite Storage

   │

   ▼

Dashboard Update
```

---


# 🤖 AI Coaching Engine

The platform integrates **GPT-OSS** through the **Groq API** to transform workout metrics into personalized fitness recommendations.

Unlike traditional gym applications that display predefined messages, the AI coach generates context-aware suggestions based on the user's exercise performance.

The coaching engine analyzes:

- Exercise Type
- Repetition Count
- Exercise Stage
- Joint Angles
- Form Validation Results
- Workout Progress

The generated response includes:

- Form Correction Tips
- Workout Suggestions
- Motivation Messages
- Injury Prevention Advice
- Performance Improvement Recommendations

The feedback is then converted into natural speech using **Google Text-to-Speech (gTTS)**, allowing users to receive hands-free coaching while exercising.

---

# 🧠 Exercise Detection Logic

Instead of training a deep learning classifier for each exercise, the application uses **joint-angle based rule-based AI**.

This approach offers:

- Low latency
- High interpretability
- Real-time inference
- No training dataset requirement
- Lightweight deployment

Each exercise detector performs the following steps:

1. Detect body landmarks.
2. Calculate relevant joint angles.
3. Determine the exercise stage.
4. Validate posture.
5. Count repetitions.
6. Generate corrective feedback.

### Example: Biceps Curl

```
Elbow Angle > 160°

        │

        ▼

Arm Fully Extended

        │

        ▼

Stage = DOWN
```

```
Elbow Angle < 50°

        │

        ▼

Arm Fully Contracted

        │

        ▼

Stage = UP

        │

        ▼

Rep Count + 1
```

---

# 💻 Technology Stack

## Programming Language

- Python

---

## Computer Vision

- OpenCV
- MediaPipe Pose

---

## Frontend

- Streamlit
- Streamlit-WebRTC

---

## Artificial Intelligence

- Groq API
-llama-3.3-70b-versatile

---

## Database

- SQLite

---

## Voice Assistant

- Google Text-to-Speech (gTTS)

---

## Deployment

- Streamlit Community Cloud

---

# 📁 Project Structure

```text
AI-Gym-Coach/

├── assets/
│
├── database/
│   ├── database.db
│   └── db_utils.py
│
├── exercises/
│   ├── base_exercise.py
│   ├── squat_detector.py
│   ├── pushup_detector.py
│   ├── biceps_detector.py
│   └── lunges_detector.py
│
├── utils/
│   ├── angle_utils.py
│   ├── drawing_utils.py
│   ├── pose_utils.py
│   └── audio_utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Supported Exercises

| Exercise | Rep Counting | Form Validation | AI Feedback |
|-----------|:------------:|:---------------:|:-----------:|
| Squats | ✅ | ✅ | ✅ |
| Push-ups | ✅ | ✅ | ✅ |
| Biceps Curls | ✅ | ✅ | ✅ |
| Lunges | ✅ | ✅ | ✅ |

---



# 🚀 Key Highlights

✔ Real-Time Computer Vision

✔ Browser-Based Webcam Streaming

✔ Pose Estimation using MediaPipe

✔ Rule-Based Exercise Recognition

✔ Finite State Machine Rep Counter

✔ AI-Powered Fitness Coach

✔ Voice-Based Workout Guidance

✔ Interactive Dashboard

✔ SQLite Database Integration

✔ Cloud Deployment

---

# 🎯 Why MediaPipe?

MediaPipe Pose was selected because it provides:

- Real-time performance
- 33 body landmarks
- High pose estimation accuracy
- Cross-platform support
- Lightweight inference
- Easy integration with OpenCV

Compared to object detection models, MediaPipe is specifically optimized for human pose estimation, making it ideal for fitness applications.

---


# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/aman12rajpoot/AI-GYM-COACH

Navigate to the project directory.

```bash
cd AI-Gym-Coach
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL="llama-3.3-70b-versatile"
```

If your application requires additional API keys or configuration, add them to the same `.env` file.

---

# ▶️ Running the Application

Start the Streamlit application.

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# ☁️ Deployment

The project is deployed using **Streamlit Community Cloud**.

### Live Demo

https://ai-gym-coach-u3qtnlbfgrcoaxhxu5kpr2.streamlit.app/

Deployment Features:

- Browser-based webcam support
- No local installation required
- Real-time pose estimation
- AI-powered workout coaching
- Cloud-hosted Streamlit application

---

# 📈 Results

The AI Gym Trainer provides:

- ✅ Real-time pose estimation using 33 body landmarks
- ✅ Accurate repetition counting
- ✅ Live posture correction
- ✅ Browser-based workout monitoring
- ✅ AI-generated exercise recommendations
- ✅ Voice-based coaching
- ✅ Workout history tracking
- ✅ Interactive dashboard
- ✅ Low-latency performance suitable for real-time exercise analysis

---

# ⚡ Performance Highlights

- Real-time webcam processing
- Lightweight pose estimation using MediaPipe
- Rule-based exercise recognition for low-latency inference
- Personalized AI coaching powered by GPT-OSS
- Browser-based deployment using Streamlit-WebRTC
- Efficient local data storage with SQLite

---

# 🧩 Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Accurate repetition counting | Implemented a Finite State Machine (FSM) to avoid duplicate counts |
| Real-time browser webcam streaming | Used Streamlit-WebRTC for low-latency communication |
| Exercise recognition | Applied joint-angle based rule engine using MediaPipe landmarks |
| Personalized coaching | Integrated GPT-OSS through the Groq API |
| Hands-free workout assistance | Generated natural voice feedback using Google Text-to-Speech |
| Workout persistence | Stored user profiles and workout history in SQLite |

---

# 📊 Skills Demonstrated

## Computer Vision

- Pose Estimation
- Human Landmark Detection
- Joint Angle Analysis
- Real-Time Video Processing
- Motion Analysis

---

## Artificial Intelligence

- Large Language Models (LLMs)
- Prompt Engineering
- AI-powered Fitness Coaching
- Groq API Integration
- GPT-OSS

---

## Software Engineering

- Object-Oriented Programming
- Modular Architecture
- Real-Time Streaming
- Database Integration
- Cloud Deployment
- Version Control using Git & GitHub

---

## Web Development

- Streamlit
- Interactive Dashboards
- Responsive UI
- Browser-based Applications

---

# 🧪 Testing

The application has been tested for:

- Squats
- Push-ups
- Biceps Curls
- Lunges

Each exercise was evaluated for:

- Repetition counting
- Exercise stage detection
- Form validation
- AI-generated feedback
- Voice coaching
- Dashboard updates

---

# 📌 Limitations

Current limitations include:

- Supports one user at a time
- Requires a webcam
- Stable internet connection needed for AI coaching
- Supports a fixed set of exercises
- Calorie estimation is approximate

These limitations provide opportunities for future enhancements.

---


# 🚀 Future Improvements

The current version focuses on real-time exercise monitoring and AI-powered coaching. Future enhancements include:

- 🤸 Automatic exercise recognition without manual selection
- 👥 Multi-person workout tracking
- 📱 Mobile application (Android & iOS)
- ☁ Cloud database integration (PostgreSQL/Firebase)
- 📈 Personalized workout plans based on user history
- 🏆 Gamification with achievements and leaderboards
- ❤️ Wearable device integration (Smartwatch/Fitness Band)
- 🧠 Deep Learning-based exercise classification
- 📊 Advanced analytics dashboard with progress visualization
- 🍎 Diet and nutrition recommendation system
- 🌍 Multi-language voice coaching
- 📹 Workout recording and replay functionality

---

# 🙏 Acknowledgements

This project was built using the following open-source technologies:

- Python
- Streamlit
- Streamlit-WebRTC
- OpenCV
- MediaPipe Pose
- SQLite
- Groq API
-llama-3.3-70b-versatile
- Google Text-to-Speech (gTTS)

Special thanks to the open-source community for developing these powerful libraries and tools.

---





# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🛠 Suggest new features
- 🐛 Report issues
- 📢 Share it with others

Your support is greatly appreciated!

---

# 📌 Project Summary

The **AI-Powered Real-Time Gym Trainer** is an end-to-end intelligent fitness coaching platform that combines **Computer Vision**, **Pose Estimation**, **Rule-Based Exercise Analysis**, and **Generative AI** to deliver a personalized workout experience.

Using **MediaPipe Pose**, the application detects **33 human body landmarks** in real time and analyzes body movements through joint-angle calculations. A **Finite State Machine (FSM)** ensures accurate repetition counting while continuously validating exercise form. Users receive instant posture correction, workout analytics, and AI-generated coaching powered by **GPT-OSS** via the **Groq API**. The guidance is further enhanced with natural voice feedback using **Google Text-to-Speech (gTTS)**.

Built with **Python**, **OpenCV**, **Streamlit**, **Streamlit-WebRTC**, and **SQLite**, the project demonstrates a complete real-time computer vision pipeline—from browser-based video streaming and pose estimation to intelligent exercise recognition, personalized coaching, and cloud deployment.

This project showcases practical skills in **Computer Vision**, **Artificial Intelligence**, **Software Engineering**, **Real-Time Video Processing**, and **Cloud Deployment**, making it a strong portfolio project for Machine Learning, AI, Computer Vision, and Software Engineering roles.

---
