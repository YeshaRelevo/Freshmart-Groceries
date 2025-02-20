from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import employee

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(employee.router, prefix="/api/v1", tags=["employees"])

@app.get("/")
def read_root():
    return {"message": "Employee Management System API"}