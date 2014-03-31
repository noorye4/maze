#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#=============================================================================#
# Name        : prim_maze_gui.py                                              #
# Autor       : Nooryes                                                       #
# Date        : march, 17 2014                                                #
# Description : Function definitions for drawing a maze in a window using     #
#               pygame                                                        #
#=============================================================================#
import sys
import pygame
import time
import pickle
import prim_maze
from A_STAR_search import A_STAR_search

#read maze data if you dont't want rebuild
def read_maze_data(maze_data, end_x, end_y):
    maze_data = open(maze_data, 'rb')
    maze = []
    while True:
        try:
            pos = pickle.load(maze_data)
            maze.append(pos)
        except EOFError:
            print "read done..."
            break
    return maze
#------------------------------------------------------------
def dis_maze(maze,grid_size,rows,cols):
    for i in maze:
        x = i.get_X()
        y = i.get_Y()
        rect = pygame.Rect((x * grid_size, y * grid_size), (grid_size , grid_size))
        pygame.draw.rect(window, WHITE, rect)
        pygame.display.update()
    pygame.image.save(window, "maze_background.png")

#------------------------------------------------------------
def dis_wall(total_wall_li, grid_size):
    for i in total_wall_li:
        x = i.get_X()
        y = i.get_Y()
        rect = pygame.Rect((x * grid_size, y * grid_size), (grid_size , grid_size))
        pygame.draw.rect(window, BLACK, rect, 2)
        pygame.display.update()
#------------------------------------------------------------
def dis_look_back(loop_back_li):
    for i in loop_back_li:
        x = i.get_X()
        y = i.get_Y()
        rect = pygame.Rect((x * grid_size, y * grid_size), (grid_size , grid_size))
        pygame.draw.rect(window, DEEP_BLUE, rect, 5)
        pygame.display.update()
#------------------------------------------------------------
def dis_solution_path(path, ani_speed, grid_size):
    maze_background = pygame.image.load('maze_background.png')
    background = window.convert_alpha()
    x, y = 0, 0
    #draw start point and end point
    pygame.draw.circle(window, GREEN, (x + 10, y + 10), grid_size / 2)
    pygame.draw.circle(window, BLUE, (rows * grid_size - 10, cols * grid_size - 10), grid_size / 2)
    for i in path:
        #window.blit(background,(0,0))
        x = i.get_X()
        y = i.get_Y()
        rect = pygame.Rect((x*grid_size,y*grid_size),(grid_size ,grid_size))
        pygame.draw.rect(window, BLACK, rect,0)
        #pygame.draw.circle(window, [0, 0, 0], [(x * grid_size) + 10, (y * grid_size) + 10], grid_size / 2, 0)
        time.sleep(ani_speed)
        pygame.display.update()
        
def dis_solution_node(node_li):
    for i in node_li:
        node = i.get_node()
        x = node.get_X()
        y = node.get_Y()
        pygame.draw.circle(window, [0, 255, 0], [(x * grid_size) + 10, (y * grid_size) + 10], grid_size / 2, 0)
        pygame.draw.circle(window, [0, 0, 0], [(x * grid_size) + 10, (y * grid_size) + 10], grid_size / 2, 5)
        time.sleep(ani_speed)
        pygame.display.update()
        
        
#================================================================================#
#                                Main Program                                    #
#================================================================================#
#color set
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BRIGHT_BLUE = (0, 255, 255)
DEEP_BLUE = (0, 0, 128)
alpha = 0
#argument set
grid_size = 20
rows = 16
cols = 16
start_x, start_y = 0, 0
end_x = rows - 1
end_y = cols - 1
ani_speed = 0.05


maze = prim_maze.gen_maze(rows,cols,start_x,start_y,end_x,end_y)

wall_li = prim_maze.add_wall(rows, cols, maze)
loop_back_wall = prim_maze.add_loop_back(wall_li,maze)
total_wall = wall_li + loop_back_wall
final_maze = set(maze) - set(loop_back_wall)
path = A_STAR_search(total_wall,start_x,start_y,end_x,end_y,rows,cols,)

#Display window
#------------------------------------------------------------
#window initial
pygame.init()
size = width, height = grid_size * rows, grid_size * cols
window = pygame.display.set_mode(size)
window.fill(RED)

dis_maze(final_maze,grid_size,rows,cols)
#dis_look_back(loop_back_wall)
dis_solution_path(path, ani_speed, grid_size)

#Event main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
