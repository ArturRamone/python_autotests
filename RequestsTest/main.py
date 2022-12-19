import requests
import json


token = '194ca2462142f8d1b6acc8df58179c7f'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульбазавр",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
 })

print(response.text)

response_put =  requests.put('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token' : token}, json={
     "pokemon_id": 2535,
    "name": "Нео",
    "photo": ""
})

print(response_put.text)


token = '194ca2462142f8d1b6acc8df58179c7f'
response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',headers={'trainer_token' : token}, json={
    
    "pokemon_id": "2535"
})

print(response.text)



