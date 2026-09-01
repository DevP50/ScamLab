# ScamLab

### Learn to spot scams by experiencing them.

ScamLab is an interactive anti-scam training platform designed to help students and daily internet users recognize common online scams before they become victims.

Instead of simply reading about scam warning signs, users are placed inside realistic scenarios and asked to decide whether a message is **SCAM** or **LEGIT**.

---

## The Problem

Online scams are becoming increasingly convincing.

Students regularly encounter suspicious messages involving:

* Exam results
* Scholarships
* Job and internship opportunities
* Mobile money accounts
* University accounts
* Impersonation
* Fake prizes and giveaways

The problem isn't always a lack of awareness. Scammers are getting better at making fraudulent messages look legitimate.

ScamLab aims to turn scam awareness into a **practical skill**.

---

## The Solution

ScamLab uses a game-like training experience where users:

1. Receive a realistic message or scenario.
2. Examine the information provided.
3. Identify suspicious clues.
4. Decide whether the message is a scam or legitimate.
5. Receive immediate feedback.
6. Earn XP and score points.
7. Receive personalized training recommendations based on their performance.

The goal is simple:

> **Don't just learn what a scam looks like. Practice recognizing one.**

---

## 🧠 Adaptive Training

ScamLab tracks a user's performance across scenarios.

The system analyzes:

* Overall accuracy
* Correct and incorrect attempts
* Performance by category
* Performance by difficulty
* Total score
* XP earned

Based on this information, ScamLab identifies areas where the user may be struggling and recommends what they should practice next.

For example, if a user consistently performs poorly on **mobile money scams**, the system can prioritize that category and adjust the recommended difficulty.

This creates a training experience that becomes more personalized as the user practices.

---

## Game System

ScamLab uses a simple progression system to encourage continued practice.

### XP

Users earn XP for correctly identifying scenarios and recognizing relevant clues.

### Score

Scores consider:

* Correct answers
* Correct clues
* Incorrect clues
* Scenario difficulty

### Levels

Users begin at **Level 1** and unlock additional training after completing the initial scenarios.

---

## Scenario Categories

The current training set includes scenarios involving:

* 🎓 Academic communication
* 🎁 Prize scams
* 💳 Mobile money scams
* 🎣 Phishing
* 💼 Job and scholarship scams
* 👤 Impersonation
* 🔐 Account security alerts

Some scenarios are intentionally subtle so that users cannot simply rely on obvious scam signals.

---

## 🤖 AI Training Insights

ScamLab includes an AI recommendation layer that interprets the user's performance data and produces a training insight.

The AI works alongside the application's existing performance and recommendation logic rather than replacing the core game mechanics.

This allows ScamLab to combine:

**User performance → Performance analysis → Training recommendation → AI insight**

---

## Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-WTF

### Database

* SQL database
* SQLAlchemy ORM

### Frontend

* HTML
* CSS
* JavaScript
* Jinja templates

### AI

* AI recommendation engine integrated with the training system

### Deployment

* Render

---

## Project Structure

```text
ScamLab/
│
├── app/
│   ├── models/
│   ├── services/
│   │   ├── calculate_score.py
│   │   ├── calculate_xp.py
│   │   ├── get_performance.py
│   │   ├── recommend_training.py
│   │   ├── scenario_selector.py
│   │   └── ai_engine.py
│   │
│   └── routes/
│
├── templates/
├── static/
├── seed.py
├── scenario_count.py
├── extensions.py
└── requirements.txt
```

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/DevP50/ScamLab.git
cd ScamLab
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize/seed the scenarios:

```bash
python seed.py
```

Run the Flask application:

```bash
python run.py
```

Then open the local address shown by Flask in your browser.

---

## Demo

A live version of ScamLab is available here:

**https://scamlab.onrender.com/**

The project also includes a recorded demonstration showing the main user flow and adaptive training experience.

---

## Future Improvements

ScamLab is currently an MVP. Future versions could include:

* More realistic WhatsApp/email-style interfaces
* Larger scenario libraries
* More advanced adaptive difficulty
* Detailed progress dashboards
* Streaks and achievements
* Leaderboards
* More sophisticated AI-generated training plans
* Regional scam datasets
* Mobile support
* Teacher or administrator dashboards

---

## Why I Built This

ScamLab started from a simple observation: students are increasingly exposed to scams through channels they already use every day.

I wanted to build something that makes cybersecurity education more practical.

Rather than telling someone:

> "Be careful of suspicious messages."

ScamLab lets them **practice being careful**.

---

## Project Status

**MVP Completed**

ScamLab currently includes authentication, scenario-based training, clue identification, scoring, XP progression, performance analysis, adaptive scenario selection, and AI-generated training insights.

Built with love  for the hackathon.
