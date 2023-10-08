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

    def test_check_city_blank_cur(self):
        cities = ["Москва", "Астана", "Рим"]
        result_label = ""
        city_label = ""
        # При первом ходе при вводе подходящего города ход принимается
        current_city = ""
        new_current_city, result_label, city_label = CityGame.check_city("Москва", current_city, cities, result_label, city_label)
        self.assertEqual(new_current_city, "Москва")
        self.assertEqual(result_label, "")
        self.assertEqual(city_label, "Город: Москва")

    def test_check_city_blank_cur_not_in_base(self):
        cities = ["Москва", "Астана", "Рим"]
        result_label = ""
        city_label = ""
        # При первом ходе проверять город на наличие в базе
        current_city = ""
        new_current_city, result_label, city_label = CityGame.check_city("Саратов", current_city, cities,
                                                                         result_label, city_label)
        self.assertEqual(new_current_city, "")
        self.assertEqual(result_label, "Города нет в базе!")

    def test_check_city_not_in_base(self):
        cities = ["Москва", "Астана", "Рим"]
        current_city = "Москва"
        result_label = ""
        city_label = ""
        # При последующих ходах проверять город на наличие в базе
        new_current_city, result_label, city_label = CityGame.check_city("Домодедово", current_city, cities,
                                                                         result_label, city_label)
        self.assertEqual(new_current_city, "Москва")
        self.assertEqual(result_label, "Города нет в базе!")

    def test_check_city_valid(self):
        cities = ["Москва", "Астана", "Рим"]
        current_city = "Москва"
        result_label = ""
        city_label = ""
        # При последующих ходах проверять равенство первой буквы введенного и последней буквы текущего городов
        new_current_city, result_label, city_label = CityGame.check_city("Астана", current_city, cities,
                                                                         result_label, city_label)
        self.assertEqual(new_current_city, "Астана")
        self.assertEqual(result_label, "")
        self.assertEqual(city_label, "Город: Астана")

    def test_check_city_uncorrect(self):
        cities = ["Москва", "Астана", "Рим"]
        current_city = "Москва"
        result_label = ""
        city_label = ""
        # При последующих ходах проверять равенство первой буквы введенного и последней буквы текущего
        # городов и выводить ошибку
        new_current_city, result_label, city_label = CityGame.check_city("Рим", current_city, cities,
                                                                         result_label, city_label)
        self.assertEqual(result_label, "Город введен неверно!")


if __name__ == '__main__':
    unittest.main()