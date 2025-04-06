import json
import requests

def main():
    # --- Config ---
    lat = 0
    lon = 0
    
    apiKeyPath = ""
    
    units = "metric"
    
    weatherIcons = {
        # day
        "01d": "",
        "02d": "",
        "03d": "󰖐",
        "04d": "󰖐",
        "09d": "",
        "10d": "",
        "11d": "",
        "13d": "",
        "50d": "",
        # night
        "01n": "",
        "02n": "",
        "03n": "󰖐",
        "04n": "󰖐",
        "09n": "",
        "10n": "",
        "11n": "",
        "13n": "",
        "50n": ""
    }
    
    unitString = ""
    if units == "metric":
        unitString = "c"
    elif units == "imperial":
        unitString = "f"
    
    # --- End Config ---
    
    try:
        apiKey = open(apiKeyPath).read()
    except FileNotFoundError:
        print("Could not find API Key")
        
    try:
        url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"
                f"&lon={lon}&units={units}&appid={apiKey}")
        weather = requests.get(url).json()
    except :
        return print("Api Request Failed")
    
    iconCode = weather["weather"][0]["icon"]
    icon = weatherIcons[iconCode]
    
    temp = round(weather["main"]["temp"])
    feelsLike = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]
    type = weather["weather"][0]["main"]
    try:
        rainMMperH = weather["rain"]["1h"]
    except KeyError:
        rainMMperH = "0"
    

    tooltipText =f"Current Weather\nTemp: {temp}{unitString}, Feels like: {feelsLike}{unitString}.\nHumidity: {humidity}%. Rainfall this hour: {rainMMperH}mm.\nCurrent Weather: {type}."
    
    out = {
        "text": f"<big>{icon}</big> {temp}{unitString}",
        "temp": temp,
        "tooltip": tooltipText
    }
    
    print(json.dumps(out))

if __name__ == "__main__":
    main()