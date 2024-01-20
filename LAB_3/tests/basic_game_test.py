import unittest
from unittest import mock
from unittest.mock import patch
import io
import contextlib
from LAB_3.src.basic_game import MazeGame


class TestMazeGame(unittest.TestCase):
    def setUp(self):
        self.game = MazeGame()

    def test_check_board_size(self):
        game = MazeGame(7)
        self.assertEqual(game.size, 7)
        self.assertEqual(len(game.board), 7)
        self.assertEqual(len(game.board[0]), 7)

    def test_check_initial_start_end(self):
        self.assertNotEqual(self.game.start, self.game.end)
        self.assertEqual(self.game.board[self.game.start[0]][self.game.start[1]], 'S')
        self.assertEqual(self.game.board[self.game.end[0]][self.game.end[1]], 'E')

    def test_check_start_end(self):
        game = MazeGame(5)
        self.assertEqual(game.board[game.start[0]][game.start[1]], 'S')
        self.assertEqual(game.board[game.end[0]][game.end[1]], 'E')

    def test_check_play(self):
        game = MazeGame(5)
        with mock.patch('builtins.input', return_value='q'):
            with io.StringIO() as buf:
                with contextlib.redirect_stdout(buf):
                    game.play()
                output = buf.getvalue()
        self.assertIn("Objective", output)

    def test_check_valid_move_up(self):
        initial_position = self.game.current_position
        self.game.move('w')
        expected_position = (initial_position[0] - 1, initial_position[1])
        self.assertEqual(self.game.current_position, expected_position)

    def test_check_valid_move_down(self):
        initial_position = self.game.current_position
        self.game.move('s')
        expected_position = (initial_position[0] + 1, initial_position[1])
        self.assertEqual(self.game.current_position, expected_position)

    def test_check_valid_move_right(self):
        initial_position = self.game.current_position
        self.game.move('d')
        expected_position = (initial_position[0], initial_position[1] + 1)
        self.assertEqual(self.game.current_position, expected_position)

    def test_check_invalid_move(self):
        old_position = self.game.current_position
        self.game.move('INVALID')
        assert self.game.current_position == old_position

    def test_check_off_board_move(self):
        self.game.current_position = (0, 0)
        with patch('builtins.print') as mocked_print:
            self.game.move('w')

        self.assertEqual(self.game.current_position, (0, 0))
        mocked_print.assert_called_with("!! You cannot leave the board.\n")

    def test_check_obstacle_move(self):
        self.game = MazeGame(size=5, obstacles=[(0, 0), (1, 0), (2, 1), (3, 3), (4, 1)], start=(2, 0), end=(2, 4))
        new_position = (3, 0)

        if self.game.start[0] < new_position[0]:
            direction = 'w'
        else:
            direction = 's'

        with patch('builtins.print') as mocked_print:
            self.game.move(direction)

        mocked_print.assert_called_with("!! You cannot move onto an obstacle.\n")

    def test_check_game_finish(self):
        game = MazeGame(5)
        game.current_position = (game.end[0] - 1, game.end[1])
        with mock.patch('builtins.input', return_value='s'):
            with io.StringIO() as buf:
                with contextlib.redirect_stdout(buf):
                    game.play()
                output = buf.getvalue()
        self.assertIn("Congratulations! You successfully completed the maze!", output)


if __name__ == '__main__':
    unittest.main()
