#! /usr/bin/env python


from random import choice
from OpenGL import GL as gl
from OpenGL import GLUT as glut

import solid_data as data


maze = [
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
    [1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
    [0,0,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0],
    [1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
]


def set_color(color):
    """Function sets the color."""
    r, g, b = color
    gl.glColor3f(r, g, b)


class Coin:
    """Class of Coin object."""

    def __init__(self, pos_x, pos_z):
        """ Constructor method of Coin class.

        :param pos_x: int, position on x axis
        :param pos_z: int, position on z axis
        """
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.radius = 0.1
        self.coin_color = data.COIN_COLOR  # coin color
        self.super_coin = False

    def draw(self):
        """Function draws coin."""

        set_color(self.coin_color)

        gl.glPushMatrix()
        gl.glTranslatef(self.pos_x + 0.5, 0.0, self.pos_z + 0.5)
        glut.glutSolidSphere(self.radius, 10, 10)
        gl.glPopMatrix()


class SuperCoin(Coin):
    """Class of SuperCoin object."""

    def __init__(self, pos_x, pos_z):
        """ Constructor method of SuperCoin class.

        :param pos_x: int, position on x axis
        :param pos_z: int, position on z axis
        """

        super().__init__(pos_x, pos_z)
        self.radius = 0.25
        self.coin_color = data.SUPER_COIN_COLOR  # super coins color red
        self.super_coin = True


class Block:
    """Class of block of wall, element of board."""

    def __init__(self, pos_xw, pos_zn, walls):
        """

        :param pos_xw: position of the west/north corner
         of block on x axis
        :param pos_zn: position of the west/north corner
        of block on z axis
        :param walls: information about which wall should
        be draw in for block
            'S' south wall
            'N' north wall
            'E' east wall
            'W' west wall
        """
        self.pos_xw = pos_xw
        self.pos_xe = pos_xw + 1
        self.pos_zn = pos_zn
        self.pos_zs = pos_zn + 1
        self.walls = walls

        self.floor_color = data.FLOOR_COLOR     # floor color
        self.celling_color = data.CELING_COLOR  # celling color
        self.celing_level = data.CELLING_LEVEL   # height of celling
        self.floor_level = data.FLOOR_LEVEL     # height of floor

    def __str__(self):
        return "Block with position: " + \
               str(self.pos_xw) + "," + \
               str(self.pos_zs) + "," + self.walls

    def _draw_vertical_square(self, axis):
        """ Function draw vertical square on axis x or z.

        :param axis: axis type where square will be draw
               if axis in "NS" - square is on X axis
               if axis in "WE" - square is on Z axis
        """

        if axis in "NS":
            pos_z = self.pos_zn if "N" in axis else self.pos_zs

            # Start drawing a polygon
            gl.glBegin(gl.GL_QUADS)
            set_color(self.floor_color)
            # Top Left
            gl.glVertex3f(self.pos_xw,  self.floor_level, pos_z)
            # Top Right
            gl.glVertex3f(self.pos_xe, self.floor_level, pos_z)

            set_color(self.celling_color)
            # Bottom Right
            gl.glVertex3f(self.pos_xe, self.celing_level, pos_z)
            # Bottom Left
            gl.glVertex3f(self.pos_xw,  self.celing_level, pos_z)
            gl.glEnd()

        elif axis in "WE":

            pos_x = self.pos_xe if "E" in axis else self.pos_xw

            # Start drawing a polygon
            gl.glBegin(gl.GL_QUADS)
            set_color(self.floor_color)
            # Top Left
            gl.glVertex3f(pos_x, self.floor_level, self.pos_zs)
            # Top Right
            gl.glVertex3f(pos_x, self.floor_level, self.pos_zn)

            set_color(self.celling_color)
            # Bottom Right
            gl.glVertex3f(pos_x, self.celing_level, self.pos_zn)
            # Bottom Left
            gl.glVertex3f(pos_x, self.celing_level, self.pos_zs)
            gl.glEnd()

        else:
            print("ERROR during drawing vertical squares:"
                  "function name: board._draw_vertical_square")

    def _draw_celling(self):
        """Function draw celing of the block."""

        # draw block celling
        gl.glBegin(gl.GL_QUADS)  # Start drawing a polygon
        set_color(self.celling_color)

        gl.glVertex3f(self.pos_xw, self.celing_level, self.pos_zn)
        gl.glVertex3f(self.pos_xw, self.celing_level, self.pos_zs)
        gl.glVertex3f(self.pos_xe, self.celing_level, self.pos_zs)
        gl.glVertex3f(self.pos_xe, self.celing_level, self.pos_zn)
        gl.glEnd()

    def draw_block(self):
        """ Function draws the block."""

        # draw celling
        self._draw_celling()

        # draw back, front, left and right wall
        for wall in "NSWE":
            if wall in self.walls:
                self._draw_vertical_square(wall)


class Board:
    """Class of Board object.

    Class contain all elements and method for crating and
    drawing the board, containig floor, walls and conis."""

    def __init__(self, maze):
        """Constructor method of __Board class.

        Constructor initializes many board parameters and
        coins objects. Contains methods responsible for
        board drawing.

        :param maze: maze

        maze - should be a list of lists containing anly integr 0 or 1.
        0 - empty square, floor
        1 - square with walls
        """

        self.maze_len = len(maze)           # len of maze
        self.maze_row_len = len(maze[0])    # width of maze

        self.super_coins_no = 5              # number of super-coins

        self.floor_level = data.FLOOR_LEVEL  # height of floor

        self.floor_color = data.FLOOR_COLOR  # floor color

        self.blocks = []                     # blocks in the board
        self.coins = []                      # coins

        self._create_board_elements(maze)
        self.super_coins = self._create_super_coins()
        self.block_positions = self.get_block_positions()

    def get_block_positions(self):

        return set((block.pos_xw, block.pos_zn) for block in self.blocks)

    def _create_board_elements(self, maze):
        """Method creating all objcts of board.

        Function creates list of Coin objects as a
        attribute of Board.

        Function creates list of Block objects as a
        attribute of Board.

        :param maze: maze - should be a list of lists
        containing anly integr 0 or 1.
        0 - empty square, floor
        1 - square with walls
        """

        maze_size = len(maze) - 1
        coins_append = self.coins.append
        blocks_append = self.blocks.append

        for row_no, row in enumerate(maze):
            row_len = len(row) - 1

            for sq_no, square in enumerate(row):
                if not square:
                    coins_append(Coin(sq_no, row_no))
                else:
                    walls = []
                    walls_append = walls.append

                    if not all([row_no, maze[row_no-1][sq_no]]):
                        walls_append("N")

                    if not all([sq_no, maze[row_no][sq_no-1]]):
                        walls_append("W")

                    if sq_no == row_len or not maze[row_no][sq_no+1]:
                        walls_append("E")

                    if row_no == maze_size or not maze[row_no+1][sq_no]:
                        walls_append("S")

                    blocks_append(Block(sq_no, row_no, ''.join(walls)))

    def _create_super_coins(self):
        """Function creates list of SuperCoin objects as a
        attribute of Board."""

        return [SuperCoin(coin.pos_x, coin.pos_z) for coin in
                [choice(self.coins) for n in range(self.super_coins_no)]]

    def _draw_floor(self):
        """ Function draw floor of the board."""

        gl.glBegin(gl.GL_QUADS)               # Start drawing a polygon
        set_color(self.floor_color)
        gl.glVertex3f(0,  self.floor_level, 0)
        gl.glVertex3f(self.maze_row_len, self.floor_level, 0)
        gl.glVertex3f(self.maze_row_len, self.floor_level, self.maze_len)
        gl.glVertex3f(0,  self.floor_level, self.maze_len)
        gl.glEnd()

    def draw(self):
        """ The main drawing function.

        Function draws all board elements, floor, blocks and coins.
        """

        # draw the board floor
        self._draw_floor()

        for block in self.blocks:
            block.draw_block()

        # draw the coins
        for coin in self.coins:
            coin.draw()

        # draw the super_coins
        for coin in self.super_coins:
            coin.draw()
