# ---------------------------------------------
# FastAPI Layered Architecture Main Entry
# ---------------------------------------------
from fastapi import FastAPI
from routes import router as item_router

app = FastAPI(title="Inventory API - Layered")

# Include the item endpoints from routes.py
app.include_router(item_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Layered Inventory API"}

# ---------------------------------------------
# Run Program
# ---------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
