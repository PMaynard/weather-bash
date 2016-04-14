import forecastio
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read('./config.ini')

forecast = forecastio.load_forecast(Config.get("config", "api_key"), Config.get("config", "lat"), Config.get("config", "lng"))
now = forecast.currently()
print now.summary
print now.temperature, "Temp"
print now.precipProbability, "Probability of rain"
print now.windSpeed, "Wind Speed"
