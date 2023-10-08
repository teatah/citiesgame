import tkinter as tk
from tkinter import messagebox


class CityGame:
    def __init__(self, cities):
        self.cities = cities
        self.current_city = ""
        self.timer = None

    def start_game(self):
        self.window = tk.Tk()

        self.window.geometry("300x200")

        self.window.title("Города")

        self.label_turn = tk.Label(self.window, text="Второй игрок")
        self.label_turn.pack()

        self.timer_label = tk.Label(self.window, text="Время: ")
        self.timer_label.pack()

        self.city_label = tk.Label(self.window, text="Город: ")
        self.city_label.pack()

        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack()

        self.button_ok = tk.Button(self.window, text="OK", command=self.ok_button_click)
        self.button_ok.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.restart_button = tk.Button(
            self.window, text="Начать заново", command=self.restart_game
        )
        self.restart_button.pack()

        self.start_new_turn()

        self.window.mainloop()

    def start_timer(self):
        if self.timer:
            self.window.after_cancel(self.timer)
        self.remaining_time = 30  # время в секундах
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text="Время: {} сек.".format(self.remaining_time))
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer = self.window.after(1000, self.update_timer)
        else:
            self.result_label.config(text="Время вышло!")
            self.current_city = ""

    def restart_game(self):
        self.window.destroy()
        self.start_game()

    def start_new_turn(self):
        if self.label_turn["text"] == "Первый игрок":
            self.label_turn.config(text="Второй игрок")
        else:
            self.label_turn.config(text="Первый игрок")
        self.result_label.config(text="")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.start_timer()

    def ok_button_click(self):
        city = self.input_entry.get().title()
        current_city = self.current_city
        cities = self.cities
        result_label = self.result_label['text']
        city_label = self.city_label['text']

        new_current_city, result_label, city_label = self.check_city(city, current_city, cities, result_label,
                                                                         city_label)

        self.result_label.config(text=result_label)
        self.city_label.config(text=city_label)
        if new_current_city != current_city:
            self.current_city = new_current_city
            self.start_new_turn()

    @staticmethod
    def check_city(city, current_city, cities, result_label, city_label):
        if len(cities) == 0:
            result_label = "База городов пуста!"
            return current_city, result_label, city_label

        if not city:
            result_label = "Введите город!"
            return current_city, result_label, city_label


# база городов
cities = ["Москва", "Астана", "Амстердам", "Минск", "Рим", "Мадрид", "Осло", "Орел"]

game = CityGame(cities)
game.start_game()
