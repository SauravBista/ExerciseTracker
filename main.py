import json
import os
from keys import NUTRITIONIX_APP_KEY, NUTRITIONIX_APP_ID,Basic_Authorization
import requests

from datetime import date, datetime
GENDER = "male"
WEIGHT_KG = "62"
HEIGHT_CM = "175"
AGE = "21"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers ={
    'Content-Type': 'application/json',
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}



exercise = input("Tell me which exercise you did:")

headers_sheety = {
    "Authorization": Basic_Authorization,
}
exercise_config = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_config)
response.raise_for_status()
result = response.json()

date = date.today().strftime("%Y-%m-%d")
time = datetime.now().time().strftime("%H:%M:%S")

#Posting data in Sheety
sheety_url = "https://api.sheety.co/3b56d3183de8a70957b7d4b9742a1186/myWorkouts/workouts"



for exercise in result["exercises"]:
    sheety_config ={
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_url, json=sheety_config, headers=headers_sheety)
    print(sheety_response.text)