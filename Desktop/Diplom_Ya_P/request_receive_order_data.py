#Семенова Ульяна 08а-марс Финальный проект. Инженер по тестирвоанию плюс

import data_orders
import request_create_order

# Функция получения данных о Заказе по треку
def test_create_orders():
    # Создаем заказ и получаем номер трека
    track_number = request_create_order.post_create_orders(data_orders.test_order).json().get("track")

    if track_number is None:
        print("Не удалось получить номер трека.")
        return

    # Получаем информацию о заказе с использованием номера трека
    number_track = request_create_order.get_track_order(track_number)

    if number_track.status_code == 200:
        print(f"Статус код: {number_track.status_code}. Успешно получена информация о Заказе - {track_number}.")
    else:
        print(f"Статус код: {number_track.status_code}. Ошибка при получении информации о Заказе - {track_number}")


# Вызываем функцию test_create_orders() для выполнения теста
test_create_orders()