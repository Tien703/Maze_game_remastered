import pygame
class Exit_gate:
    def __init__(self, starting_r, starting_C):
        self.r = starting_r
        self.c = starting_C
        self.color = (100,200,100)
    def draw_exit(self, screen, ts):
        size = ts - max(2, ts // 5)
        offset = (ts - size) // 2
        pixel_x = self.c * ts + offset
        pixel_y = self.r * ts + offset
        pygame.draw.rect(screen, self.color, (pixel_x, pixel_y, size, size), border_radius=6)
        
        