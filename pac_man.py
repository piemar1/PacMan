from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class SinglePacMan:

    class __PacMan:
        def __init__(self, pos_x, pos_z):
            self.pos_x = pos_x
            self.pos_z = pos_z
            self.direction = 'N'

            self.wall_top = 1  # height of celling
            self.wall_bottom = -1.0  # height of floor

            self.rotate = 0


        def draw(self):

            glPushMatrix()
            glTranslatef(self.pos_x, 0.0, self.pos_z)
            # glRotate(self.rotate, 0, 1, 0)


            # draw back wall
            glColor3f(1, 0, 0)
            glBegin(GL_QUADS)                 # Start drawing a polygon
            glVertex3f(self.pos_x  , self.wall_bottom, self.pos_z+0.1)  # Top Left
            glVertex3f(self.pos_x+1, self.wall_bottom, self.pos_z+0.1)  # Top Right
            glVertex3f(self.pos_x+1, self.wall_top, self.pos_z+0.1)  # Bottom Right
            glVertex3f(self.pos_x  , self.wall_top, self.pos_z+0.1)  # Bottom Left
            glEnd()                             # We are done with the polygon
            # #

            # draw front wall
            glColor3f(0, 1, 0)
            glBegin(GL_QUADS)  # Start drawing a polygon
            glVertex3f(self.pos_x  , self.wall_bottom, self.pos_z+0.9)  # Top Left
            glVertex3f(self.pos_x+1, self.wall_bottom, self.pos_z+0.9)  # Top Right
            glVertex3f(self.pos_x+1, self.wall_top, self.pos_z+0.9)  # Bottom Right
            glVertex3f(self.pos_x  , self.wall_top, self.pos_z+0.9)  # Bottom Left
            glEnd()  # We are done with the polygon

            # draw left wall
            glBegin(GL_QUADS)                 # Start drawing a polygon
            glVertex3f(self.pos_x+0.1, self.wall_bottom, self.pos_z)  # Top Left
            glVertex3f(self.pos_x+0.1, self.wall_bottom, self.pos_z+1)  # Top Right
            glVertex3f(self.pos_x+0.1, self.wall_top, self.pos_z+1)  # Bottom Right
            glVertex3f(self.pos_x+0.1, self.wall_top, self.pos_z)  # Bottom Left
            glEnd()                             # We are done with the polygon

            # # draw right wall
            glBegin(GL_QUADS)  # Start drawing a polygon
            glVertex3f(self.pos_x+0.9, self.wall_bottom, self.pos_z)  # Top Left
            glVertex3f(self.pos_x+0.9, self.wall_bottom, self.pos_z + 1)  # Top Right
            glVertex3f(self.pos_x+0.9, self.wall_top, self.pos_z + 1)  # Bottom Right
            glVertex3f(self.pos_x+0.9, self.wall_top, self.pos_z)  # Bottom Left
            glEnd()  # We are done with the polygon
            glPopMatrix()

    instance = None

    def __init__(self, pos_x, pos_z):
        if not SinglePacMan.instance:
            SinglePacMan.instance = SinglePacMan.__PacMan(pos_x, pos_z)
        else:
            return
