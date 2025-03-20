import requests 

api_key = '8afe82a694888c49a744529c5a653407'
city = 'Tashkent'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
res = requests.get(url)
if res.status_code == 200:
    data = res.json()
    main = data["main"]
    print(f"""
    City: {city}
    Temperature: {main['temp']} °C
    Humidity: {main['humidity']} %
    Pressure: {main['pressure']} hPa

    """)    
else:
    print(f"error occured while fetching the weather data(Status Code: {res.status_code})")
