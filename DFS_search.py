#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import random
from get_Adjacent_Node import get_Adj_Node

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
    def __init__(self,parent_node,child_node):
        self.node = parent_node
        self.child_node = child_node
    def __repr__(self):
        return repr((self.parent_node,self.child_node))
    def get_Parent_Node(self):
        return self.parent_node
    def get_Child_Node(self):
        return self.child_node

class Path_Inf():
    def __init__(self,path,node_li,visited_li):
        self.path = path
        self.node_li = node_li
        self.visited_li = visited_li
    def __repr__(self):
        return repr((self.path,self.node_li,self.visited_li))
    def get_path(self):
        return self.path
    def get_node_li(self):
        return self.node_li
    def get_best_path(self):
        return self.visited_li
#----------------------------------------------------
def DFS_search(wall_li,rows,cols,start_x,start_y,end_x,end_y):
    #node initial
    step = 0
    print  step
    path = []
    node_li = []
    visited_li = []
    init_node = Position(start_x,start_y)
    print "節點 " + repr(init_node)
    init_child_node = get_Adj_Node(wall_li,init_node,rows,cols,visited_li)
    visited_li.append(init_node)
    path.append(init_node)
    next_node = random.choice(init_child_node)
    print "next node " + repr(next_node)
    init_child_node.remove(next_node)
    print "子節點 " + repr(init_child_node)
    node = Node(init_node,init_child_node)
    node_li.append(node)
    print "節點狀態 " + repr(node)
    print "-----------------------------"
    while 1:
        step += 1
        print "節點 " + repr(next_node)
        next_child_node = get_Adj_Node(wall_li,next_node,rows,cols,visited_li)
        if next_child_node:
            visited_li.append(next_node)
            path.append(next_node)
            next_node = random.choice(next_child_node)
            next_child_node.remove(next_node)
            print "子節點 " + repr(next_child_node)
            print "next node " + repr(next_node)
            node = Node(next_node,next_child_node)
            node_li.append(node)
            print "節點狀態 " + repr(node)
            print "-----------------------------"
        else:
            path.append(next_node)
            print "死路" + repr(next_node)
            
            for i in node_li[::-1]:
                node = i.get_Parent_Node()
                child_node = i.get_Child_Node()
                print "node " + repr(node)
                print "child_node " + repr(child_node)
                if child_node:
                    print "有子節點" + repr(child_node)
                    next_node = random.choice(child_node)
                    path.append(next_node)
                    child_node.remove(next_node)
                    break
                else:
                    print "無子節點"
                    node_li.remove(i)
        n_x = next_node.get_x()
        n_y = next_node.get_y()
        if n_x == end_x and n_y == end_y:
            print "search down..."
            break
    path_inf = Path_Inf(path,node_li,visited_li)
    print "路經" + repr(path)
    print "節點鍊錶" + repr(node_li)
    print "step " + repr(step)
    return path_inf
    
    