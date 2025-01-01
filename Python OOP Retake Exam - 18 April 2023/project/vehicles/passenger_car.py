from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILLAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILLAGE)

    def drive(self, mileage: float):
        percentage = round(mileage / self.MAX_MILLAGE * 100)
        self.battery_level -= percentage
