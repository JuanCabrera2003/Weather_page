import requests

API_KEY = "68a1057ba594e8a534afce84742b791e"

def get_data(place, forecastDays, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values = 8 * forecastDays
    filtered_data = filtered_data[:number_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind =="Sky": 
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data





#if __name__=="__main__":