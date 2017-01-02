from main import Main
from board import SuperCoin


test_maze = [
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1]
]


class TestMain:

    def setup_method(self):
        self.main = Main(test_maze)
        self.board = self.main.board
        self.pacman = self.main.pacman
        self.ghost = self.main.ghost1

    def set_pacman_to_position(self, x, y):
        """"""
        self.pacman.pos_x, self.pacman.pos_z = x, y

    def set_ghost_to_position(self, x, y):
        """"""
        self.ghost.pos_x, self.ghost.pos_z = x, y

    def test_outside_board1(self):
        """"""
        self.pacman.pos_x = -self.pacman.step
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_x == self.board.maze_row_len-1

    def test_outside_board2(self):
        """"""
        self.pacman.pos_x = 0
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_x != self.board.maze_row_len-1

    def test_outside_board3(self):
        """"""
        self.pacman.pos_x = self.board.maze_row_len + self.pacman.step
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_x == 0

    def test_outside_board4(self):
        """"""
        self.pacman.pos_x = self.board.maze_row_len -1
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_x != 0

    def test_outside_board5(self):
        """"""
        self.pacman.pos_z = -self.pacman.step
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_z == self.board.maze_len -1

    def test_outside_board6(self):
        """"""
        self.pacman.pos_z = 0
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_z != self.board.maze_len -1

    def test_outside_board7(self):
        """"""
        self.pacman.pos_z = self.board.maze_len + self.pacman.step
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_z == 0

    def test_outside_board8(self):
        """"""
        self.pacman.pos_z = self.board.maze_len -1
        self.main.outside_board(self.pacman)
        assert self.pacman.pos_z != 0

    def test_outside_board9(self):
        """"""
        self.ghost.pos_x = -self.ghost.step
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_x == self.board.maze_row_len-1

    def test_outside_board10(self):
        """"""
        self.ghost.pos_x = 0
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_x != self.board.maze_row_len-1

    def test_outside_board11(self):
        """"""
        self.ghost.pos_x = self.board.maze_row_len + self.ghost.step
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_x == 0

    def test_outside_board12(self):
        """"""
        self.ghost.pos_x = self.board.maze_row_len -1
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_x != 0

    def test_outside_board13(self):
        """"""
        self.ghost.pos_z = -self.ghost.step
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_z == self.board.maze_len -1

    def test_outside_board14(self):
        """"""
        self.ghost.pos_z = 0
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_z != self.board.maze_len -1

    def test_outside_board15(self):
        """"""
        self.ghost.pos_z = self.board.maze_len + self.ghost.step
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_z == 0

    def test_outside_board16(self):
        """"""
        self.ghost.pos_z = self.board.maze_len -1
        self.main.outside_board(self.ghost)
        assert self.ghost.pos_z != 0

    def test_collision_pacman_coin1(self):
        """No collision with coin."""
        self.set_pacman_to_position(1.60, 1)
        coin_no = len(self.board.coins)
        self.main.collision_pacman_coin(self.board.coins[0])
        assert len(self.board.coins) == coin_no

    def test_collision_pacman_coin2(self):
        """Collision with coin."""
        self.set_pacman_to_position(1.59, 1)
        coin_no = len(self.board.coins)
        self.main.collision_pacman_coin(self.board.coins[1])
        assert len(self.board.coins) == coin_no - 1

    def test_collision_pacman_super_coin1(self):
        """No collision with super coin."""

        self.set_pacman_to_position(1, 2.25)
        self.board.super_coins.append(SuperCoin(1, 3))
        super_coin_no = len(self.board.super_coins)
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        assert len(self.board.super_coins) == super_coin_no

    def test_collision_pacman_super_coin2(self):
        """Collision with super coin. One coin less"""

        self.set_pacman_to_position(1, 2.26)
        self.board.super_coins.append(SuperCoin(1, 3))
        super_coin_no = len(self.board.super_coins)
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        assert len(self.board.super_coins) == super_coin_no - 1

    def test_collision_pacman_super_coin3(self):
        """Collision with super coin. Ghosts become eatable"""

        self.set_pacman_to_position(1, 2.26)
        self.board.super_coins.append(SuperCoin(1, 3))
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        assert self.ghost.eatable is True

    def test_collision_pacman_super_coin4(self):
        """Collision with super coin. Ghosts change color"""

        self.set_pacman_to_position(1, 2.26)
        self.board.super_coins.append(SuperCoin(1, 3))
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        assert self.ghost.color == (0.75, 0.75, 0.75)

    def test_collision_pacman_super_coin5(self):
        """Collision with super coin. Ghost become again normal after 10 sek"""

        self.set_pacman_to_position(1, 2.26)
        self.board.super_coins.append(SuperCoin(1, 3))
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        self.ghost.eatable_time -= 10  # shift in time for 10 sek
        self.ghost.become_not_eatable()
        assert self.ghost.eatable is False

    def test_collision_pacman_super_coin6(self):
        """Collision with super coin. Ghost is normal color after 10 sek"""

        self.set_pacman_to_position(1, 2.26)
        self.board.super_coins.append(SuperCoin(1, 3))
        self.main.collision_pacman_coin(self.board.super_coins[-1])
        self.ghost.eatable_time -= 10  # shift in time for 10 sek
        self.ghost.become_not_eatable()
        assert self.ghost.color == self.ghost.primary_color

    def test_collision_pacman_super_coin7(self):
        """Collision with 2 super coins."""
        # TODO

    def test_collision_pacman_ghost1(self):
        """Collision with eatable ghost"""
        self.set_pacman_to_position(1, 1)
        self.set_ghost_to_position(1, 1.99)
        self.ghost.eatable = True
        self.main.collision_pacman_ghost(self.ghost)
        assert self.ghost.was_eaten is True

    def test_collision_pacman_ghost2(self):
        """No collision with ghost"""
        self.set_pacman_to_position(1, 1)
        self.set_ghost_to_position(1, 2)
        self.ghost.eatable = True
        self.main.collision_pacman_ghost(self.ghost)
        assert self.ghost.was_eaten is False

    def test_collision_pacman_ghost3(self):
        """Collision with no eatable ghost"""
        # TODO

    def test_pacman_move1(self):
        """PacMan outside knot"""
        self.set_pacman_to_position(1, 2)
        self.pacman.direction = "W"
        self.main.pacman_move()
        assert self.pacman.pos_x == 1 - self.pacman.step

    def test_pacman_move2(self):
        """PacMan outside knot"""
        self.set_pacman_to_position(1, 2)
        self.pacman.direction = "E"
        self.main.pacman_move()
        assert self.pacman.pos_x == 1 + self.pacman.step

    def test_pacman_move3(self):
        """PacMan outside knot"""
        self.set_pacman_to_position(2, 1)
        self.pacman.direction = "N"
        self.main.pacman_move()
        assert self.pacman.pos_z == 1 - self.pacman.step

    def test_pacman_move4(self):
        """PacMan outside knot"""
        self.set_pacman_to_position(2, 1)
        self.pacman.direction = "S"
        self.main.pacman_move()
        assert self.pacman.pos_z == 1 + self.pacman.step

    def test_pacman_move5(self):
        """PacMan in knot, next_direction in knot direction"""
        self.set_pacman_to_position(1, 1)
        self.pacman.next_direction = "S"
        self.main.pacman_move()
        assert self.pacman.pos_z == 1 + self.pacman.step

    def test_pacman_move6(self):
        """PacMan in knot, next_direction in knot direction"""
        self.set_pacman_to_position(1, 1)
        self.pacman.next_direction = "E"
        self.main.pacman_move()
        assert self.pacman.pos_x == 1 + self.pacman.step

    def test_pacman_move7(self):
        """PacMan in knot, next_direction in knot direction"""
        self.set_pacman_to_position(1, 1)
        self.pacman.next_direction = "E"
        self.main.pacman_move()
        assert self.pacman.direction == "E"

    def test_pacman_move8(self):
        """PacMan in knot, next_direction not in knot direction"""
        self.set_pacman_to_position(1, 1)
        self.pacman.next_direction = "N"
        self.main.pacman_move()
        assert self.pacman.pos_z == 1

    def test_pacman_move9(self):
        """PacMan in knot, next_direction not in knot direction"""
        self.set_pacman_to_position(1, 1)
        self.pacman.next_direction = "W"
        self.main.pacman_move()
        assert self.pacman.pos_x == 1




    def test_ghost_move1(self):
        """Ghost outside knot"""
        self.set_ghost_to_position(1, 2)
        self.ghost.direction = "W"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_x == 1 - self.ghost.step

    def test_ghost_move2(self):
        """Ghost outside knot"""
        self.set_ghost_to_position(1, 2)
        self.ghost.direction = "E"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_x == 1 + self.ghost.step

    def test_ghost_move3(self):
        """Ghost outside knot"""
        self.set_ghost_to_position(2, 1)
        self.ghost.direction = "N"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_z == 1 - self.ghost.step

    def test_ghost_move4(self):
        """Ghost outside knot"""
        self.set_ghost_to_position(2, 1)
        self.ghost.direction = "S"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_z == 1 + self.ghost.step

    def test_ghost_move5(self):
        """Ghost in knot, next_direction in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "E"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_x == 1 + self.ghost.step

    def test_ghost_move6(self):
        """Ghost in knot, next_direction in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "S"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_z == 1 + self.ghost.step

    def test_ghost_move6a(self):
        """Ghost in knot, next_direction in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "S"
        self.main.ghost_move(self.ghost)
        assert self.ghost.direction == "S"

    def test_ghost_move6b(self):
        """Ghost in knot, next_direction in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "S"
        self.main.ghost_move(self.ghost)
        assert self.ghost.next_direction in "NEW"

    def test_ghost_move7(self):
        """Ghost in knot, next_direction not in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "N"
        self.main.ghost_move(self.ghost)
        assert self.ghost.pos_z == 1

    def test_ghost_move8(self):
        """Ghost in knot, next_direction not in knot directions"""
        self.set_ghost_to_position(1, 1)
        self.ghost.next_direction = "W"
        self.main.ghost_move(self.ghost)
        assert self.ghost.next_direction in "W"
        # TODO check new next direction  TEST NIE DZIAŁA PRAWIDŁOWO !!!!


    def test_ghost_move9(self):
        """Ghost in knot with one direction."""

    # TODO
    """Ghost in knot, direction not in knot directions"""
    """Ghost in knot, direction in knot directions"""

    """Ghost in knot, direction and next_direction not in knot directions
    new next direction"""



    def test_ghost_move(self):
        pass




















