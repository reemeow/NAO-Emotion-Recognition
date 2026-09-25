from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from PIL import Image
from io import BytesIO
import os
from datetime import datetime


app = FastAPI(
    title="NAO Emotion Training Backend",
    version="1.0"
)


scenarios_db = [
    {
        "id": 1,
        "emotion": "happy",
        "question": "Look at me! Am I happy or sad?",
        "options": ["Happy", "Sad"],
        "correct": "Happy",
        "image_url": "/static/images/happy_scenario.jpg"
    },
    {
        "id": 2,
        "emotion": "sad",
        "question": "How do I look now? Do I look sad or angry?",
        "options": ["Sad", "Angry"],
        "correct": "Sad",
        "image_url": "/static/images/sad_scenario.jpg"
    }
]


class ChildResponse(BaseModel):
    scenario_id: int
    spoken_text: str


@app.get("/")
def read_root():
    return {"status": "online"}


@app.post("/api/session/start")
def start_session():
    return {
        "status": "success",
        "total_scenarios": len(scenarios_db)
    }


@app.get("/api/scenario/next")
def get_next_scenario(index: int = 0):
    if index < len(scenarios_db):
        return {
            "status": "success",
            "has_more": True,
            "scenario": scenarios_db[index]
        }

    return {
        "status": "success",
        "has_more": False,
        "message": "All scenarios completed."
    }


@app.post("/api/response/submit")
def submit_response(data: ChildResponse):
    return {
        "status": "success",
        "message": "Response received and logged successfully",
        "scenario_id": data.scenario_id,
        "received_text": data.spoken_text
    }


@app.post("/api/camera/frame")
async def upload_camera_frame(frame: UploadFile = File(...)):
    folder = "data/nao_frames"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    extension = os.path.splitext(frame.filename)[1].lower()

    if not extension:
        extension = ".jpg"

    filename = f"frame_{timestamp}{extension}"
    file_path = os.path.join(folder, filename)

    contents = await frame.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "status": "success",
        "message": "Camera frame saved successfully",
        "file_path": file_path
    }


@app.post("/api/camera/raw-frame")
async def upload_raw_camera_frame(
    width: int = Form(...),
    height: int = Form(...),
    frame: UploadFile = File(...)
):
    folder = "data/nao_frames"
    os.makedirs(folder, exist_ok=True)

    raw_data = await frame.read()

    expected_size = width * height * 3

    if len(raw_data) != expected_size:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid RGB frame size. Expected {expected_size} bytes, received {len(raw_data)}."
        )

    image = Image.frombytes(
        "RGB",
        (width, height),
        raw_data
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"nao_frame_{timestamp}.jpg"
    file_path = os.path.join(folder, filename)

    image.save(
        file_path,
        format="JPEG",
        quality=90
    )

    return {
        "status": "success",
        "message": "NAO camera frame received and saved successfully",
        "width": width,
        "height": height,
        "file_path": file_path
    }