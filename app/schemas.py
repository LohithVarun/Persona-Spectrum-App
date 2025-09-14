# app/schemas.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    responses = relationship("UserResponse", back_populates="user")
    results = relationship("PersonalityResult", back_populates="user")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_number = Column(Integer, unique=True, index=True, nullable=False)
    text = Column(Text, nullable=False)
    category = Column(String)
    
    # Store the list of Likert options as a JSON object
    options_data = Column(JSON, nullable=False)

class UserResponse(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    selected_value = Column(Integer, nullable=False)
    
    # Use a proper DateTime column
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="responses")
    question = relationship("Question")

class PersonalityResult(Base):
    __tablename__ = "personality_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String)
    summary_statement = Column(Text)
    
    # Use a proper DateTime column
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Store the dictionary of scores directly as JSON
    scores = Column(JSON, nullable=False)

    user = relationship("User", back_populates="results")
