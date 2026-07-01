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
        assert actual[0][2] == 2

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

    def test_move_left__dont_merge_after_merge(self, env):
        expected_merge = 8
        expected_remaining = 4
        env.board[0][0] = 4
        env.board[0][2] = 4
        env.board[0][3] = 4

        actual = env.move_left()

        assert actual[0][0] == expected_merge
        assert actual[0][1] == expected_remaining

    def test_move_right__move_value_to_right_boarder(self, env):
        expected = 2
        env.board[0][1] = expected

        actual = env.move_right()

        assert actual[0][3] == expected

    def test_move_right__merge_two_values(self, env):
        expected = 4
        env.board[0][0] = 2
        env.board[0][2] = 2

        actual = env.move_right()

        assert actual[0][3] == expected

    def test_move_right__merge_when_seperated_by_a_zero(self, env):
        expected = 4
        env.board[0][0] = 2
        env.board[0][2] = 2

        actual = env.move_right()

        assert actual[0][3] == expected

    def test_move_right__dont_merge_when_different_values(self, env):
        env.board[0][1] = 2
        env.board[0][2] = 4

        actual = env.move_right()

        assert actual[0][2] == 2
        assert actual[0][3] == 4

    def test_move_right__dont_merge_when_seperated_by_a_different_value(self, env):
        env.board[0][0] = 2
        env.board[0][1] = 4
        env.board[0][3] = 2

        actual = env.move_right()

        assert actual[0][1] == 2
        assert actual[0][2] == 4
        assert actual[0][3] == 2

    def test_move_right__double_merge(self, env):
        expected_first_merge = 8
        expected_second_merge = 4
        env.board[0][0] = 4
        env.board[0][1] = 4
        env.board[0][2] = 2
        env.board[0][3] = 2

        actual = env.move_right()

        assert actual[0][2] == expected_first_merge 
        assert actual[0][3] == expected_second_merge

    def test_move_right__dont_merge_after_merge(self, env):
        expected_merge = 8
        expected_remaining = 4
        env.board[0][0] = 4
        env.board[0][2] = 4
        env.board[0][3] = 4

        actual = env.move_right()

        assert actual[0][2] == expected_remaining
        assert actual[0][3] == expected_merge
    
    def test_move_up__move_value_to_upper_boarder(self, env):
        expected = 2
        env.board[3][1] = expected

        actual = env.move_up()

        assert actual[0][1] == expected

    def test_move_up__merge_two_values(self, env):
        expected = 4
        env.board[1][2] = 2
        env.board[3][2] = 2

        actual = env.move_up()

        assert actual[0][2] == expected

    def test_move_up__merge_when_seperated_by_a_zero(self, env):
        expected = 4
        env.board[0][2] = 2
        env.board[2][2] = 2

        actual = env.move_up()

        assert actual[0][2] == expected

    def test_move_up__dont_merge_when_different_values(self, env):
        env.board[1][2] = 2
        env.board[2][2] = 4

        actual = env.move_up()

        assert actual[0][2] == 2
        assert actual[1][2] == 4

    def test_move_up__dont_merge_when_seperated_by_a_different_value(self, env):
        env.board[1][3] = 2
        env.board[2][3] = 4
        env.board[3][3] = 2

        actual = env.move_up()

        assert actual[0][3] == 2
        assert actual[1][3] == 4
        assert actual[2][3] == 2

    def test_move_up__double_merge(self, env):
        expected_first_merge = 8
        expected_second_merge = 4
        env.board[0][0] = 4
        env.board[1][0] = 4
        env.board[2][0] = 2
        env.board[3][0] = 2

        actual = env.move_up()

        assert actual[0][0] == expected_first_merge 
        assert actual[1][0] == expected_second_merge

    def test_move_up__dont_merge_after_merge(self, env):
        expected_merge = 8
        expected_remaining = 4
        env.board[0][2] = 4
        env.board[2][2] = 4
        env.board[3][2] = 4

        actual = env.move_up()

        assert actual[1][2] == expected_remaining
        assert actual[0][2] == expected_merge

        


    def test_move_down__move_value_to_lower_boarder(self, env):
        expected = 2
        env.board[1][1] = expected

        actual = env.move_down()

        assert actual[3][1] == expected

    def test_move_down__merge_two_values(self, env):
        expected = 4
        env.board[1][2] = 2
        env.board[2][2] = 2

        actual = env.move_down()

        assert actual[3][2] == expected

    def test_move_down__merge_when_seperated_by_a_zero(self, env):
        expected = 4
        env.board[0][2] = 2
        env.board[2][2] = 2

        actual = env.move_down()

        assert actual[3][2] == expected

    def test_move_down__dont_merge_when_different_values(self, env):
        env.board[1][2] = 2
        env.board[2][2] = 4

        actual = env.move_down()

        assert actual[2][2] == 2
        assert actual[3][2] == 4

    def test_move_down__dont_merge_when_seperated_by_a_different_value(self, env):
        env.board[1][3] = 2
        env.board[2][3] = 4
        env.board[3][3] = 2

        actual = env.move_down()

        assert actual[1][3] == 2
        assert actual[2][3] == 4
        assert actual[3][3] == 2

    def test_move_down__double_merge(self, env):
        expected_first_merge = 8
        expected_second_merge = 4
        env.board[0][0] = 4
        env.board[1][0] = 4
        env.board[2][0] = 2
        env.board[3][0] = 2

        actual = env.move_down()

        assert actual[2][0] == expected_first_merge 
        assert actual[3][0] == expected_second_merge

    def test_move_down__dont_merge_after_merge(self, env):
        expected_merge = 8
        expected_remaining = 4
        env.board[0][2] = 4
        env.board[2][2] = 4
        env.board[3][2] = 4

        actual = env.move_down()

        assert actual[2][2] == expected_remaining
        assert actual[3][2] == expected_merge


    def test_move_left__merge_on_multiple_rows(self, env):
        env.board[0][0] = 2
        env.board[0][1] = 2
        env.board[1][2] = 4
        env.board[1][3] = 4

        actual = env.move_left()

        assert actual[0][0] == 4
        assert actual[1][0] == 8

    def test_move_left__merge_on_multiple_rows_and_columns(self, env):
        env.board[0][0] = 2
        env.board[0][1] = 2
        env.board[1][2] = 4
        env.board[1][3] = 4
        env.board[0][2] = 8
        env.board[0][3] = 8

        actual = env.move_left()

        assert actual[0][0] == 4
        assert actual[1][0] == 8
        assert actual[0][1] == 16
        

    def test_move_left__merge_on_multiple_rows_and_columns_but_only_in_left_direction(self, env):
        env.board[0][0] = 2
        env.board[0][1] = 2
        env.board[1][2] = 4
        env.board[1][3] = 4
        env.board[2][2] = 8
        env.board[3][3] = 8

        actual = env.move_left()

        assert actual[0][0] == 4
        assert actual[1][0] == 8
        assert actual[2][0] == 8
        assert actual[3][0] == 8
