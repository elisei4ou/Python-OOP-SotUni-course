from unittest import TestCase, main

from ex_3_code import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.our_list = IntegerList("1", 1, 2, 3, 4, [1, 2])

    def test_init(self):
        expected_data = [1, 2, 3, 4]

        self.assertEqual(self.our_list.get_data(), expected_data)

    def test_add_when_element_is_integer_appended_to_the_data(self):
        expected_list = [1, 2, 3, 4, 5]
        our_list = self.our_list.add(5)

        self.assertEqual(our_list, expected_list)

    def test_add_when_element_is_not_integer_raises_value_error(self):
        expected_result = "Element is not Integer"
        # Maybe we have to check the data too

        with self.assertRaises(ValueError) as ve:
            self.our_list.add("not int")

        self.assertEqual(expected_result, str(ve.exception))

    def test_remove_index_when_index_is_in_range_removes_the_current_idx(self):
        expected_result = 1
        removed_el = self.our_list.remove_index(0)
        expected_list = [2, 3, 4]
        our_list = self.our_list.get_data()

        self.assertEqual(expected_result, removed_el)
        self.assertEqual(expected_list, our_list)

    def test_remove_index_when_idx__not_in_range_raise_index_error(self):
        expected_result = "Index is out of range"
        # Maybe check the data too

        with self.assertRaises(IndexError) as ie:
            self.our_list.remove_index(10)

        self.assertEqual(expected_result, str(ie.exception))

    def test_get_when_index_is_in_range_return_the_element(self):
        expected_result = 1
        our_element = self.our_list.get(0)

        self.assertEqual(expected_result, our_element)

    def test_get_when_index_is_out_of_range_raises_index_error(self):
        expected_result = "Index is out of range"

        with self.assertRaises(IndexError) as ie:
            self.our_list.get(10)

        self.assertEqual(expected_result, str(ie.exception))

    def test_insert_when_index_is_in_range_and_element_is_integer(self):
        expected_result = [1, 1, 2, 3, 4]
        self.our_list.insert(1, 1)

        self.assertEqual(expected_result, self.our_list.get_data())

    def test_insert_when_index_is_out_of_range_raises_index_error(self):
        expected_result = "Index is out of range"

        with self.assertRaises(IndexError) as ie:
            self.our_list.insert(10, 1)

        self.assertEqual(expected_result, str(ie.exception))

    def test_insert_when_el_is_not_integer_raises_value_error(self):
        expected_result = "Element is not Integer"

        with self.assertRaises(ValueError) as ve:
            self.our_list.insert(1, "string")

        self.assertEqual(expected_result, str(ve.exception))

    def test_get_biggest_return_the_biggest_integer_in_our_data(self):
        expected_result = 4
        our_result = self.our_list.get_biggest()

        self.assertEqual(expected_result, our_result)

    def test_get_index_return_the_index_of_element_in_our_data(self):
        expected_result = 0
        our_result = self.our_list.get_index(1)

        self.assertEqual(expected_result, our_result)



if __name__ == "__main__":
    main()