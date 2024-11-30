import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start_old(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            # На каждой итерации, в конце которой мы проверим, кто финишировал
            for participant in self.participants[:]:  # Используем срез для безопасного удаления
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    dict1: dict = {}  # Вначале теста создаем пустой словарь
    dict2: dict = {}  # Вначале теста создаем пустой словарь
    dict3: dict = {}  # Вначале теста создаем пустой словарь

    @classmethod
    def setUpClass(cls):
        cls.dict1.clear()  # Очистка словаря
        cls.dict2.clear()  # Очистка словаря
        cls.dict3.clear()  # Очистка словаря

    @classmethod
    def tearDownClass(cls):
        print(cls.dict1)
        print(cls.dict2)
        print(cls.dict3)

    def setUp(self):
        # Создаем трех бегунов
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    def test_usain_and_nick(self):
        tournament = Tournament(90, *[self.usain, self.nick])
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.dict1.update({1: 'Усэйн', 2: 'Ник'})

    def test_andrey_and_nick(self):
        tournament = Tournament(90, *[self.andrey, self.nick])
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.dict2.update({1: 'Андрей', 2: 'Ник'})

    def test_all_three_runners(self):
        tournament = Tournament(90, *[self.usain, self.andrey, self.nick])
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.dict3.update({1: 'Усэйн', 2: 'Андрей', 3: 'Ник'})

    def test_finish_order(self):
        tournament = Tournament(90, *[self.usain, self.andrey, self.nick])
        finishers = tournament.start()
        # Проверяем порядок финиша
        self.assertEqual(list(finishers.keys()), [1, 2, 3])
        self.assertEqual(finishers[1].name, "Усэйн")
        self.assertEqual(finishers[2].name, "Андрей")
        self.assertEqual(finishers[3].name, "Ник")


if __name__ == '__main__':
    unittest.main()
