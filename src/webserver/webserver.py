from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from src.config.config import celery_app

app = FastAPI(docs_url="/")

class Args(BaseModel):
    identifier: str

@app.post("/submit_job/")
async def submit_job(args: Args):
    results = []
    for i in range(10):
        results.append(celery_app.send_task("src.tasks.tasks.execute_task", args=(f"{args.identifier}-{i}",)))
    for i in range(10):
        results[i].wait()
    return {"response": args.identifier}

if __name__ == "__main__":
    uvicorn.run("webserver:app", host="0.0.0.0", port=8000, workers=5)