import requests
from pandas.io.json import json_normalize

url = "https://shadowverse-portal.com/api/v1/cards"

querystring = {"format":"json","lang":"en"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "33242c8a-d0b5-4dee-a08c-468bd2b80c27"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
cards_json = response.json()
cards_df = json_normalize(cards_json["data"]["cards"])
print(cards_df.head())
cards_df.to_csv("cards.csv")