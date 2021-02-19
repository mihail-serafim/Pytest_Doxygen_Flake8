## @file TriangleT.py
#  @author Mihail Serafimovski
#  @brief Defines a triangle ADT
#  @date Jan. 10, 2021

from Shape import Shape

## @brief Defines a triangle ADT. Assumption: Assume all inputs
#         provided to methods are of the correct type
#  @details Extends the Shape interface


class TriangleT(Shape):
    ## @brief Constructor for TriangleT
    #  @param x A real number which is the x-component of the center of mass
    #  @param y A real number which is the y-component of the center of mass
    #  @param s A real number which is the side length of the triangle
    #  @param m A real number which is the mass of the triangle
    #  @throws ValueError if the side length or mass are invalid values
    def __init__(self, x, y, s, m):
        if not(s > 0 and m > 0):
            raise ValueError

        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Getter for x-component of center of mass
    #  @returns A real number which is the x-component
    #           of the triangle's center of mass
    def cm_x(self):
        return self.x

    ## @brief Getter for y-component of center of mass
    #  @returns A real number which is the y-component
    #           of the triangle's center of mass
    def cm_y(self):
        return self.y

    ## @brief Getter for mass of triangle
    #  @returns A real number which is the mass of the triangle
    def mass(self):
        return self.m

    ## @brief Getter for moment of inertia of the triangle
    #  @returns A real number which is the moment of inertia of the triangle
    def m_inert(self):
        return self.m * (self.s**2) / 12

    ## @brief Method to help with object comparison when testing
    #  @param other Another shape to test for equality
    #  @returns A boolean, true iff both objects have the same state variables
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
