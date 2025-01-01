from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Ivan", 18, 100)
        self.other = TennisPlayer("Pesho", 23, 2000)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_with_exact_2_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Iv"

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_name_setter_with_less_than_2_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "I"

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_setter_with_less_than_18_years_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_with_correct_tournament_name(self):
        self.player.add_new_win("First Win")
        self.assertEqual(["First Win"], self.player.wins)

    def test_add_new_win_with_name_who_is_already_added(self):
        self.player.add_new_win("First Win")
        result = self.player.add_new_win("First Win")

        self.assertEqual(result, f"First Win has been already added to the list of wins!")
        self.assertEqual(["First Win"], self.player.wins)

    def test__lt__method_when_player_is_worse(self):
        result = self.player.__lt__(self.other)

        self.assertEqual(result, f'{self.other.name} is a top seeded player and he/she is better than {self.player.name}')

    def test__lt__method_when_player_is_better(self):
        self.player.points = 3000
        result = self.player.__lt__(self.other)

        self.assertEqual(result, f'{self.player.name} is a better player than {self.other.name}')

    def test__str__method(self):
        self.player.wins = ["1", "2", "3"]
        result = f"Tennis Player: {self.player.name}\n" \
                 f"Age: {self.player.age}\n" \
                 f"Points: {self.player.points:.1f}\n" \
                 f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(str(self.player), result)


if __name__ == "__main__":
    main()