import pygame
import random

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface=surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image=pygame.Surface((20,20))
        self.rect=self.image.get_rect()
        self.neighbours = []

    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)

    def draw(self):
        if self.alive:
            self.image.fill((0,0,0))
        else:
            self.image.fill((0,0,0))
            pygame.draw.rect(self.image,(255,255,255), (2,2,16,16))
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))



    def get_neighbours(self, grid):
        neighbour_list = [[1,1], [-1,-1], [1,-1], [-1,1], [0,-1], [0,1], [1,0], [-1,0]]
        for neighbor in neighbour_list:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y
        for neighbor in neighbour_list:
            if neighbor[0] < 0:
                neighbor[0] += 20

            if neighbor[1] < 0:
                neighbor[1] += 20

            if neighbor[1] > 19:
                neighbor[1] -= 20

            if neighbor[0] > 19:
                neighbor[0] -= 20

        for neighbor in neighbour_list:
            try:
                self.neighbours.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)