'''
driver for graph search problem
for'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


class Timer:
    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """  
    def __init__(self):
        "Timer - Start a timer"
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        "elapsed_s - Seconds elapsed since start (wall clock time)"
        return time.time() - self.start

    def elapsed_min(self):
        "elapsed_min - Minutes elapsed since start (wall clock time)"
        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min
   
    
def driver() :
    
    #Define number of problems and get user input for search algorithm
    num_problems = 32
    num_steps = [[],[],[]]
    num_nodes = [[],[],[]]
    time = [[],[],[]]
    
    #Begin timer and define problem state. Then begin BFS search    
    for i in range(1, num_problems):
        np_BFS = NPuzzle(8, g = BreadthFirst.g, h = BreadthFirst.h)
        if  (graph_search(np_BFS)): 
            t = Timer()
            steps, nodes = graph_search(np_BFS)
            time[0].append(t.elapsed_s())
            num_steps[0].append(steps)
            num_nodes[0].append(nodes) 
    #Display results        
    print("\nBreadth First Search Results")
    print("Time(s) (AVG): ", mean(time[0]))
    print("Time(s) (STD): ", stdev(time[0]))
    print("Nodes expanded (AVG): ", mean(num_nodes[0]))
    print("Nodes expanded (STD): ", stdev(num_nodes[0]))
    print("Steps taken (AVG): ", mean(num_steps[0]))
    print("Steps taken (STD): ", stdev(num_steps[0]), "\n")
    
    
   #Begin timer and conduct DFS search and print results
    for i in range(1, num_problems):  
        np_DFS = NPuzzle(8, g = DepthFirst.h, h = DepthFirst.g)
        if  (graph_search(np_DFS)): 
            t2 = Timer()
            steps, nodes = graph_search(np_DFS)
            time[1].append(t2.elapsed_s())
            num_steps[1].append(steps)
            num_nodes[1].append(nodes)  
    #Display results    
    print("\nDepth First Search Results for 31 Searches")
    print("Time(s) (AVG): ", mean(time[1]))
    print("Time(s) (STD): ", stdev(time[1]))
    print("Nodes expanded (AVG): ", mean(num_nodes[1]))
    print("Nodes expanded (STD): ", stdev(num_nodes[1]))
    print("Steps taken (AVG): ", mean(num_steps[1]))
    print("Steps taken (STD): ", stdev(num_steps[1]), "\n")
    
    
    #Begin timer and conduct A* search and print results
    for i in range(1, num_problems):
        np_A = NPuzzle(8, g = Manhattan.g, h = Manhattan.h)
        if  (graph_search(np_A)): 
            t3 = Timer()
            steps, nodes = graph_search(np_A)
            time[2].append(t3.elapsed_s())
            num_steps[2].append(steps)
            num_nodes[2].append(nodes) 
    #Display results    
    print("\nA* Search Results For 31 Searches")
    print("Time(s) (AVG): ", mean(time[2]))
    print("Time(s) (STD): ", stdev(time[2]))
    print("Nodes expanded (AVG): ", mean(num_nodes[2]))
    print("Nodes expanded (AVG): ", stdev(num_nodes[2]))
    print("Steps taken (AVG): ", mean(num_steps[2]))
    print("Steps taken (STD): ", stdev(num_steps[2])) 
    
   
    
if __name__ == '__main__':
    driver()



