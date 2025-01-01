from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Gosho", 10)
        self.other_driver = TruckDriver("Pesho", 20)
        self.other_driver.available_cargos = {"Barcelona": 50, "Bulgaria": 5}

    def test_init_correct(self):
        self.assertEqual(self.driver.name, "Gosho")
        self.assertEqual(self.driver.money_per_mile, 10)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_setter_lower_than_0_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_that_already_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.other_driver.add_cargo_offer("Barcelona", 30)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_correct_return_string(self):
        result = self.driver.add_cargo_offer("Barcelona", 30)
        expected_cargos = {"Barcelona": 30}

        self.assertEqual(result, f"Cargo for 30 to Barcelona was added as an offer.")
        self.assertEqual(expected_cargos, self.driver.available_cargos)

    def test_drive_best_cargo_offer_when_zero_offers(self):
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("California", 2000)
        self.driver.add_cargo_offer("Los Angeles", 20000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.driver.earned_money, 4000)
        self.assertEqual(self.driver.miles, 20000)

    def test_check_for_activities(self):
        self.driver.earned_money = 20_000
        self.driver.check_for_activities(10_000)

        self.assertEqual(self.driver.earned_money, 8250)

    def test_eat(self):
        self.driver.earned_money = 100
        self.driver.eat(250)

        self.assertEqual(80, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 100
        self.driver.sleep(1000)

        self.assertEqual(55, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)

        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 10_000
        self.driver.repair_truck(10_000)

        self.assertEqual(2500, self.driver.earned_money)


if __name__ == "__main__":
    main()