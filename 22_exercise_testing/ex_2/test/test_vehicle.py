from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_when_fuel_is_not_enough_raises_exception(self):
        expected_result = "Not enough fuel"

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual(expected_result, str(ex.exception))

    def test_drive_when_fuel_is_enough_reduce_fuel(self):
        expected_fuel = 100 - (1.25 * 10)
        self.vehicle.drive(10)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_refuel_when_its_get_bigger_than_capacity_raises_exception(self):
        expected_result = "Too much fuel"

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual(expected_result, str(ex.exception))

    def test_refuel_when_fuel_its_not_bigger_than_capacity_increase_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(50)

        expected_fuel = 50

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_str_method_that_returns_string_information_about_vehicle(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == '__main__':
    main()
