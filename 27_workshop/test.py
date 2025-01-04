from unittest import TestCase, main
from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.l = CustomList()

    def test_init(self):
        self.assertEqual(self.l.list, [])

    def test_append_return_list_with_new_value_at_the_end(self):
        self.l.list = [1]
        result = [1, 2]

        self.l.append(2)

        self.assertEqual(result, self.l.list)

    def test_remove_with_valid_index(self):
        self.l.list = [1, 2, 3]
        result = [1, 3]

        self.l.remove(1)

        self.assertEqual(result, self.l.list)

    def test_remove_with_invalid_indexes_returns_string(self):
        self.l.list = [1, 2, 3]
        invalid_indexes = ["abv", 1.1, [1, 2], (1, 2), {1: 2}, True, None]
        result = "You can not remove with invalid index"


        for idx in invalid_indexes:
            self.assertEqual(result, self.l.remove(idx))

    def test_get_with_valid_index(self):
        self.l.list = [1, 2, 3]
        result = 1

        self.assertEqual(result, self.l.get(0))

    def test_get_with_invalid_indexes_returns_string(self):
        invalid_indexes = ["abv", 1.1, [1, 2], (1, 2), {1: 2}]
        result = "You can not get with invalid index"


        for idx in invalid_indexes:
            self.assertEqual(result, self.l.get(idx))

    def test_extend_with_valid_iterable_returns_extended_list(self):
        self.l.list = [1, 2, 3]
        result = [1, 2, 3, 4, "abv"]

        self.assertEqual(result, self.l.extend([4, "abv"]))

    def test_extend_with_non_iterable_objects(self):
        invalid_indexes = [1.1, 2, 3 + 4j, True, None]
        result = "You can not extend with not iterable object"

        for idx in invalid_indexes:
            self.assertEqual(result, self.l.extend(idx))

    def test_insert_with_non_int_obj_returns_string(self):
        expected_result = f"You can not insert with str"

        self.assertEqual(expected_result, self.l.insert("abc", 1))

    def test_insert_with_negative_index_returns_string(self):
        expected_result = "You can not insert with negative index"

        self.assertEqual(expected_result, self.l.insert(-1, 1))

    def test_insert_with_index_bigger_than_len_of_list_returns_string(self):
        expected_result = "You can not insert with invalid index"

        self.assertEqual(expected_result, self.l.insert(100, 1))

    def test_insert_with_valid_index_returns_the_new_list(self):
        result = [3, 2, 1]
        self.l.list = [3, 2]
        self.l.insert(2, 1)

        self.assertEqual(result, self.l.list)

    def test_pop_when_the_list_is_empty_returns_string(self):
        result = "You can not pop when the list is empty"

        self.assertEqual(result, self.l.pop())

    def test_pop_when_list_is_filled_returns_the_last_element(self):
        result = 1
        self.l.list = [3, 2, 1]

        self.assertEqual(result, self.l.pop())

    def test_clear_when_the_list_is_empty_returns_string(self):
        result = "You can not clear when the list is already empty"

        self.assertEqual(result, self.l.clear())

    def test_clear_when_list_is_filled_list_get_empty(self):
        result = []
        self.l.list = [3, 2, 1]
        self.l.clear()

        self.assertEqual(result, self.l.list)

    def test_index_with_invalid_value_returns_string(self):
        result = "The index is invalid"
        invalid_indexes = ["abv", 1.1, [1, 2], (1, 2), {1: 2}, True, None]

        for el in invalid_indexes:
            self.assertEqual(result, self.l.index(el))

    def test_index_with_valid_value_returns_the_index_of_given_value(self):
        self.l.list = [1, 2, 3]
        result = 0

        self.assertEqual(result, self.l.index(1))

    def test_copy_when_list_is_not_empty(self):
        self.l.list = [1, 2, 3]
        result = [1, 2, 3]

        self.assertEqual(result, self.l.copy())
        self.assertIsNot(self.l.list, self.l.copy())

    def test_size_returns_len_of_the_list(self):
        self.l.list = [1, 2, 3]
        result = 3

        self.assertEqual(result, self.l.size())

    def test_add_first_append_value_at_the_first_position(self):
        self.l.list = [1, 2, 3]
        result = [0, 1, 2, 3]
        self.l.add_first(0)

        self.assertEqual(result, self.l.list)

    def test_dictionize_when_len_of_list_is_even(self):
        self.l.list = [1, 2, 3, 4]
        result = {1: 2, 3: 4}

        self.assertEqual(result, self.l.dictionize())

    def test_dictionize_when_len_of_list_is_odd(self):
        self.l.list = [1, 2, 3]
        result = {1: 2, 3: " "}

        self.assertEqual(result, self.l.dictionize())

    def test_move_when_amount_is_bigger_than_len_of_list(self):
        result = "You can not move when the amount is invalid"

        self.assertEqual(result, self.l.move(100))

    def test_move_when_amount_is_smaller_than_list_len_return_new_list(self):
        self.l.list = [1, 2, 3, 4]
        result = [3, 4, 1, 2]
        action = self.l.move(2)

        self.assertEqual(result, action)
        self.assertIsNot(self.l.list, action)

    def test_move_when_amount_is_same_as_list_len_return_new_list(self):
        self.l.list = [1, 2, 3, 4]
        result = [1, 2, 3, 4]
        action = self.l.move(4)

        self.assertEqual(result, action)
        self.assertIsNot(self.l.list, action)

    def test_sum_whith_numbers_strings_and_lists(self):
        self.l.list = [1, "ab", [1, 2, 3]]
        result = 6

        self.assertEqual(result, self.l.sum())

    def test_overbound_when_list_is_empty_returns_string(self):
        result = "The list is empty"

        self.assertEqual(result, self.l.overbound())

    def test_overbound_with_number_string_and_lists_return_the_index_of_largest(self):
        self.l.list = [1, "ab", [1, 2, 3]]

        result = 2

        self.assertEqual(result, self.l.overbound())

    def test_underbound_when_list_is_empty_returns_string(self):
        result = "The list is empty"

        self.assertEqual(result, self.l.underbound())

    def test_underbound_with_number_string_and_lists_return_the_index_of_largest(self):
        self.l.list = [1, "ab", [1, 2, 3]]

        result = 0

        self.assertEqual(result, self.l.underbound())


if __name__ == '__main__':
    main()