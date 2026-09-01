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
        "category": "academic_communication",
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
        "category": "job_scholarship",
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
        "category": "account_alert",
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
        "category": "job_scholarship",
        "explanation": "This message combines several manipulation techniques: urgency, artificial scarcity, a payment demand, and requests for sensitive documents. Legitimate scholarship programs should be verified through their official organization or institution."
    },
    { "title": "A Classmate Needs a Quick Favor",
     "content": "Hey, I'm in the library and my phone is about to die. I need to pay for some printing before the office closes. Can you send 8,000 FCFA to this number for me? I'll pay you back when I see you tomorrow.",
      "correct_answer": "scam", 
      "clues": [ "Unexpected money request",
                 "Creates a time constraint", 
                "Uses a different payment number", 
                "Identity has not been verified" 
                ], 
      "clue_options": [ 
       "Unexpected money request", 
       "Creates a time constraint", 
       "Uses a different payment number", 
       "Identity has not been verified", 
       "Normal request from a classmate", 
       "Small amount of money" 
       ], 
       "difficulty": ScenarioDifficulty.MEDIUM, 
       "category": "impersonation", 
       "explanation": "The message sounds like it could genuinely come from a classmate, but the request involves sending money to an unfamiliar number under time pressure. Verify the person's identity through a trusted contact method before sending money."

    },
    { "title": "Message From Your Lecturer",
      "content": "Good afternoon. This is Dr. Mensah. I am finalizing the continuous assessment records and noticed your student file is incomplete. Please send me your registration number and a photo of your student ID here so I can update the record before submission.", 
      "correct_answer": "scam",
        "clues": [ 
         "Requests sensitive student information", 
         "Identity is not independently verified",
           "Uses academic pressure", 
           "Requests documents through a personal message"
             ], 
        "clue_options": [ 
         "Requests sensitive student information",
        "Identity is not independently verified",
          "Uses academic pressure",
          "Requests documents through a personal message", 
          "Uses the lecturer's name", 
          "Mentions continuous assessment" 
          ], 
        "difficulty": ScenarioDifficulty.HARD,
        "category": "impersonation", 
        "explanation": "The sender uses an academic context to make the request appear legitimate. A real lecturer may know your name and academic details, but that does not prove the identity of the sender. Sensitive documents should be submitted through verified institutional channels."
      },

      { "title": 
       "Student Affairs Follow-Up", 
       "content": "Hello Nana, this is the Student Affairs Office following up on your accommodation registration. "
       "We noticed your file was not fully processed. "
       "To resolve the issue, please confirm the phone number linked to your student account and forward the verification code you receive. This will allow us to complete the update.", 
       "correct_answer": "scam", 
       "clues": [ 
        "Requests a verification code", 
        "Uses personal information to appear credible", 
        "Creates an administrative problem", 
        "Requests action through an unverified channel" 
        ], 
        "clue_options": [ 
         "Requests a verification code", 
         "Uses personal information to appear credible", 
         "Creates an administrative problem", 
         "Requests action through an unverified channel", 
         "Mentions accommodation", 
         "Knows the student's name"
         ], 
        "difficulty": ScenarioDifficulty.HARD,
        "category": "impersonation", 
        "explanation": "Knowing your name or mentioning a real university process does not prove that a message is genuine. Verification codes should never be shared with someone contacting you unexpectedly. Confirm the request through an official university channel."
        },

        { 
           "title":  "Student Portal Security Verification",
           "content": "Student Portal Security Notice: We are updating account security for all students. Your account requires verification before the next portal maintenance window. Please review your account information using the verification page provided in this message.",
            "correct_answer": "scam",
            "clues": [ "Unexpected verification request", "Creates a maintenance deadline", "Link destination is not independently verified", "Requests account action through a message" ], 
            "clue_options": [ 
             "Unexpected verification request", 
             "Creates a maintenance deadline", 
             "Link destination is not independently verified", 
             "Requests account action through a message", 
             "Uses formal language", 
             "Mentions account security" 
             ], 
             "difficulty": ScenarioDifficulty.MEDIUM, 
             "category": "phishing", 
             "explanation": "The message uses professional language and a believable university context, but the request still needs independent verification. Instead of following an unexpected link, open the official student portal yourself."
          },

          { "title":
            "Unusual Sign-In Activity", 
            "content": "We detected a sign-in to your student account from a device we don't recognize. If this was you, no action is required. If you don't recognize this activity, review your account security using the security page linked in this message.",
             "correct_answer": "scam", 
             "clues": [ 
              "Unexpected security message",
              "Encourages clicking a provided link", 
              "Account activity cannot be verified from the message itself"
             ], 
             "clue_options": [ 
              "Unexpected security message", 
              "Encourages clicking a provided link", 
              "Account activity cannot be verified from the message itself", 
              "Professional security wording", 
              "Mentions an unfamiliar device", 
              "Does not request money"
             ], 
             "difficulty": ScenarioDifficulty.HARD, 
             "category": "phishing", 
             "explanation": "This message is intentionally convincing because it does not immediately ask for money or a password. The safest response is to open the official service directly rather than using a link supplied in an unexpected message." 
           },

           { 
            "title": "Mobile Money Security Update", 
            "content": "Your Mobile Money account is scheduled for a routine security review. To prevent delays during the update, please confirm your account number with the support representative who contacted you. Do not share your PIN.",
             "correct_answer": "scam",
             "clues": [ 
              "Unexpected contact from support", 
              "Creates concern about account access", 
              "Requests account information through an unverified channel" 
              ], 
              "clue_options": [ 
               "Unexpected contact from support", 
               "Creates concern about account access", 
               "Requests account information through an unverified channel", 
               "Explicitly says not to share your PIN", 
               "Uses security language", 
               "Mentions a routine update" 
               ], 
               "difficulty": ScenarioDifficulty.MEDIUM, 
               "category": "mobile_money", 
               "explanation": "The message is more subtle because it explicitly warns you not to share your PIN. However, an unexpected request for account information should still be independently verified through the provider's official support channels."
             },

             { 
              "title": "Transaction Review Required", 
              "content": "A recent Mobile Money transaction could not be fully processed. Our support team is reviewing the issue. Please confirm whether you authorized the transaction by replying YES. A representative may contact you if additional verification is required.", 
              "correct_answer": "legit", 
              "clues": [ 
               "Does not request a PIN", 
               "Does not request payment", 
               "Does not ask for a verification code", 
               "Provides a limited confirmation request" 
               ], 
               "clue_options": [ 
                "Does not request a PIN", 
                "Does not request payment", 
                "Does not ask for a verification code", 
                "Provides a limited confirmation request", 
                "Mentions a transaction", 
                "Uses security language" 
                ], 
                "difficulty": ScenarioDifficulty.HARD, 
                "category": "mobile_money", 
                "explanation": "Not every unexpected security message is a scam. This example avoids requesting sensitive credentials or money. However, users should still verify unexpected account activity through the official Mobile Money application or support channel." 
              },

    {
     "title": "Software Internship Screening",
     "content": "Dear Applicant, your application has been shortlisted for our remote software internship program. The next stage involves a short technical assessment. Please complete the assessment through the company's official careers portal before the application deadline.",
     "correct_answer": "legit",
     "clues": [
        "Uses an official careers portal",
        "Describes a normal recruitment step",
        "Does not request payment",
        "Does not request sensitive credentials"
     ],
     "clue_options": [
        "Uses an official careers portal",
        "Describes a normal recruitment step",
        "Does not request payment",
        "Does not request sensitive credentials",
        "Mentions an internship",
        "Has an application deadline"
     ],
     "difficulty": ScenarioDifficulty.HARD,
     "category": "job_scholarship",
     "explanation": "This message describes a plausible recruitment process and directs the applicant to an established careers portal. The absence of payment or credential requests is an important positive sign, although applicants should still verify the organization independently."
    },

    { 
     "title": "Scholarship Selection Notice", 
     "content": "Dear Student, your application has progressed to the next stage of the university scholarship review. The committee requires you to confirm your eligibility and review the remaining documentation requirements through the university's student portal. The final submission deadline is Friday.", 
     "correct_answer": "legit", 
     "clues": [ 
      "Uses an established university portal", 
      "Describes a normal application process", 
      "Provides a reasonable deadline", 
      "Does not request immediate payment" 
     ], 
     "clue_options": [ 
      "Uses an established university portal", 
      "Describes a normal application process", 
      "Provides a reasonable deadline", 
      "Does not request immediate payment", 
      "Mentions scholarship selection", 
      "Requests documentation through the official portal" 
      ], 
      "difficulty": ScenarioDifficulty.HARD, 
      "category": "job_scholarship", 
      "explanation": "The message provides a normal administrative update and directs the student to an established university portal. The communication does not demand money, passwords, or sensitive information through the message itself." 
    },

   { 
    "title": "Student Technology Giveaway", 
    "content": "Congratulations! Your student email was selected during our annual technology giveaway. Your account is eligible for a new smartphone. To confirm your eligibility, review the winner notification and collection instructions through the organization's official website. No payment is required to claim the prize.", 
    "correct_answer": "scam", 
    "clues": [ 
     "Unexpected prize notification", 
     "The user did not necessarily enter the giveaway", 
     "Prize claim needs independent verification", 
     "Unexpected selection can be a manipulation tactic" 
     ],

    "clue_options": [ 
     "Unexpected prize notification", 
     "The user did not necessarily enter the giveaway",
     "Prize claim needs independent verification", 
     "Unexpected selection can be a manipulation tactic", 
     "No payment is requested", 
     "Provides collection instructions" 
     ], 
     "difficulty": ScenarioDifficulty.HARD, 
     "category": "prize_scam", 
     "explanation": "This scenario is deliberately difficult because it avoids the obvious payment demand. An unexpected prize should still be independently verified, especially when the recipient does not remember entering the giveaway. A professional-looking message alone does not prove legitimacy." 
    }
    ]
print("NUMBER OF SCENARIOS:", len(scenarios))
with app.app_context():
  if Scenario.query.count() > 0:
        print("SCENARIOS ALREADY EXIST. SKIPPING SEED.")
  else:
   for data in scenarios:
     print("SEEDING:", data["title"])

     scenario = Scenario(
                title=data["title"],
                content=data["content"],
                correct_answer=data["correct_answer"],
                clues=data["clues"],
                category=data["category"],
                explanation=data["explanation"],
                difficulty=data["difficulty"],
                clue_options=data["clue_options"]
            )

     db.session.add(scenario)

   db.session.commit()
   print("SEEDED", len(scenarios), "SCENARIOS") 