import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key = os.getenv("API_KEY")
parameters = {
    "appid":api_key,
    "lat":os.getenv("LAT"),
    "lon":os.getenv("LON"),
    "cnt":os.getenv("CNT"),
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    print(hour_data["weather"][0]["id"])
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring umbrella")        
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=f'whatsapp:{os.getenv("FROM_NUM")}',
    body='Raining, bring umbrella',
    to=f'whatsapp:{os.getenv("PHONE_NUM")}'
    )

    print(message.status)