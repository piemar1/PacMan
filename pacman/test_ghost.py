from ghost import Ghost
from solid_data import MOVES, OPPOSITE_MOVES

# TODO Test for pyopengl function !!!!


class TestPacMan:

    def setup_method(self):
        self.ghost = Ghost(1, 1, "N", (1.0, 0.0, 1.0))

    def test_ghost_init__1(self):
        """"""
        assert self.ghost.pos_x == 1

    def test_ghost_init__2(self):
        """"""
        assert self.ghost.pos_z == 1

    def test_ghost_init__3(self):
        """"""
        assert self.ghost.eatable is False

    def test_ghost_init__4(self):
        """"""
        assert self.ghost.eatable_time == 0

    def test_ghost_init__5(self):
        """"""
        assert self.ghost.was_eaten is False

    def test_ghost_init__6(self):
        """"""
        assert self.ghost.direction in MOVES

    def test_ghost_init__7(self):
        """"""
        assert len(self.ghost.direction) == 0

    def test_ghost_init__8(self):
        """"""
        assert self.ghost.next_direction in MOVES

    def test_ghost_init__9(self):
        """"""
        assert len(self.ghost.next_direction) == 1

    def test_ghost_init__10(self):
        """Ghost step must be able to be mulitplied to 1"""
        avaiable_step = (1, 0.5, 0.25, 0.2, 0.125, 0.1, 0.0625, 0.05)
        assert self.ghost.step in avaiable_step
