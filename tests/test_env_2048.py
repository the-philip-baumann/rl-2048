import pytest
import numpy as np

from env.env_2048 import Env2048


@pytest.fixture
def env():
    env =  Env2048(render_mode="human")
    env.board = np.zeros((4, 4), dtype=np.int32) 
    return env


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
        for i in range(0, env.width * env.height + 1):
            env.add_tile_at_random_empty_position(i)

        x, y = np.where(env.board == 0)
        assert len(x) == 0
        assert len(y) == 0

    def test_move_left__move_value_to_left_boarder(self, env):
        expected = 2
        env.board[0][3] = expected

        actual = env.move_left()

        assert actual[0][0] == expected

    def test_move_left__merge_two_values(self, env):
        expected = 4
        env.board[0][2] = 2
        env.board[0][3] = 2

        actual = env.move_left()

        assert actual[0][0] == expected

    def test_move_left__merge_when_seperated_by_a_zero(self, env):
        expected = 4
        env.board[0][1] = 2
        env.board[0][3] = 2

        actual = env.move_left()

        assert actual[0][0] == expected

    def test_move_left__dont_merge_when_different_values(self, env):
        env.board[0][2] = 2
        env.board[0][3] = 4

        actual = env.move_left()

        assert actual[0][0] == 2
        assert actual[0][1] == 4

    def test_move_left__dont_merge_when_seperated_by_a_different_value(self, env):
        env.board[0][0] = 2
        env.board[0][1] = 4
        env.board[0][3] = 2

        actual = env.move_left()

        assert actual[0][0] == 2
        assert actual[0][1] == 4

    def test_move_left__double_merge(self, env):
        expected_first_merge = 8
        expected_second_merge = 4
        env.board[0][0] = 4
        env.board[0][1] = 4
        env.board[0][2] = 2
        env.board[0][3] = 2

        actual = env.move_left()

        assert actual[0][0] == expected_first_merge 
        assert actual[0][1] == expected_second_merge

    def test_move_left__merge_after_merge(self, env):
        expected_merge = 8
        expected_remaining = 4
        env.board[0][0] = 4
        env.board[0][2] = 4
        env.board[0][3] = 4

        actual = env.move_left()

        assert actual[0][0] == expected_merge
        assert actual[0][1] == expected_remaining

        


        