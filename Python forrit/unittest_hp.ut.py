import unittest
from unittest import mock
from unittest.mock import patch
import sys
import random
import os
import io
from io import StringIO
from subprocess import call

from level import Level
from level import Level1
from level import Level2
from character import Character
from character import ChooseChar
from hangman import Hangman

class TestLevel(unittest.TestCase):
    call(['clear'])
    def setUp(self):
        self.lev = Level()

    def test_1(self):
        self.assertEqual(self.lev.inputWrong(0), 'Heyrðu nú mig! Það má aðeins velja svarmöguleika já/nei, svo reyndu aftur!\n')
        self.assertEqual(self.lev.inputWrong(2), 'Heyrðu nú mig! Þú verður að ýta á \"enter\" til að halda áfram, svo reyndu aftur\n')

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = Character()

    def test_2(self):
        self.char = Character()
        self.char.setName("Haraldur Pottur")
        self.char.setDescription("Hinn útvaldi! Haraldur Pottur er 16 ára galdrastrákur sem hefur ekki átt sjö dagana sæla. Hann hefur barist við sjálfan Lávarð Valdimar og býr hann því að mikilli reynslu. Haraldur er fljótur á fótum og ræður við galdra sem fáir jafnaldrar hans þora að kljást við.\n")
        self.assertEqual(self.char.getName(), "Haraldur Pottur")
        self.assertEqual(self.char.getDescription(), "Hinn útvaldi! Haraldur Pottur er 16 ára galdrastrákur sem hefur ekki átt sjö dagana sæla. Hann hefur barist við sjálfan Lávarð Valdimar og býr hann því að mikilli reynslu. Haraldur er fljótur á fótum og ræður við galdra sem fáir jafnaldrar hans þora að kljást við.\n")

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.a = Hangman()

    def test_3(self):
        self.assertEqual(self.a.rightGuess("ron", "___", "r"), "r__")






#class TestLevel1(unittest.TestCase):
#    def setUp(self):
#        self.lev1 = Level1()
#        self.lev = Level()
#        self.character = ChooseChar()

#    @patch("sys.stdin", StringIO("já"))
#    def test_2(self):
#        answer = self.lev1.createCharacter()
#        self.assertEqual(answer, 'já')
#        self.assertTrue(answer)

#    def test_2(self):
#        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#            self.lev.looseLevel()
#            assert mock_stdout.getvalue() == "Nú hefur þú brugðist félögum þínum í Hogwarts, þú ert komin/nn aftur á byrjunarreit\n"

#    @mock.patch('sys.stdout', new_callable=StringIO)
#    def main_op(self, tst_str, mock_stdout):
#        with mock.patch('builtins.input', side_effect=tst_str):
#            self.lev1.happyChoice('Haraldur Pottur')
#        return mock_stdout.getvalue()


#    def test_4(self):
#        b = 'já'
#        it( 'já', function() expect self.readyInput();
#        self.assertEqual(self.main_op([b]), b)

        #for s in ('a', '1', '<' ):
        #    self.assertEqual(self.main_op([s]), s + self.lev.inputWrong(0))



    #def test_3(self):

#    def test_4(self):
#        capturedOutput = io.StringIO()
#        sys.stdout = capturedOutput
#        self.lev1.startLevel1()
#        sys.stdout = sys.__stdout__
#        print ('Captured', capturedOutput.getvalue())
#        self.lev1.createCharacter()
#        sys.stdin = open("preprogrammed_inputs.txt")
#        self.assertEqual(0, self.lev1.createCharacter)
    #def test_1(self):
    #    sys.stdin = open("wrong_ready_input.txt")
    #    self.level = level()
    #    level.wrongInput()


    #    capturedOutput = io.StringIO()                  # Create StringIO object
    #    sys.stdout = capturedOutput                     #  and redirect stdout.
    #    self.lev.looseLevel()                           # Call function.
    #    sys.stdout = sys.__stdout__                     # Reset redirect
    #    print ('Captured', capturedOutput.getvalue())   # Now works as before.



unittest.main()
