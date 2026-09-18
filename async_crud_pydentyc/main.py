import fastapi, uvicorn, pydantic

app = fastapi.FastAPI()
tasks=[]

class Task(pydantic.BaseModel):
    title: str = pydantic.Field(min_length=1)

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.post("/tasks")
async def post_task(task_data: Task):
    index=len(tasks)+1
    title=task_data.title
    done=False
    tasks.append({"index":index,"title":title,"done":done})
    return {"message": "All OK"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id:int):
    for i in tasks:
        if i["index"]==task_id:
            tasks.remove(i)
    return {"message": "All OK"}

@app.patch("/tasks/{task_id}")
async def patch_task(task_id:int):
    for i in tasks:
        if i["index"]==task_id:
            i["done"]=True
    return {"message": "All OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)