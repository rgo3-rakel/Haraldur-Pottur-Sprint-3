import unittest
import sys


from level import Level
from subprocess import call

class TestLevel(unittest.TestCase):
    call(['clear'])
    def setUp(self):
        self.lev1 = Level()

    #def test_1(self):
    #    sys.stdin = open("wrong_ready_input.txt")
    #    self.level = level()
    #    level.wrongInput(

    def test_2(self):pass
    #    self.assertEqual(self.lev1.inputWrong(0), 'Heyrðu nú mig! Það má aðeins velja svarmöguleika já/nei, svo reyndu aftur!')

if __name__ == '__main__':
    unittest.main()
