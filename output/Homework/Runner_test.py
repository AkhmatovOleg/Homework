import Runner_12_1
import unittest


def skip_is_frozen(func):
    def wrapped(self, *args, **kwargs):
        if self.is_frozen:
            print('Тесты в этом кейсе заморожены')
            return
        return func(self, *args, **kwargs)

    return wrapped


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_is_frozen
    def test_walk(self):
        runner_1 = Runner_12_1.Runner('Oleg')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @skip_is_frozen
    def test_run(self):
        runner_2 = Runner_12_1.Runner('Tolay')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @skip_is_frozen
    def test_challenge(self):
        runner_3 = Runner_12_1.Runner('Mila')
        runner_4 = Runner_12_1.Runner('Luda')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == '__main__':
    unittest.main()
