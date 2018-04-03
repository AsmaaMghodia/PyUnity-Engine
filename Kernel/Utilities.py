"""
    This is the Utilities module.

    the Utilities has:
        Vector3: A Universal class that describe a direction in a 3d space, it also works as 3 element array.

        Transform2D: A Universal class that describe the orientation of a game object in a 2d space.

    -- Author : AbdElAziz Mofath
    -- Date: 4th of April 2018 at 7:40 PM
"""

import math
from OpenGL.GL import *


class Vector3:
    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "}"

    def __init__(self, x, y, z):
        """

        :param x: x value
        :param y: y value
        :param z: z value
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        newVec = Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z)
        return newVec

    def __sub__(self, other):
        newVec = Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z)
        return newVec

    def __mul__(self, i):
        return Vector3(self.x * i, self.y * i, self.z * i)

    def __truediv__(self, i):
        return Vector3(self.x / i, self.y / i, self.z / i)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def setValues(self, x, y, z):
        """
        set the values of the vector

        :param x: x
        :param y: y
        :param z: z
        """
        self.x = x
        self.y = y
        self.z = z

    def normalized(self, ):
        """
        This function makes a copy of the current vector, Then normalize it so that its length be exactly one.

        * Doesnt affect the current vector values.

        :return: Vector3
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if length == 0:
            return Vector3(0, 0, 0)
        else:
            Nx = self.x / length
            Ny = self.y / length
            Nz = self.z / length
            return Vector3(Nx, Ny, Nz)

    def normalize(self, ):
        """
            Normalize the current vector so that its length be exactly one.

            * Change the current values of the vector
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if length == 0:
            self.x, self.y, self.z = 0, 0, 0
        else:
            self.x = self.x / length
            self.y = self.y / length
            self.z = self.z / length

    def cross(self, vec):
        """
        the cross product of multiplying the current vector by vector vec
        * Doesnt affect the current vector values.

        :param vec: vector b in the notation cross = a * b
        :return: Vector3
        """
        newVec = Vector3(self.y * vec.z - self.z * vec.y,
                         self.z * vec.x - self.x * vec.z,
                         self.x * vec.y - self.y * vec.x)
        return newVec

    def magnitude(self, ):
        """
        The length of the vector.

        :return: float: the length of the vector
        """
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return length


class Transform2D:
    def __init__(self, ):
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)

        self.__up = Vector3(0, 1, 0)
        self.__right = Vector3(1, 0, 0)

    def applyTransformation(self):
        """
            Apply the current transformation to the game object
        """
        glTranslatef(self.position.x, self.position.y, self.position.z)

        glRotatef(self.rotation.x, 1, 0, 0)
        glRotatef(self.rotation.y, 0, 1, 0)
        glRotatef(self.rotation.z, 0, 0, 1)

        glScalef(self.scale.x, self.scale.y, self.scale.z)

    def up(self):
        """
        the normalized up direction of the game object
        :return: Vector3
        """

        ang = math.radians(self.rotation.z)
        return Vector3(math.sin(ang), math.cos(ang), 0)

    def right(self):
        """
        the normalized right direction of the game object
        :return: Vector3
        """

        ang = math.radians(self.rotation.z)
        return Vector3(math.cos(ang), -math.sin(ang), 0)
