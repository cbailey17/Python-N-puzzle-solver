'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue 
from explored import Explored

        
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    #Initial tileboard for testing
    tb = problem.initial   
    #Create first node and test if node passes goal
    node0 = Node(problem, tb)
    if problem.goal_test(node0.state) == True:
            return node0.solution()   
    #define frontier set as priority queue and the explored set
    pq = PriorityQueue()
    pq.append(node0)
    new_nodes = []
    exploredSet = Explored()    
    frontier = Explored()
    frontier.add(node0)
    nodesExpanded = 0
    
    #Expand the search tree until the goal state is found
    found = False
    #time.sleep(2)
    while (not found):   
        #Check if the frontier is empty signifying failure
        if pq.__len__() == 0:
            print("No solution found")
            break   
        #Take the next node from the priority queue and add it to explored set
        node = pq.pop()  
        exploredSet.add(node)
        #Check if the goal state has been found
        if problem.goal_test(node.state) == True: 
            path = node.path()
            solution = node.solution()
            steps = len(path)-1
            found = True
            if verbose == True:
                verboseFunc(solution, steps, tb, path)
        else:
            #Expand the search tree and check if the nodes have been explored
            new_nodes = node.expand(problem)    
        for j in range(len(new_nodes)):
            if exploredSet.exists(new_nodes[j].state) or frontier.exists(new_nodes[j].state):
                continue
            else:
                #Add one to the number of nodes explored
                nodesExpanded += 1
                pq.append(new_nodes[j]) #Add the nodes to the priority queue
                frontier.add(new_nodes[j]) #use hashed set to decrease lookup time
                if debug == True:
                    debugFunc(debug, pq)
    return (steps, nodesExpanded);
            
#Verbose setting will display the actions taken and states to solution
def verboseFunc(solution, steps, tb, path):
    if len(solution) == 0:
        print("No solution found")
    print("\nSolution in", steps, "moves")
    print("Initial state")
    print(tb)
    for i in range(1, steps+1):
        print("Move", i, "- ", solution[i-1])
        print(path[i].state)

#debug function for debugging the graph search and printing nodes       
def debugFunc(debug, pq):
    if debug == True:
        print("Now printing nodes from the priority queue")
        print_nodes(pq)
        
        
        
        
    

    
    
    
    
    
    
