import numpy as np
import gymnasium as gym

class Env2048(gym.Env):
    
    def __init__(self, dimension: tuple=(4, 4), render_mode: str=None):
        self.width, self.height = dimension
        self.board = np.zeros((self.width, self.height), dtype=np.int32)
        self.score = 0

        self.add_tile_at_random_empty_position(2)
        self.add_tile_at_random_empty_position(2)

        self.metadata = {"render_modes": ["human"]}
        self.render_mode = render_mode if render_mode in self.metadata["render_modes"] else None


    def reset(self): 
        self.board = np.zeros((self.width, self.height), dtype=np.int32)
        self.score = 0

    def add_tile_at_random_empty_position(self, value: int):
        x, y = np.where(self.board == 0)

        if len(x) == 0 or len(y) == 0:
            raise ValueError("No empty positions available to add a tile.")

        coordinates = list(zip(x, y))
        index = np.random.randint(0, len(coordinates))
        coordinate = coordinates[index]
        self.board[coordinate] = value

    def render(self):
        if self.render_mode == "human":
            print("-----------------------------")
            for row in self.board:
                print("|", end="")
                for column in row:
                    if column == 0:
                        print(f"{'-':>6}", end="|")
                    else:
                        print(f"{column:>6}", end="|")
                print("\n-----------------------------")
                

