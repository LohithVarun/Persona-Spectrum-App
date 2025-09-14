# app/ml_analysis.py
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from typing import List, Dict, Any
import numpy as np
import random

# Define your personality dimensions
PERSONALITY_DIMENSIONS = [
    "Power", "Visionary", "Resourcefulness", "Communication", "Extraversion",
    "Sociability", "Empathy", "Self-Control", "Conscientiousness", "Rationality", "Assurance",
    "Resilience" # <<< ADDED 'Resilience' HERE
]

# --- QUESTION-SPECIFIC INDICATORS for each Personality Dimension ---
# (The rest of this dictionary should be the same as my last provided ml_analysis.py code block)
QUESTION_SPECIFIC_INDICATORS = {
    1: { # Question 1: Underperforming team member
        "Power": ["take decisive action", "set strict deadlines", "assert authority", "demand improvement", "fire them"],
        "Communication": ["have a direct conversation", "discuss privately", "offer clear feedback", "listen to their side", "mediate"],
        "Empathy": ["understand their challenges", "offer support", "consider personal issues", "be compassionate", "show concern"],
        "Rationality": ["analyze performance data", "focus on objective metrics", "evaluate impact on project", "logical steps"],
        "Self-Control": ["remain calm and professional", "avoid emotional reactions", "maintain composure", "disciplined response"],
        "Conscientiousness": ["document instances", "follow protocol", "ensure fairness", "systematic approach"],
        "Assurance": ["confidently address the issue", "stand firm on expectations", "be resolute", "trust my judgment"]
    },
    2: { # Question 2: Learning a complex new skill
        "Visionary": ["look for future applications", "see long-term benefits", "imagine new possibilities", "innovative uses"],
        "Resourcefulness": ["find unconventional resources", "experiment with solutions", "use existing tools creatively", "learn by doing", "adapt existing knowledge"],
        "Conscientiousness": ["create a structured plan", "break down into steps", "practice consistently", "follow a curriculum", "methodical learning"],
        "Rationality": ["research best practices", "analyze learning methods", "seek logical explanations", "understand theory"],
        "Self-Control": ["dedicate focused time", "stick to a schedule", "manage distractions", "disciplined study"],
        "Assurance": ["confidently tackle the challenge", "trust my ability to learn", "believe in success", "embrace the unknown"]
    },
    3: { # Question 3: Colleague taking shortcuts
        "Conscientiousness": ["report to management", "prioritize integrity", "ensure fair play", "address dishonest behavior", "uphold standards", "document the shortcuts", "follow company policy", "ensure quality standards"],
        "Rationality": ["evaluate risks objectively", "focus on long-term damage", "logical assessment", "analyze impact"],
        "Communication": ["confront them directly", "discuss consequences", "explain the impact", "open dialogue"],
        "Empathy": ["understand their motives", "consider their pressure", "show understanding"],
        "Power": ["take control of the situation", "demand they stop", "enforce standards", "impose consequences"],
        "Self-Control": ["handle conflict professionally", "remain objective"],
        "Assurance": ["be firm about principles", "stand by convictions"]
    },
    4: { # Question 4: Transformative opportunity with risk
        "Visionary": ["focus on long-term goals", "see the bigger picture", "imagine future success", "innovative mindset"],
        "Resourcefulness": ["identify new learning paths", "seek mentors", "find support systems", "leverage networks"],
        "Rationality": ["weigh pros and cons", "analyze potential outcomes", "research thoroughly", "make data-driven choice"],
        "Assurance": ["trust my capabilities", "confidently pursue it", "believe in my adaptability", "strong self-belief"],
        "Power": ["take decisive control", "drive the initiative", "command the new role"],
        "Resilience": ["adapt to new challenges", "handle initial setbacks"] # Re-added for Question 4 context
    },
    5: { # Question 5: Project cancellation
        "Resilience": ["bounce back quickly", "find new motivation", "learn from failure", "adapt and move on", "positive outlook", "process disappointment constructively", "overcome setbacks"], # Updated resilience indicators
        "Self-Control": ["manage emotions", "process disappointment calmly", "avoid dwelling on it", "stay composed"],
        "Rationality": ["analyze what went wrong", "identify lessons learned", "focus on facts", "objective review"],
        "Conscientiousness": ["reflect on effort", "document experience for future reference", "diligent post-mortem"],
        "Empathy": ["connect with colleagues", "support team members", "share feelings"],
        "Assurance": ["maintain self-worth", "confidently accept areas for growth", "trust in my value"]
    },
    6: { # Question 6: Innovation under constraints
        "Visionary": ["imagine breakthrough ideas", "envisions new possibilities", "future-oriented solutions"],
        "Resourcefulness": ["think outside the box", "find novel solutions", "creative brainstorming", "unconventional approaches", "break boundaries", "leverage limited resources", "use existing tools differently", "find workarounds", "invent solutions"], # Expanded resourcefulness for 'innovation'
        "Rationality": ["analyze constraints systematically", "break down the problem logically", "structured approach"],
        "Conscientiousness": ["focus on iterative development", "deliver practical solutions", "meticulous execution"]
    },
    7: { # Question 7: Overload of urgent tasks
        "Conscientiousness": ["triage tasks", "identify critical items", "rank by importance/urgency", "categorize workload", "plan effectively", "organize workflow", "manage time efficiently", "prioritize"],
        "Self-Control": ["stay calm under pressure", "avoid panic", "maintain focus", "disciplined management"],
        "Communication": ["communicate expectations", "negotiate deadlines", "delegate tasks", "transparent updates"],
        "Rationality": ["evaluate true impact", "allocate resources logically", "systematic decision-making"]
    },
    8: { # Question 8: Disagreement on project strategy
        "Communication": ["persuade with data", "present logical arguments", "listen actively", "seek common ground", "facilitate discussion"],
        "Power": ["assert my viewpoint", "drive the decision", "take charge of discussion", "build consensus", "sway opinions", "lead without authority", "advocate effectively", "mobilize support"],
        "Rationality": ["focus on objective facts", "analyze strategy merits", "use evidence", "logical reasoning"],
        "Empathy": ["understand their perspective", "acknowledge concerns", "validate feelings"],
        "Assurance": ["confidently present my case", "stand firm in my beliefs"]
    },
    9: { # Question 9: Organizational restructuring
        "Resourcefulness": ["embrace change", "flexibility", "adjust quickly", "thrive in uncertainty", "open to new roles", "find opportunities"],
        "Self-Control": ["remain calm", "manage anxiety", "stay composed", "emotional regulation"],
        "Rationality": ["seek clarity logically", "understand implications", "objective assessment"],
        "Communication": ["stay informed", "ask questions", "discuss with peers", "seek updates"],
        "Assurance": ["maintain confidence", "trust in new path", "see opportunities", "self-assured during transition"]
    },
    10: { # Question 10: Receiving critical feedback
        "Self-Control": ["listen without interrupting", "remain composed", "manage defensiveness", "controlled reaction"],
        "Rationality": ["analyze feedback objectively", "seek clarification", "identify root causes", "logical review"],
        "Conscientiousness": ["create action plan", "seek improvement", "implement changes", "diligent follow-up"],
        "Empathy": ["understand the critic's perspective", "consider their viewpoint"],
        "Assurance": ["maintain self-worth", "confidently accept areas for growth", "strong self-image"],
        "Communication": ["ask follow-up questions", "engage in dialogue about feedback", "open discussion"]
    }
}

