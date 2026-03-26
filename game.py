import pygame, sys
from src.system.Maze import Maze
from src.system.Player import Player
from src. system.exit_gate import Exit_gate

W, H = 10, 10
INIT_TILE = 20

def reset_game():
    m = Maze(W, H)
    p = Player(*m.path[0])
    e = Exit_gate(W*2-1, H*2-1)
    return m, p, e, 0, 0

def get_tile_size(screen_w, screen_h, grid_w, grid_h):
    return min(screen_w // grid_w, screen_h // grid_h)

def main():
    
    pygame.init()
    screen = pygame.display.set_mode(((W*2+1)*INIT_TILE, (H*2+1)*INIT_TILE), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    maze, player, exit_gate, state, ani_idx = reset_game()

    while True:
        sw, sh = screen.get_size()
        ts = get_tile_size(sw, sh, maze.cols, maze.rows)

        screen.fill((30, 30, 30))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: sys.exit()
            if ev.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((ev.w, ev.h), pygame.RESIZABLE)
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_1 and state == 0: state = 2
                if ev.key == pygame.K_2 and state == 0: state = 1; ani_idx = 0
                if ev.key == pygame.K_r: maze, player, state, ani_idx = reset_game()
                if state == 2:
                    move = {pygame.K_UP: 1, pygame.K_DOWN: 2, pygame.K_LEFT: 3, pygame.K_RIGHT: 4}.get(ev.key)
                    if move: player.update_player(move, maze.grid)

        if state == 1:
            maze.draw_step(screen, ts, ani_idx)
            ani_idx += 2
            if ani_idx >= len(maze.path): state = 2
        elif state == 2:
            maze.draw(screen, ts)
            player.draw_player(screen, ts)
        else: # Menu
            maze.draw_step(screen, ts, 0)
        exit_gate.draw_exit(screen, ts)
        if player.r== exit_gate.r and player.c == exit_gate.c:
            print("you win ")
            break

        

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__": main()
