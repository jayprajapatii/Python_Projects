import requests

API_KEY = "630b3b066a36bb5169953461eddc4df4"  # Paste your OpenWeatherMap API key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\n🌤 Weather Details")
            print("--------------------")
            print(f"📍 City: {data['name']}")
            print(f"🌡 Temperature: {data['main']['temp']}°C")
            print(f"☁ Condition: {data['weather'][0]['description']}")
            print(f"💧 Humidity: {data['main']['humidity']}%")
        else:
            print("❌ City not found or API issue!")
            print("👉 Please check city name or API key.")

    except Exception as e:
        print("⚠ Error:", e)


# Run program
city = input("Enter city name: ")
get_weather(city)
