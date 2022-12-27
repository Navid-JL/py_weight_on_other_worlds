from decimal import Decimal
from constants.planets import surface_gravity as planets_gravity
from constants.moons import surface_gravity as moons_gravity
from constants.dwarf_planets import surface_gravity as dwarf_planets_gravity
from functions.calculate_gravity import calculate_gravity
weight_on_earth = Decimal(0.0)

try:
    weight_on_earth = Decimal(input('Enter your weight in kg:\n'))
except ValueError:
    print('Enter a valid weight like 23.4 or 20')

calculate_gravity([planets_gravity, moons_gravity,
                  dwarf_planets_gravity], weight_on_earth)
