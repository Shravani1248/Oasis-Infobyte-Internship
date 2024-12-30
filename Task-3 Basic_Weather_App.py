import requests  # Import the requests library to make HTTP requests

# Function to fetch weather data from the OpenWeatherMap API
def get_weather_data(city: str, api_key: str) -> dict:
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Parameters:
        city (str): The name of the city to get weather information for.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: A dictionary containing weather data if the request is successful, or None if an error occurs.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"  # Base URL for the API

    try:
        # Make a GET request to the API with the specified parameters
        response = requests.get(
            base_url,
            params={"q": city, "units": "imperial", "APPID": api_key},
            timeout=10  # Set a timeout to avoid hanging indefinitely
        )
        response.raise_for_status()  # Raise an error for HTTP response codes 4xx or 5xx
        return response.json()  # Return the JSON response as a dictionary
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions and print the error
        print(f"Error fetching weather data: {e}")
        return None  # Return None in case of an error

# Function to display the weather data in a user-friendly format
def display_weather(data: dict, city: str):
    """
    Displays weather information in a readable format.

    Parameters:
        data (dict): The dictionary containing weather data.
        city (str): The name of the city the weather data corresponds to.
    """
    try:
        # Extract specific weather details from the API response
        weather = data["weather"][0]["main"]  # General weather condition
        temperature = round(data["main"]["temp"])  # Current temperature, rounded
        humidity = data["main"]["humidity"]  # Humidity percentage

        # Print the weather information
        print(f"\nWeather Information for {city.capitalize()}:")
        print(f"- Weather: {weather}")
        print(f"- Temperature: {temperature}°F")
        print(f"- Humidity: {humidity}%")
    except KeyError:
        # Handle cases where the API response is not in the expected format
        print("Error: Unexpected data format from the weather API.")

# Main function to handle user input and program flow
def main():
    """
    Main function to get user input, fetch weather data, and display it.
    """
    # OpenWeatherMap API key
    api_key = "f319c6d4e0bae33941024e8cacd3d8f0"

    # Prompt the user to enter a city name
    city = input("Enter city name: ").strip()

    # Fetch the weather data for the entered city
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        # Check if the API response is successful (HTTP status code 200)
        if weather_data.get('cod') == 200:
            display_weather(weather_data, city)  # Display the weather information
        else:
            # Handle cases where the city is not found or other errors occur
            print(f"City not found: {city.capitalize()} (Error: {weather_data.get('message', 'Unknown error')})")

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()  # Call the main function
