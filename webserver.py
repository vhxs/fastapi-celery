from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from celery_config import execute_task

app = FastAPI(docs_url="/")

class Args(BaseModel):
    identifier: str

@app.post("/submit_job/")
async def submit_job(args: Args):
    results = []
    for i in range(10):
        results.append(execute_task.delay(f"{args.identifier}-{i}"))
    for i in range(10):
        results[i].wait()
    return {"response": args.identifier}

if __name__ == "__main__":
    uvicorn.run("webserver:app", host="0.0.0.0", port=8000, workers=5)