from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from app.services.recommend_training import recommend_training
performance = {
    "category_performance": {
        "impersonation": {
            "attempts": 5,
            "correct": 2,
            "accuracy": 40
        },
        "phishing": {
            "attempts": 5,
            "correct": 5,
            "accuracy": 100
        },
        "mobile_money": {
            "attempts": 5,
            "correct": 4,
            "accuracy": 80
        }
    },
    "difficulty_performance": {}
}
recommendation = {
    "primary_weakness": "impersonation",
    "recommended_difficulty": "easy",
    "focus_categories": ["impersonation"],
    "reason": "The user is weakest in impersonation with 40% accuracy."
}
ai_recommendation = recommend_training(
        performance=performance
)
client = OpenAI(
    base_url= "https://openrouter.ai/api/v1",
    api_key= os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(
     model="openai/gpt-chat-latest",
    messages=[
        {
            "role": "user",
            "content": f""" Using {ai_recommendation} data Suggest which scenario the user should do next and at which difficulty do not show the AI recommandation stats in you output
            but rather use that information to give the output """
        }
    ],
    max_tokens=100#Note: Always remember to explicitly specific the amount of tokens that you will use because you're models might have a default max_tokens limit
)
print(response.choices[0].message.content)