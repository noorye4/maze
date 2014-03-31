    #!/usr/bin/env python
    #-*- encoding: utf-8 -*-
import random

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
    def __init__(self,node,child_node):
        self.node = node
        self.child_node = child_node
    def __repr__(self): 
        return repr((self.node,self.child_node))
    def get_node(self):
        return self.node
    def get_child_node(self):
        return self.child_node
    
#----------------------------------------------------
def get_Adj_Node(wall_li,cur_node,rows,cols,visited_li):
    tmp_node = []
    cur_x = cur_node.get_X()
    cur_y = cur_node.get_Y()
    if not(cur_x + 1 > rows-1):
        cur_x += 1
        cur_node = Position(cur_x,cur_y)
        tmp_node.append(cur_node)
        cur_x -= 1
    if not(cur_x - 1 < 0):
        cur_x -= 1
        cur_node = Position(cur_x,cur_y)
        tmp_node.append(cur_node)
        cur_x += 1
    if not(cur_y + 1 > cols-1):
        cur_y += 1
        cur_node = Position(cur_x,cur_y)
        tmp_node.append(cur_node)
        cur_y -= 1
    if not(cur_y - 1 < 0):
        cur_y -= 1
        cur_node = Position(cur_x,cur_y)
        tmp_node.append(cur_node)
        cur_y += 1
    adjacent_node = []
    for i in tmp_node:
        ok = True
        t_x = i.get_X()
        t_y = i.get_Y()
        for j in wall_li:
            w_x = j.get_X()
            w_y = j.get_Y()
            if t_x == w_x and t_y == w_y:ok = False
        if ok :adjacent_node.append(i)
    for j in adjacent_node:
        rp = False
        m_x = j.get_X() 
        m_y = j.get_Y()
        for i in visited_li:
            u_x = i.get_X()
            u_y = i.get_Y()
            if m_x == u_x and m_y == u_y:
                rp = True
        if rp :adjacent_node.remove(j)
    return adjacent_node
