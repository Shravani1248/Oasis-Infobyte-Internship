import requests


def get_weather_data(city: str, api_key: str) -> dict:

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(
            base_url,
            params={"q": city, "units": "imperial", "APPID": api_key},
            timeout=10
        )
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def display_weather(data: dict, city: str):

    try:
        weather = data["weather"][0]["main"]
        temperature = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]

        print(f"\nWeather Information for {city.capitalize()}:")
        print(f"- Weather: {weather}")
        print(f"- Temperature: {temperature}°F")
        print(f"- Humidity: {humidity}%")
    except KeyError:
        print("Error: Unexpected data format from the weather API.")


def main():
    api_key = "f319c6d4e0bae33941024e8cacd3d8f0"
    city = input("Enter city name: ").strip()

    weather_data = get_weather_data(city, api_key)

    if weather_data:
        if weather_data.get('cod') == 200:
            display_weather(weather_data, city)
        else:
            print(f"City not found: {city.capitalize()} (Error: {weather_data.get('message', 'Unknown error')})")


if __name__ == "__main__":
    main()
