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


# Класс для тестирования
class RunnerTest(unittest.TestCase):

    # Метод для тестирования метода walk
    def test_walk(self):
        runner = Runner("Tester")
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    # Метод для тестирования метода run
    def test_run(self):
        runner = Runner("Sprinter")
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    # Метод для тестирования комбинаций методов run и walk
    def test_challenge(self):
        runner1 = Runner("Walker")
        runner2 = Runner("Racer")

        for _ in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()