# Base score to ensure everyone has a starting point (neutral or slightly above)
BASE_SCORE = 50.0
# The maximum contribution a single question can make to a dimension score
MAX_QUESTION_CONTRIBUTION = 20.0 # From BASE_SCORE, so a max pushes to 70, min pulls to 30

class PersonalityAnalyzer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PersonalityAnalyzer, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        print("Loading DistilBERT tokenizer and model for embeddings...")
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = AutoModel.from_pretrained("distilbert-base-uncased")
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval() # Set model to evaluation mode
        print(f"DistilBERT model loaded on {self.device} for embeddings!")

        # --- Pre-compute embeddings for all question-specific indicators ---
        self.indicator_embeddings = {} # Stores {question_num: {dim_name: Tensor (normalized embedding)}}
        print("Generating embeddings for question-specific indicators...")
        with torch.no_grad():
            for q_num, dim_indicators in QUESTION_SPECIFIC_INDICATORS.items():
                self.indicator_embeddings[q_num] = {}
                for dim_name, phrases in dim_indicators.items():
                    if not phrases:
                        continue
                    
                    phrase_embeddings = []
                    for phrase in phrases:
                        inputs = self.tokenizer(phrase, return_tensors="pt", truncation=True, padding=True, max_length=512)
                        inputs = {k: v.to(self.device) for k, v in inputs.items()}
                        outputs = self.model(**inputs)
                        embedding = outputs.last_hidden_state[:, 0, :].cpu() # [CLS] token embedding
                        phrase_embeddings.append(embedding)
                    
                    # Concatenate and normalize all phrase embeddings for this dimension in this question
                    # Then average them to get a single representative embedding for this indicator group
                    combined_embedding = torch.cat(phrase_embeddings, dim=0).mean(dim=0, keepdim=True)
                    self.indicator_embeddings[q_num][dim_name] = combined_embedding / combined_embedding.norm(p=2, dim=-1, keepdim=True)
        print("Question-specific indicator embeddings generated and normalized.")

    async def analyze_responses(self, answers: List[str]) -> Dict[str, float]:
        """
        Analyzes a list of text responses and returns personality scores based on semantic similarity
        to question-specific indicators.
        """
        if not answers:
            return {dim: BASE_SCORE for dim in PERSONALITY_DIMENSIONS} # Return base scores if no answers

        # Initialize raw accumulated scores for each dimension to 0
        raw_accumulated_scores = {dim: 0.0 for dim in PERSONALITY_DIMENSIONS}
        # Keep track of how many relevant questions contributed to each dimension
        question_contributions_count = {dim: 0 for dim in PERSONALITY_DIMENSIONS}

        print(f"Analyzing {len(answers)} user responses against indicators...")
        
        with torch.no_grad():
            for i, answer_text in enumerate(answers):
                q_num = i + 1 # Assuming answers list corresponds to question_numbers 1-10

                # Ensure we only process questions that have defined indicators
                if q_num not in QUESTION_SPECIFIC_INDICATORS:
                    print(f"Warning: No indicators defined for Question {q_num}. Skipping.")
                    continue

                if not answer_text.strip():
                    print(f"Warning: Empty answer for Question {q_num}. Skipping.")
                    continue

                # Generate embedding for the user's answer
                inputs = self.tokenizer(answer_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                outputs = self.model(**inputs)
                user_answer_embedding = outputs.last_hidden_state[:, 0, :].cpu()
                user_answer_embedding = user_answer_embedding / user_answer_embedding.norm(p=2, dim=-1, keepdim=True) # Normalize

                # Compare user's answer to relevant indicator embeddings for this question
                for dim_name, indicator_embedding_for_q in self.indicator_embeddings[q_num].items():
                    # This is the line that caused the KeyError previously
                    # Ensure dim_name is always in PERSONALITY_DIMENSIONS
                    if dim_name not in PERSONALITY_DIMENSIONS:
                        print(f"Error: Dimension '{dim_name}' found in QUESTION_SPECIFIC_INDICATORS for Q{q_num} but not in PERSONALITY_DIMENSIONS. Skipping contribution.")
                        continue # Skip this dimension's contribution to prevent KeyError
                    
                    similarity = F.cosine_similarity(user_answer_embedding, indicator_embedding_for_q).item()
                    
                    # Add contribution to the raw sum for this dimension
                    raw_accumulated_scores[dim_name] += similarity
                    question_contributions_count[dim_name] += 1 # This question contributed to this dimension

        # Final score calculation: Average accumulated similarities and scale to 1-99 range
        final_scores = {}
        for dim in PERSONALITY_DIMENSIONS:
            if question_contributions_count[dim] > 0:
                # Average the similarities for this dimension across all relevant questions
                avg_similarity = raw_accumulated_scores[dim] / question_contributions_count[dim]
                
                # Scale average similarity (typically -1 to 1) to a 1-99 range
                # (similarity + 1) * 49 + 1  -> maps -1 to 1, 0 to 50, 1 to 99
                scaled_score = (avg_similarity + 1) * 49 + 1
            else:
                # If a dimension received no contributions from any question, default to BASE_SCORE
                scaled_score = BASE_SCORE
            
            final_score = round(float(min(max(scaled_score, 1), 99)), 2) # Ensure within 1-99
            final_scores[dim] = final_score
            
        print("Analysis complete. Returning scores based on question-specific semantic similarity.")
        return final_scores

# Instantiate the analyzer as a singleton for easy access
analyzer = PersonalityAnalyzer()