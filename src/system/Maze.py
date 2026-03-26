import pygame
from generator.Randomized_DFS import Randomized_DFS as DFS


class Maze:
    def __init__(self, w, h, algo=DFS):
        self.grid, self.path = algo(w, h).generate()
        self.rows, self.cols = self.grid.shape

    def draw(self, surface, ts):
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                color = (20, 20, 20) if val == 1 else (240, 240, 240)
                pygame.draw.rect(surface, color, (c * ts, r * ts, ts, ts))

    def draw_step(self, surface, ts, index):
        surface.fill((20, 20, 20))
        for i in range(min(index + 1, len(self.path))):
            r, c = self.path[i]
            pygame.draw.rect(surface, (240, 240, 240), (c * ts, r * ts, ts, ts))
    
    
