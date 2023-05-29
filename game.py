from itertools import combinations


class Game:
    """
    A game State is determined by 3 lists.
    sideA represents the people in side A
    sideB represents the people in side B
    boat[0] represents the side that the boat is on
    boat[1-2] are the places for people on the boat
    """


    def __init__(self):
        self.sides = (['C', 'C', 'C', 'M', 'M', 'M'], [])
        self.boatSide = 0
        self.openedStates = 0

    def isWin(self):
        return len(self.sides[0]) == 0

    def getSuccessors(self):

        successors = []
        to_boat = list(combinations(self.sides[self.boatSide], 1)) + list(combinations(self.sides[self.boatSide], 2))

        for option in to_boat:
            fromSide = self.sides[self.boatSide].copy()
            for person in option:
                fromSide.remove(person)
            toSide = self.sides[(self.boatSide+1) % 2] + list(option)
            if self.isLegal(fromSide, toSide):
                if self.boatSide == 0:
                    sides = (fromSide, toSide)
                else:
                    sides = (toSide, fromSide)
                successors.append(sides)
        self.openedStates += 1
        print(self.sides)
        return successors

    def isLegal(self, a, b):
        aLegal = a.count('M') == 0 or a.count('C') <= a.count('M')
        bLegal = b.count('M') == 0 or b.count('C') <= b.count('M')
        return aLegal and bLegal

    def setState(self, sides, boatSide):
        self.sides = sides
        self.boatSide = boatSide