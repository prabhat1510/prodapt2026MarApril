from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logger
#from app.db.database import Base, engine
from app.routes.restra_routes import router as restraunt_router

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# Create DB tables
#Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(restraunt_router)

@app.get("/")
def root():
    return {"message": "FastAPI Restraunt CRUD App Running"}