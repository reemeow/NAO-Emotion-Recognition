from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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