#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from get_Adjacent_Node import get_Adj_Node

class Position:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def __repr__(self):
        return repr((self.X,self.Y))
    def get_X(self):
        return self.X
    def get_Y(self):
        return self.Y

class Node:
    def __init__(self,parent_node,child_node):
        self.parent_node = parent_node
        self.child_node = child_node
    def __repr__(self):
        return repr((self.parent_node,self.child_node))
    def get_Parent_Node(self):
        return self.parent_node
    def get_Child_Node(self):
        return self.child_node
    
class Individual:
    def __init__(self,pos,fitness):
        self.pos = pos
        self.fitness = fitness
    def __repr__(self):
        return repr((self.pos,self.fitness))
    def get_Pos(self):
        return self.pos
    def get_Fitness(self):
        return self.fitness

def get_Manhattan_Distance(cur_pos,end_pos):
    cur_x = cur_pos.get_X()
    cur_y = cur_pos.get_Y()
    end_x = end_pos.get_X()
    end_y = end_pos.get_Y()
    distance = ( abs(end_y - cur_y) + abs(end_x - cur_x) )
    return distance

def get_Optional_Pos(adj_node_li,close_li,cur_pos,end_pos):
    open_li = []
    for i in adj_node_li:
        fitness = get_Fitness(close_li,i,end_pos)
        individual = Individual(i,fitness)
        open_li.append(individual)
    return open_li
def get_Fitness(close_li,cur_pos,end_pos):
    G = len(close_li)
    H = get_Manhattan_Distance(cur_pos,end_pos)
    F = G + H
    #F = H
    return F

def A_STAR_search(wall_li,start_x,start_y,end_x,end_y,rows,cols,):
    file=open('fitness_data.txt','w')
    step = 0
    path = []
    node_li = []
    close_li = []
    init_node = Position(start_x,start_y)
    end_node = Position(end_x,end_y)
    close_li.append(init_node)
    path.append(init_node)
    print "init_node " + repr(init_node)
    print "CLOSE " + repr(close_li)
    adj_node_li = get_Adj_Node(wall_li,init_node,rows,cols,close_li)
    print "adjacent node " + repr(adj_node_li)
    open_li = get_Optional_Pos(adj_node_li,close_li,init_node,end_node)
    print "OPEN" + repr(open_li)
    open_li = sorted(open_li, key=lambda individual: individual.fitness)
    node = Node(init_node,open_li)
    node_li.append(node)
    print "Node" + repr(node)
    print "="*30
    
    while True:
        step += 1
        if open_li:
            individual = open_li[0]
            fitness = individual.get_Fitness()
            file.write(repr(fitness) + "\n")
            open_li.remove(individual)
            next_node = individual.get_Pos()
            print "next_node " + repr(next_node)
            close_li.append(next_node)
            path.append(next_node)
            print "CLOSE " + repr(close_li)
            adj_node_li = get_Adj_Node(wall_li,next_node,rows,cols,close_li)
            print "adjacent node " + repr(adj_node_li)
            open_li = get_Optional_Pos(adj_node_li,close_li,next_node,end_node)
            print "OPEN" + repr(open_li)
            open_li = sorted(open_li, key=lambda individual:individual.fitness)
            node = Node(next_node,open_li)
            node_li.append(node)
            print "="*30
        else:
            while True:
                print "dead road"
                jmp = False
                for i in node_li[::-1]:
                    child_node = i.get_Child_Node()
                    if child_node:
                        parent_node = i.get_Parent_Node()
                        path.append(parent_node)
                        open_li = child_node
                        print open_li
                        jmp = True
                    else:
                        next_node = close_li.pop()
                        path.append(next_node)
                        node_li.remove(i)
                    if jmp:break
                if jmp:break
        next_x = next_node.get_X()
        next_y = next_node.get_Y()
        if next_x == end_x and next_y == end_y:
            print "search down..."
            print "total step: " + repr(step)
            file.close()
            break
    return path
            
