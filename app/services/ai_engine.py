import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def ai_recommendation_engine(performance, recommendation):

    primary_weakness = recommendation["primary_weakness"]
    recommended_difficulty = recommendation["recommended_difficulty"]
    reason = recommendation["reason"]

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    prompt = f"""
You are the AI training coach for ScamLab, an educational
anti-scam training game.

The deterministic training system has identified:
- Primary weakness: {primary_weakness}
- Recommended difficulty: {recommended_difficulty}
- Reason: {reason}

Performance data:
{performance["category_performance"]}

Give the player a short, encouraging recommendation for
what type of scenario they should practice next.

Do not mention percentages, statistics, performance data,
or internal recommendation logic.

Keep the response to 2 sentences maximum.
"""

    response = client.chat.completions.create(
        model="openai/gpt-chat-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=100
    )

    return response.choices[0].message.content