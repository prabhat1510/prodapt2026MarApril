from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.logger import setup_logger
from app.routes.restra_routes import router as restraunt_router
from app.routes.user_routes import router as user_router
from app.routes.cuisine_routes import router as cuisine_router
from app.utils.exceptions import RestrauntNotFoundException, UserExistsException, InvalidCredentialsException, CustomerNotFoundException, CuisineNotFoundException
from fastapi.middleware.cors import CORSMiddleware

# Setup
setup_logger()

app = FastAPI(title=settings.app_name)

#allowed origins
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception Handlers
@app.exception_handler(RestrauntNotFoundException)
async def restraunt_not_found_exception_handler(request: Request, exc: RestrauntNotFoundException):
    return JSONResponse(status_code=404, content={"message": str(exc)})

@app.exception_handler(UserExistsException)
async def user_exists_exception_handler(request: Request, exc: UserExistsException):
    return JSONResponse(status_code=400, content={"message": str(exc)})

@app.exception_handler(InvalidCredentialsException)
async def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsException):
    return JSONResponse(status_code=401, content={"message": str(exc)})

@app.exception_handler(CustomerNotFoundException)
async def customer_not_found_exception_handler(request: Request, exc: CustomerNotFoundException):
    return JSONResponse(status_code=404, content={"message": str(exc)})

@app.exception_handler(CuisineNotFoundException)
async def cuisine_not_found_exception_handler(request: Request, exc: CuisineNotFoundException):
    return JSONResponse(status_code=404, content={"message": str(exc)})

# Include routes with prefixes
app.include_router(restraunt_router, prefix="/restraunt", tags=["Restraunt"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(cuisine_router, prefix="/cuisine", tags=["Cuisine"])

@app.get("/")
def root():
    return {"message": "FastAPI Restraunt CRUD App Running"}