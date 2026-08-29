from extensions import db
from enum import Enum
from datetime import datetime
class ScenarioDifficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(35), nullable= False)
    email = db.Column(db.String(100), nullable= False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer,nullable=False)
    xp = db.Column(db.Integer, nullable=False)
    user = db.relationship("Attempt", back_populates='user_attempt')

    
class Scenario(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.Enum(ScenarioDifficulty), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)

    clues = db.Column(db.JSON, nullable=False)
    clues_options = db.Column(db.JSON, nullable=False)
    explanation = db.Column(db.String(1000), nullable=False)
    scenario = db.relationship('Attempt',back_populates='user_scenario')
    #Note: back_populates should point to the relationship name on the other column no to the  ForeignKey
    # back_populates on relationship 'User.user' refers to attribute 'Attempt.user_id' that is not a relationship.  The back_populates parameter should refer to the name of a relationship on the target class. 


class Attempt(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    answer =db.Column(db.String(150),nullable=False)
    correct = db.Column(db.Boolean, nullable=False )
    score = db.Column(db.Integer, nullable=False)
    xp_earned = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_attempt = db.relationship("User", back_populates='user')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_scenario = db.relationship("Scenario", back_populates='scenario' )
    scenario_id = db.Column(db.Integer,db.ForeignKey('scenario.id'), nullable=False)