from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("hero", 100, 100, 100)
        self.enemy = Hero("enemy", 50, 50, 50)

    def test_correct_init(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_enemy_hero_username_same_as_hero_username_raises_exception(self):
        self.enemy.username = "hero"
        expected_result = "You cannot fight yourself"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ex.exception))

    def test_battle_when_hero_health_is_zero_raises_value_error(self):
        self.hero.health = 0
        expected_result = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_battle_when_enemy_health_is_zero_raises_value_error(self):
        self.enemy.health = 0
        expected_result = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_battle_when_hero_health_and_enemy_health_become_zero_result_is_draw(self):
        expected_result = "Draw"

        self.enemy.level = 100
        self.enemy.health = 100
        self.enemy.damage = 100

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_result, result)

    def test_battle_when_hero_health_is_bigger_than_zero_but_enemy_health_is_below_zero_result_is_win(self):
        self.hero = Hero("hero", 100, 100, 100)
        self.enemy = Hero("enemy", 1, 1, 1)

        expected_level = 101
        expected_health = 104
        expected_damage = 105
        expected_result = "You win"

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual(expected_result, result)

    def test_battle_when_hero_health_is_below_zero_but_enemy_health_is_bigger_than_zero_result_is_lose(self):
        self.hero = Hero("hero", 1, 1, 1)
        self.enemy = Hero("enemy", 100, 100, 100)

        expected_level = 101
        expected_health = 104
        expected_damage = 105
        expected_result = "You lose"

        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)
        self.assertEqual(expected_result, result)

    def test_repr_method_returns_string_for_hero(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        result = str(self.hero)

        self.assertEqual(expected_result, result)



if __name__ == "__main__":
    main()
