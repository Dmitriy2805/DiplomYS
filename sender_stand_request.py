import requests
import configuration
import data

# 1. Функция для создания заказа:

def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, 
                         json=data.order_body, 
                         headers=data.headers)

# 2. Функция для получения данных о заказе по трек номеру:

def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER, params={"t": track_number})


