import unittest
from shapley_game.game import ShapleyGame, powerset


class TestSol(unittest.TestCase):
    def test_rdm_gen(self):
        game = ShapleyGame(5)
        game.compute_solution()


if __name__ == "__main__":
    unittest.main()
