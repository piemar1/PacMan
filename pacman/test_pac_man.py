from pac_man import SinglePacMan

# TODO Test for pyopengl function !!!!


class TestSinglePacMan:

    pacman = SinglePacMan(1, 1)
    pacman = pacman.instance

    def test_set_pacman_to_proper_position(self):
        """Function for seting pacman to proper position."""
        self.pacman.pos_x = 1
        self.pacman.pos_z = 1

    def test__pacman__init__1(self):
        """"""
        assert self.pacman.pos_x == 1

    def test__pacman__init__2(self):
        """"""
        assert self.pacman.pos_z == 1

    def test_move1(self):
        self.pacman.direction = 'N'
        self.pacman.move()
        assert self.pacman.rotate == 0

    def test_move2(self):
        pos, self.pacman.direction = self.pacman.pos_z, "N"
        self.pacman.move()
        assert self.pacman.pos_z == pos - self.pacman.step

    def test_move3(self):
        self.pacman.direction = 'S'
        self.pacman.move()
        assert self.pacman.rotate == 180

    def test_move4(self):
        pos, self.pacman.direction = self.pacman.pos_z, "S"
        self.pacman.move()
        assert self.pacman.pos_z == pos + self.pacman.step

    def test_move5(self):
        self.pacman.direction = 'W'
        self.pacman.move()
        assert self.pacman.rotate == 90

    def test_move6(self):
        pos, self.pacman.direction = self.pacman.pos_x, "W"
        self.pacman.move()
        assert self.pacman.pos_x == pos - self.pacman.step

    def test_move7(self):
        self.pacman.direction = 'E'
        self.pacman.move()
        assert self.pacman.rotate == 270

    def test_move8(self):
        pos, self.pacman.direction = self.pacman.pos_x, "E"
        self.pacman.move()
        assert self.pacman.pos_x == pos + self.pacman.step
