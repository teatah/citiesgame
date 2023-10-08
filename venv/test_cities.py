import unittest
from cities import CityGame


class TestCityGame(unittest.TestCase):
    def test_check_city_base_filling(self):
        cities = []
        result_label = ""
        city_label = ""
        # Проверка базы городов
        current_city = ""
        new_current_city, result_label, city_label = CityGame.check_city("", current_city, cities, result_label, city_label)
        self.assertEqual("", "")
        self.assertEqual(result_label, "База городов пуста!")


if __name__ == '__main__':
    unittest.main()