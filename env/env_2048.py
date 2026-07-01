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

        self.add_tile_at_random_empty_position()
        self.add_tile_at_random_empty_position()

        self.metadata = {"render_modes": ["human"]}
        self.render_mode = render_mode if render_mode in self.metadata["render_modes"] else None

        self.action_space = gym.spaces.Discrete(len(Actions))
        self.observation_space = gym.spaces.Box(low=0, high=131072, shape=(self.width, self.height), dtype=np.int32) # 2^17 is theoretical highest value

    def reset(self): 
        self.board = np.zeros((self.width, self.height), dtype=np.int32)
        self.score = 0

        self.add_tile_at_random_empty_position()
        self.add_tile_at_random_empty_position()

    def add_tile_at_random_empty_position(self, value: int = None):
        x, y = np.where(self.board == 0)

        if value is None:
            value = 2 if np.random.rand() < 0.9 else 4

        if len(x) == 0 or len(y) == 0:
            raise ValueError("No empty positions available to add a tile.")

        coordinates = list(zip(x, y))
        index = np.random.randint(0, len(coordinates))
        coordinate = coordinates[index]
        self.board[coordinate] = value

    def act(self, action: Actions):
        if action == Actions.LEFT:
            self.board, delta_score = self.move_left(False)
        elif action == Actions.RIGHT:
            self.board, delta_score = self.move_right(False)
        elif action == Actions.UP:
            self.board, delta_score = self.move_up(False)
        elif action == Actions.DOWN:
            self.board, delta_score = self.move_down(False)
        else:
            raise ValueError(f"Invalid action: {action}")
        return delta_score

    def move_right(self, dry_run=False):
        temp_board = np.rot90(self.board, k=2)
        temp_board, score_delta = self.move_left(temp_board, dry_run=dry_run)
        return np.rot90(temp_board, k=2), score_delta
    
    def move_up(self, dry_run=False):
        temp_board = np.rot90(self.board, k=1)
        temp_board, score_delta = self.move_left(temp_board, dry_run=dry_run)
        return np.rot90(temp_board, k=-1), score_delta
    
    def move_down(self, dry_run=False):
        temp_board = np.rot90(self.board, k=-1)
        temp_board, score_delta = self.move_left(temp_board, dry_run=dry_run)
        return np.rot90(temp_board, k=1), score_delta

    def move_left(self, board=None, dry_run=False):
        if board is None:
            board = self.board

        temp_score = self.score

        temp_board = [row[row != 0] for row in board]

        for row in temp_board:
            for i in range(len(row) - 1):
                if self._is_cell_touching_right_border(row, i):
                    continue
                if row[i] == row[i + 1]:
                    row[i] = row[i] * 2
                    row[i + 1] = 0
                    if not dry_run:
                        self.score += row[i] + row[i + 1]

        temp_board = [row[row != 0] for row in temp_board]

        return np.array([np.pad(row, (0, self.width - len(row))) for row in temp_board]), self.score - temp_score
   
    def is_terminated(self):
        is_same_as_left = np.array_equal(self.move_left(dry_run=True)[0], self.board)
        is_same_as_right = np.array_equal(self.move_right(dry_run=True)[0], self.board)
        is_same_as_up = np.array_equal(self.move_up(dry_run=True)[0], self.board)
        is_same_as_down = np.array_equal(self.move_down(dry_run=True)[0], self.board)
        return is_same_as_left and is_same_as_right and is_same_as_up and is_same_as_down

    def has_board_changed(self, previous_board):
        return not np.array_equal(previous_board, self.board)

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
