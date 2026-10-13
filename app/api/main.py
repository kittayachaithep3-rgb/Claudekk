# 1. Import FastAPI
from fastapi import FastAPI, HTTPException
# 2. Import our Service Layer
from app.services import pet_service

# 3. Create FastAPI application
app = FastAPI(
    title="Happy Paws API",
    description="Pet Management API",
    version="1.0.0"
)

# 4. Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Happy Paws API"}

# 5. Get all pets
@app.get("/pets")
def get_all_pets():
    return pet_service.get_all_pets()

# 6. Get one pet by ID
@app.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    pet = pet_service.get_pet(pet_id)
    if pet is None:
        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )
    return pet