from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.find_car(model)
        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CAR:
            new_car = self.VALID_CAR[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.find_obg_by_name(driver_name, self.drivers)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.find_obg_by_name(race_name, self.races)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        car = self.find_car_type(car_type)
        driver: Driver = self.find_obg_by_name(driver_name, self.drivers)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            old_model = driver.car.model
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver: Driver = self.find_obg_by_name(driver_name, self.drivers)
        race: Race = self.find_obg_by_name(race_name, self.races)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race: Race = self.find_obg_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        winners = sorted_drivers[:3]
        result = []

        for x in winners:
            x.number_of_wins += 1
            result.append(f"Driver {x.name} wins the {race_name} race with a speed of {x.car.speed_limit}.")

        return '\n'.join(result)

    def find_car(self, model):
        try:
            return next(filter(lambda c: c.model == model, self.cars))
        except StopIteration:
            return None

    def find_obg_by_name(self, name, collection):
        try:
            return next(filter(lambda x: x.name == name, collection))
        except StopIteration:
            return None

    def find_car_type(self, car_type):
        available_cars = []

        for car in self.cars:
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    available_cars.append(car)

        if available_cars:
            return available_cars[-1]
