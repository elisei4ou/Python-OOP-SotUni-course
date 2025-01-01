from unittest import TestCase, main

from ex_4_code import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("make", "BMW", 10, 100)

    def test_innit(self):
        expected_make = "make"
        expected_model = "BMW"
        expected_fuel_consumption = 10
        expected_fuel_capacity = 100
        expected_fuel_amount = 0

        self.assertEqual(expected_make, self.car.make)
        self.assertEqual(expected_model, self.car.model)
        self.assertEqual(expected_fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(expected_fuel_capacity, self.car.fuel_capacity)
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_make_when_value_is_empty_string_raises_exception(self):
        expected_result = "Make cannot be null or empty!"

        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual(expected_result, str(ex.exception))

    def test_model_when_value_is_empty_string_raises_exception(self):
        expected_result = "Model cannot be null or empty!"

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_consumption_when_its_zero_raises_exception(self):
        expected_result = "Fuel consumption cannot be zero or negative!"

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_capacity_when_its_zero_raises_exception(self):
        expected_result = "Fuel capacity cannot be zero or negative!"

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_amount_whet_its_negative_raises_exception(self):
        expected_result = "Fuel amount cannot be negative!"

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual(expected_result, str(ex.exception))

    def test_refuel_when_fuel_amount_its_not_bigger_than_fuel_capacity_increase_fuel_amount_with_fuel(self):
        expected_fuel_amount = 50
        self.car.refuel(50)

        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_refuel_when_fuel_amount_ist_bigger_than_fuel_capacity(self):
        expected_fuel_amount = self.car.fuel_capacity
        self.car.refuel(200)

        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_refuel_when_fuel_is_zero_or_negative_number_raises_exception(self):
        expected_result = "Fuel amount cannot be zero or negative!"

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(expected_result, str(ex.exception))

    def test_drive_when_there_is_enough_fuel(self):
        self.car.fuel_amount = 100
        expected_fuel_amount = 99

        self.car.drive(10)

        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_drive_when_there_is_NOT_enough_fuel_amount_raises_exception(self):
        expected_result = "You don't have enough fuel to drive!"

        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual(expected_result, str(ex.exception))


if __name__ == "__main__":
    main()
