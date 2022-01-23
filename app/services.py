
from typing import List


fake_db = [
    {"id": 1, "name": "Hood", "automobile_id": 1},
    {"id": 2, "name": "Bumper", "automobile_id": 1},
    {"id": 3, "name": "Speedometer", "automobile_id": 1},
    {"id": 4, "name": "Hinge", "automobile_id": 2},
    {"id": 5, "name": "Fog light", "automobile_id": 2},
    {"id": 6, "name": "Fuel tank", "automobile_id": 2},
    {"id": 7, "name": "Trunk", "automobile_id": 3},
    {"id": 8, "name": "Tire", "automobile_id": 3},
    {"id": 9, "name": "Radiator ", "automobile_id": 3},
]


class PartService:
    def get(self, id: int) -> List[dict]:
        return list(filter(lambda p: p["id"] == id, fake_db))

    def get_by_automobile_id(self, id: int) -> List[dict]:
        return list(filter(lambda p: p["automobile_id"] == id, fake_db))


part_service = PartService()
