class question:
    def __init__(self):
        self._description = '' #Setjum sem private breytu
        self._name = ''

    def setImage():pass

    def getDescription(self):
        return self._description

    def setDescription(self, des):
        self._description = des

    def quitGame():pass
    #Set nafnið með getName
    def getName(self):
        return self._name
    #Sæki nafnið með setName
    def setName(self, name):
        self._name = name

    def choice(): pass
class questionPack1(question):
    def __init__(self):
        #Setja inn hvort leikmaður vilji breyta um karakter og þannig tengja við borð 1
        #Spurningar komnar inn á docs!
        #Setja inn spurningar og svarmöguleika


class questionPack2(question):
    def __init__(self):
        self.setName('Hermína Guðmundsdóttir\n')
        des = "Þú hefur valið bráðkláran mugga sem má líkja við gangandi orðabók. Þegar kemur að erfiðum tímum er ávallt hægt að stóla á visku hennar til þess að sigrast á öllum áskorunum.\n"
        self.setDescription(des)
        super(Character, self).__init__()

class questionPack3(question):
    def __init__(self):
        self.setName('Guðrún Vilmundardóttir\n')
        des = "Þú hefur valið einn úr Vilmundarættinni! Guðrún er kraftmikil og öflug galdrakona sem ræður við erfiða galdra og er ein af bestu ,,quidditch” spilurum Hogwarts.\n"
        self.setDescription(des)
        super(Character, self).__init__()

class questionPack3(question):
    def __init__(self):
        self.setName('Rúnar Vilmundarson\n')
        des = "Þú kemur frá stórri galdraætt sem er hvað þekktust fyrir sitt eldrauða hár. Alltaf er hægt að treysta á skopskyn og hæfileika hans að hugsa út fyrir kassann í erfiðum aðstæðum.\n"
        self.setDescription(des)
        super(Character, self).__init__()
