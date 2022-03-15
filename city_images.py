import requests
import os



def get_image_of_city(city_name):

    # if already_have(city_name):
    #     print(1)
    #     return f'{city_name}.jpg'

    static_server = 'http://static-maps.yandex.ru/1.x/'
    geocode_server = 'http://geocode-maps.yandex.ru/1.x/'

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": city_name,
        "format": "json",
        "results": 1
    }

    geocode_response = requests.get(geocode_server, params=geocoder_params).json()
    # на всякий случай bbox
    # bbox = geocode_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    ll = geocode_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    
    
    map_params = {
        "ll": ",".join(ll.split(' ')),
        # "bbox": ",".join(bbox['lowerCorner'].split(' ')) + "~" + ",".join(bbox['upperCorner'].split(' ')),
        "z": 13,
        "size": "450,450",
        "l": "map"
    }

    map_response = requests.get(static_server, params=map_params)
    print(map_response)

    with open(f'./static/img/{city_name}.jpg', mode='wb') as f:
        f.write(map_response.content)
    
    return f'{city_name}.jpg'


def already_have(city_name):
    return f'{city_name}.jpg' in os.listdir('./static/img')


get_image_of_city('Санкт-петербург')