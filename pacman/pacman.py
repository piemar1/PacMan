from OpenGL import GL as gl
from OpenGL import GLUT as glut

from solid_data import set_color


class PacMan:
    def __init__(self, pos_x, pos_z):
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.direction = ''
        self.next_direction = ''

        self.radius = 0.5
        self.rotate = 0
        self.step = 0.1
        self.color = 1, 1, 0
        self.was_eaten = False

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

        set_color(self.color)

        gl.glPushMatrix()
        gl.glTranslatef(self.pos_x + 0.5, 0.0, self.pos_z + 0.5)
        gl.glRotate(self.rotate, 0, 1, 0)

        # gl.glBegin(gl.GL_TRIANGLE_FAN)
        # gl.glColor3f(0, 1, 0)
        # gl.glVertex2f(self.pos_x, self.pos_z)
        # for i in range(13):  # Rysujemy okrag z odcietym malym kawalkiem
        # Obrocony o podany offset.
        #     # i = i + DisplayFunc.dolna + DisplayFunc.off
        #     x = self.pos_x + 0.3 * sin(2 * pi * i / 24.0)
        #     y = self.pos_z + 0.3 * cos(2 * pi * i / 24.0)
        #     gl.glVertex2f(x, y)
        #     gl.glEnd()

        glut.glutSolidSphere(self.radius, 10, 10)
        gl.glPopMatrix()

