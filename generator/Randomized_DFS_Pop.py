from generator.GenAlgo import GenAlgo
import random
import numpy as np

class Randomized_DFS_Pop(GenAlgo):
    def __init__(self, w, h):
        super(Randomized_DFS_Pop, self).__init__(w, h)

    def generate(self):
        grid = np.ones((self.W, self.H), dtype=np.int8)
        curr_r, curr_c = 1, 1
        grid[curr_r][curr_c] = 0
        
        track = [(curr_r, curr_c)]
        path = [(curr_r, curr_c)]

        while track:
            crow, ccol = track[-1]
            neighbors = self._find_neighbors(crow, ccol, grid, True)

            if not neighbors:
                track.pop() # Tối ưu hóa tại đây O(1)
            else:
                nrow, ncol = random.choice(neighbors)
                grid[nrow][ncol] = 0
                grid[(nrow + crow) // 2][(ncol + ccol) // 2] = 0

                track.append((nrow, ncol)) # Tối ưu hóa tại đây O(1)
                path.append(((nrow + crow) // 2, (ncol + ccol) // 2))
                path.append((nrow, ncol))
        return grid, path
