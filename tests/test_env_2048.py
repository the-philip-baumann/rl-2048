import pytest
import numpy as np

from env.env_2048 import Env2048


@pytest.fixture
def env():
    return Env2048()


class TestEnv2048:
        
    def test_add_tile_at_random_empty_position__correct_value(self, env):
        expected = 20
        board = env.board

        env.add_tile_at_random_empty_position(expected)

        x, y = np.where(board == expected)
        assert len(x) == 1
        assert len(y) == 1
        assert board[x[0]][y[0]] == expected

    def test_add_tile_at_random_empty_position__no_overriding(self, env):
        for i in range(0, env.width * env.height + 1 - 2): # -2 since constructor adds two tiles initially
            env.add_tile_at_random_empty_position(i)

        print(env.board)
        x, y = np.where(env.board == 0)
        assert len(x) == 0
        assert len(y) == 0


        