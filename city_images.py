import requests
import os
import random
 

class CityChecker:
    def __init__(self):
        self.cities_left = ['Москва', 'Санкт-Петербург', 'Казань', 'Севастополь', 'Нижний Новгород']
        self.curr = random.choice(self.cities_left)
        self.cities_left.remove(self.curr)
        self.first = True
    
    def check_city(self, city):
        return self.curr.lower() == city.lower()
    
    def get_new_city(self):

        try:
            self.curr = random.choice(self.cities_left)
            self.cities_left.remove(self.curr)
        except IndexError:
            return None, None
        
        return self.curr, self._get_image_of_city(self.curr)
    
    def get_curr_city(self):
        return self.curr, self._get_image_of_city(self.curr)
        
    
    def _get_image_of_city(self, city_name):

        if self._already_have(city_name):
            print(1)
            return f'{city_name}.jpg'

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

        with open(f'./static/img/{city_name}.jpg', mode='wb') as f:
            f.write(map_response.content)
        
        return f'{city_name}.jpg'


    def _already_have(self, city_name):
        return f'{city_name}.jpg' in os.listdir('./static/img')
    
    def restart(self):
        self.cities_left = ['Москва', 'Санкт-Петербург', 'Казань', 'Севастополь']
        self.curr = random.choice(self.cities_left)
        self.cities_left.remove(self.curr)
        self.first = True