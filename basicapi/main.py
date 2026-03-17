from fastapi import FastAPI
app=FastAPI(
title="my api",
    description="this is my first api",
    version="0.0.1"
)
#routes or end point
#http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}
    
#http://127.0.0.1:8000/about
@app.get("/about")
async def about():
    return {"message": "about page"}
