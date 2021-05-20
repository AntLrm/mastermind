import unittest
from mastermind.board import board
from mastermind.master import master

class test_evaluation(unittest.TestCase):
    def test_evaluation(self):
        mboard = board(4, 4)
        mmaster = master()
        mboard.set_secret([0,1,2,3])
        self.assertEqual([2,2,1,0], mmaster.evaluate_guess([1,1,2,0], mboard.secret_code))
        self.assertEqual([2,2,2,0], mmaster.evaluate_guess([0,1,2,0], mboard.secret_code))
        self.assertEqual([2,2,2,2], mmaster.evaluate_guess([0,1,2,3], mboard.secret_code))
        self.assertEqual([1,1,1,1], mmaster.evaluate_guess([3,2,1,0], mboard.secret_code))
        self.assertEqual([0,0,0,0], mmaster.evaluate_guess([4,4,4,4], mboard.secret_code))
        self.assertEqual([2,1,0,0], mmaster.evaluate_guess([4,4,1,3], mboard.secret_code))
        mboard.set_secret([2,2,3,0])
        self.assertEqual([2,1,0,0], mmaster.evaluate_guess([1,1,2,0], mboard.secret_code))
        self.assertEqual([2,1,0,0], mmaster.evaluate_guess([0,1,2,0], mboard.secret_code))
        self.assertEqual([1,1,1,0], mmaster.evaluate_guess([0,1,2,3], mboard.secret_code))
        self.assertEqual([2,2,1,0], mmaster.evaluate_guess([3,2,1,0], mboard.secret_code))
        self.assertEqual([0,0,0,0], mmaster.evaluate_guess([4,4,4,4], mboard.secret_code))
        self.assertEqual([1,0,0,0], mmaster.evaluate_guess([4,4,1,3], mboard.secret_code))
        self.assertEqual([2,2,2,2], mmaster.evaluate_guess([2,2,3,0], mboard.secret_code))
        self.assertEqual([2,2,1,1], mmaster.evaluate_guess([3,2,2,0], mboard.secret_code))
        self.assertEqual([2,1,1,0], mmaster.evaluate_guess([3,2,2,2], mboard.secret_code))