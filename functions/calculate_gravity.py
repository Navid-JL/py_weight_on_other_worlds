from decimal import Decimal
from typing import List


def calculate_gravity(surface_gravity: List[dict], weight: Decimal):
    surface_gravity_combined = {}

    for entry in surface_gravity:
        surface_gravity_combined.update(entry)

    for key, value in surface_gravity_combined.items():
        print(f"{str.title(key)}: {round(weight * Decimal(value),2)}kg\n")
