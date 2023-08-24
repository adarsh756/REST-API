import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return []


def get_option_from_user():
    print("Menu:")
    print("1. Get Temperature")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return input("Enter your choice: ")


def get_weather_property(weather_entry, property_name):
    return weather_entry["main"][property_name]

def main():
    weather_data = get_weather_data()

    while True:
        option = get_option_from_user()

        if option == "1":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print_temperature(weather_data, date_time)
        elif option == "2":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print_wind_speed(weather_data, date_time)
        elif option == "3":
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            print_pressure(weather_data, date_time)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def print_temperature(weather_data, date_time):
    found = False
    for entry in weather_data:
        if entry["dt_txt"] == date_time:
            temperature = get_weather_property(entry, "temp")
            print(f"Temperature on {date_time}: {temperature}°C")
            found = True
            break
    if not found:
        print("Weather data not available for the given date and time.")


def print_wind_speed(weather_data, date_time):
    found = False
    for entry in weather_data:
        if entry["dt_txt"] == date_time:
            wind_speed = entry["wind"]["speed"]
            print(f"Wind Speed on {date_time}: {wind_speed} m/s")
            found = True
            break
    if not found:
        print("Weather data not available for the given date and time.")


def print_pressure(weather_data, date_time):
    found = False
    for entry in weather_data:
        if entry["dt_txt"] == date_time:
            pressure = get_weather_property(entry, "pressure")
            print(f"Pressure on {date_time}: {pressure} hPa")
            found = True
            break
    if not found:
        print("Weather data not available for the given date and time.")


if __name__ == "__main__":
    main()
