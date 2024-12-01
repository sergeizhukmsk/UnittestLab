import unittest


# Ваш исходный класс Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, 'is_frozen', False):
            print(f'Тест {method.__name__} пропущен, так как is_frozen = True')
        else:
            method(self, *args, **kwargs)

    return wrapper


# Класс для тестирования
class RunnerTest(unittest.TestCase):
    is_frozen = True # False  # Переменная для проверки, что тест не пропущен

    # Метод для тестирования метода walk
    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Tester")
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    # Метод для тестирования метода run
    @skip_if_frozen
    def test_run(self):
        runner = Runner("Sprinter")
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    # Метод для тестирования комбинаций методов run и walk
    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Walker")
        runner2 = Runner("Racer")

        for _ in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
