from unittest import TestCase, main

from ex_1_code import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Gosho", 1000, 100)

    def test_init(self):
        expected_name = "Gosho"
        expected_salary = 1000
        expected_energy = 100
        expected_money = 0

        self.assertEqual(expected_name, self.worker.name)
        self.assertEqual(expected_salary, self.worker.salary)
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_money_increase_with_salary_energy_decrease_with_one(self):
        self.worker.work()
        expected_money = 1000
        expected_energy = 99

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_when_energy_is_zero_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        expected_result = 'Not enough energy.'

        self.assertEqual(expected_result, str(ex.exception))

    def test_rest_which_increase_energy_with_one(self):
        self.worker.rest()

        expected_energy = 101

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_string_with_worker_info(self):
        expected_result = f'Gosho has saved 0 money.'

        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == "__main__":
    main()
