from OpenGL import GL as gl
from OpenGL import GLUT as glut


def set_color(color):
    """Function sets the color."""
    r, g, b = color
    gl.glColor3f(r, g, b)


class PacMan:
    def __init__(self, pos_x, pos_z):
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.direction = ''
        self.next_direction = ''

        self.wall_top = 1  # height of celling
        self.wall_bottom = -1.0  # height of floor
        self.radius = 0.5

        self.rotate = 0
        self.step = 0.1

    def move(self):

        if self.direction == 'N':
            self.pos_z -= self.step
            self.rotate = 0

        elif self.direction == 'S':
            self.pos_z += self.step
            self.rotate = 180

        elif self.direction == 'W':
            self.pos_x -= self.step
            self.rotate = 90

        elif self.direction == 'E':
            self.pos_x += self.step
            self.rotate = 270

        self.pos_x, self.pos_z = round(self.pos_x, 2), round(self.pos_z, 2)

    def draw(self):

        gl.glColor3f(0, 1, 0)

        gl.glPushMatrix()
        gl.glTranslatef(self.pos_x + 0.5, 0.0, self.pos_z + 0.5)
        gl.glRotate(self.rotate, 0, 1, 0)

        glut.glutSolidSphere(self.radius, 10, 10)
        gl.glPopMatrix()
