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
- [x] Handled the Virtual NAO microphone limitation without crashing the behavior

## Still To Do

- [ ] Test the microphone on the real NAO
- [ ] Record a real audio file
- [ ] Save/transfer the audio to the PC
- [ ] Create the camera capture
- [ ] Test the camera on NAO
- [ ] Capture face images/frames
- [ ] Save/transfer the images to the PC
- [ ] Make audio and camera capture work at the same time
- [ ] Connect the captured data with the backend
- [ ] Test the full data capture process

## Current Status

The audio capture flow is ready for testing on the real NAO.

The Virtual NAO does not provide the ALAudioRecorder service, so I used it to test the flow and timing only. Real audio recording still needs to be tested using the physical NAO.

## Next

Start working on the camera capture using Choregraphe.

## My Part

My responsibility is:

NAO microphone + NAO camera -> capture the data -> save/send it to the PC.

The other team members will handle speech-to-text, emotion recognition, facial expression recognition, and comparing the final results.