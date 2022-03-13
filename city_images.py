import requests



def get_image_of_city(city_name):
    static_server = 'http://static-maps.yandex.ru/1.x/'
    geocode_server = 'http://geocode-maps.yandex.ru/1.x/'

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": city_name,
        "format": "json",
        "results": 1
    }

    geocode_response = requests.get(geocode_server, params=geocoder_params).json()
    bbox = geocode_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    ll = geocode_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    print(ll, bbox)
    
    map_params = {
        "ll": ",".join(ll.split(' ')),
        "bbox": ",".join(bbox['lowerCorner'].split(' ')) + "~" + ",".join(bbox['upperCorner'].split(' ')),
        "l": "sat"
    }

    map_response = requests.get(static_server, params=map_params)

    with open('1.jpg', mode='wb') as f:
        f.write(map_response.content)


get_image_of_city('Москва')