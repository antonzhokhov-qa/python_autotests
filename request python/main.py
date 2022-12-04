import requests

url = 'https://pokemonbattle.me:5000/pokemons'
response = requests.post(url, json={
    "name": "Нидоквиник",
    "photo": "https://pokemongolife.ru/p/Nidoqueen.png"
},
headers={'Accept': 'application/json', 'trainer_token':'5d60d0033c4187ebbc123b18b96bcf55'})
print(response.text)

url ='https://pokemonbattle.me:5000/pokemons'
response = requests.put(url,
headers={'Accept': 'application/json', 'trainer_token':'5d60d0033c4187ebbc123b18b96bcf55'},
json={
    "pokemon_id": 1361,
    "name": "German"
})
print(response.text)

url = 'https://pokemonbattle.me:5000/trainers/addPokebol'
response = requests.post(url,
headers={'Accept': 'application/json', 'trainer_token':'5d60d0033c4187ebbc123b18b96bcf55'},
json= {"pokemon_id": "1362"})

print(response.text)