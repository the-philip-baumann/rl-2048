import numpy as np
import gymnasium as gym
import numpy.ma as ma

from enum import Enum

class Actions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Env2048(gym.Env):
    
    def __init__(self, dimension: tuple=(4, 4), render_mode: str=None):
        self.width, self.height = dimension
        self.board = np.zeros((self.width, self.height), dtype=np.int32)
        self.score = 0

        self.add_tile_at_random_empty_position(2)
        self.add_tile_at_random_empty_position(2)

        self.metadata = {"render_modes": ["human"]}
        self.render_mode = render_mode if render_mode in self.metadata["render_modes"] else None

        self.action_space = gym.spaces.Discrete(len(Actions))
        self.observation_space = gym.spaces.Box(low=0, high=131072, shape=(self.width, self.height), dtype=np.int32) # 2^17 is theoretical highest value

    def reset(self): 
        self.board = np.zeros((self.width, self.height), dtype=np.int32)
        self.score = 0

        self.add_tile_at_random_empty_position(2)
        self.add_tile_at_random_empty_position(2)

    def add_tile_at_random_empty_position(self, value: int):
        x, y = np.where(self.board == 0)

        if len(x) == 0 or len(y) == 0:
            raise ValueError("No empty positions available to add a tile.")

        coordinates = list(zip(x, y))
        index = np.random.randint(0, len(coordinates))
        coordinate = coordinates[index]
        self.board[coordinate] = value

    def move_right(self):
        temp_board = np.rot90(self.board, k=2)
        temp_board = self.move_left(temp_board)
        return np.rot90(temp_board, k=2)
    
    def move_up(self):
        temp_board = np.rot90(self.board, k=1)
        temp_board = self.move_left(temp_board)
        return np.rot90(temp_board, k=-1)
    
    def move_down(self):
        temp_board = np.rot90(self.board, k=-1)
        temp_board = self.move_left(temp_board)
        return np.rot90(temp_board, k=1)

    def move_left(self, board=None):
        if board is None:
            board = self.board
            
        temp_board = [row[row != 0] for row in board]

        for row in temp_board:
            for i in range(len(row) - 1):
                if self._is_cell_touching_right_border(row, i):
                    continue
                if row[i] == row[i + 1]:
                    row[i] = row[i] * 2
                    row[i + 1] = 0

        temp_board = [row[row != 0] for row in temp_board]

        return np.array([np.pad(row, (0, self.width - len(row))) for row in temp_board])
 

   
    def _is_cell_touching_right_border(self,row, i):
        return i == len(row) - 1






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
                

