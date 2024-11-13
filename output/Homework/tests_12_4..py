import logging
import unittest
import Runner_12_2


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = Runner_12_2.Runner('Oleg', -5)
        for i in range(10):
            runner_1.walk()
        try:
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        runner_2 = Runner_12_2.Runner(45, 5)
        for i in range(10):
            runner_2.run()
        try:
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s, %(levelname)s | %(message)s")
