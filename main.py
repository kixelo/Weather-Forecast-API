import requests

def get_weather(city_name, api_key='ebcbc2350eb4d70eaa9b6233dc8ef567', units='metric'):
    city_name=city_name.lower()
    city_name = input("Enter city name: ")
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    content = content["list"]
    results = []
    for item in content:
        for condition in item["weather"]:
            results.append(f'{city_name.title()}, {item["dt_txt"]}, {item["main"]["temp"]}, {condition["description"]}')

    for item in results:
        with open("data.txt", "a+") as file:
            file.write("\n" + item)
    return results

print(get_weather(""))