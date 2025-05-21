# Дмитрий Овчинников, 29-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

# Автоматизация:

def test_create_and_fetch_order():

    # 1. Создание нового заказа:

    create_response = sender_stand_request.create_order(data.order_body)

    if create_response.status_code == 201:
        tracker_id = create_response.json().get("track")
        print(f"Заказ успешно создан. Номер трекера: {tracker_id}")
    else:
        print(f"Ошибка при создании заказа: {create_response.status_code}")
        return

    # 2. Получение информации о заказе по трекеру:

    fetch_response = sender_stand_request.fetch_order_by_tracker(tracker_id)

    assert fetch_response.ok, f"Ошибка при получении данных заказа: {fetch_response.status_code}"

    # 3. Проверка статус-кода:
    
    if fetch_response.status_code == 200:
        order_details = fetch_response.json()
        print("Информация о заказе:")
        print(order_details)
    else:
        print(f"Ошибка: получен статус-код {fetch_response.status_code}")