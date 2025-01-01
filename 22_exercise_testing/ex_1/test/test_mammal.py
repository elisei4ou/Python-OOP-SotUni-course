from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("pesho", "bear", "rwar")

    def test_correct_init(self):
        self.assertEqual("pesho", self.mammal.name)
        self.assertEqual("bear", self.mammal.type)
        self.assertEqual("rwar", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_return_string(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_info_return_string_info_for_the_mammal(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()
