## @file BodyT.py
#  @author Mihail Serafimovski
#  @brief Defines an ADT which specifies a body (a collection of point masses)
#  @date Jan. 10, 2021

from Shape import Shape

## @brief Defines a body ADT. Assumption: Assume all inputs
#         provided to methods are of the correct type
#  @details Extends the Shape interface. A body can be visualized
#           as a set of point-masses in 2-d space.


class BodyT(Shape):
    ## @brief Constructor for BodyT
    #  @param x_s A sequence of real numbers which
    #             are the x-component of each point mass
    #  @param y_s A sequence of real numbers which
    #             are the y-component of each point mass
    #  @param m_s A sequence of real numbers which
    #             are the mass of each point mass
    #  @throws ValueError if the the moment of inertia or mass
    #          are invalid values, or if the sequences x_s, y_s,
    #           and m_s aren't the same length
    def __init__(self, x_s, y_s, m_s):
        if not(len(x_s) == len(y_s) and len(y_s) == len(m_s)):
            raise ValueError

        for mass in m_s:
            if not(mass > 0):
                raise ValueError

        cm_x = self.__cm__(x_s, m_s)
        cm_y = self.__cm__(y_s, m_s)
        m = sum(m_s)

        self.cmx = cm_x
        self.cmy = cm_y
        self.m = m

        moment = self.__mmom__(x_s, y_s, m_s) - m * (cm_x**2 + cm_y**2)
        self.moment = moment

    ## @brief Getter for x-component of center of mass
    #  @returns A real number which is the x-component
    #           of the body's center of mass
    def cm_x(self):
        return self.cmx

    ## @brief Getter for y-component of center of mass
    #  @returns A real number which is the y-component
    #           of the body's center of mass
    def cm_y(self):
        return self.cmy

    ## @brief Getter for mass of body
    #  @returns A real number which is the mass of the body
    def mass(self):
        return self.m

    ## @brief Getter for moment of inertia of the body
    #  @returns A real number which is the moment of inertia of the body
    def m_inert(self):
        return self.moment

    ## @brief helper method to calculate center of mass of body
    #  @param z A sequence of real numbers which are 1-dimensional positions
    #  @param m A sequence of real numbers which are the masses of the points
    #  @return A real number which is the 1-d center of mass of the points
    def __cm__(self, z, m):
        weighted_sum = 0
        for i in range(len(z)):
            weighted_sum += z[i] * m[i]

        return weighted_sum / sum(m)

    ## @brief helper method to calculate the moment of inertia of the body
    #  @param x A sequence of real numbers which are the x-coords of the points
    #  @param y A sequence of real numbers which are the y-coords of the points
    #  @param m A sequence of real numbers which are the masses of the points
    #  @return A real number which helps calculate the moment of inertia
    def __mmom__(self, x, y, m):

        running_sum = 0
        for i in range(len(x)):
            running_sum += m[i] * (x[i]**2 + y[i]**2)

        return running_sum

    ## @brief Method to help with object comparison when testing
    #  @param other Another shape to test for equality
    #  @returns A boolean, true iff both objects have the same state variables
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
