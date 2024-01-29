import requests

def get_weather(city):
    api_key = '85f0f64a4ea4fafbb26c685e5ee4001b'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather_info(weather_data):
    if weather_data:
        print("\nWeather Information")
        print("===================")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description'].capitalize()}")
    else:
        print("Unable to retrieve weather information.")

def main():
    print("Weather Information App")
    print("=======================")

    city_name = input("Enter the name of the city: ")
    weather_data = get_weather(city_name)

    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
