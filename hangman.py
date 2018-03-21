import time
import random


class Hangman:
    def __init__(self):
        self.words = ["hogwarts", "harry", "ron", "voldemort", "dobby", "hedwig", "snape", "potter", "hagrid", "muggi", "blendingsprinsinn"]

    def __del__(self):
       print("destructor")

    def wordPuzzle(self):
        rightWord = random.choice(self.words)

        #Setjum _ í stað fjölda þeirra stafa sem eru í random orðinu.
        emptyLetter = "_" * len(rightWord)

        guessCountdown = 10
        #Söfnum guesses spilara í lista til að hafa bókhald
        guesses = []

        while guessCountdown >= 0 and not emptyLetter == rightWord:
            print(emptyLetter)
            print(str(guessCountdown))

            guessLetter = input("Þín ágiskun:")

            if guessLetter in rightWord:
                print ("Flott ágiskun! Stafurinn: " + guessLetter + " er einmitt í leyniorðinu.")
                guesses.append(guessLetter)
                #Setjum réttan staf inn fyrir _
                emptyLetter = self.rightGuess(rightWord, emptyLetter, guessLetter)

            elif len(guessLetter) > 1:
                print ("Heyrðu nú mig! Þú veist að í hengimann má aðeins velja 1 staf í einu, svo reyndu aftur:")

            elif guessLetter in guesses:
                print("Þú hefur valið þennan staf áður, vinsamlegast veldu annan staf!\n")

            else:
                print ("Oh nei nei nei! Stafurinn: " + guessLetter + ", er ekki í leyniorðinu kjánarassgat.\n")
                guesses.append(guessLetter)
                if guessCountdown <= 0:
                    print("Æji nei, rétta orðið var: " + rightWord + ".")
                    break
                #mögulega setja inn nei nei nei með áttunni hljóðbút
                else:
                    guessCountdown -= 1
                    print("Nú áttu aðeins " + str(guessCountdown) + " rangar ágiskanir upp á að hlaupa. \nEf þú nærð ekki orðinu birtist hinn illi Lávarður Valdimar og hver veit hvað hann getur gert þér!")

        if guessCountdown == 0:
            print ("Ó jæja fall er fararheill. \nÞú tapaðir í þetta skiptið og Dumbledore er mjög vonsvikinn en hefur ákveðið að gefa þér annað tækifæri, nýttu það vel!\n")
            time.sleep(3)
            loss = "loss"
            return loss
        else:
            print ("Jibbí til hamingju! Leyniorðið var: " + rightWord + "! Þú ert hér með búinn að ná öllum prófum Hogwarts og nú er ekkert annað til fyrirstöðu en að fagna og útskrifast...")
            win = "win"
            return win
            #reyna hér að kalla á readyInput úr klasanum Level()...
            #setja inn textann: Ýttu á enter til að fagna útskrift og samþykkja sigur þinn í leiknum Haraldur Pottur og félagar í háska!

    def rightGuess(self, correctWord, emptySpace, playerGuess):
        guessWord = ""

        for i in range(len(correctWord)):
            if correctWord[i] == playerGuess:
                guessWord = guessWord + playerGuess
            else:
                guessWord = guessWord + emptySpace[i]

        return guessWord

def main():
    lev4 = Hangman()
    lev4.wordPuzzle()

if __name__ == '__main__':
    main()
