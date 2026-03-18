from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import student_routes
from app.exceptions import StudentNotFoundException
from app.utils.response import error_response

# Creating FastAPI instance
#The title parameter is used to set the title of the API
app=FastAPI(title="FastAPI Student CRUD Project")

# Include routes
# The include_router method is used to include the routes from the student_routes module
app.include_router(student_routes.router)


# Global Exception Handler
@app.exception_handler(StudentNotFoundException)
async def not_found_exception_handler(request: Request, exc: StudentNotFoundException):
    return JSONResponse(
        status_code=404,
        content=error_response(message=exc.message, code=404)
    )



# Root endpoint
@app.get("/")
def home():
    return {"message": "FastAPI Studnet CRUD App Running"}

#uvicorn app.main:app --reload