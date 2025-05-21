import requests
import configuration

# 1. Функция для создания заказа:

def create_order(order_data):
    url = f"{configuration.URL_SERVICE}{configuration.CREATE_ORDERS}"
    response = requests.post(url, json=order_data)
    return response


# 2. Функция для получения данных о заказе по трек номеру:

def fetch_order_by_tracker(tracker_id):
    url = f"{configuration.URL_SERVICE}{configuration.FETCH_ORDER_TRACK}"
    params = {"t": tracker_id}
    response = requests.get(url, params=params)
    return response