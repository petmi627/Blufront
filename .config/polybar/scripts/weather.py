#!/usr/bin/python3
import requests,sys
from datetime import datetime

API_KEY = ""
if len(sys.argv) == 1:
    CITY = "Diekirch,LU"
else:
    CITY = sys.argv[1]

def transform_weather(weather):
    icons = {
                "light_intensity_drizzle": {"icon": "wi-fog", "txt": ""},
                "drizzle": {"icon": "wi-fog", "txt": ""},
                "heavy_intensity_drizzle": {"icon": "wi-fog", "txt": ""},
                "light_intensity_drizzle_rain": {"icon": "wi-fog", "txt": ""},
                "drizzle_rain": {"icon": "wi-fog", "txt": ""},
                "heavy_intensity_drizzle_rain ": {"icon": "wi-fog", "txt": ""},
                "shower_rain and_drizzle": {"icon": "wi-fog", "txt": ""},
                "heavy_shower_rain and_drizzle": {"icon": "wi-fog", "txt": ""},
                "shower_drizzle ": {"icon": "wi-fog", "txt": ""},
                "mist": {"icon": "wi-fog", "txt": ""},
                "smoke": {"icon": "wi-smoke", "txt": ""},
                "haze": {
                    "day": {"icon": "wi-day-fog", "txt": ""},
                    "night": {"icon": "wi-night-fog", "txt": ""}
                },
                "sand_dust_whirls": {"icon": "wi-sandstorm", "txt": ""},
                "sand": {"icon": "wi-sandstorm", "txt": ""},
                "fog": {"icon": "wi-fog", "txt": ""},
                "dust": {"icon": "wi-dust", "txt": ""},
                "volcanic_ash": {"icon": "wi-volcano", "txt": ""},
                "squalls": {"icon": "wi-storm-showers", "txt": ""},
                "tornado": {"icon": "wi-tornado", "txt": ""},
                "clear_sky": {
                    "day": {"icon": "wi-day-sunny", "txt": ""},
                    "night": {"icon": "wi-night-clear", "txt": ""}
                },
                "few_clouds": {
                    "day": {"icon": "wi-day-cloudy", "txt": ""},
                    "night": {"icon": "wi-night-alt-cloudy", "txt": ""}
                },
                "scattered_clouds": {"icon": "wi-cloud", "txt": ""},
                "broken_clouds": {"icon": "wi-cloudy", "txt": ""},
                "overcast_clouds": {
                    "day": {"icon": "wi-day-sunny-overcast", "txt": ""},
                    "night": {"icon": "wi-night-alt-partly-cloudy", "txt": ""}
                },
                "light_snow": {
                    "day": {"icon": "wi-day-snow", "txt": ""},
                    "night": {"icon": "wi-night-alt-snow", "txt": ""}
                },
                "snow": {"icon": "wi-snow", "txt": ""},
                "heavy_snow": {"icon": "wi-snow", "txt": ""},
                "sleet": {"icon": "wi-sleet", "txt": ""},
                "shower_sleet": {"icon": "wi-sleet", "txt": ""},
                "light_rain_and_snow": "wi-{}-rain-mix",
                "rain_and_snow": {"icon": "wi-rain-mix", "txt": ""},
                "light_shower_snow": "wi-{}-rain-mix",
                "shower_snow": {"icon": "wi-rain-mix", "txt": ""},
                "heavy_shower_snow": {"icon": "wi-rain-mix", "txt": ""},
                "light_rain": {
                    "day": {"icon": "wi-day-sleet", "txt": ""},
                    "night": {"icon": "wi-night-sleet", "txt": ""}
                },
                "moderate_rain": {"icon": "wi-rain", "txt": ""},
                "heavy_intensity_rain": {"icon": "wi-rain", "txt": ""},
                "very heavy_rain": {"icon": "wi-rain", "txt": ""},
                "extreme_rain": {"icon": "wi-rain", "txt": ""},
                "freezing_rain": {"icon": "wi-rain", "txt": ""},
                "light_intensity shower_rain": {"icon": "wi-rain", "txt": ""},
                "shower_rain": {"icon": "wi-rain", "txt": ""},
                "heavy_intensity shower_rain": {"icon": "wi-rain", "txt": ""},
                "ragged_shower_rain": {"icon": "wi-rain", "txt": ""},
                "thunderstorm_with_light_rain": {"icon": "wi-thunderstorm", "txt": ""},
                "thunderstorm_with_heavy_rain": {"icon": "wi-thunderstorm", "txt": ""},
                "light_thunderstorm": {
                    "day": {"icon": "wi-day-thunderstorm", "txt": ""},
                    "night": {"icon": "wi-night-thunderstorm", "txt": ""}
                },
                "thunderstorm": {"icon": "wi-thunderstorm", "txt": ""},
                "heavy_thunderstorm": {"icon": "wi-thunderstorm", "txt": ""},
                "thunderstorm_with_light_drizzle": {"icon": "wi-thunderstorm", "txt": ""},
                "thunderstorm_with_drizzle": {"icon": "wi-thunderstorm", "txt": ""},
                "thunderstorm_with_heavy_drizzle": {"icon": "wi-thunderstorm", "txt": ""}
    }

    if weather['weather'][0]['description'].replace(' ', '_').replace(',', '') in icons.keys():
        icon = icons[weather['weather'][0]['description'].replace(' ', '_').replace(',', '')]
        if "icon" in icon.keys():
            return icon["txt"]
        else:
            sunrise = datetime.fromtimestamp(weather['sys']['sunrise'])
            sunset = datetime.fromtimestamp(weather['sys']['sunset'])
            now = datetime.now()

            icon_format = "night"
            if sunrise < now and sunset > now:
                icon_format = "day"

            return icon[icon_format]["txt"]


    else:
        return ""


request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + CITY + '&units=metric&appid=' + API_KEY)
if not request.status_code == 200:
    print("Cannot get weather data for city {}".format(CITY))

weather = request.json()
print("{} {}°C".format(transform_weather(weather), int(weather['main']['temp'])))
