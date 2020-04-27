# dijkstras without a grid
inf = float('inf')
start = "Noob"
end  = "GodOfCode"

graphs = {}

graphs['Noob'] = {}
graphs['Noob']['Bachelor'] = 4
graphs['Noob']['Bootcamp'] = 1
graphs['Noob']['Self Taught'] = 2

graphs['Bachelor'] = {}
graphs['Bachelor']['Master'] = 2
graphs['Bachelor']['EntryLevel'] = 0.5

graphs['Bootcamp'] = {}
graphs['Bootcamp']['EntryLevel'] = 0.5

graphs['Self Taught'] ={}
graphs['Self Taught']['EntryLevel'] = 2
graphs['Self Taught']['Networking'] = 1

graphs['Networking'] = {}
graphs['Networking']['EntryLevel'] = 0.5

graphs['Master'] = {}
graphs['Master']['PhD'] = 3
graphs['Master']['MidLevel'] = 1

graphs['EntryLevel'] = {}
graphs['EntryLevel']['MidLevel'] = 5

graphs['PhD'] ={}
graphs['PhD']['MidLevel'] = 0
graphs['PhD']['Expert'] = 2
graphs['PhD']['PostDoc'] = 2

graphs['MidLevel'] = {}
graphs['MidLevel']['Expert'] = 5

graphs['PostDoc'] = {}
graphs['PostDoc']['Academic'] = 20

graphs['Expert'] = {}
graphs['Expert']['GodOfCode'] = 5

graphs['Academic'] = {}
graphs['Academic']['GodOfCode'] = inf

graphs['GodOfCode'] = {}

parents ={}
costs = {}

for node in graphs:
    costs[node]= inf
    parents[node]={}

costs[start]=0

def find_cheapest_node(costs,openList):
    lowestCost = inf
    cheapestNode = ''
    for node in costs:
        if node in openList and costs[node] <= lowestCost:
            lowestCost = costs[node]
            cheapestNode = node
    return cheapestNode
                   
if  __name__ == '__main__':
    openList = [node for node in costs]
    node = find_cheapest_node(costs, openList)
    while openList:
        print(f'Open: {openList}')
        cost = costs[node]
        child_cost = graphs[node]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                parents[c] = node
        openList.remove(node)
        node = find_cheapest_node(costs,openList)

print(f'Costs: {costs}')
print(f"The cost to go from {start} to {end} is {costs[end]}!")

if costs[end] < inf:
    path  = [end]
    while start not in path:
        path.append(parents[path[-1]])
    
    print(f'The shortest path is {path[::-1]}')
else:
    print('A path could not be found')
        
    
