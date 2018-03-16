import time
import sys
#importa klasanum Character úr file-num character
from character import Character
from character import ChooseChar

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
        print("Nú hefur þú brugðist félögum þínum í Hogwarts, þú ert komin/nn aftur á byrjunarreit")
        keepGoing = input("Viltu reyna aftur við leikinn? (já/nei) ")
        if keepGoing == 'já':
            self.beginning()
        elif keepGoing == 'nei':
            sys.exit()


class Level1(Level):
    def __init__(self):
        super(Level, self).__init__()


    def startLevel(self): #HP tónlist bababa
        print("Nú erum við staðsett í Diagon Alley")
        time.sleep(2)
        self.createCharacter()

    def createCharacter(self):
        choice = input("Viltu velja karakter? (já/nei) ")
        if choice == 'já' :
            print ("Velkomin/nn í búningaherbergið")
            time.sleep(2)
            #Búum til tilvik af klasanum chooseChar() (þessum object)
            chooseChar = ChooseChar()
            # Veljum character
            character = chooseChar.choice()
            print('Þú ert ' + character.getName())
            time.sleep(1)
            print(character.getDescription())
            time.sleep(2)
            confirm = input('Ertu ánægð/ur með valið? (já/nei)\n')
            if confirm == 'já':
                print("Ertu tilbúin/nn? Nú hefst ferð á vit ævintýranna. \nGakktu nú um borð í lestina sem er við lestarpall 9 3/4 \nsem flytur þig í galdraskólann Hogwarts!!!")
            elif confirm == 'nei':
                self.createCharacter()
        elif choice == 'nei':
            sys.exit()

#Ath level2 ekki tilbúið en verður gert í næsta sprint!
class Level2(Level):
    def __init__(self):
        super(Level, self).__init__()

    def level2(self):
        print("Þú ert nemandi í galdraskólanum en týndir sprotanum þínum. Þú ert að vera of seinn í próf og þarft að hafa galdrasprotann með þér því annars verður þú rekinn úr skólanum. Að ná sprotanum er erfiðara en þú heldur því ýmsar hindranir eru á leiðinni.")
        #Voldemort birtist ef valin er röng kista
        #Dobby birtist ef valin er rétt kista

        print("Þú náðir galdrasprotanum og býrð nú yfir galdramætti")

        #print("Þú hefur nú fengið inngöngu í galdraskólann Hogwarts")
