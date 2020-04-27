import pygame
# dijkstras without a grid
inf = float('inf')

start = (0,0)
end  = (49,49)

graphs = {}

screen = 500

width = 50

columns = int(screen/width)

for col in range(width+1):
    for row in range(width+1):
        graphs[(row,col)]={}
        if row < width:
            graphs[(row,col)][(row+1,col)] = 1
        if row < width and col > 0:
            graphs[(row,col)][(row+1,col-1)] = 2**0.5 
        if col > 0:
            graphs[(row,col)][(row,col-1)] = 1
        if col > 0 and row > 0:
            graphs[(row,col)][(row-1,col-1)] = 2**0.5
        if row > 0:
            graphs[(row,col)][(row-1,col)] = 1
        if row  and col < width:
            graphs[(row,col)][(row-1,col+1)] = 2**0.5
        if col < width:
            graphs[(row,col)][(row,col+1)] = 1
        if row < width and col <width:
            graphs[(row,col)][(row+1,col+1)] = 2**0.5

parents ={}
costs = {}

for node in graphs:
    costs[node]= inf
    parents[node]={}

costs[start]=0

def draw_grid(window,screen,field):
    for x in range(0,width,field):
        pygame.draw.line(window,(0,0,0),(x,0),(x,screen))
        pygame.draw.line(window,(0,0,0),(0,x),(screen,x))
        
def draw_list(window,dlist,columns,color):
    for x in dlist:
        pygame.draw.rect(window,color,(x[0]*columns,x[1]*columns,columns,columns))
        
    
def find_cheapest_node(costs,openList):
    lowestCost = inf
    cheapestNode = ''
    for node in costs:
        if node in openList and costs[node] <= lowestCost:
            lowestCost = costs[node]
            cheapestNode = node
    return cheapestNode
                   
if  __name__ == '__main__':
       
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((screen,screen))
    pygame.display.set_caption("Pathfinder")
    window.fill((255,255,255))
    
    openList = [node for node in costs]
    closedList = []
    node = find_cheapest_node(costs, openList)
    
    while node != end :
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    
        cost = costs[node]
        child_cost = graphs[node]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                parents[c] = node
        openList.remove(node)
        closedList.append(node)
        node = find_cheapest_node(costs,openList)
        window.fill((255,255,255))
        draw_grid(window,screen, columns)
        draw_list(window,openList,columns,(255,0,0))
        draw_list(window,closedList,columns,(0,255,0))
        pygame.display.update() 
        
if costs[end] < inf:
    path  = [end]
    while start not in path:
        path.append(parents[path[-1]])

draw_list(window,path,columns,(0,0,255))
pygame.display.update()  
