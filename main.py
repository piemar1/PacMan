#! /usr/bin/env python

import sys
from time import time

from OpenGL import GL as gl
from OpenGL import GLUT as glut
from OpenGL import GLU as glu

import board
import pac_man

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'


class Main:
    """
    Main class of the PacMan game.

    Class contains all method for initialising OpenGL objects.
    Contains also all game objects as board, coins, PacMan and ghosts.
    """
    def __init__(self):
        """Constructor method of Main Class.

        It initialases all object needed for start the game
        board, coins, PacMan and ghosts.
        """
        self.time_point = time()
        self.fps_no = 0

        # board creating
        self.board = board.SingleBoard(board.maze)
        self.board = self.board.instance

        # PacMan player creating
        self.pac_man = pac_man.SinglePacMan(1, 1)
        self.pac_man = self.pac_man.instance


    @staticmethod
    def init_gl(width, height):
        """A general OpenGL initialization function.

        Sets all of the initial parameters.
        This is called right after our OpenGL window is created.
        :param width: window width
        :param height: window height
        """
        # This Will Clear The Background Color To Black
        gl.glClearColor(0.0, 0.0, 0.0, 0.0)

        # Enables Clearing Of The Depth Buffer
        gl.glClearDepth(1.0)

        # The Type Of Depth Test To Do
        gl.glDepthFunc(gl.GL_LESS)
        # Enables Depth Testing
        gl.glEnable(gl.GL_DEPTH_TEST)
        # Enables Smooth Color Shading
        gl.glShadeModel(gl.GL_SMOOTH)

        gl.glMatrixMode(gl.GL_PROJECTION)

        # Reset The Projection Matrix.
        # Calculate The Aspect Ratio Of The Window.
        gl.glLoadIdentity()
        glu.gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

        gl.glMatrixMode(gl.GL_MODELVIEW)

    @staticmethod
    def re_size_gl_scene(width, height):
        """The function called when our window is resized
        (which shouldn't happen if you enable fullscreen, below)

        :param width: window width
        :param height: window height
        """
        # Prevent A Divide By Zero If The Window Is Too Small
        if height == 0:
            height = 1

        # Reset The Current Viewport And Perspective Transformation
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(60.0, float(width)/float(height), 0.1, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def key_pressed(self, key, x, y):
        """The function called whenever a key is pressed.
        Note the use of Python tuples to pass in: (key, x, y)

        :param args: string represented pushed key
        """

        if key == b'\033':
            sys.exit()

    def get_pacman_possible_move(self):

        pos_x, pos_z = self.pac_man.pos_x, self.pac_man.pos_z
        pos_x_mod, pos_z_mod = pos_x % 1, pos_z % 1
        pos_x_div, pos_z_div = pos_x // 1, pos_z // 1
        block_positions = self.board.block_positions
        possible_moves = []

        if not pos_x_mod and not pos_z_mod:
            if (pos_x - 1, pos_z) not in block_positions:
                possible_moves.append('W')
            if (pos_x + 1, pos_z) not in block_positions:
                possible_moves.append('E')
            if (pos_x, pos_z - 1) not in block_positions:
                possible_moves.append('N')
            if (pos_x, pos_z + 1) not in block_positions:
                possible_moves.append('S')

        elif pos_x_mod and not pos_z_mod:
            possible_moves.append('WE')
            if (pos_x_div, pos_z - 1) not in block_positions and \
               (pos_x_div + 1, pos_z - 1) not in block_positions:
                possible_moves.append('N')

            if (pos_x_div, pos_z + 1) not in block_positions and \
               (pos_x_div + 1, pos_z + 1) not in block_positions:
                possible_moves.append('S')

        elif not pos_x_mod and pos_z_mod:
            possible_moves.append('NS')

            if (pos_x - 1, pos_z_div - 1) not in block_positions and \
               (pos_x - 1, pos_z_div) not in block_positions:
                possible_moves.append('W')

            if (pos_x + 1, pos_z_div) not in block_positions and \
               (pos_x + 1, pos_z_div - 1) not in block_positions:
                possible_moves.append('E')

        elif pos_x_mod and pos_z_mod:
            possible_moves.append('NSWE')

        return ''.join(possible_moves)

    def out_side_board(self):

        if self.pac_man.pos_x < 0:
            self.pac_man.pos_x = self.board.maze_row_len

        elif self.pac_man.pos_x > self.board.maze_row_len:
            self.pac_man.pos_x = 0

        if self.pac_man.pos_z < 0:
            self.pac_man.pos_z = self.board.maze_len

        elif self.pac_man.pos_z > self.board.maze_len:
            self.pac_man.pos_z = 0

    def collision_coin(self, coin):

        wall1 = (self.pac_man.pos_x - coin.pos_x)**2
        wall2 = (self.pac_man.pos_z - coin.pos_z)**2
        radius = (self.pac_man.radius + coin.radius)**2

        if radius > wall1 + wall2:
            if coin.super_coin:
                self.board.super_coins.remove(coin)
            else:
                self.board.coins.remove(coin)

    def key_pressed_special(self, key, x, y):
        """The function called whenever a key is pressed.
        Note the use of Python tuples to pass in: (key, x, y)

        :param args: integer represented pushed key
        """
        # działanie klawiszy w osobnej funkcji

        if key == 100:
            print("LEFT arrow pressed")
            self.pac_man.next_direction = 'W'

        elif key == 102:
            print("RIGHT arrow pressed")
            self.pac_man.next_direction = 'E'

        elif key == 101:
            print("UP arrow pressed")
            self.pac_man.next_direction = 'N'

        elif key == 103:
            print("DOWN arrow pressed")
            self.pac_man.next_direction = 'S'

    def key_pressed_specialUP(self, key, x, y):
        pass
        # print("pressed UP", key)

    def draw_gl_scene(self):
        """The function draws all game elements."""

        # if time() - self.time_point > 0.5:
        #     self.time_point = time()

        # print("pacman position --> ", self.pac_man.pos_x, " ", self.pac_man.pos_z)
        # print("self.pac_man.next_direction", self.pac_man.next_direction)
        # print("self.pac_man.direction", self.pac_man.direction)
        # print(self.get_pacman_possible_move())

        # Clear The Screen And The Depth Buffer
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Reset The View
        gl.glLoadIdentity()
        gl.glTranslatef(-self.board.maze_row_len/2, 10.0, -30.0)
        gl.glRotate(80, 1, 0, 0)

        self.board.draw()
        self.pac_man.draw()

        if self.pac_man.next_direction and \
           self.pac_man.next_direction in self.get_pacman_possible_move():
            self.pac_man.direction = self.pac_man.next_direction
            self.pac_man.next_direction = ''

        if self.pac_man.direction and \
           self.pac_man.direction in self.get_pacman_possible_move():
            self.pac_man.move()

        self.out_side_board()

        for coin in self.board.coins:
            self.collision_coin(coin)

        for coin in self.board.super_coins:
            self.collision_coin(coin)

        # counts number of frames
        self.fps()

        #  since this is double buffered,
        # swap the buffers to display what just got drawn.
        glut.glutSwapBuffers()

    def fps(self):
        """Function counts number of frames per second (fps)."""

        if time() - self.time_point > 1.0:
            # print("pacman position --> ", self.pac_man.pos_x, " ", self.pac_man.pos_z)

            print("FPS - ", self.fps_no)
            self.time_point, self.fps_no = time(), 0
        else:
            self.fps_no += 1

    def main(self):
        """Main function responsible for run the game."""

        glut.glutInit(sys.argv)

        # Select type of Display mode:
        #  Double buffer
        #  RGBA color
        # Alpha components supported
        # Depth buffer
        glut.glutInitDisplayMode(
            glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_DEPTH
        )

        # get a 640 x 480 window
        glut.glutInitWindowSize(1000, 800)

        # the window starts at the upper left corner of the screen
        glut.glutInitWindowPosition(0, 0)

        # Asign name of the window
        glut.glutCreateWindow("PacMan")

        # Register the function called when the keyboard is pressed.
        glut.glutKeyboardFunc(self.key_pressed)

        glut.glutSpecialFunc(self.key_pressed_special)

        glut.glutSpecialUpFunc(self.key_pressed_specialUP)

        # Register the drawing function with glut.
        glut.glutDisplayFunc(self.draw_gl_scene)

        # Uncomment this line to get full screen.
        # glut.glutFullScreen()

        # When we are doing nothing, redraw the scene.
        glut.glutIdleFunc(self.draw_gl_scene)

        # Register the function called when our window is resized.
        glut.glutReshapeFunc(self.re_size_gl_scene)

        # Initialize our window.
        self.init_gl(640, 480)

        # Start Event Processing Engine
        glut.glutMainLoop()


if __name__ == "__main__":

    # Print message to console, and kick off the main to get it rolling.
    print("Hit ESC key to quit.")
    game = Main()
    game.main()
