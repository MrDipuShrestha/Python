import requests

app_id = "f51abeada576be46347d8f0b2581a21c"
OWM_api = "https://api.openweathermap.org/data/3.0/onecall"
weather_param = {
    "lat": 52.460152,
    "lon": 34.961681,
    "appid": app_id,
}

response = requests.get(OWM_api, params=weather_param)
# response.raise_for_status()

data = response.json()

print(data)
