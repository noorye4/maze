#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#=============================================================================#
# Name        : prim_maze.py                                                  #
# Autor       : Nooryes                                                       #
# Date        : march, 17 2014                                                #
# Description : Function definitions for get excavation path in maze          #
#=============================================================================#
import random
import pickle

#----------------------------------------------------
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
    
#----------------------------------------------------
def filter_outside(pos,rows,cols):
    outside_li = []
    x = pos.get_X()
    y = pos.get_Y()
    if x + 1 > rows-1:pass 
    else:
        x += 1
        pos = Position(x,y)
        outside_li.append(pos)
        x -= 1
    if x - 1 < 0:pass
    else:
        x -= 1
        pos = Position(x,y)
        outside_li.append(pos)
        x += 1
    if y + 1 > cols-1:pass
    else:
        y += 1
        pos = Position(x,y)
        outside_li.append(pos)
        y -= 1
    if y - 1 < 0:pass
    else:
        y -= 1
        pos = Position(x,y)
        outside_li.append(pos)
        y += 1
    return outside_li
#----------------------------------------------------
def filter_visited(visited_li,outside_li):
    for i in visited_li:
        vis_x = i.get_X()
        vis_y = i.get_Y()
        for j in outside_li:
            fo_x = j.get_X()
            fo_y = j.get_Y()
            if fo_x == vis_x and fo_y == vis_y:
                outside_li.remove(j)
    fv_li = outside_li 
    return fv_li
#----------------------------------------------------
def filter_repeat(visited_li,fv_li):
    rp_li = []
    for i in fv_li:
        rp = 0
        fv_x = i.get_X()
        fv_y = i.get_Y()
        for j in visited_li:
            vis_x = j.get_X()
            vis_y = j.get_Y()
            if fv_x + 1 == vis_x and fv_y == vis_y:rp += 1
            if fv_x - 1 == vis_x and fv_y == vis_y:rp += 1
            if fv_x == vis_x and fv_y + 1 == vis_y:rp += 1
            if fv_x == vis_x and fv_y - 1 == vis_y:rp += 1
        if rp > 1:
            rp_li.append(i)
    for i in rp_li:
        rp_x = i.get_X()
        rp_y = i.get_Y()
        for j in fv_li:
            fv_x = j.get_X()
            fv_y = j.get_Y()
            if rp_x == fv_x and fv_y == rp_y:
                fv_li.remove(j)
    #print rp_li
    fr_li = fv_li
    return fr_li
#----------------------------------------------------
def add_wall(rows,cols,visited_li):
    total_wall_li = []
    for i in range(rows):
        for j in range(cols):
            pos = Position(i,j)
            total_wall_li.append(pos)
    for i in visited_li:
        v_x = i.get_X()
        v_y = i.get_Y()
        for j in total_wall_li:
            t_x = j.get_X()
            t_y = j.get_Y()
            if t_x == v_x and t_y == v_y:
                total_wall_li.remove(j)
    return total_wall_li
#----------------------------------------------------
def add_loop_back(total_wall_li,visited_li):
    loop_back_li = []
    for i in total_wall_li:
        up = 0
        down = 0
        left = 0
        right = 0
        t_x = i.get_X()
        t_y = i.get_Y()
        for j in visited_li:
            v_x = j.get_X()
            v_y = j.get_Y()
            if t_x -1 == v_x and t_y == v_y:left = 1
            if t_x +1 == v_x and t_y == v_y:right = 1
            if t_x == v_x and t_y -1 == v_y:down = 1
            if t_x == v_x and t_y +1 == v_y:up = 1
            if left == 0 and right == 0 and down == 1 and up == 1:
                loop_back_li.append(i)
            if left == 1 and right == 1 and down == 0 and up == 0:
                loop_back_li.append(i)
        f_loop_back_li = []
        for i in range(len(loop_back_li)):
            if random.random() > 0.8:
                z = random.choice(loop_back_li)
                f_loop_back_li.append(z)
    return f_loop_back_li

#----------------------------------------------------
def console_output(visited_li,rows,cols):
    wall = "  "
    road = "[]"
    maze = [[wall for col in range(cols)] for row in range(rows)]
    for i in visited_li:
        x = i.get_X()
        y = i.get_Y()
        maze[x][y] = road 
    for i in maze:print i 

#----------------------------------------------------
def gen_maze(rows,cols,start_x,start_y,end_x,end_y):
    #initial
    #wall_li = gen_wall(rows,cols)
    visited_li = []
    pos_start = Position(start_x,start_y)
    pos_end = Position(end_x,end_y)
    #start point
    visited_li.append(pos_start)
    visited_li.append(pos_end)
    start_outside_li = filter_outside(pos_start,rows,cols)
    start_fv_li = filter_visited(visited_li,start_outside_li)
    start_fr_li = filter_repeat(visited_li,start_fv_li)
    start_next_pos = random.choice(start_fr_li)
    print "maze  creating...."
    file=open('maze_data.pkl','wb')
    while len(visited_li) < rows*cols:
        try:
            #--------------------------------------------------------------
            #start point
            visited_li.append(start_next_pos)
            pickle.dump(start_next_pos,file)
            start_fo_li_temp = filter_outside(start_next_pos,rows,cols)
            start_outside_li = start_outside_li + start_fo_li_temp
            start_fv_li = filter_visited(visited_li,start_outside_li)
            start_fr_li = filter_repeat(visited_li,start_fv_li)
            start_next_pos = random.choice(start_fr_li)
        except:
            file.close()
            print "done..."
            break
    pos_end = Position(end_x-1,end_y)
    visited_li.append(pos_end)
    pos_end = Position(end_x,end_y-1)
    visited_li.append(pos_end)
    pos_end = Position(end_x-1,end_y-1)
    visited_li.append(pos_end)
    return visited_li

if __name__ == "__main__":
    print ""