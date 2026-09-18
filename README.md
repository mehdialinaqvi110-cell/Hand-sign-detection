# 🤟 Sign Language Detection Using MediaPipe

A real-time **Sign Language Detection** application built using **MediaPipe, OpenCV, Streamlit, and Python**.

The application uses a webcam to capture hand gestures, detects hand landmarks using **MediaPipe**, processes the detected hand information, and displays the recognized sign through a user-friendly **Streamlit web application**.

## 🚀 Project Overview

Communication can be challenging for people who use sign language, especially when interacting with people who do not understand it.

This project demonstrates a computer-vision-based approach to recognizing hand signs in real time.

The application:

* 📷 Captures video using a webcam
* ✋ Detects hands using MediaPipe
* 📍 Extracts hand landmarks
* 🧠 Processes the detected hand information
* 🔤 Identifies the corresponding sign
* 🔊 Converts recognized text into speech using `pyttsx3`
* 🌐 Provides an interactive interface using Streamlit

## 🛠️ Technologies Used

| Technology       | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Python           | Core programming language                 |
| MediaPipe        | Hand detection and landmark extraction    |
| OpenCV           | Image/video processing                    |
| Streamlit        | Web application and deployment            |
| Streamlit-WebRTC | Real-time webcam/video streaming          |
| NumPy            | Numerical operations                      |
| Pyttsx3          | Text-to-speech conversion                 |
| Matplotlib       | Visualization/supporting image processing |

## 🏗️ Project Architecture

```text
Webcam
   │
   ▼
OpenCV / WebRTC
   │
   ▼
MediaPipe Hand Detection
   │
   ▼
Hand Landmark Extraction
   │
   ▼
Sign Recognition
   │
   ├──────────────► Display Recognized Sign
   │
   └──────────────► Text-to-Speech
                         │
                         ▼
                    Spoken Output
```

## 📁 Project Structure

```text
Sign-Language-Detection/
│
├── app.py
│
├── backend/
│   └── hand_landmarker.py
│
├── model/
│   └── hand_landmarker.task
│
├── requirements.txt
│
└── README.md
```

> The exact file structure can be adjusted according to the files in your repository.

## ⚙️ Installation

### 1. Clone the Repository

```bash
https://github.com/mehdialinaqvi110-cell/Hand-sign-detection/tree/main
```

Move into the project directory:

```bash
cd sign-language-detection
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv signLanguage
```

Activate it:

```bash
signLanguage\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The project uses packages such as:

```text
mediapipe
opencv-python
numpy
streamlit
streamlit-webrtc
av
pyttsx3
```

## ▶️ Run the Application

Because this is a Streamlit application, run it using:

```bash
streamlit run app.py
```

You should see something similar to:

```text
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

Open:

```text
http://localhost:8501
```

in your browser.

## ✋ How It Works

### Step 1 — Webcam Input

The application accesses the user's webcam and receives video frames in real time.

### Step 2 — Hand Detection

MediaPipe is used to detect the hand from each video frame.

MediaPipe identifies important points, or **landmarks**, on the hand.

### Step 3 — Landmark Processing

The detected hand landmarks provide information about the position of different parts of the hand, such as:

* Wrist
* Thumb
* Index finger
* Middle finger
* Ring finger
* Little finger

These landmark coordinates can then be used to identify different hand gestures.

### Step 4 — Sign Recognition

The processed hand information is used to determine the corresponding sign.

The recognized sign is displayed in the Streamlit interface.

### Step 5 — Text-to-Speech

The recognized output can be converted into speech using:

```python
pyttsx3
```

This allows the detected sign to be communicated as spoken output.

## 🎯 Features

* Real-time hand detection
* Webcam-based sign recognition
* MediaPipe hand landmark detection
* Interactive Streamlit interface
* Real-time video processing
* Text-to-speech functionality
* Browser-based application
* Python virtual-environment support

## 📦 Requirements

Example `requirements.txt`:

```text
mediapipe
opencv-python
numpy
streamlit
streamlit-webrtc
av
pyttsx3
```

## 🖥️ Running Locally

After activating the virtual environment:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

Allow the browser to access your webcam when prompted.


## ⚠️ Limitations

The current project may have limitations such as:

* Recognition can depend on lighting conditions.
* Camera quality can affect detection.
* Hand position and orientation can affect recognition.
* Multiple hands may require additional handling.
* Recognition accuracy depends on the signs supported by the implementation.
* Real-time processing performance depends on the user's system and browser.

## 🔮 Future Improvements

Possible improvements include:

* Add more sign-language gestures
* Improve recognition accuracy
* Support continuous sign sequences
* Recognize complete words and sentences
* Add multiple-hand detection
* Improve robustness under different lighting conditions
* Add a sign-to-text history
* Improve the user interface
* Add multilingual text-to-speech
* Deploy a more optimized real-time inference pipeline

## 📚 Key Concepts Demonstrated

This project demonstrates practical experience with:

* Computer Vision
* Hand Landmark Detection
* MediaPipe
* OpenCV
* Real-Time Video Processing
* Streamlit
* WebRTC
* Python
* Text-to-Speech
* Virtual Environments
* Application Deployment

## 👨‍💻 Author

**Mehdi Ali**

B.Tech Biotechnology
National Institute of Technology Warangal

## ⭐ Acknowledgements

This project uses the following technologies and libraries:

* MediaPipe
* OpenCV
* Streamlit
* Streamlit-WebRTC
* Python
* pyttsx3

---

## 📌 Project Summary

**Sign Language Detection** is a real-time computer vision application that uses **MediaPipe for hand landmark detection**, **OpenCV/WebRTC for video processing**, and **Streamlit for the web interface**. The recognized signs can also be converted into speech using **pyttsx3**, providing a practical demonstration of real-time gesture recognition and human-computer interaction.
