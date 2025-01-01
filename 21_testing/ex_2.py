from unittest import TestCase, main

from ex_2_code import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Peshko")

    def test_init(self):
        expected_name = "Peshko"
        expected_size = 0

        self.assertEqual(expected_name, self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_eat_fed_become_true_sleepy_become_true_size_increase_with_one(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_eat_while_fed_is_true_raise_exception(self):
        expected_result = 'Already fed.'
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(expected_result, str(ex.exception))

    def test_sleep_while_cat_is_not_hungry_sleepy_become_false(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleep_while_cat_is_hungry_raise_exception(self):
        expected_result = 'Cannot sleep while hungry'

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(expected_result, str(ex.exception))


if __name__ == "__main__":
    main()