from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/data/")
async def api_data(request: Request):
    params = dict(request.query_params) # Convert immutable QueryParams to a standard dictionary
    return {"query_params": params}