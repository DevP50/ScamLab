from app.models import Scenario,ScenarioDifficulty
from extensions import db
from app import create_app
app = create_app()
scenarios =[ {
    "title": "GCE 2026 UPDATES AND RESULTS",
    "content": "Congratulations! Your results are available early. Pay a small verification fee to receive them now.",
    "correct_answer": "scam",
    "clues":  [
           "Urgency",
           "Suspicious link",
            "Payment request"  ],
    "clue_options": [
       "Urgency",
    "Suspicious link",
    "Payment request",
    "Official announcement",
    "Normal school communication",
    "Clear identification"
    ],
    "difficulty": ScenarioDifficulty.EASY,
    "category": "phishing",
    "explanation": "Why was this a scam? 🚩The message tried to pressure you with the promise of early access to GCE results, creating urgency and excitement. It also requested a 5,000 FCFA payment for information that should be accessed through official channels. These are strong warning signs. Always verify exam-related information directly through official sources instead of trusting unsolicited messages."
    },
    {
     "title": "Your Student Account Is Expiring",
     "content": "IMPORTANT: Your student account will be permanently suspended in 30 minutes. Confirm your password immediately using the verification link below to avoid losing access.",
     "correct_answer": "scam",
     "clues": [
      "Urgency",
      "Threat of consequences",
      "Password request",
      "Suspicious link"
     ],

     "clue_options": [
    "Urgency",
    "Threat of consequences",
    "Password request",
    "Suspicious link",
    "Normal account notification",
    "Official app verification"
    ],
     "difficulty": ScenarioDifficulty.EASY,
     "category": "phishing",
     "explanation": "The message uses extreme urgency and threatens account suspension to pressure you into giving away your password. Legitimate organizations generally provide safer ways to verify account issues."
    },
     {
        "title": "Computer Science Department Reminder",
        "content": "Reminder: The Computer Science Department will hold its scheduled student meeting tomorrow at 10:00 AM in Room 204. Please check the student portal for the agenda.",
        "correct_answer": "legit",
        "clues": [
            "Normal school communication",
            "No payment request",
            "Uses an existing student portal"
        ],
        "clue_options": [
          "Urgency",
          "Threat of consequences",
          "Password request",
          "Suspicious link",
          "Normal account notification",
          "Official app verification"
          ],
        "difficulty": ScenarioDifficulty.EASY,
        "category": "legitimate",
        "explanation": "This is a normal informational message. It does not request money, passwords, or sensitive information and directs students to an existing official portal."
    },

    {
        "title": "Win a Free Smartphone!",
        "content": "🎉 CONGRATULATIONS! You have been randomly selected to receive a brand-new smartphone. Claim your prize within 10 minutes by paying a 2,000 FCFA delivery fee and submitting your phone number.",
        "correct_answer": "scam",
        "clues": [
            "Unexpected prize",
            "Urgency",
            "Payment request"
        ],
        "clue_options": [
          "Unexpected prize",
          "Urgency",
          "Payment request",
          "Official contest registration",
          "Clear prize eligibility",
          "Normal notification"
        ],
        "difficulty": ScenarioDifficulty.EASY,
        "category": "prize_scam",
        "explanation": "You cannot normally win a legitimate prize you never entered. The unexpected reward, short deadline, and request for a delivery payment are strong warning signs."
    },

    {
        "title": "University Scholarship Opportunity",
        "content": "The Student Financial Aid Office has announced applications for its annual scholarship program. Eligible students can review the requirements and application deadline through the university's official student portal.",
        "correct_answer": "legit",
        "clues": [
            "Uses an official portal",
            "Provides normal application information",
            "No immediate payment request"
        ],

        "clue_options": [
          "Uses an official portal",
          "Provides normal application information",
          "No immediate payment request",
          "Threat of losing the scholarship",
          "Request for password",
          "Suspicious payment link"
          ],
        "difficulty": ScenarioDifficulty.MEDIUM,
        "category": "legitimate",
        "explanation": "The message provides general scholarship information and directs students to an established official portal rather than requesting money or sensitive information through a message."
    },

    {
        "title": "Mobile Money Account Warning",
        "content": "Your Mobile Money account has been selected for a security upgrade. To prevent your account from being blocked, send your PIN to the support agent below for verification.",
        "correct_answer": "scam",
        "clues": [
            "Request for PIN",
            "Threat of account blocking",
            "Urgency"
        ],

        "clue_options": [
          "Request for PIN",
          "Threat of account blocking",
          "Urgency",
          "Official support channel",
          "Normal account notification",
          "No sensitive information requested"
        ],
        "difficulty": ScenarioDifficulty.MEDIUM,
        "category": "mobile_money",
        "explanation": "Your PIN is sensitive information and should never be shared with someone claiming to provide support. The threat of account blocking is being used to pressure you into revealing it."
    },
     {
        "title": "Remote Internship Offer",
        "content": "Hello! We reviewed your profile and would like to offer you a remote software internship. Before your interview, purchase a 15,000 FCFA registration package using the payment link below. Your position will be reserved after payment.",
        "correct_answer": "scam",
        "clues": [
            "Unexpected job offer",
            "Payment required before interview",
            "Pressure to reserve the position",
            "Suspicious payment link"
        ],

        "clue_options": [
          "Unexpected job offer",
          "Payment required before interview",
          "Pressure to reserve the position",
          "Suspicious payment link",
          "Official interview invitation",
          "Normal job application process"
          ],
        "difficulty": ScenarioDifficulty.MEDIUM,
        "category": "job_scam",
        "explanation": "Requiring payment before an interview or to reserve a job is a major warning sign. The message also creates pressure around losing the opportunity."
    },

    {
        "title": "Your Friend Needs Help",
        "content": "Hey, I'm stuck at the hospital and my phone battery is almost dead. Can you send 25,000 FCFA to this number right now? I'll explain everything when I get home. Please don't call because I can't answer.",
        "correct_answer": "scam",
        "clues": [
            "Emotional pressure",
            "Urgency",
            "Unusual payment request",
            "Avoids verification"
        ],

        "clue_options": [
          "Emotional pressure",
          "Urgency",
          "Unusual payment request",
          "Avoids verification",
          "Normal conversation",
          "Verified identity"
],
        "difficulty": ScenarioDifficulty.MEDIUM,
        "category": "impersonation",
        "explanation": "The message creates an emotional emergency and asks for money while preventing you from verifying the person's identity. Contact your friend through a known communication method before sending anything."
    },

    {
        "title": "Account Login Alert",
        "content": "Security alert: A new login was detected on your account. If this was not you, open the official app and review your recent login activity. Do not share your password or verification codes with anyone.",
        "correct_answer": "legit",
        "clues": [
            "Provides a safe verification method",
            "Does not request a password",
            "Does not request payment"
        ],
        "clue_options":[
           "Provides a safe verification method",
           "Does not request a password",
           "Does not request payment",
           "Threatens immediate account closure",
           "Requests a verification code",
           "Suspicious payment link"
        ],
        "difficulty": ScenarioDifficulty.HARD,
        "category": "legitimate",
        "explanation": "The message gives the user a safe way to investigate the alert through the official app and explicitly warns against sharing sensitive information."
    },

    {
        "title": "The Scholarship Agent",
        "content": "URGENT SCHOLARSHIP NOTICE: A government scholarship worth 500,000 FCFA has been reserved for you. Only 20 students will receive this opportunity. Send your ID card, school credentials, and a 10,000 FCFA processing fee to the agent before midnight or your place will be given to someone else.",
        "correct_answer": "scam",
        "clues": [
            "Artificial scarcity",
            "Urgency",
            "Payment request",
            "Request for sensitive documents",
            "Unverified agent"
        ],
        "clue_options": [
          "Artificial scarcity",
          "Urgency",
          "Payment request",
          "Request for sensitive documents",
          "Unverified agent",
          "Official scholarship portal"
        ],
        "difficulty": ScenarioDifficulty.HARD,
        "category": "social_engineering",
        "explanation": "This message combines several manipulation techniques: urgency, artificial scarcity, a payment demand, and requests for sensitive documents. Legitimate scholarship programs should be verified through their official organization or institution."
    }
    ]
print("NUMBER OF SCENARIOS:", len(scenarios))
with app.app_context():
 for data in scenarios:
  print("SEEDING:", data["title"])
  title = data['title']
  content = data['content']
  correct_answer = data['correct_answer']
  clues = data['clues']
  difficulty = data['difficulty']
  category = data['category']
  explanation = data['explanation']
  clue_options = data['clue_options']
  scenario = Scenario(
    title = title,
    content = content,
    correct_answer = correct_answer,
    clues = clues,
    category = category,
    explanation = explanation,
    difficulty = difficulty,
    clue_options = clue_options
    )

  db.session.add(scenario)
  print("ADDED:", scenario.title)
 db.session.commit()