import requests
API_KEY="01234567890123456789012345678901"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        if data.get('cod')!=200:
            print(f"获取天气信息失败，错误码：{data.get('cod')}")
            return
        
        city_name=data['name']
        temperature=data['main']['temp']
        weather_description=data['weather'][0]['description']
        humidity=data['main']['humidity']
        wind_speed=data['wind']['speed']

        print(f"城市：{city_name}")
        print(f"天气：{weather_description}")
        print(f"温度：{temperature}°C")
        print(f"湿度：{humidity}%")
        print(f"风速：{wind_speed}m/s")
    except requests.exceptions.RequestException as e:
        print(f"获取天气信息失败，错误：{e}")

if __name__=="__main__":
    city=input("请输入城市名称：")
    get_weather(city)
