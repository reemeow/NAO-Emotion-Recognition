# Reem — NAO Data Acquisition & Backend Progress

## 1. My Responsibilities

My primary responsibility is developing and testing the data acquisition and communication pipeline between the NAO V6 humanoid robot and the PC-based emotion recognition system.

My work focuses on:

- NAO microphone and camera integration.
- Audio recording and image acquisition.
- Data transfer and file organization.
- FastAPI backend development.
- Testing and troubleshooting robot-to-PC communication.
- Preparing acquired data for downstream AI processing.

## 2. Completed Work

### Audio Acquisition

- [x] Created the NAO Data Capture project in Choregraphe.
- [x] Developed the `Capture_Audio` component.
- [x] Implemented recording using `ALAudioRecorder`.
- [x] Configured an approximately 8-second response recording window.
- [x] Implemented recording start and stop logic.
- [x] Tested the recording workflow with Virtual NAO.
- [x] Handled Virtual NAO microphone limitations.
- [x] Tested local microphone recording.
- [x] Successfully recorded audio using the physical NAO V6 microphone.
- [x] Transferred recorded WAV files from NAO to the PC.
- [x] Organized recordings using sequential filenames.

### Camera Acquisition

- [x] Developed the `Capture_Camera` component in Choregraphe.
- [x] Accessed `ALVideoDevice` using Virtual NAO.
- [x] Captured 320 × 240 RGB frames.
- [x] Implemented raw RGB frame transfer to FastAPI.
- [x] Converted received RGB data into JPEG images.
- [x] Saved captured images in `data/nao_frames/`.
- [x] Tested the complete Virtual NAO camera-to-backend workflow.
- [x] Tested camera acquisition using the laptop camera and OpenCV.
- [x] Successfully captured images using the physical NAO V6 camera.
- [x] Tested physical robot image acquisition using `ALPhotoCapture`.

### Robot Communication & File Transfer

- [x] Established SSH communication with the physical NAO robot.
- [x] Configured SCP file transfers between NAO and the PC.
- [x] Set up passwordless SSH authentication.
- [x] Successfully retrieved recorded audio and captured images.
- [x] Developed file-monitoring and sequential naming scripts to support automated data transfer.

### Backend Development

Developed a Python backend using FastAPI.

Implemented endpoints:

- [x] `GET /` — Backend health check.
- [x] `POST /api/session/start` — Initialize a session.
- [x] `GET /api/scenario/next` — Retrieve a predefined interaction scenario.
- [x] `POST /api/response/submit` — Receive a spoken-response transcript.
- [x] `POST /api/camera/frame` — Receive and save an image.
- [x] `POST /api/camera/raw-frame` — Receive raw RGB data, convert it to JPEG, and save it.

The current backend provides the basic API structure for managing scenarios and receiving data. Full session persistence and automatic AI evaluation are not yet integrated.

### Data Management & Privacy

- [x] Organized separate folders for recorded audio and captured images.
- [x] Added recorded audio directories to `.gitignore`.
- [x] Added captured-image directories to `.gitignore`.
- [x] Excluded locally recorded audio and image files from Git tracking.

## 3. Verified Data Acquisition Workflows

### Physical NAO Audio Workflow

NAO Microphone → Audio Recording → WAV File → SSH/SCP → PC Storage

**Status:** Successfully tested with the physical NAO V6.

### Physical NAO Image Acquisition

NAO Camera → ALPhotoCapture → Image File → PC Transfer

**Status:** Physical robot image capture and file retrieval tested successfully.

### Virtual NAO Camera-to-Backend Workflow

Virtual NAO Camera → ALVideoDevice → Raw RGB Frame → HTTP → FastAPI → JPEG Conversion → Local Storage

**Status:** Successfully tested.

### Laptop Camera-to-Backend Workflow

Laptop Camera → OpenCV → FastAPI → Local Storage

**Status:** Successfully tested.

These workflows have been tested separately. A fully synchronized audio-and-camera session is still under development.

## 4. Preliminary AI Processing Tests

The captured data is intended to be processed by separate team modules.

Standalone experiments have included:

- Speech transcription using Whisper.
- Facial expression analysis using DeepFace.
- Preliminary language model evaluation for text-based emotion classification.

These experiments do not mean that all AI components have been integrated into the final NAO interaction workflow.

The Speech-to-Text and Computer Vision modules are primarily handled by other team members.

## 5. Remaining Tasks

### System Integration

- [ ] Synchronize audio recording and camera capture during the same interaction.
- [ ] Connect the physical NAO data acquisition workflow to the complete backend session pipeline.
- [ ] Integrate the Speech-to-Text component.
- [ ] Integrate the selected MLLM emotion classification component.
- [ ] Integrate the selected facial expression recognition component.
- [ ] Implement persistent session-level data logging.
- [ ] Connect classification results to the backend response evaluation process.

### Evaluation and Reporting

- [ ] Implement complete response correctness evaluation.
- [ ] Integrate descriptive verbal–facial emotion comparison.
- [ ] Generate structured session reports.
- [ ] Perform end-to-end testing with predefined labeled scenarios.
- [ ] Measure workflow completion and processing latency.
- [ ] Resolve integration issues identified during testing.

## 6. Current Project Status

**Status: Core data acquisition and backend components implemented; full system integration in progress.**

The physical NAO V6 has been successfully used for image capture and audio recording.

Robot-to-PC data transfer has also been demonstrated, and basic FastAPI endpoints have been developed to receive and process acquired data.

The next major milestone is connecting the existing components into a single coordinated interaction workflow.

The complete emotion recognition and reporting system has not yet been validated end-to-end.

## 7. Data Directories

```text
data/
├── laptop_audio/
├── nao_audio/
└── nao_frames/
```

These directories store locally captured data and are excluded from version control.

## 8. Project Scope

The project is designed to support structured emotion-recognition activities involving four target emotions:

- Happiness
- Sadness
- Anger
- Neutrality

The system uses predefined emotional images, open-ended verbal responses, and independent facial-expression analysis.

The current evaluation scope is limited to prototype testing using predefined labeled scenarios. Testing with children with Autism Spectrum Disorder (ASD) is not part of the current implementation phase.

---

**Contributor:** Reem Abdulhameed

**Project:** NAO-Based Emotion Recognition System

**University:** University of Jeddah

**Academic Year:** 2026–2027
