# Reem - NAO Data Capture Progress

## What I am working on

My part is to capture audio and camera data from NAO and prepare the data to be sent to the PC.

## Done

- [x] Created the GitHub repository
- [x] Connected the project to VS Code
- [x] Created the FastAPI backend
- [x] Added the basic backend endpoints
- [x] Created my NAO Data Capture project in Choregraphe
- [x] Created the Capture_Audio box
- [x] Added the NAO audio recorder code
- [x] Added an 8-second response time
- [x] Added start and stop recording logic
- [x] Tested the audio capture flow using Virtual NAO
- [x] Handled the Virtual NAO microphone limitation without crashing
- [x] Tested audio recording using the laptop microphone
- [x] Saved each laptop recording with a different name
- [x] Created separate folders for laptop and NAO audio
- [x] Added .gitignore to keep audio recordings out of GitHub

## Still To Do

- [ ] Test the microphone on the real NAO
- [ ] Record a real audio file using NAO
- [ ] Transfer NAO audio to data/nao_audio on the PC
- [ ] Create the camera capture
- [ ] Test the camera
- [ ] Capture face images/frames
- [ ] Save camera data on the PC
- [ ] Make audio and camera capture work at the same time
- [ ] Connect the captured data with the backend
- [ ] Test the full data capture process

## Current Status

The audio capture flow is ready.

The Virtual NAO was used to test the NAO audio flow and timing.

Since Virtual NAO does not provide the ALAudioRecorder service, I also tested real audio recording using the laptop microphone. The recording is saved successfully on the PC.

The physical NAO microphone still needs to be tested when the robot is available.

## Audio Files

Laptop microphone recordings are saved in:

data/laptop_audio/

NAO recordings will be transferred and saved in:

data/nao_audio/

These audio folders are ignored by Git and are not uploaded to GitHub.

## Next

Start working on the camera capture.

## My Part

My responsibility is:

NAO microphone + NAO camera -> capture the data -> save/send it to the PC.

The other team members will handle speech-to-text, emotion recognition, facial expression recognition, and comparing the final results.