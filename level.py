import time
import sys
import random
#Importa klösum úr öðrum file-num
from character import Character
from character import ChooseChar
#from questions import question

#Skoða sql (gagnagrunn fyrir texta)
#Pygame - nota músík og grafík með því!

class Level:

    def __init__(self):
        pass
    #def __del__(self):
    #    print("destructor")

    def beginning(self): #Dumbledore talar
        print("Velkomin/nn í leikinn svaðilfari!")
        #setja mynd inn

        time.sleep(1)
        level1 = Level1()
        level1.startLevel1()

    def inputWrong (self, value):
        if value == 0:
            sentence = "Heyrðu nú mig! Það má aðeins velja svarmöguleika já/nei, svo reyndu aftur!\n"
        elif value == 1:
            sentence = "Heyrðu nú mig! Það má aðeins velja svarmöguleika (1, 2, 3, 4), svo reyndu aftur!\n"
        elif value == 2:
            sentence = "Heyrðu nú mig! Þú verður að ýta á \"enter\" til að halda áfram, svo reyndu aftur\n"
        else:
            sys.exit()
        return sentence

    def readyInput(self):
        words = ""
        ready = input("Ýttu á \"enter\" þegar þú ert tilbúin/nn að halda áfram:\n")
        if ready == "":
            return words
        else:
            sentence = self.inputWrong(2)
            print(sentence)
            time.sleep(2)
            self.readyInput()

    def looseLevel(self):
        print("Nú hefur þú brugðist félögum þínum í Hogwarts, þú ert komin/nn aftur á byrjunarreit\n")
        keepGoing = input("Viltu reyna aftur við leikinn? (já/nei) ")
        if keepGoing == 'já':
            self.beginning()
        elif keepGoing == 'nei':
            sys.exit()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.looseLevel()

class Level1(Level):
    def __init__(self):
        super(Level, self).__init__()

    #ATH: forritið virkar ekki ef ég nota destructor!!
    #def __del__(self):
    #    print("destructor")

    def startLevel1(self): #HP tónlist bababa
        print("Nú erum við staðsett í Diagon Alley")
        time.sleep(2)
        self.createCharacter()

    def createCharacter(self):
        choice = input("Viltu velja karakter? (já/nei) \n")
        #Búum til tilvik af klasanum chooseChar() (þessum object)
        chooseChar = ChooseChar()
        level2 = Level2()
        if choice == 'já' :
            print ("Velkomin/nn í búningaherbergið")
            time.sleep(2)

            # Veljum character
            character = chooseChar.choice()
            print('Þú ert ' + character.getName())
            time.sleep(2)
            print(character.getDescription())
            time.sleep(2)
            self.happyChoice(character)
        elif choice == 'nei':
            sys.exit()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.createCharacter()
    #fær inn tilvikið af character til að halda áfram að vinna með það
    def happyChoice(self, character):
        level2 = Level2()
        confirm = input('Ertu ánægð/ur með valið? (já/nei)\n')
        if confirm == 'já':
            print("Ertu tilbúin/nn? Nú hefst ferð á vit ævintýranna. \nGakktu nú um borð í lestina sem er við lestarpall 9 3/4 \nsem flytur þig í galdraskólann Hogwarts!\n")
            time.sleep(2)
            self.readyInput()
            print("Velkomin/nn í borð 2! Farðu varlega á vit ævintýranna\n")
            time.sleep(2)
            level2.findWand(character)
        elif confirm == 'nei':
            print("Nú jæja, þá stenduru frammi fyrir ákvörðun...")
            time.sleep(2)
            self.createCharacter()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.happyChoice()

