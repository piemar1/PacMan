from main import Main
from board import SingleBoard
from pac_man import SinglePacMan


test_maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]


class TestMain:

    main = Main()

    board = SingleBoard(test_maze)
    board = board.instance

    pacman = SinglePacMan(1, 1)
    pacman = pacman.instance

    def set_pacman_to_position(self, x, y):
        self.pacman.pos_x, self.pacman.pos_z = x, y

    def test_get_pacman_possible_move1(self):
        """"""
        self.set_pacman_to_position(1, 1)
        assert self.main.get_pacman_possible_move() == "ES"

    def test_get_pacman_possible_move2(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 5, 1
        assert self.main.get_pacman_possible_move() == "WS"

    def test_get_pacman_possible_move3(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1, 6
        assert self.main.get_pacman_possible_move() == "EN"

    def test_get_pacman_possible_move4(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 5, 6
        assert self.main.get_pacman_possible_move() == "WN"

    def test_get_pacman_possible_move5(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1.5, 1
        assert self.main.get_pacman_possible_move() == "WES"

    def test_get_pacman_possible_move6(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1.6, 4
        assert self.main.get_pacman_possible_move() == "WEN"

    def test_get_pacman_possible_move7(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1.9, 7
        assert self.main.get_pacman_possible_move() == "WEN"

    def test_get_pacman_possible_move8(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 3.5, 2
        assert self.main.get_pacman_possible_move() == "WENS"

    def test_get_pacman_possible_move9(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1, 3.3
        assert self.main.get_pacman_possible_move() == "NSE"

    def test_get_pacman_possible_move10(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 2, 4.1
        assert self.main.get_pacman_possible_move() == "NSW"

    def test_get_pacman_possible_move11(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 4, 5.9
        assert self.main.get_pacman_possible_move() == "NSE"

    def test_get_pacman_possible_move12(self):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = 1, 2.5
        assert self.main.get_pacman_possible_move() == "NSE"

    def test_outside_board1(self):
        """"""
        self.pacman.pos_x = -self.pacman.step
        self.main.outside_board()
        assert self.pacman.pos_x == self.board.maze_row_len

    def test_outside_board2(self):
        """"""
        self.pacman.pos_x = 0
        self.main.outside_board()
        assert self.pacman.pos_x != self.board.maze_row_len

    def test_outside_board3(self):
        """"""
        self.pacman.pos_x = self.board.maze_row_len + self.pacman.step
        self.main.outside_board()
        assert self.pacman.pos_x == 0

    def test_outside_board4(self):
        """"""
        self.pacman.pos_x = self.board.maze_row_len
        self.main.outside_board()
        assert self.pacman.pos_x != 0

    def test_outside_board5(self):
        """"""
        self.pacman.pos_z = -self.pacman.step
        self.main.outside_board()
        assert self.pacman.pos_z == self.board.maze_len

    def test_outside_board6(self):
        """"""
        self.pacman.pos_z = 0
        self.main.outside_board()
        assert self.pacman.pos_z != self.board.maze_len

    def test_outside_board7(self):
        """"""
        self.pacman.pos_z = self.board.maze_len + self.pacman.step
        self.main.outside_board()
        assert self.pacman.pos_z == 0

    def test_outside_board8(self):
        """"""
        self.pacman.pos_z = self.board.maze_len
        self.main.outside_board()
        assert self.pacman.pos_z != 0

    def test_collision_coin(self):
        """"""
        self.set_pacman_to_position(1.1, 1)
        coin_no = len(self.board.coins)

        self.main.collision_coin(self.board.coins[0])
        assert len(self.board.coins) == coin_no - 1

    def test_collision_coin2(self):
        """"""
        self.set_pacman_to_position(1.11, 1)
        coin_no = len(self.board.coins)

        self.main.collision_coin(self.board.coins[0])
        assert len(self.board.coins) == coin_no
