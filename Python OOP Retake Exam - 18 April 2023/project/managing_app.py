from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_user_by_driving_licence(driving_license_number)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.find_vehicle_by_license_plate(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route = self.find_route(start_point, end_point, length)
        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        shorter_route = self.find_shorter_route(start_point, end_point, length)
        if shorter_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        longer_route = self.find_longer_route(start_point, end_point, length)
        if longer_route:
            longer_route.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self.find_user_by_driving_licence(driving_license_number)
        vehicle = self.find_vehicle_by_license_plate(license_plate_number)
        route = self.find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicle = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicle = sorted(damaged_vehicle, key=lambda v: (v.brand, v.model))[:count]

        for v in sorted_vehicle:
            v.is_damaged = False
            v.recharge()
        return f"{len(sorted_vehicle)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_user = sorted(self.users, key=lambda z: -z.rating)
        result = "*** E-Drive-Rent ***"

        for d in sorted_user:
            result += f"\n{str(d)}"

        return result

    def find_user_by_driving_licence(self, driving_license_number):
        try:
            return next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        except StopIteration:
            return None

    def find_vehicle_by_license_plate(self, license_plate_number):
        try:
            return next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        except StopIteration:
            return None

    def find_route(self, start_point, end_point, length):
        try:
            return next(filter(lambda r: r.start_point == start_point
                                         and r.end_point == end_point
                                         and r.length == length, self.routes))
        except StopIteration:
            return None

    def find_shorter_route(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point:
                if route.end_point == end_point:
                    if route.length < length:
                        return route

    def find_longer_route(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point:
                if route.end_point == end_point:
                    if route.length > length:
                        return route

    def find_route_by_id(self, route_id):
        return next(filter(lambda r: r.route_id == route_id, self.routes))

