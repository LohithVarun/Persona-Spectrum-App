# app/crud.py
from sqlalchemy.orm import Session
from typing import List, Dict

from . import models, schemas, auth

# --- User CRUD ---
def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(schemas.User).filter(schemas.User.username == username).first()

def create_user(db: Session, user: models.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = schemas.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Question CRUD ---
def create_question(db: Session, question: models.QuestionCreate):
    db_question = schemas.Question(
        question_number=question.question_number,
        text=question.text,
        category=question.category,
        options_data=[opt.model_dump() for opt in question.options_data]
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.Question).order_by(schemas.Question.question_number).offset(skip).limit(limit).all()

# --- Recommendation Logic ---
def generate_development_plan(scores: Dict[str, float]) -> List[Dict]:
    recommendations = []
    recommendation_map = {
        "Introvert_Extrovert": {
            "low_score_trait": "Introvert",
            "low_score_advice": "To develop extroverted skills, practice initiating small conversations. Try joining a club or group activity like Toastmasters to build confidence in social settings.",
            "low_score_apps": "App suggestion: Meetup - for finding local groups and events.",
            "high_score_trait": "Extrovert",
            "high_score_advice": "To balance your energy, practice active listening without interrupting. Schedule quiet time for reflection to recharge and process your thoughts.",
            "high_score_apps": "App suggestion: Headspace or Calm - for practicing mindfulness and reflection."
        },
        "Sensing_Intuition": {
            "low_score_trait": "Sensing",
            "low_score_advice": "To foster your intuition, try brainstorming without judgment or exploring abstract art. Engage in strategic games that require forward-thinking.",
            "low_score_apps": "App suggestion: Brilliant.org - for tackling problems with logic and creativity.",
            "high_score_trait": "Intuition",
            "high_score_advice": "To ground your ideas in reality, create detailed project plans with concrete steps. Practice mindfulness to focus on the present moment and sensory details.",
            "high_score_apps": "App suggestion: Trello or Asana - for organizing ideas into actionable plans."
        },
        "Thinking_Feeling": {
            "low_score_trait": "Thinking",
            "low_score_advice": "To develop your emotional awareness, practice asking others how they feel about a decision. Try to express appreciation and give positive feedback more often.",
            "low_score_apps": "App suggestion: Gratitude Journal - to practice focusing on positive emotions.",
            "high_score_trait": "Feeling",
            "high_score_advice": "To strengthen your analytical skills, practice making pro-and-con lists for important decisions. Try to identify the logical principles behind your value-driven choices.",
            "high_score_apps": "App suggestion: Elevate or Lumosity - for brain training and logical reasoning."
        },
        "Judging_Perceiving": {
            "low_score_trait": "Judging",
            "low_score_advice": "To become more flexible, intentionally leave some parts of your day unscheduled. Practice saying 'yes' to spontaneous opportunities, even small ones.",
            "low_score_apps": "App suggestion: Any.do or Todoist - to manage tasks but allow for flexible rescheduling.",
            "high_score_trait": "Perceiving",
            "high_score_advice": "To improve your organization, break down large projects into smaller, manageable tasks. Set deadlines for yourself to create structure and ensure completion.",
            "high_score_apps": "App suggestion: Notion - for creating structured plans and tracking progress."
        }
    }
    threshold = 30.0
    for dimension, score in scores.items():
        if dimension in recommendation_map:
            plan = recommendation_map[dimension]
            if score <= -threshold:
                recommendations.append({
                    "dimension": dimension, "trait": plan["low_score_trait"],
                    "advice": plan["low_score_advice"], "app_suggestion": plan.get("low_score_apps")
                })
            elif score >= threshold:
                recommendations.append({
                    "dimension": dimension, "trait": plan["high_score_trait"],
                    "advice": plan["high_score_advice"], "app_suggestion": plan.get("high_score_apps")
                })
    return recommendations

# --- Answer and Result CRUD ---
def calculate_and_save_personality_result(db: Session, user_id: int, answers: List[models.Answer], assessment_name: str):
    dimension_weights = {
        1: {"Introvert_Extrovert": -1.0}, 2: {"Introvert_Extrovert": 1.0}, 3: {"Introvert_Extrovert": -1.0}, 4: {"Introvert_Extrovert": 1.0}, 5: {"Introvert_Extrovert": 1.0}, 6: {"Introvert_Extrovert": -1.0}, 7: {"Introvert_Extrovert": 1.0},
        8: {"Sensing_Intuition": 1.0}, 9: {"Sensing_Intuition": -1.0}, 10: {"Sensing_Intuition": 1.0}, 11: {"Sensing_Intuition": -1.0}, 12: {"Sensing_Intuition": 1.0}, 13: {"Sensing_Intuition": -1.0}, 14: {"Sensing_Intuition": 1.0},
        15: {"Thinking_Feeling": -1.0}, 16: {"Thinking_Feeling": 1.0}, 17: {"Thinking_Feeling": -1.0}, 18: {"Thinking_Feeling": 1.0}, 19: {"Thinking_Feeling": -1.0}, 20: {"Thinking_Feeling": 1.0}, 21: {"Thinking_Feeling": -1.0},
        22: {"Judging_Perceiving": 1.0}, 23: {"Judging_Perceiving": -1.0}, 24: {"Judging_Perceiving": 1.0}, 25: {"Judging_Perceiving": -1.0}, 26: {"Judging_Perceiving": 1.0}, 27: {"Judging_Perceiving": -1.0}, 28: {"Judging_Perceiving": 1.0}, 29: {"Judging_Perceiving": -1.0}, 30: {"Judging_Perceiving": 1.0},
    }
    scores = { "Introvert_Extrovert": 0.0, "Sensing_Intuition": 0.0, "Thinking_Feeling": 0.0, "Judging_Perceiving": 0.0 }
    norm_factors = {dim: 0.0 for dim in scores}
    for answer in answers:
        if answer.question_id in dimension_weights:
            weights = dimension_weights[answer.question_id]
            for dimension, weight in weights.items():
                centered_score = (answer.selected_value - 3) * 2
                scores[dimension] += centered_score * weight
                norm_factors[dimension] += 1
    for dimension in scores:
        if norm_factors[dimension] > 0:
            max_possible_score = 4 * norm_factors[dimension]
            scores[dimension] = (scores[dimension] / max_possible_score) * 100 if max_possible_score != 0 else 0
    development_plan = generate_development_plan(scores)
    dominant_traits = [rec['trait'] for rec in development_plan]
    summary = f"Your results show strong tendencies as a {', '.join(dominant_traits)}. Here are some areas for potential growth." if dominant_traits else "Your results indicate a well-balanced personality profile."
    db_result = schemas.PersonalityResult(user_id=user_id, name=assessment_name, scores=scores, summary_statement=summary)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    result_with_recs = {
        "id": db_result.id, "user_id": db_result.user_id, "timestamp": db_result.timestamp,
        "name": db_result.name, "summary_statement": db_result.summary_statement,
        "scores": db_result.scores, "recommendations": development_plan
    }
    return result_with_recs

# --- Database Population ---
def populate_initial_questions(db: Session):
    if db.query(schemas.Question).first() is not None:
        return
    print("Populating initial questions...")
    likert_options = [
        models.Option(value=1, text="Strongly Disagree"), models.Option(value=2, text="Disagree"),
        models.Option(value=3, text="Neutral"), models.Option(value=4, text="Agree"), models.Option(value=5, text="Strongly Agree")
    ]
    questions_to_add = [
        # --- Energy (Introvert vs. Extrovert) ---
        models.QuestionCreate(question_number=1, text="You find it draining to be in large social gatherings for extended periods.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=2, text="You often take the initiative to start conversations with new people.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=3, text="You prefer a quiet evening with a book or a movie over a large, loud party.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=4, text="You feel energized and excited after spending time with a large group of friends.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=5, text="You are often described as talkative and outgoing.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=6, text="You tend to think things through carefully before you speak.", category="Energy", options_data=likert_options),
        models.QuestionCreate(question_number=7, text="Being the center of attention is something you enjoy.", category="Energy", options_data=likert_options),

        # --- Information (Sensing vs. Intuition) ---
        models.QuestionCreate(question_number=8, text="You are more interested in abstract ideas and future possibilities than concrete, immediate realities.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=9, text="You trust practical experience and proven facts more than theories and concepts.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=10, text="You often find yourself lost in thought, exploring hypothetical scenarios.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=11, text="You prefer to focus on the details and specifics of a situation rather than the big picture.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=12, text="You enjoy discussing symbolic or metaphorical meanings in art and literature.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=13, text="You would rather work with tangible things you can see and touch.", category="Information", options_data=likert_options),
        models.QuestionCreate(question_number=14, text="You rely on your gut feelings and hunches to make connections.", category="Information", options_data=likert_options),

        # --- Decisions (Thinking vs. Feeling) ---
        models.QuestionCreate(question_number=15, text="When making decisions, you prioritize logic, objectivity, and impartial principles.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=16, text="You consider how your decisions will affect others' feelings and well-being.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=17, text="You believe being truthful and direct is more important than being diplomatic to protect someone's feelings.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=18, text="You often make decisions based on your personal values and what feels right to you.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=19, text="You can stay emotionally detached and objective in tense situations.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=20, text="You are more motivated by appreciation and harmony than by achieving a goal.", category="Decisions", options_data=likert_options),
        models.QuestionCreate(question_number=21, text="You find it easy to identify flaws in an argument or plan.", category="Decisions", options_data=likert_options),

        # --- Lifestyle (Judging vs. Perceiving) ---
        models.QuestionCreate(question_number=22, text="You prefer to have a flexible, adaptable approach to life rather than a structured, organized plan.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=23, text="You feel a sense of satisfaction from completing tasks on a to-do list.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=24, text="You like to keep your options open and enjoy spontaneity.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=25, text="You prefer to have matters decided and settled, and dislike uncertainty.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=26, text="Your workspace tends to be cluttered and disorganized, but you know where everything is.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=27, text="You work best when you have a clear set of rules and deadlines.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=28, text="You enjoy starting new projects more than finishing existing ones.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=29, text="You see deadlines as important goals to be met on time.", category="Lifestyle", options_data=likert_options),
        models.QuestionCreate(question_number=30, text="You are comfortable changing plans at the last minute.", category="Lifestyle", options_data=likert_options),
    ]
    for q in questions_to_add:
        create_question(db, q)
    print(f"Initial population complete. {len(questions_to_add)} questions have been added.")

def get_latest_personality_result(db: Session, user_id: int):
    result = db.query(schemas.PersonalityResult).filter(schemas.PersonalityResult.user_id == user_id).order_by(schemas.PersonalityResult.timestamp.desc()).first()
    if result:
        recommendations = generate_development_plan(result.scores)
        return {
            "id": result.id, "user_id": result.user_id, "timestamp": result.timestamp,
            "name": result.name, "summary_statement": result.summary_statement,
            "scores": result.scores, "recommendations": recommendations
        }
    return None

def get_user_assessment_history(db: Session, user_id: int):
    results = db.query(schemas.PersonalityResult).filter(schemas.PersonalityResult.user_id == user_id).order_by(schemas.PersonalityResult.timestamp.desc()).all()
    history_with_recs = []
    for result in results:
        recommendations = generate_development_plan(result.scores)
        history_with_recs.append({
            "id": result.id, "user_id": result.user_id, "timestamp": result.timestamp,
            "name": result.name, "summary_statement": result.summary_statement,
            "scores": result.scores, "recommendations": recommendations
        })
    return history_with_recs
