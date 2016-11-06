#! /usr/bin/env python


from random import choice

from OpenGL import GL as gl
from OpenGL import GLUT as glut


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
        self.coin_color = 0.9, 0.9, 0  # coins color yellow
        self.super_coin = False

    def draw(self):
        """Function draws coin."""

        r, g, b = self.coin_color
        gl.glColor3f(r, g, b)

        gl.glPushMatrix()
        gl.glTranslatef(self.pos_z + 0.5, 0.0, self.pos_x + 0.5)
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
        self.coin_color = 0.9, 0.3, 0  # super coins color red
        self.super_coin = True


class SingleBoard:
    """Singleton Board class. """

    class __Board:
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
            1 - square of wall
            """

            self.maze_len = len(maze[0])        # width of maze
            self.super_coins_no = 5             # number of super-coins

            self.wall_top = 1                   # height of celling
            self.wall_bottom = -1.0             # height of floor

            self.floor_color = 0.15, 0.15, 0.15  # floor color
            self.celling_color = 0, 0, 0.8       # celling color

            # maze transformation into a "drawable" lists
            self.floor_pos, self.transformed_maze = self._transform_maze(maze)

            # Coins creation
            self.coins = self._create_coins()

            # Super Coins creation
            self.super_coins = self._create_super_coins()

        @staticmethod
        def _transform_maze(maze):
            """Method transforms maze object.

            Method return 2 list (floor_pos, wall_pos)
            containing all information needed for draw a board.

            floor_pos - list containing position (row, column)
             of all floor squares

            transformed_maze - transformed maze list,
            instead of 1 (wall) there is a string with
            information about which wall should be draw in
            particular position in maze
            'S' south wall
            'N' north wall
            'E' east wall
            'W' west wall

            :param maze: maze
            :return: floor_pos
            :return: transformed_maze
            """

            floor_pos, transformed_maze, maze_len = [], [], len(maze) - 1
            floor_append = floor_pos.append
            transformed_maze_append = transformed_maze.append

            for row_no, row in enumerate(maze):
                row_len = len(row) - 1

                new_row = []
                new_row_append = new_row.append

                for sq_no, square in enumerate(row):
                    if not square:

                        floor_append([row_no, sq_no])
                        new_row_append(square)

                    else:
                        new_square = []
                        new_square_append = new_square.append
                        if not row_no or not maze[row_no-1][sq_no]:
                            new_square_append("N")
                        if not sq_no or not maze[row_no][sq_no-1]:
                            new_square_append("W")
                        if sq_no == row_len or not maze[row_no][sq_no+1]:
                            new_square_append("E")
                        if row_no == maze_len or not maze[row_no+1][sq_no]:
                            new_square_append("S")
                        new_row_append(''.join(new_square))

                transformed_maze_append(new_row)

            return floor_pos, transformed_maze

        def _create_coins(self):
            """Function creates list of Coin objects as a
            attribute of Board."""

            return [Coin(x, z) for x, z in self.floor_pos]

        def _create_super_coins(self):
            """Function creates list of SuperCoin objects as a
            attribute of Board."""

            return [SuperCoin(x, z)
                    for x, z in [choice(self.floor_pos)
                    for n in range(self.super_coins_no)]]

        @staticmethod
        def load_textures(image):
            """Function loads texture from image file.

            :param image: texture image file
            """
            image = image.tobytes("raw", "RGBX", 0, -1)
            ix, iy = image.size[0], image.size[1]

            # Create Texture
            # 2d texture (x and y size)
            gl.glBindTexture(gl.GL_TEXTURE_2D, gl.glGenTextures(1))

            gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
            gl.glTexImage2D(
                gl.GL_TEXTURE_2D,
                0, 3,
                ix, iy, 0,
                gl.GL_RGBA,
                gl.GL_UNSIGNED_BYTE,
                image
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST
            )
            gl.glTexParameterf(
                gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST
            )
            gl.glTexEnvf(
                gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE, gl.GL_DECAL
            )
            gl.glEnable(gl.GL_TEXTURE_2D)

        @staticmethod
        def _set_color(color):
            """Function set color."""
            r, g, b = color
            gl.glColor3f(r, g, b)

        def _draw_horizontal_square(self, pos_x, pos_z, color, height):
            """ Function draw horizontal square.

            :param pos_x: int, position on x axis of left front corner
            :param pos_z: int, position on z axis of left front corner
            :param color: color, tuple with 3 floats
            :param height: int, position on y axis
            :return:
            """
            pos_x1, pos_z1 = pos_x + 1, pos_z + 1

            gl.glBegin(gl.GL_QUADS)        # Start drawing a polygon
            self._set_color(color)
            gl.glVertex3f(pos_x,  height, pos_z)
            gl.glVertex3f(pos_x1, height, pos_z)
            gl.glVertex3f(pos_x1, height, pos_z1)
            gl.glVertex3f(pos_x,  height, pos_z1)
            gl.glEnd()

        def _draw_vertical_square(self, axis, pos_x, pos_z):
            """ Function draw vertical square on x or z axis.

            :param axis: axis type where square will be draw
                   if axis in "XNS" - square is on X axis
                   if axis in "ZWE" - square is on Z axis
            :param pos_x: int, position on x axis of left front corner
            :param pos_z: int, position on z axis of left front corner
            """

            pos_x1, pos_z1 = pos_x + 1, pos_z + 1
            color_b, color_t = self.floor_color, self.celling_color

            if axis in "XNS":
                if axis == "S":
                    pos_z += 1

                gl.glBegin(gl.GL_QUADS)  # Start drawing a polygon
                self._set_color(color_b)
                gl.glVertex3f(pos_x,  self.wall_bottom, pos_z)  # Top Left
                gl.glVertex3f(pos_x1, self.wall_bottom, pos_z)  # Top Right

                self._set_color(color_t)
                gl.glVertex3f(pos_x1, self.wall_top, pos_z)  # Bottom Right
                gl.glVertex3f(pos_x,  self.wall_top, pos_z)  # Bottom Left
                gl.glEnd()

            elif axis in "ZWE":
                if axis == "E":
                    pos_x += 1

                gl.glBegin(gl.GL_QUADS)  # Start drawing a polygon
                self._set_color(color_b)
                gl.glVertex3f(pos_x, self.wall_bottom, pos_z)  # Top Left
                gl.glVertex3f(pos_x, self.wall_bottom, pos_z1)  # Top Right

                self._set_color(color_t)
                gl.glVertex3f(pos_x, self.wall_top, pos_z1)  # Bottom Right
                gl.glVertex3f(pos_x, self.wall_top, pos_z)  # Bottom Left
                gl.glEnd()

            else:
                print("ERROR during drawing vertical squares:"
                      "function name: board._draw_vertical_square")

        def _draw_floor(self, pos_x, pos_z):
            """ Function draws floor squares."""

            self._draw_horizontal_square(
                pos_x,
                pos_z,
                self.floor_color,
                self.wall_bottom
            )

        def _draw_wall(self, pos_x, pos_z, square):
            """ Function draws wall squares."""

            # draw celling
            self._draw_horizontal_square(
                pos_x,
                pos_z,
                self.celling_color,
                self.wall_top
            )

            # draw back, front, left and right wall
            for axis in "NSWE":
                if axis in square:
                    self._draw_vertical_square(axis, pos_x, pos_z)

        def draw(self):
            """ The main drawing function.

            Function draws all board elements, floor, blocks and coins.
            """

            for row_no, row in enumerate(self.transformed_maze):
                for square_no, square in enumerate(row):
                    if not square:
                        # draw the floor
                        self._draw_floor(square_no, row_no)
                    else:
                        # draw the walls
                        self._draw_wall(square_no, row_no, square)

            # draw the coins
            for coin in self.coins:
                coin.draw()

            # draw the super_coins
            for coin in self.super_coins:
                coin.draw()

    instance = None

    def __init__(self, maze):
        if not SingleBoard.instance:
            SingleBoard.instance = SingleBoard.__Board(maze)
        else:
            return
