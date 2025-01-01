from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_shelf_not_exist_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "something")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_name_already_in_shelf_raise_exception(self):
        self.store.toy_shelf = {
            "A": "Superman",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Superman")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_already_taken(self):
        self.store.toy_shelf = {
            "A": "Superman",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Batman")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_correct_way(self):
        expected_return = self.store.add_toy("A", "Superman")

        self.assertEqual(expected_return, f"Toy:Superman placed successfully!")
        self.assertEqual({
            "A": "Superman",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_remove_toy_shelf_doesnt_exist_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Superman")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_that_doesnt_exist_on_shelf(self):

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Superman")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_correct_remove_toy(self):
        self.store.toy_shelf = {
            "A": "Superman",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.store.remove_toy("A", "Superman")
        expected_shelf = None

        self.assertEqual(f"Remove toy:Superman successfully!", result)
        self.assertEqual(expected_shelf, self.store.toy_shelf["A"])



if __name__ == "__main__":
    main()