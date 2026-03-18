from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import employee_routes
from app.exceptions import EmployeeNotFoundException
from app.utils.response import error_response

app = FastAPI(title="FastAPI CRUD Project")

# Include routes
app.include_router(employee_routes.router)

# Global Exception Handler
@app.exception_handler(EmployeeNotFoundException)
async def not_found_exception_handler(request: Request, exc: EmployeeNotFoundException):
    return JSONResponse(
        status_code=404,
        content=error_response(message=exc.message, code=404)
    )

# Root endpoint
@app.get("/")
def home():
    return {"message": "FastAPI CRUD App Running"}
