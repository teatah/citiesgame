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

    def test_check_city_blank_inp(self):
        cities = ["Москва", "Астана", "Рим"]
        result_label = ""
        city_label = ""
        # Если пустой ввод, то вывести "Введите город!"
        current_city = ""
        new_current_city, result_label, city_label = CityGame.check_city("", current_city, cities, result_label, city_label)
        self.assertEqual("", "")
        self.assertEqual(result_label, "Введите город!")




if __name__ == '__main__':
    unittest.main()