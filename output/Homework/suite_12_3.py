import unittest
import Tournament_test
import Runner_test

tournamentST = unittest.TestSuite()
runnerST = unittest.TestSuite()

tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament_test.TournamentTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_test.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner_1 = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)
runner_1.run(runnerST)

