from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import employees, attendance, dashboard

app = FastAPI()

# CORS Middleware
origins = [
    "http://localhost:5173", # Vite default
    "http://localhost:3000",
    "*" # For development simplicity, restrict in prod
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, tags=["Employees"], prefix="/employees")
app.include_router(attendance.router, tags=["Attendance"], prefix="/attendance")
app.include_router(dashboard.router, tags=["Dashboard"], prefix="/dashboard")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to HRMS Lite API"}
