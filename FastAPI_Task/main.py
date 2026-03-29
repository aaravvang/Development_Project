from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Supabase setup
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Request body model
class Task(BaseModel):
    title: str
    description: str
    status: str


# -------------------------
# READ ALL TASKS
# -------------------------
@app.get("/tasks")
def get_tasks():
    response = supabase.table("Tasks").select("*").execute()
    return response.data


# -------------------------
# READ SINGLE TASK
# -------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    response = supabase.table("Tasks").select("*").eq("task_id", task_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Task not found")

    return response.data[0]


# -------------------------
# CREATE TASK
# -------------------------
@app.post("/tasks")
def create_task(task: Task):
    response = supabase.table("Tasks").insert(task.dict()).execute()
    return response.data


# -------------------------
# UPDATE TASK
# -------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    response = supabase.table("Tasks").update(task.dict()).eq("task_id", task_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Task not found")

    return response.data


# -------------------------
# DELETE TASK
# -------------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    response = supabase.table("Tasks").delete().eq("task_id", task_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
