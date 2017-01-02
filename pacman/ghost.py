from random import choice
from time import time

from OpenGL import GL as gl
from OpenGL import GLUT as glut

from pacman import PacMan
from solid_data import MOVES, OPPOSITE_MOVES, set_color


class Ghost(PacMan):
    def __init__(self, pos_x, pos_z, direction, color):
        super().__init__(pos_x, pos_z)

        self.primary_color = color
        self.step = 0.1
        self.eatable_time = 0
        self.eatable = False
        self.was_eaten = False
        self.direction = ""
        self.next_direction = direction

    def choice_next_direction(self):
        """"""
        self.next_direction = choice(
            MOVES.replace(OPPOSITE_MOVES[self.direction], "")
        )

    def draw(self):

        set_color(self.color)

        gl.glPushMatrix()
        gl.glTranslatef(self.pos_x + 0.5, 0.0, self.pos_z + 0.5)
        gl.glRotate(self.rotate, 0, 1, 0)

        glut.glutSolidSphere(self.radius, 10, 10)
        gl.glPopMatrix()

    def become_eatable(self):
        """"""

        if not self.eatable:
            # TODO color should be the same but more transparent
            # TODO TESTS
            self.eatable, self.color = True, (0.75, 0.75, 0.75)
        self.eatable_time = time()

    def become_not_eatable(self):
        """"""

        if time() - self.eatable_time >= 10:
            self.eatable, self.color = False, self.primary_color
            self.eatable_time = 0
