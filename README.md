# 🌦️ Weather CLI Application — The Mega Challenge  

**Course:** Python Development  
**Trainer:** *Engr. Uzaif Talpur*  
**Program:** The People’s Information Technology Program (PITP)  
**Institution:** The University of Modern Sciences, Tando Muhammad Khan, Sindh, Pakistan  

---

## 📌 Project Overview  

This Command-Line Interface (CLI) Weather Application is developed in **Python** as part of the *Mega Challenge Assignment (Assignment 5)*.  
It retrieves **real-time weather data** for any city using the **OpenWeatherMap API**, processes the response, and displays user-friendly weather information such as temperature, humidity, weather condition, and outfit suggestions.  
It also saves the API response in a structured JSON file.

---

## 🧠 Objective  

This project combines multiple Python concepts learned during the course, including:  
- API Requests using the `requests` module  
- JSON parsing and file handling  
- Working with `datetime` and timezones  
- Loops, functions, and conditional statements  
- Clean CLI output formatting  

---

## ⚙️ Features  

✅ Get real-time weather by entering any city name  
✅ Displays:  
- Temperature (°C / °F)  
- Humidity (%)  
- Weather condition (e.g., Clear, Rainy, Smoke, etc.)  
- Local time of the city  
✅ Smart outfit suggestions based on temperature and humidity  
✅ Saves data as JSON file → `weather_<city>_<date>.json`  
✅ Handles errors (invalid city, no internet, bad API key, etc.) gracefully  

---

## 🧩 Technologies & Libraries Used  

| Library | Purpose |
|----------|----------|
| `requests` | Fetching data from OpenWeatherMap API |
| `json` | Parsing and saving weather data |
| `os` | Accessing environment variables |
| `datetime` | Managing time and date |
| `timedelta` | Handling timezone offsets |

---

## 🚀 How to Run  

1. Clone or download this project folder:  
   ```bash
   git clone https://github.com/YourGitHubUsername/Weather_CLI_App_SheZan.git
   cd Weather_CLI_App_SheZan
