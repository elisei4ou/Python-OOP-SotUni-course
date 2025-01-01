from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "part type", 100, 100)

    def test_proper_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("part type", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_allowed_categories(self):
        categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

        self.assertEqual(self.robot.ALLOWED_CATEGORIES, categories)

    def test_wrong_category_setter_raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "wrong category"

        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        result = self.robot.get_used_capacity()

        self.assertEqual(result, 10)

    def test_get_available_capacity(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        result = self.robot.get_available_capacity()

        self.assertEqual(result, 90)

    def test_get_used_memory(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        result = self.robot.get_used_memory()

        self.assertEqual(result, 50)

    def test_get_available_memory(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        result = self.robot.get_available_memory()

        self.assertEqual(result, 50)

    def test_install_software_with_correct_software(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        software = {"name": "name2", 'memory_consumption': 10, 'capacity_consumption': 10}

        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        second_result = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}, software]

        self.assertEqual(expected_result, result)
        self.assertEqual(second_result, self.robot.installed_software)

    def test_install_software_with_incorrect_software(self):
        self.robot.installed_software = [{"name": "Gosho", 'memory_consumption': 50, 'capacity_consumption': 10}]
        software = {"name": "name2", 'memory_consumption': 100, 'capacity_consumption': 100}
        result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, self.robot.install_software(software))

    def test_install_software_exact_capacity_memory(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.installed_software = []
        self.robot.capacity = software['capacity_consumption']
        self.robot.memory = software['memory_consumption']

        result = self.robot.install_software(software)

        expected_message = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_memory_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.installed_software = []
        self.robot.capacity = software['capacity_consumption'] - 5
        self.robot.memory = software['memory_consumption'] + 10

        result = self.robot.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_capacity_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.installed_software = []
        self.robot.capacity = software['capacity_consumption'] + 10
        self.robot.memory = software['memory_consumption'] - 5

        result = self.robot.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [])

if __name__ == "__main__":
    main()