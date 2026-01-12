
from database import Database

def test_statistics_counts(tmp_path):
    db_path = tmp_path / "service_center_import.db"
    db = Database(str(db_path))

    # создаём 2 заявки
    id1 = db.add_request({
        "equipment_type": "Кондиционер",
        "device_model": "Midea X",
        "fault_type": "Не включается",
        "problem_description": "Не запускается",
        "customer_name": "Иванов",
        "customer_phone": "89990000000",
        "estimated_cost": 1000
    })
    id2 = db.add_request({
        "equipment_type": "Кондиционер",
        "device_model": "LG Y",
        "fault_type": "Шум",
        "problem_description": "Сильный шум",
        "customer_name": "Петров",
        "customer_phone": "89991111111",
        "estimated_cost": 2000
    })

    assert id1 is not None
    assert id2 is not None

    stats = db.get_statistics(30)

    # ожидаем минимум 2 заявки
    assert stats["total_requests"] >= 2