class Level2(Level):
    def __init__(self):
        super(Level, self).__init__()

    #Setjum upp skeiðklukku og leikmaður hefur ákveðinn langa tíma til að finna 3 sprota
    def findWand(self, character):
        print("Þú ert nemandi í galdraskólanum en hinn alræmdi Lávarður Valdimar hefur stolið galdrasprotanum þínum og vina þinna. Þið eruð að verða of sein í próf og þurfið að hafa galdrasprotana með ykkur því annars verðið þið rekin úr skólanum. Markmið þitt er að finna sprotana en það er erfiðara en þú heldur og tíminn en naumur. Lávarður Valdimar birtist ef þú ert of lengi að leita og gerir þig brottrækan úr heimi ævintýranna! Þú þarft að finna 3 sprota á gefnum tíma, en ef þú nærð 2 sprotum færðu annað tækifæri til að spreyta þig en annars ertu gerður brottrækur fyrir fullt og allt!\n")

        time.sleep(3)

        self.readyInput()
        words = "Galdrasprotarnir eru faldir undir einni af eftirfarandi 4 töfraskikkjum. Hafðu í huga að þú getur aðeins fundið 1 sprota í einu.\n"
        print(words)
        time.sleep(2)
        self.chooseWand(character)


        #EF LEIKMAÐUR TAPAR BORÐINU ÞÁ KALLA Á LOOSELEVEL FALLIÐ!!
        #Voldemort birtist ef valin er röng kista
        #Dobby birtist ef valin er rétt kista

    def chooseWand(self, character):
        listi = [1, 2, 3, 4]
        wand = random.randint(1,4)
        listi.remove(wand)
        countWand = 0
        #Setjum af stað skeiðklukku svo leikmaður hafi takmarkaðan tíma
        now = time.time()
        timeLimit = now + 30
        #Gera lykkju sem hættir þegar leikmaður hefur fundið 3 sprota!
        while time.time() < timeLimit:
            choiceWand = int(input("Undir hvaða skikkju er töfrasproti? (1, 2, 3, 4)?\n"))
            if choiceWand == wand:
                countWand = countWand + 1
                print("Vel gert " +  character.getName() + ", þú fannst 1 töfrasprota! Núna ertu komin með " + str(countWand) + " sprota")
                if countWand == 1:
                    print("Nú vantar þig aðeins 2 sprota til viðbótar")
                    listi = [1, 2, 3, 4]
                    wand = random.randint(1,4)
                    listi.remove(wand)

                elif countWand == 2:
                    print("Nú vantar þig aðeins 1 sprota til viðbótar")
                    listi = [1, 2, 3, 4]
                    wand = random.randint(1,4)
                    listi.remove(wand)

                elif countWand == 3:
                    print("Til hamingju, þú hefur fundið alla 3 sprotanna og þar með bjargað þér, " + character.getName() + ", og félögum þínum frá brottrekstri.")
                    self.readyInput()
                    words = "Gakktu hægt um gleðinnar dyr þegar stígur þín fyrstu skref inn í borð 3. " + character.getName() + ", þú ert mætt/ur í lokapróf í Hogwarts..."
                    print(words)
            elif choiceWand == listi[0] or choiceWand == listi[1] or choiceWand == listi[2]:
                print("Því miður, gettu betur! En hafðu hraðar hendur því Lávarður Valdimar nálgast!")
            else:
                sentence = self.inputWrong(1)
                print(sentence)
        

class Level3(Level):
    def __init__(self):
        super(Level, self).__init__()

    #def __del__(self):
        #print("destructor")

#Sækja klasann question úr file questions og tengja hér við eins og í level1

class Level4(Level):
    def __init__(self):
        super(Level, self).__init__()

    def startLevel4(self, character):
        self.readyInput()
        words = "Velkomin í borð númer 4!\n"
        print(words)
        print("Þú hefur nú náð bóklega hluta námsins í Hogwarts og ert kominn skrefinu nær því að útskrifast sem alvöru galdramaður, " + character.getName() + ". Til að ljúka burtfararprófi verður lögð fyrir þig verkleg þraut. Þú átt að nýta þér þá galdra sem þér hafa verið kenndir beita sprotanum þínum í að galdra fram rétt orð. Athugaðu að hér er aðeins notast við enska stafrófið og lágstafi.")
        time.sleep(1)
        self.readyInput()
        self.wordPuzzle()

    def wordPuzzle(self):
        choice = input("Ertu tilbúin í lokaþraut þína í Hogwarts? (já/nei)")
        #if choice = "já":
        #elif choice = "nei":
        #    print("Hér í Hogwarts er ekki liðinn aumingjaskapur svo þú ert hér með gerð/ur brottrækur fyrir fullt og allt!")
        #    time.sleep(5)
        #    sys.exit()
        #else:
        #    sentence = self.inputWrong()
        #    print(sentence)
        #    self.wordPuzzle()
