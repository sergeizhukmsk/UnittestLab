from unittest_12_3 import RunnerTest
from metod_testcase_12_3 import TournamentTest
import unittest


def create_suite():
    # Создаем TestSuite
    test_suite = unittest.TestSuite()

    # Добавляем тесты RunnerTest и TournamentTest
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(create_suite())
