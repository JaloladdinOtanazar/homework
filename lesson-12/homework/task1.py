from bs4 import BeautifulSoup
# Parse HTML with BeautifulSoup
with open('weather.html', "r") as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract weather information 
data = []
for row in soup.find('tbody').find_all('tr'):
    cols = row.find_all('td')
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))
    con = cols[2].text
    data.append({'day': day, 'temperature': temp, 'condition': con })

# Display data
print("\n5-Day Weather Forecast")
print("_"*50)
for d in data:
    print(f"Day: {d['day']} Temperature: {d['temperature']}°C Conditon: {d['condition']} ")


# Find Day with Highest Temperature
max_temp = max(data, key=lambda x: x['temperature'])
print("\nHighest Temperature of Day:")
print(f"{max_temp['day']}: {max_temp['temperature']}")

# Identify Day with Sunny Condition
sunny_days = (info['day'] for info in data if info['condition'] == "Sunny")
print("\nSunny days:")
for day in sunny_days:
    print(day)

#calculate average temp
average_temp = sum(info['temperature'] for info in data) / len(data)
print("\nAverage Temperature for a week:")
print(average_temp)



