import requests
import config


# Функция для оформления Заказа на сервере
def post_create_orders(create_orders):
    return requests.post(config.url + config.create_order,
                         json=create_orders)


# Функция для получения Заказа по треку
def get_track_order(track):
    return requests.get(config.url + config.get_track + str(track))
