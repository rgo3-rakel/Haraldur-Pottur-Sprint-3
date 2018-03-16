import time
import sys
import random
#Importa klösum úr öðrum file-num
from character import Character
from character import ChooseChar
#from questions import question

class Level:

    #Búa til breytu sem heitir Victory = False
    def __init__(self):
        pass

    def beginning(self): #Dumbledore talar
        print("Velkomin/nn í leikinn svaðilfari!")
        #setja mynd inn
        time.sleep(1)
        print("")
        level1 = Level1()
        level1.startLevel()

    def looseLevel(self):
        print("Nú hefur þú brugðist félögum þínum í Hogwarts, þú ert komin/nn aftur á byrjunarreit\n")
        keepGoing = input("Viltu reyna aftur við leikinn? (já/nei) ")
        if keepGoing == 'já':
            self.beginning()
        elif keepGoing == 'nei':
            sys.exit()
        else:
            print("Þú þekkir reglurnar! Það má aðeins velja annan hvorn svörmöguleikann: já/nei\n")
            self.looseLevel()

class Level1(Level):
    def __init__(self):
        super(Level, self).__init__()


    def startLevel(self): #HP tónlist bababa
        print("Nú erum við staðsett í Diagon Alley")
        time.sleep(2)
        self.createCharacter()

    def createCharacter(self):
        choice = input("Viltu velja karakter? (já/nei) ")
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
            time.sleep(4)
            confirm = input('Ertu ánægð/ur með valið? (já/nei)\n')
            if confirm == 'já':
                print("Ertu tilbúin/nn? Nú hefst ferð á vit ævintýranna. \nGakktu nú um borð í lestina sem er við lestarpall 9 3/4 \nsem flytur þig í galdraskólann Hogwarts!\n")
                time.sleep(4)
                level2.readyInput()
                print("Velkomin/nn í borð 2! Farðu varlega á vit ævintýranna\n")
                time.sleep(2)
                level2.findWand()
            elif confirm == 'nei':
                print("Nú jæja, þá stenduru frammi fyrir ákvörðun...")
                time.sleep(2)
                self.createCharacter()
        elif choice == 'nei':
            sys.exit()
        else:
            print("Heyrðu nú mig! Það má aðeins velja já/nei, svo reyndu aftur")
            self.createCharacter()


#Tengja saman level1 og level2 í sprint 3
#Ath level2 ekki tilbúið en verður gert í næsta sprint!
class Level2(Level):
    def __init__(self):
        super(Level, self).__init__()

    def readyInput(self):
        words = ""
        ready = input("Ýttu á bilstöng þegar þú ert tilbúin/nn að halda áfram:\n")
        if ready == " ":
            return words
        else:
            print("Vinsamlegast ýttu á bilstöng til að halda áfram:\n")
            time.sleep(2)
            self.readyInput()
    #Setjum upp skeiðklukku og leikmaður hefur ákveðinn langa tíma til að finna 3 sprota
    def findWand(self):
        print("Þú ert nemandi í galdraskólanum en hinn alræmdi Lávarður Valdimar hefur stolið galdrasprotanum þínum og vina þinna. Þið eruð að verða of sein í próf og þurfið að hafa galdrasprotana með ykkur því annars verðið þið rekin úr skólanum. Markmið þitt er að finna sprotana en það er erfiðara en þú heldur og tíminn en naumur. Lávarður Valdimar birtist ef þú ert of lengi að leita og gerir þig brottrækan úr heimi ævintýranna! Þú þarft að finna 3 sprota á gefnum tíma, en ef þú nærð 2 sprotum færðu annað tækifæri til að spreyta þig en annars ertu gerður brottrækur fyrir fullt og allt!\n")

        time.sleep(5)

        self.readyInput()
        words = "Galdrasprotarnir eru faldir undir einni af eftirfarandi 4 töfraskikkjum. Hafðu í huga að þú getur aðeins fundið 1 sprota í einu.\n"
        print(words)
        time.sleep(2)

        #Setjum af stað skeiðklukku svo leikmaður hafi takmarkaðan tíma
        now = time.time()
        timeLimit = now + 40

        while time.time() < timeLimit:
            self.chooseWand()


        #Voldemort birtist ef valin er röng kista
        #Dobby birtist ef valin er rétt kista

        print("Þú náðir galdrasprotanum og býrð nú yfir galdramætti")

    def chooseWand(self):
        chooseChar = ChooseChar()
        character = chooseChar.choice()

        listi = [1, 2, 3, 4]
        wand = random.randint(1,4)
        countWand = 0
        remove.listi(wand)

        choiceWand = input("Undir hvaða skikkju er töfrasproti? (1, 2, 3, 4)?")
        #Gera lykkju sem hættir þegar leikmaður hefur fundið 3 sprota!
        while countWand < 4:
            if(choiceWand == wand):
                countWand = countWand + 1
                print("Vel gert" +  character.getname() + ", þú fannst 1 töfrasprota! Núna ertu komin með" + countWand + "spota")
                if countWand == 1:
                    print("Nú vantar þig aðeins 2 sprota til viðbótar")
                elif countWand == 2:
                    print("Nú vantar þig aðeins 1 sprota til viðbótar")
                elif countWand == 3:
                    print("Til hamingju, þú hefur fundið alla 3 sprotanna og þar með bjargað þér, " + character.getname() + ", og félögum þínum frá brottreksri.")
                    self.readyInput()
                    words = "Gakktu hægt um gleðinnar dyr þegar stígur þín fyrstu skref inn í borð 3. " + character.getname() + " er mætt/ur í lokapróf í Hogwarts..."
                    print(words)
            elif choiceWand == listi[0] or choiceWand == listi[1] or choiceWand == listi[2]:
                print("Því miður, gettu betur! En hafðu hraðar hendur því Lávarður Valdimar nálgast!")
            else:
                print("Nei heyrðu nú mig, þú veist reglurnar... Aðeins velja einn af eftirfarandi svarmöguleikum (1, 2, 3, 4)")
                time.sleep(2)
                self.chooseWand()

class Level3(Level):
    def __init__(self):
        super(Level, self).__init__()
#Sækja klasann question úr file questions og tengja hér við eins og í level1



class Level4(Level):
    def __init__(self):
        super(Level, self).__init__
