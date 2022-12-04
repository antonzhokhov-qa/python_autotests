import requests
import pytest

def test_statuscode():
    url ='https://pokemonbattle.me:5000/trainers'   
    response = requests.get(url,
    headers={'trainer_token':'5d60d0033c4187ebbc123b18b96bcf55'})
    assert response.status_code == 200

def test_id():
    url ='https://pokemonbattle.me:5000/trainers?trainer_id=1199'   
    response = requests.get(url,
    headers={'trainer_token':'5d60d0033c4187ebbc123b18b96bcf55'})
    assert response.json()['trainer_name'] == 'Tony_montana'