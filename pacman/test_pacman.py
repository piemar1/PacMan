from pacman import PacMan

# TODO Test for pyopengl function !!!!


class TestPacMan:

    def setup_method(self):
        self.pacman = PacMan(1, 1)

    def test_pacman_init__1(self):
        """"""
        assert self.pacman.pos_x == 1

    def test_pacman_init__2(self):
        """"""
        assert self.pacman.pos_z == 1

    def test_pacman_init__3(self):
        """"""
        assert self.pacman.direction == ""

    def test_pacman_init__4(self):
        """"""
        assert self.pacman.next_direction == ""

    def test_pacman_init__5(self):
        """PacMan step must be able to be mulitplied to 1"""
        avaiable_step = (1, 0.5, 0.25, 0.2, 0.125, 0.1, 0.0625, 0.05)
        assert self.pacman.step in avaiable_step

    def test_move1(self):
        """"""
        self.pacman.direction = 'N'
        self.pacman.move()
        assert self.pacman.rotate == 0

    def test_move2(self):
        """"""
        pos, self.pacman.direction = self.pacman.pos_z, "N"
        self.pacman.move()
        assert self.pacman.pos_z == pos - self.pacman.step

    def test_move3(self):
        """"""
        self.pacman.direction = 'S'
        self.pacman.move()
        assert self.pacman.rotate == 180

    def test_move4(self):
        """"""
        pos, self.pacman.direction = self.pacman.pos_z, "S"
        self.pacman.move()
        assert self.pacman.pos_z == pos + self.pacman.step

    def test_move5(self):
        """"""
        self.pacman.direction = 'W'
        self.pacman.move()
        assert self.pacman.rotate == 90

    def test_move6(self):
        """"""
        pos, self.pacman.direction = self.pacman.pos_x, "W"
        self.pacman.move()
        assert self.pacman.pos_x == pos - self.pacman.step

    def test_move7(self):
        """"""
        self.pacman.direction = 'E'
        self.pacman.move()
        assert self.pacman.rotate == 270

    def test_move8(self):
        """"""
        pos, self.pacman.direction = self.pacman.pos_x, "E"
        self.pacman.move()
        assert self.pacman.pos_x == pos + self.pacman.step


