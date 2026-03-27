from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.database import Base, engine
from app.api.routes.customer_routes import router as customer_router
from app.utils.exceptions import CustomerNotFoundException
from fastapi.responses import JSONResponse
from fastapi import Request

from fastapi.middleware.cors import CORSMiddleware

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(customer_router)

@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}

@app.exception_handler(CustomerNotFoundException)
def customer_not_found_exception_handler(request: Request, exc: CustomerNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
