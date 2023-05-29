import util
import game


def searchBFS():
    g = game.Game()
    q = util.Queue()
    visited = set()

    path = "-"*25 + "BFS SOLUTION" + "-"*25 + "\n"
    path += "Side A" + ' '*30 + "Side B\n"
    path += str(g.sides[0]) + ' '*(35-len(str(g.sides[0]))) + str(g.sides[1]) + '\n'
    q.push((g.sides, 0, path))

    while not q.isEmpty():
        curSides, curBoatSide, curPath = q.pop()
        g.setState(curSides, curBoatSide)

        if g.isWin():
            print(curPath)
            print("Total opened states : " + str(g.openedStates))
            return

        else:
            for successorSides in g.getSuccessors():
                setkey = (util.sideHash(successorSides), (curBoatSide + 1) % 2)
                if setkey not in visited:
                    visited.add(setkey)
                    newPath = curPath + str(successorSides[0]) + ' '*(35-len(str(successorSides[0]))) + str(successorSides[1]) + '\n'
                    q.push((successorSides, (curBoatSide + 1) % 2, newPath))

def searchIDDFS():
    g = game.Game()
    q = util.Stack()
    visited = set()

    maxDepth = 0
    startPath = "-" * 25 + "IDDFS SOLUTION" + "-" * 25 + "\n"
    startPath += "Side A" + ' ' * 30 + "Side B\n"
    startPath += str(g.sides[0]) + ' ' * (35 - len(str(g.sides[0]))) + str(g.sides[1]) + '\n'
    startSides = g.sides

    while True:
        q.push((startSides, 0, startPath, 0))
        maxDepth += 1
        visited.clear()
        while not q.isEmpty():
            curSides, curBoatSide, curPath, curDepth = q.pop()
            g.setState(curSides, curBoatSide)

            if g.isWin():
                print(curPath)
                print("Total opened states : " + str(g.openedStates))
                return

            elif curDepth < maxDepth:
                for successorSides in g.getSuccessors():
                    setkey = (util.sideHash(successorSides), (curBoatSide + 1) % 2)
                    if setkey not in visited:
                        visited.add(setkey)
                        newPath = curPath + str(successorSides[0]) + ' ' * (35 - len(str(successorSides[0]))) + str(
                            successorSides[1]) + '\n'
                        q.push((successorSides, (curBoatSide + 1) % 2, newPath, curDepth+1))


def searchGBFS():
    g = game.Game()
    q = util.PriorityQueue()
    visited = set()

    path = "-" * 25 + "GBFS SOLUTION" + "-" * 25 + "\n"
    path += "Side A" + ' ' * 30 + "Side B\n"
    path += str(g.sides[0]) + ' ' * (35 - len(str(g.sides[0]))) + str(g.sides[1]) + '\n'
    q.push((g.sides, 0, path), heuristicFunction(g.sides, 0))

    while not q.isEmpty():
        curSides, curBoatSide, curPath = q.pop()
        g.setState(curSides, curBoatSide)

        if g.isWin():
            print(curPath)
            print("Total opened states : " + str(g.openedStates))
            return

        else:
            for successorSides in g.getSuccessors():
                setkey = (util.sideHash(successorSides), (curBoatSide + 1) % 2)
                if setkey not in visited:
                    visited.add(setkey)
                    newPath = curPath + str(successorSides[0]) + ' ' * (35 - len(str(successorSides[0]))) + str(
                        successorSides[1]) + '\n'
                    newBoatSide = (curBoatSide + 1) % 2
                    q.push((successorSides, newBoatSide, newPath), heuristicFunction(successorSides, newBoatSide))


def searchAStar():
    g = game.Game()
    q = util.PriorityQueue()
    visited = set()

    path = "-" * 25 + "A* SOLUTION" + "-" * 25 + "\n"
    path += "Side A" + ' ' * 30 + "Side B\n"
    path += str(g.sides[0]) + ' ' * (35 - len(str(g.sides[0]))) + str(g.sides[1]) + '\n'
    q.push((g.sides, 0, path, 0), heuristicFunction(g.sides, 0))

    while not q.isEmpty():
        curSides, curBoatSide, curPath, curDepth = q.pop()
        g.setState(curSides, curBoatSide)

        if g.isWin():
            print(curPath)
            print("Total opened states : " + str(g.openedStates))
            return

        else:
            for successorSides in g.getSuccessors():
                setkey = (util.sideHash(successorSides), (curBoatSide + 1) % 2)
                if setkey not in visited:
                    visited.add(setkey)
                    newPath = curPath + str(successorSides[0]) + ' ' * (35 - len(str(successorSides[0]))) + str(
                        successorSides[1]) + '\n'
                    newBoatSide = (curBoatSide + 1) % 2
                    q.push((successorSides, newBoatSide, newPath, curDepth+1),
                           curDepth + heuristicFunction(successorSides))


def heuristicFunction(sides):
    return len(sides[0])//2

