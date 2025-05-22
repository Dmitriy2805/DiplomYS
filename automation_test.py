# Дмитрий Овчинников, 29-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Автоматизация:

def test_get_order_info_by_track():
    request_result = sender_stand_request.create_order()
    track_number=request_result.json()["track"]
    request_result = sender_stand_request.get_order_info_by_track(track_number)
    assert request_result.status_code == 200
