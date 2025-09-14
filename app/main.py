# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from contextlib import asynccontextmanager

from . import crud, models, schemas, auth, database, dependencies

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting up...")
    schemas.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()
    try:
        crud.populate_initial_questions(db)
    finally:
        db.close()
    print("Startup complete.")
    yield
    print("Application shutting down...")

my_app = FastAPI(lifespan=lifespan)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@my_app.get("/")
def read_root():
    return {"message": "Welcome to the Persona Spectrum API!"}

# --- Authentication Endpoints (No Changes) ---
@my_app.post("/api/auth/register", response_model=models.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: models.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    return crud.create_user(db=db, user=user)

@my_app.post("/api/auth/token", response_model=models.Token)
async def login_for_access_token(login_request: models.LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=login_request.username)
    if not user:
        user = crud.get_user_by_username(db, username=login_request.username)

    if not user or not auth.verify_password(login_request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- User Endpoint (No Changes) ---
@my_app.get("/api/users/me", response_model=models.UserResponse)
async def read_users_me(current_user: schemas.User = Depends(dependencies.get_current_user)):
    return current_user

# --- Assessment Endpoints (UPDATED) ---
@my_app.get("/api/questions", response_model=List[models.Question])
async def get_all_questions(current_user: schemas.User = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
    return crud.get_questions(db)

@my_app.post("/api/submit-assessment", response_model=models.PersonalityResult)
async def submit_assessment(
    request: models.SubmitAnswersRequest,
    current_user: schemas.User = Depends(dependencies.get_current_user),
    db: Session = Depends(get_db)
):
    result = crud.calculate_and_save_personality_result(
        db=db, user_id=current_user.id, answers=request.answers, assessment_name=request.assessment_name
    )
    if not result:
        raise HTTPException(status_code=500, detail="Could not process assessment results.")
    return result

@my_app.get("/api/results/latest", response_model=models.PersonalityResult)
async def get_latest_result(current_user: schemas.User = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
    result = crud.get_latest_personality_result(db, user_id=current_user.id)
    if not result:
        raise HTTPException(status_code=404, detail="No personality results found for this user.")
    return result

@my_app.get("/api/results/history", response_model=List[models.PersonalityResult])
async def get_assessment_history(current_user: schemas.User = Depends(dependencies.get_current_user), db: Session = Depends(get_db)):
    return crud.get_user_assessment_history(db, user_id=current_user.id)

