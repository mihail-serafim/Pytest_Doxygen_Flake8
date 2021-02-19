## @file CircleT.py
#  @author Mihail Serafimovski
#  @brief Defines a circle ADT
#  @date Jan. 10, 2021

from Shape import Shape

## @brief Defines a circle ADT. Assumption: Assume all inputs
#         provided to methods are of the correct type
#  @details Extends the Shape interface


class CircleT(Shape):
    ## @brief Constructor for CircleT
    #  @param x A real number which is the x-component of the center of mass
    #  @param y A real number which is the y-component of the center of mass
    #  @param r A real number which is the radius of the circle
    #  @param m A real number which is the mass of the circle
    #  @throws ValueError if the radius or mass are not both greater than zero
    def __init__(self, x, y, r, m):
        if not(r > 0 and m > 0):
            raise ValueError

        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief Getter for x-component of center of mass
    #  @returns A real number which is the x-component
    #           of the circle's center of mass
    def cm_x(self):
        return self.x

    ## @brief Getter for y-component of center of mass
    #  @returns A real number which is the y-component
    #           of the circle's center of mass
    def cm_y(self):
        return self.y

    ## @brief Getter for mass of circle
    #  @returns A real number which is the mass of the circle
    def mass(self):
        return self.m

    ## @brief Getter for moment of inertia of the circle
    #  @returns A real number which is the moment of inertia of the circle
    def m_inert(self):
        return self.m * (self.r**2) / 2

    ## @brief Method to help with object comparison when testing
    #  @param other Another shape to test for equality
    #  @returns A boolean, true iff both objects have the same state variables
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
