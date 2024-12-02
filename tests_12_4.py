import logging
import unittest

# Настройка базового конфигуратора для логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s: %(levelname)s: %(message)s'
)


# Ваш исходный класс Runner
class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")

        if speed < 0:
            raise ValueError("Скорость должна быть положительной")

        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name


# Класс для тестирования
class RunnerTest(unittest.TestCase):

    # Метод для тестирования метода walk
    def test_walk(self):
        try:
            runner = Runner("Tester", -10)  # Передаем отрицательное значение speed
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')

        except ValueError as exc:  # Runner выбрасывает ValueError
            logging.warning("Неверная скорость для Runner: %s", exc)

    # Метод для тестирования метода run
    def test_run(self):
        try:
            runner = Runner(12345, 10)  # Передаем что-то кроме строки в name
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')

        except TypeError as exc:  # Здесь предполагается, что Runner выбрасывает TypeError
            logging.warning("Неверный тип данных для объекта Runner: %s", exc)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
