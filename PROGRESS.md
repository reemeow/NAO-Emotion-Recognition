# Reem - NAO Data Capture Progress

## What I am working on

My part is to capture audio and camera data from NAO and prepare the data to be sent to the PC for emotion analysis.

## Done

### Audio Capture

- [x] Created the NAO Data Capture project in Choregraphe
- [x] Created the Capture_Audio box
- [x] Added the NAO audio recorder code
- [x] Added an 8-second response time
- [x] Added start and stop recording logic
- [x] Tested the audio capture flow using Virtual NAO
- [x] Handled the Virtual NAO microphone limitation without crashing
- [x] Tested audio recording using the laptop microphone
- [x] Saved laptop recordings with unique filenames
- [x] Created separate folders for laptop and NAO audio

### Camera Capture

- [x] Created the Capture_Camera box in Choregraphe
- [x] Accessed ALVideoDevice successfully on Virtual NAO
- [x] Captured a 320x240 RGB camera frame
- [x] Created a FastAPI endpoint for camera frame transfer
- [x] Sent a raw RGB frame from Choregraphe to the PC
- [x] Converted the raw RGB frame to JPEG on the PC
- [x] Saved NAO camera frames in data/nao_frames/
- [x] Tested the complete Virtual NAO camera transfer flow
- [x] Created a laptop camera test using OpenCV
- [x] Captured a real frame using the laptop camera
- [x] Sent the laptop camera frame to FastAPI successfully
- [x] Saved the laptop camera test frame successfully

### Data and Privacy

- [x] Added audio folders to .gitignore
- [x] Added camera frames folder to .gitignore
- [x] Prevented recorded audio and captured images from being uploaded to GitHub

## Current Camera Flow

Virtual NAO camera flow:

NAO Camera -> Capture_Camera -> Raw RGB Frame -> HTTP -> FastAPI -> JPEG -> data/nao_frames/

Laptop camera test flow:

Laptop Camera -> OpenCV -> FastAPI -> data/nao_frames/

Both PC-side camera transfer and image saving have been tested successfully.

## Still To Do

- [ ] Test the microphone on the physical NAO V6
- [ ] Record a real audio file using the physical NAO
- [ ] Transfer NAO audio to data/nao_audio/ on the PC
- [ ] Test the camera on the physical NAO V6
- [ ] Capture a real face frame using the physical NAO camera
- [ ] Send the physical NAO camera frame to FastAPI
- [ ] Verify the physical NAO frame is saved correctly on the PC
- [ ] Synchronize audio and camera capture during the same interaction
- [ ] Connect captured data with the other emotion recognition modules
- [ ] Test the complete end-to-end data capture process

## Current Status

The audio capture flow is ready for physical NAO testing.

The camera capture and frame transfer pipeline has been successfully tested using Virtual NAO. A raw RGB frame can be captured in Choregraphe, sent through HTTP to the FastAPI backend, converted to JPEG, and saved on the PC.

The PC-side camera pipeline was also tested using the laptop camera with OpenCV, and real camera frames were successfully captured, transferred, and saved.

The physical NAO V6 microphone and camera still need to be tested.

## Data Folders

Laptop microphone test recordings:

data/laptop_audio/

Physical NAO audio:

data/nao_audio/

Camera frames:

data/nao_frames/

These folders are ignored by Git and their recorded data is not uploaded to GitHub.

## Next

Test the audio and camera capture using the physical NAO V6.

## My Part

My responsibility is:

NAO microphone + NAO camera -> capture audio and face data -> send/save the data on the PC.

The Speech & Text Emotion module will process the spoken response.

The Computer Vision module will process the captured face frames and classify the facial expression.

The other team modules will combine and display the final emotion results.