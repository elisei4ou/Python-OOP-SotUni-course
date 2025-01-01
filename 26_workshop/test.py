from unittest import TestCase, main

from hashtable import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.table = HashTable()

    def test_correct_init(self):
        self.assertEqual([None, None, None, None], self.table.get_keys())
        self.assertEqual([None, None, None, None], self.table.get_values())
        self.assertEqual(4, len(self.table))

    def test_setitem_thunder_method_and_erase_length(self):
        self.table._HashTable__keys = ["1", "2", "3", "4"]
        self.table._HashTable__values = ["a", "b", "c", "d"]
        expected_keys = ["1", "2", "3", "4", "name", None, None, None]
        expected_values = ["a", "b", "c", "d", "Peter", None, None, None]

        self.table.__setitem__("name", "Peter")

        self.assertEqual(expected_values, self.table.get_values())
        self.assertEqual(expected_keys, self.table.get_keys())
        self.assertEqual(8, len(self.table))

    def test_getitem_thunder_method_which_returns_the_value_of_given_key(self):
        self.table._HashTable__keys = ["1", "2", "3", "4"]
        self.table._HashTable__values = ["a", "b", "c", "d"]
        expected_result = "a"

        self.assertEqual(expected_result, self.table.__getitem__("1"))

    def test_getitem_thunder_method_when_the_key_does_not_exist(self):
        expected_result = "The key does not exist"

        with self.assertRaises(KeyError) as ke:
            self.table.__getitem__("invalid")

        self.assertEqual(expected_result, ke.exception.args[0])

    def test_len_method(self):
        self.assertEqual(4, len(self.table))

    def test_str_thunder_method_returns_string_information_in_dict_form(self):
        expected_result = "{'name': Peter 'age': 25}"
        self.table["name"] = "Peter"
        self.table["age"] = 25

        self.assertEqual(expected_result, str(self.table))

    def test_hash_returns_given_index(self):
        expected_result = 1
        self.table["name"] = "Peter"

        self.assertEqual(expected_result, self.table.hash("name"))

    def test_get_method_returns_value_from_given_key(self):
        self.table["name"] = "Peter"

        self.assertEqual("Peter", self.table.get("name"))

    def test_get_method_returns_None_for_invalid_key(self):
        self.assertEqual(None, self.table.get("name"))

    def test_sort_method_returns_string_information_in_dict_format(self):
        expected_result = "{'age': 25 'name': Peter}"
        self.table._HashTable__keys = [None, "name", "age", None]
        self.table._HashTable__values = [None, "Peter", 25, None]

        self.assertEqual(expected_result, str(self.table.sort()))

    def test_sort(self):
        self.table["name"] = "test"
        self.table["age"] = 25

        result = self.table.sort()

        self.assertEqual(self.table._HashTable__keys, [None, "name", "age", None])
        self.assertEqual(self.table._HashTable__values, [None, "test", 25, None])
        self.assertEqual(self.table._HashTable__length, 4)

        self.assertEqual(result._HashTable__keys, ["age", "name", None, None])
        self.assertEqual(result._HashTable__values, [25, "test", None, None])
        self.assertEqual(result._HashTable__length, 4)

    def test_add__method_and_erase_length(self):
        self.table._HashTable__keys = ["1", "2", "3", "4"]
        self.table._HashTable__values = ["a", "b", "c", "d"]
        expected_keys = ["1", "2", "3", "4", "name", None, None, None]
        expected_values = ["a", "b", "c", "d", "Peter", None, None, None]

        self.table.add("name", "Peter")

        self.assertEqual(expected_values, self.table.get_values())
        self.assertEqual(expected_keys, self.table.get_keys())
        self.assertEqual(8, len(self.table))


if __name__ == '__main__':
    main()
