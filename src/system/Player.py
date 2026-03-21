import pygame
from src.system.Character import Character

class Player(Character):
    def __init__(self, starting_r, starting_c, color=(0, 255, 0)):
        super(Player, self).__init__(starting_r, starting_c)
        self.color = color

    def update_player(self, move, grid):
        if self.valid_direction(grid, move):
            self.moves(direction=move)

    def draw_player(self, screen, ts):
        size = ts - max(2, ts // 5)
        offset = (ts - size) // 2
        pixel_x = self.c * ts + offset
        pixel_y = self.r * ts + offset
        pygame.draw.rect(screen, self.color, (pixel_x, pixel_y, size, size), border_radius=6)
