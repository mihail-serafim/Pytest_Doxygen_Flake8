## @file Scene.py
#  @author Mihail Serafimovski
#  @brief Defines a scene module
#  @details The scene module is used for simulating a physical
#   environment. A scene features a shape, forces, and initial velocities
#  @date Feb. 10, 2021

import scipy.integrate as sp

## @brief Defines the scene module
#  @details The scene module is used for simulating a physical
#   environment. A scene features a shape, forces, and initial velocities


class Scene:
    ## @brief Constructor for Scene
    #  @param s A shape whose motion is to be simulated
    #  @param F_x A function which inputs and outputs real numbers,
    #         represents the unbalanced force in the x-direction
    #  @param F_x A function which inputs and outputs real numbers,
    #         represents the unbalanced force in the y-direction
    #  @param v_x A real number which is the initial velocity in the x-dir
    #  @param v_y A real number which is the initial velocity in the y-dir
    def __init__(self, s, F_x, F_y, v_x, v_y):

        self.s = s
        self.F_x = F_x
        self.F_y = F_y
        self.v_x = v_x
        self.v_y = v_y

    ## @brief Getter for the scene's shape
    #  @returns A Shape object which is the shape
    #           present in the scene
    def get_shape(self):
        return self.s

    ## @brief Getter for the x and y forces in the scene
    #  @returns A sequence of functions which represent
    #           the unbalanced forces F_x(t) and F_y(t)
    def get_unbal_forces(self):
        return self.F_x, self.F_y

    ## @brief Getter for the x and y initial velocities
    #  @returns A sequence of real numbers which represent
    #           the initial velocities v_x and v_y
    def get_init_velo(self):
        return self.v_x, self.v_y

    ## @brief Setter for the scene's shape
    #  @param new_s Shape object which replaces the scene's current shape
    def set_shape(self, new_s):
        self.s = new_s

    ## @brief Setter for the scene's unbalanced forces
    #  @param new_F_x Function which takes a real number as input
    #                 and outputs a real number representing force in the x-dir
    #  @param new_F_y Function which takes a real number as input
    #                 and outputs a real number representing force in the y-dir
    def set_unbal_forces(self, new_F_x, new_F_y):
        self.F_x = new_F_x
        self.F_y = new_F_y

    ## @brief Setter for the scene's initial velocities
    #  @param new_v_x Real number which represents init. velocity in the x-dir
    #  @param new_v_y Real number which represents init. velocity in the y-dir
    def set_init_velo(self, new_v_x, new_v_y):
        self.v_x = new_v_x
        self.v_y = new_v_y

    ## @brief Simulates motion of the shape in the scene
    #  @details Solves Newton's motion differential equation for
    #           different steps in time
    #  @param t_final A real number which specifies the amount
    #         of time the simulation should run for
    #  @param nsteps A natural number which specifies how many
    #         steps of time there should be in the simulation
    #  @returns A sequence of real numbers representing the time steps and a
    #           second sequence with the results of scipy's odeint calculations
    def sim(self, t_final, nsteps):
        def ode(w, t):
            param_3 = self.F_x(t) / self.s.mass()
            param_4 = self.F_y(t) / self.s.mass()
            return w[2], w[3], param_3, param_4

        t = []
        for i in range(nsteps):
            t.append(i * t_final / (nsteps - 1))

        ode_init_conds = [self.s.cm_x(), self.s.cm_y(), self.v_x, self.v_y]
        return t, sp.odeint(ode, ode_init_conds, t)
