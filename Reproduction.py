from random import *

## POPULATION SIMULATOR

populationSize = int(500)
reproductionFactor = int(populationSize / 10)    ##  number of death and birth (=) in each generation
advantage = 3     ## strenght advantage for Alpha+


########################################
class Individual:
    " main class for all the individuals in the population"

    def __init__(self, name, race, strenght):
        self.name = name
        self.race = race
        self.strenght = strenght
   
    def displayIdentity(self):
        print("name:", self.name)
        print("race:", self.race)
        print("strength:", self.strenght)
########################################



def createNewPopulation():   ## returns a list
    global populationList
    populationList = []
    nbr=1
    while nbr <= populationSize:
        indName = "ind" + str(nbr)
        strenght = randrange(10,21)                      ## min and max strenght
        alpha = randrange(1,3)
        if alpha == 1:
            strenght += advantage                               ## ind is Alpha+ (has more strenght)
        populationList.append((indName, alpha, strenght))             ## alpha=1: Alpha+   /// alpha=2: Alpha-        
        nbr += 1
    return populationList


def sortIndividuals(lst):   ## returns a list
    global populationList
    sortedList = []
    for n in range(len(lst)):
        maxStrenght = 0
        lastInd = lst[0]
        for i in range(len(lst)):
            if lst[i][2] > maxStrenght:
                maxStrenght = lst[i][2]
                lastInd = lst[i]
        lst.remove(lastInd)
        sortedList.append(lastInd)
    populationList = sortedList
    return populationList


def newGeneration(lst):    ## returns a list    [45:]
    global populationList
    totalSize = (populationSize - reproductionFactor) + 1
    del lst[totalSize:]
    nbr=totalSize
    while nbr <= populationSize:
        indName = "ind" + str(nbr)
        strenght = randrange(10,21)                      ## min and max strenght
        alpha = randrange(1,3)
        if alpha == 1:
            strenght += advantage                               ## ind is Alpha+ (has more strenght)
        lst.append((indName, alpha, strenght))                  ## alpha=1: Alpha+   /// alpha=2: Alpha-        
        nbr += 1
    populationList = lst
    return populationList


def drawResults(lst):
    global populationList
    nbrAlphaPos = 0
    nbrAlphaNeg = 0
    strenghtAvg = 0
    for i in range(len(lst)):
        if lst[i][1] == 1:
            nbrAlphaPos += 1
        else:
            nbrAlphaNeg += 1
    for i in range(len(lst)):
        strenghtAvg += int(lst[i][2])
    strenghtAvg = (strenghtAvg/len(lst))
    print("Number of Alpha+ individuals: ", nbrAlphaPos)
    print("Number of Alpha- individuals: ", nbrAlphaNeg)
    print("Strenght average: ", int(strenghtAvg))


def mainProgram(nbrGen):
    global populationList
    createNewPopulation()
    while nbrGen > 0:
        sortIndividuals(populationList)
        newGeneration(populationList)
        nbrGen -= 1
    drawResults(populationList)
    

mainProgram(500)





