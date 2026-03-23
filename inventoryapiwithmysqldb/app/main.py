from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.database import Base, engine
from app.api.routes.item_routes import router as item_router

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(item_router)

@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}

@app.exception_handler(ItemNotFoundException)
def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(InvalidStockException)
def invalid_stock_exception_handler(request: Request, exc: InvalidStockException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )