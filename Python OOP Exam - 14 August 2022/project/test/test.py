from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("BMW", "M5", 1000, 100_000)

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("M5", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(100_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_car_price_setter_under_1_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_under_100_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_mileage_setter_100_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_with_higher_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(111_111)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_same_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100_000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_lower_price(self):
        result = self.car.set_promotional_price(90_000)

        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 90_000)

    def test_need_repair_when_repair_price_higher_than_half_of_the_car_price(self):
        result = self.car.need_repair(60_000, "Broken engine")

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_lower_repair_price(self):
        result = self.car.need_repair(10_000, "Broken engine")

        self.assertEqual(self.car.price, 110_000)
        self.assertEqual(self.car.repairs, ["Broken engine"])
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test__gt__with_other_type_car(self):
        second_car = SecondHandCar("BMW", "M3", 10000, 50_000)
        result = self.car.__gt__(second_car)

        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test__gt__with_same_car_type(self):
        second_car = SecondHandCar("BMW", "M5", 10000, 50_000)
        result = self.car.__gt__(second_car)

        self.assertTrue(result)

    def test__str__method(self):
        expected_result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(expected_result, str(self.car))



if __name__ == "__main__":
    main()