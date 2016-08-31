import json 
import requests 
card = requests.get('http://mtgjson.com/json/AllCards.json')
card.json()
cards = card.json 
for item in cards['Air Elemental']['manaCost']:
    print(item['manaCost'])