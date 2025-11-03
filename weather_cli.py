import requests 
import json 
import os 
from datetime import datetime, timedelta

API_KEY = os.getenv("OWM_API_KEY") or "f9138c5b32c3f0b62f323095483d92ad"

OWM_URL = "https://api.openweathermap.org/data/2.5/weather?"

DEFAULT_CITY = "Karachi"

def celsius_from_k(kelvin):
    return kelvin - 273.15

def fahrenheit_from_k(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY
    }
    try:
        resp = requests.get(OWM_URL, params=params, timeout=10)
    except requests.RequestException as e:
        return {"ok": False, "error": f"Network error: {e}"}
    
    if resp.status_code != 200:
        try:
            err = resp.json()
            msg = err.get("message", resp.text)
        except Exception:
            msg = resp.text
        return {"ok": False, "error": f"API error {resp.status_code}: {msg}"}
    try:
        data = resp.json()
    except Exception as e:
        return {"ok": False, "error": f"Failed to parse JSON: {e}"}
    return {"ok": True, "data": data}
def local_time_from_utc_and_offset(ustc_dt, offset_seconds):
    return ustc_dt + timedelta(seconds=offset_seconds)
def outfit_suggestion(temp_c, humidity, condition):
    if "rain" in condition.lower() or "drizzle" in condition.lower() or "thunder" in condition.lower():
        return "Carry an umbrella and wear water-resistant shoes."
    if temp_c <= 10:
        return "It's cold — wear warm clothes and a jacket!"
    if temp_c <= 20:
        return "Mild — a sweater or light jacket should be fine."
    if temp_c <= 27:
        if humidity > 70:
            return "Warm and humid — light clothing and stay hydrated."
        return "Comfortable — light clothing is fine."
    if temp_c > 27:
        return "Hot — wear breathable clothes, hat and use sunscreen."

def save_response(city, data):
    safe_city = city.strip().replace(" ", "_")
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"weather_{safe_city}_{date_str}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return filename

def pretty_print(city, data):
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    sys = data.get("sys", {})
    timezone_offset = data.get("timezone", 0)  

    temp_k = main.get("temp")
    humidity = main.get("humidity")
    condition = weather_list[0]["description"] if weather_list else "Unknown"

    if temp_k is None:
        print("Temperature data not available.")
        return

    temp_c = celsius_from_k(temp_k)
    temp_f = fahrenheit_from_k(temp_k)

    now_utc = datetime.utcnow()
    local_dt = local_time_from_utc_and_offset(now_utc, timezone_offset)
    local_dt_str = local_dt.strftime("%Y-%m-%d %H:%M:%S")

    print("-" * 50)
    print(f"Weather for {city.title()} (as of local time: {local_dt_str})")
    print("-" * 50)
    print(f"Condition : {condition.title()}")
    print(f"Temperature: {temp_c:.1f}°C / {temp_f:.1f}°F")
    print(f"Humidity: {humidity}%")
    
    if temp_c < 12:
        print(f"It's cold in {city.title()}, wear warm clothes!")
    elif humidity and humidity > 75 and temp_c > 24:
        print(f"{city.title()} feels humid today.")
    elif "snow" in condition.lower():
        print(f"Snowing in {city.title()} — be careful on the roads!")
    else:
        print(f"{city.title()} has {condition} conditions.")

    
    suggestion = outfit_suggestion(temp_c, humidity or 0, condition or "")
    if suggestion:
        print("Suggestion:", suggestion)
    print("-" * 50)

def main():
    if not API_KEY or API_KEY.startswith("<PUT_YOUR_API_KEY_HERE>"):
        print("ERROR: Please set your OpenWeatherMap API key in the script or set environment variable OWM_API_KEY.")
        print("Get API key from: https://openweathermap.org/")
        return

    print("=== Weather CLI Application ===")
    print(f"Press Enter to use default city: {DEFAULT_CITY}")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        if city == "":
            city = DEFAULT_CITY

        print(f"Fetching weather for {city} ...")
        result = get_weather(city)
        if not result["ok"]:
            print("Error:", result["error"])
        
            continue

        data = result["data"]
        
        pretty_print(city, data)

        filename = save_response(city, data)
        print(f"Saved API response to: {filename}")

        again = input("Check another city? (y/N): ").strip().lower()
        if again != "y":
            print("Exiting. Good luck with your submission!")
            break

if __name__ == "__main__":
    main()   