# -*- coding: utf-8 -*-
import requests

url = "https://car-data.p.rapidapi.com/cars"

querystring = {"limit":"100","page":"0"}

headers = {
	"X-RapidAPI-Key": "ad839a6ac6mshf7161cafaed8f61p161bd2jsn36f66fd7c0f2",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
