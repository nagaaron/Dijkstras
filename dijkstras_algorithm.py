# Dijkstras  Algorithm

class Node:
    
    def __init__(self, pos ,parent = None,):
        self.pos = pos
        self.cost  = float('inf')
        self.parent = parent
        
def dijkstra():
    
    grid = [(col,row) for row in range(0,5) for col in range(0,5)]
    
    startNode = Node((0,0))
    startNode.cost = 0
    endNode = Node((4,4))
    
    closedList = []
    openList =[]
    openList.append(startNode)
    
    while True:
    
        # find node in openList with smallest cost set it to currentNode
        currentNode = openList[0]
        currentIndex = 0
        for index,node in enumerate(openList):
            if node.cost <= currentNode.cost:
                currentIndex = index
                currentNode = node
        # stop if currentNode is endNode
        if currentNode.pos == endNode.pos:
            
            goalNode = currentNode
            path  = [goalNode]
            while goalNode.pos != startNode.pos:
                
                neighbors =[]
                currentCol = goalNode.pos[1]
                currentRow = goalNode.pos[0]
                
                
                for col in range(-1,2):
                    for row in range(-1,2):
                        if col !=0 and row != 0:
                            neighborRow = row +currentRow
                            neighborCol = col + currentCol
                            neighbors.append(neighborCol,neighborRow)
                currentCost = goalNode.cost
                for neighbor in neighbors:          
                    for openNode in openList:
                        if openNode.pos == neighbor.pos:
                            if openNode.cost < currenCost:
                                goalNode = openNode
                
                path.append(goalNode)
            return path
        # find all neighbors of currentNode
        neighbors =[]
        currentCol = currentNode.pos[1]
        currentRow = currentNode.pos[0]
        for col in range(-1,2):
            for row in range(-1,2):
                if col !=0 and row != 0:
                    neighborRow = row +currentRow
                    neighborCol = col + currentCol
                    if (neighborCol,neighborRow) in grid:
                        neighbors.append(Node((currentRow,currentCol)))
        
        # calculate costs for all neighbors
        for neighbor in neighbors:
            additionalcost = ((neighbor.pos[0] - currentNode.pos[0])**2+(neighbor.pos[1]- currentNode.pos[1])**2)**0.5
            neighbor.cost = currentNode.cost + additionalcost

        # if costs of neighbor are smaller
        for neighbor in neighbors:
            inopen = False
            for openNode in openList:
                if neighbor.pos == openNode.pos:
                    if neighbor.cost < openNode.cost:
                        openNode.cost = neighbor.cost
                        inopen = True
                        break
            if inopen == False:
                openList.append(neighbor)
        
print(dijkstra())