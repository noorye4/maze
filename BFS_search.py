#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import random
from get_Adjacent_Node import *
class Position:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def __repr__(self):
        return repr((self.X,self.Y))
    def get_x(self):
        return self.X
    def get_y(self):
        return self.Y

class Node:
    def __init__(self,node,child_node):
        self.node = node
        self.child_node = child_node
    def __repr__(self):
        return repr((self.node,self.child_node))
    def get_node(self):
        return self.node
    def get_child_node(self):
        return self.child_node

class Path_Inf():
    def __init__(self,path,node_li):
        self.path = path
        self.node_li = node_li
    def __repr__(self):
        return repr((self.path,self.node_li))
    def get_path(self):
        return self.path
    def get_node_li(self):
        return self.node_li

def search_down(child_node, end_x, end_y):
    find = False
    for i in child_node:
        ch_x = i.get_x()
        ch_y = i.get_y()
        if end_x == ch_x and end_y == ch_y:
            print "search down"
            find = True
            break
    return find

def add_child_node(child_node,queue_li):
    for i in child_node:
        queue_li.insert(0,i)
    return queue_li

def BFS_search(wall_li,rows,cols,start_x,start_y,end_x,end_y):
    step = 0
    queue_li = []
    visited_li = []
    path = []
    start_node = Position(start_x,start_y)
    print "start node " + repr(start_node)
    visited_li.append(start_node)
    print "visited " + repr(visited_li)
    child_node = get_Adj_Node(wall_li, start_node, rows, cols, visited_li)
    print "adjacent node " + repr(child_node)
    queue_li = add_child_node(child_node,queue_li)
    print "queue " + repr(queue_li)
    path.append(start_node)
    print "="*30
    find = False
    while True:
        step += 1
        #next_node = random.choice(queue_li)
        next_node = queue_li[0]
        queue_li.remove(next_node)
        path.append(next_node)
        print "next node " + repr(next_node)
        visited_li.append(next_node)
        print "visited " + repr(visited_li)
        child_node = get_Adj_Node(wall_li, start_node, rows, cols, visited_li)
        print "adjacent node " + repr(child_node)
        find = search_down(child_node, end_x, end_y)
        if find:break
        else:
            queue_li = add_child_node(child_node,queue_li)
            print "queue " + repr(queue_li)
    path_inf = Path_Inf(path,queue_li)
    print "step " + repr(step)
    return path_inf