from app.services.get_performance import get_performance
from app.services.recommend_training import recommend_training
from app.services.ai_engine import ai_recommendation_engine
from app import create_app
app = create_app()

USER_ID = 6#Hardcoded user id

with app.app_context():
 performance = get_performance(USER_ID)#Get the actual performance data using the user_id

print("PERFORMANCE:")
print(performance)

recommendation = recommend_training(performance)

print("\nDETERMINISTIC RECOMMENDATION:")
print(recommendation)

ai_message = ai_recommendation_engine(
    performance=performance,
    recommendation=recommendation
)

print("\nAI RECOMMENDATION:")
print(ai_message)