import Runner_12_2
import unittest


class TournamentTest(unittest.TestCase):

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner_12_2.Runner('Усэйн', 10)
        self.runner_2 = Runner_12_2.Runner('Андрей', 9)
        self.runner_3 = Runner_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({place: str(participant) for place, participant in result.items()})

    def test_1(self):
        tournament_1 = Runner_12_2.Tournament(90, self.runner_1, self.runner_3)
        results = tournament_1.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    def test_2(self):
        tournament_2 = Runner_12_2.Tournament(90, self.runner_2, self.runner_3)
        results = tournament_2.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)

    def test_3(self):
        tournament_3 = Runner_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament_3.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner_3)


if __name__ == "__main__":
    unittest.main()
