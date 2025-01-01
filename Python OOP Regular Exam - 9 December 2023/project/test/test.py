from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(1000, 50, True)
        self.second_trip = Trip(1000, 1, True)

    def test_correct_init(self):
        self.assertEqual(1000, self.trip.budget)
        self.assertEqual(50, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_below_1_raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_travelers_smaller_than_2(self):
        self.assertEqual(False, self.second_trip.is_family)

    def test_book_a_trip_with_destination_not_in_offers(self):
        result = self.trip.book_a_trip("Oresh")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_with_family_but_not_enough_budget(self):
        result = self.trip.book_a_trip("New Zealand")
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_a_trip_enough_budget(self):
        self.second_trip.budget = 1_000_000
        expected_book_destination = {"New Zealand": 7500}
        expected_budget = 992_500
        result = self.second_trip.book_a_trip("New Zealand")

        self.assertEqual(expected_budget, self.second_trip.budget)
        self.assertEqual(expected_book_destination, self.second_trip.booked_destinations_paid_amounts)
        self.assertEqual(result, f'Successfully booked destination New Zealand! Your budget left is {expected_budget:.2f}')

    def test_book_a_trip_family(self):
        self.trip.budget = 1_000_000
        self.trip.travelers = 2
        expected_book_destination = {"New Zealand": 13_500}
        expected_budget = 986_500
        result = self.trip.book_a_trip("New Zealand")

        self.assertEqual(expected_budget, self.trip.budget)
        self.assertEqual(expected_book_destination, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(result,
                         f'Successfully booked destination New Zealand! Your budget left is {expected_budget:.2f}')

    def test_booking_status_without_booking_yet(self):
        result = self.trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: {self.trip.budget:.2f}')

    def test_booking_status_with_2_destination(self):
        self.second_trip.budget = 100_000
        self.second_trip.book_a_trip("Bulgaria")
        self.second_trip.book_a_trip("New Zealand")
        result = []
        sorted_bookings = sorted(self.second_trip.booked_destinations_paid_amounts.items())
        for booked_destination, paid_amount in sorted_bookings:
            result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        result.append(f"""Number of Travelers: {self.second_trip.travelers}
Budget Left: {self.second_trip.budget:.2f}""")

        self.assertEqual('\n'.join(result), self.second_trip.booking_status())


if __name__ == "__main__":
    main()
