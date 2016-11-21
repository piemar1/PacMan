from board import Board
import solid_data as data

# TODO Test for pyopengl function !!!!

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

test_blocks_positions = {
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 0), (1, 6),
    (2, 0), (2, 6),
    (3, 0), (3, 6),
    (4, 0), (4, 3), (4, 6),
    (5, 0), (5, 2), (5, 3), (5, 4), (5, 6),
    (6, 0), (6, 3), (6, 6),
    (7, 0), (7, 1), (7, 5), (7, 6),
    (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6),
}

test_blocks = {
    (0, 0, "NW"), (0, 1, "NS"), (0, 2, "NS"), (0, 3, "NS"),
    (0, 4, "NS"), (0, 5, "NS"), (0, 6, "NE"),
    (1, 0, "WE"), (1, 6, "WE"),
    (2, 0, "WE"), (2, 6, "WE"),
    (3, 0, "WE"), (3, 6, "WE"),
    (4, 0, "WE"), (4, 3, "NWE"), (4, 6, "WE"),
    (5, 0, "WE"), (5, 2, "NWS"), (5, 3, ""), (5, 4, "NES"), (5, 6, "WE"),
    (6, 0, "WE"), (6, 3, "WES"), (6, 6, "WE"),
    (7, 0, "W"), (7, 1, "NE"), (7, 5, "NW"), (7, 6, "E"),
    (8, 0, "WS"), (8, 1, "S"), (8, 2, "NS"), (8, 3, "NS"), (8, 4, "NS"),
    (8, 5, "S"), (8, 6, "ES"),
}

test_coins_positions = {
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
    (4, 1), (4, 2), (4, 4), (4, 5),
    (5, 1), (5, 5),
    (6, 1), (6, 2), (6, 4), (6, 5),
    (7, 2), (7, 3), (7, 4)
}


class TestBoard:

    def setup_method(self):
        self.board = Board(test_maze)

    def test_board_init__1(self):
        """"""
        assert self.board.maze_len == len(test_maze)

    def test_board_init__2(self):
        """"""
        assert self.board.maze_row_len == len(test_maze[0])

    def test_board_init__3(self):
        """"""
        assert self.board.floor_level == data.FLOOR_LEVEL

    def test_board_init__4(self):
        """"""
        assert self.board.floor_color == data.FLOOR_COLOR

    def test_board_get_blosk_positions(self):
        """"""
        for block in self.board.blocks:
            assert (block.pos_xw, block.pos_zn) in self.board.block_positions

    def test_board_create_board_elements1(self):
        """"""
        assert len(self.board.blocks) == 35

    def test_board_create_board_elements2(self):
        """"""
        for block in self.board.blocks:
            assert (block.pos_zn, block.pos_xw) in test_blocks_positions

    def test_board_create_board_elements3(self):
        """"""
        for block in self.board.blocks:
            assert (block.pos_zn, block.pos_xw, block.walls) in test_blocks

    def test_board_create_board_elements4(self):
        """"""
        assert len(self.board.coins) == 28

    def test_board_create_board_elements5(self):
        """"""
        for coin in self.board.coins:
            assert (coin.pos_z, coin.pos_x) in test_coins_positions

    def test_board_create_super_coins1(self):
        """"""
        assert len(self.board.super_coins) == self.board.super_coins_no == 5

    def test_board_create_super_coins2(self):
        """"""
        for coin in self.board.super_coins:
            assert (coin.pos_z, coin.pos_x) in test_coins_positions
