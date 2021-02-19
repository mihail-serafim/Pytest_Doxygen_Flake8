## @file Shape.py
#  @author Mihail Serafimovski
#  @brief Defines a Shape interface module
#  @date Jan. 10, 2021

from abc import ABC, abstractmethod

## @brief Shape defines a Shape interface module
#  @details The Shape interface provides abstract methods
#   which need to be overwritten by classes that inherit it


class Shape(ABC):

    @abstractmethod
    ## @brief A generic method related to the x-componenet of the
    #   shape's center of mass
    #  @return A real number which is the x-component of the shape's CM
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief A generic method related to the y-componenet of the
    #   shape's center of mass
    #  @return A real number which is the y-component of the shape's CM
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief a generic method representing the mass of the shape
    #  @return a real number which is the mass of the shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief a generic method representing the moment of inertia of the shape
    #  @return a real number which is the moment of inertia of the shape
    def m_inert(self):
        pass
