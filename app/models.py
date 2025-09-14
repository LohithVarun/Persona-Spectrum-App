# app/models.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List, Dict
from datetime import datetime

# --- User Authentication Models ---
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- Question and Answer Models ---
class Option(BaseModel):
    value: int
    text: str

class Question(BaseModel):
    id: int
    question_number: int
    text: str
    category: Optional[str] = None
    options_data: List[Option]
    model_config = ConfigDict(from_attributes=True)

class QuestionBase(BaseModel):
    question_number: int
    text: str
    category: Optional[str] = None

class QuestionCreate(QuestionBase):
    options_data: List[Option]


class Answer(BaseModel):
    question_id: int
    selected_value: int

class SubmitAnswersRequest(BaseModel):
    answers: List[Answer]
    assessment_name: Optional[str] = "Initial Assessment"

class Recommendation(BaseModel):
    dimension: str
    trait: str
    advice: str
    app_suggestion: Optional[str] = None
    app_link: Optional[str] = None

# --- Personality Result Models ---
class PersonalityResult(BaseModel):
    id: int
    user_id: int
    timestamp: datetime
    name: Optional[str] = None
    summary_statement: Optional[str] = None
    scores: Dict[str, float]
    recommendations: List[Recommendation] # <<< ADD THIS LINE
    model_config = ConfigDict(from_attributes=True)