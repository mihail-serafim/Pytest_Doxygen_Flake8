## @file test_driver.py
#  @author Mihail Serafimovski
#  @brief My test driver, using pytest
#  @date Jan. 10, 2021

from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene

import pytest
import math
from random import randrange
import scipy.integrate as sp

### CircleT ###


def test_CircleT_exception1():
    with pytest.raises(ValueError):
        CircleT(0, 0, 0, 1)


def test_CircleT_exception2():
    with pytest.raises(ValueError):
        CircleT(0, 0, 1, 0)


def test_CircleT_cm_x_1():
    assert CircleT(-289, 10454, 1, 1).cm_x() == -289


def test_CircleT_cm_x_2():
    assert CircleT(0, 0, 1, 1).cm_x() == 0


def test_CircleT_cm_y_1():
    assert CircleT(-289, 10454, 1, 1).cm_y() == 10454


def test_CircleT_cm_y_2():
    assert CircleT(0, 0, 1, 1).cm_y() == 0


def test_CircleT_mass_1():
    assert CircleT(-289, 10454, 1, 1).mass() == 1


def test_CircleT_mass_2():
    assert CircleT(0, 0, 1, 8930293400).mass() == 8930293400


def test_CircleT_m_intert_1():
    assert CircleT(-289, 10454, 289, 10454).m_inert() == 436564267


def test_CircleT_m_inert_2():
    assert CircleT(0, 0, 1, 1).m_inert() == 0.5

### TriangleT ###


def test_TriangleT_exception1():
    with pytest.raises(ValueError):
        TriangleT(0, 0, 0, 1)


def test_TriangleT_exception2():
    with pytest.raises(ValueError):
        TriangleT(0, 0, 1, 0)


def test_TriangleT_cm_x_1():
    assert TriangleT(-289, 10454, 1, 1).cm_x() == -289


def test_TriangleT_cm_x_2():
    assert TriangleT(0, 0, 1, 1).cm_x() == 0


def test_TriangleT_cm_y_1():
    assert TriangleT(-289, 10454, 1, 1).cm_y() == 10454


def test_TriangleT_cm_y_2():
    assert TriangleT(0, 0, 1, 1).cm_y() == 0


def test_TriangleT_mass_1():
    assert TriangleT(-289, 10454, 1, 1).mass() == 1


def test_TriangleT_mass_2():
    assert TriangleT(0, 0, 1, 8930293400).mass() == 8930293400


def test_TriangleT_m_intert_1():
    assert round(TriangleT(-289, 10454, 289, 10454).m_inert()) == 72760711


def test_TriangleT_m_inert_2():
    m_inert = TriangleT(0, 0, 1, 1).m_inert()
    assert math.isclose(m_inert, 0.0833333, rel_tol=0.0001)

### BodyT ###


def test_BodyT_exception1():
    with pytest.raises(ValueError):
        BodyT([0, 0, 0], [0, 0, 0], [0, 0, 0, 0])


def test_BodyT_exception2():
    with pytest.raises(ValueError):
        BodyT([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1])


def test_BodyT_cm_x_1():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]

    assert BodyT(x, y, m).cm_x() == cm(x, m)


def test_BodyT_cm_x_2():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).cm_x() == cm(x, m)


def test_BodyT_cm_y_1():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).cm_y() == cm(y, m)


def test_BodyT_cm_y_2():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).cm_y() == cm(y, m)


def test_BodyT_mass_1():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).mass() == sum(m)


def test_BodyT_mass_2():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).mass() == sum(m)


def test_BodyT_m_intert_1():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).m_inert() == moment(x, y, m)


def test_BodyT_m_inert_2():
    length = randrange(10e4)
    x = [randrange(-10e6, 10e6) for _ in range(length)]
    y = [randrange(-10e6, 10e6) for _ in range(length)]
    m = [randrange(1, 10e6) for _ in range(length)]
    assert BodyT(x, y, m).m_inert() == moment(x, y, m)

### SCENE ###


def test_Scene_get_shape_c():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    r = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    c = CircleT(x, y, r, m)
    assert Scene(c, F_x, F_y, v_x, v_y).get_shape() == c


def test_Scene_get_shape_t():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)
    assert Scene(t, F_x, F_y, v_x, v_y).get_shape() == t


def test_Scene_get_shape_b():
    length = randrange(10e4)
    x_s = [randrange(-10e6, 10e6) for _ in range(length)]
    y_s = [randrange(-10e6, 10e6) for _ in range(length)]
    m_s = [randrange(1, 10e6) for _ in range(length)]

    b = BodyT(x_s, y_s, m_s)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    assert Scene(b, F_x, F_y, v_x, v_y).get_shape() == b


def test_Scene_get_unbal_forces_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)
    assert Scene(t, F_x, F_y, v_x, v_y).get_unbal_forces() == (F_x, F_y)


def test_Scene_get_unbal_forces_2():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return 0

    def F_y(t):
        return 0

    t = TriangleT(x, y, s, m)
    assert Scene(t, F_x, F_y, v_x, v_y).get_unbal_forces() == (F_x, F_y)


def test_Scene_get_init_velo_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)
    assert Scene(t, F_x, F_y, v_x, v_y).get_init_velo() == (v_x, v_y)


def test_Scene_get_init_velo_2():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = 0
    v_y = 0

    def F_x(t):
        return 0

    def F_y(t):
        return 0

    t = TriangleT(x, y, s, m)
    assert Scene(t, F_x, F_y, v_x, v_y).get_init_velo() == (v_x, v_y)


def test_Scene_set_shape_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    length = randrange(10e4)
    x_s = [randrange(-10e6, 10e6) for _ in range(length)]
    y_s = [randrange(-10e6, 10e6) for _ in range(length)]
    m_s = [randrange(1, 10e6) for _ in range(length)]

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)
    b = BodyT(x_s, y_s, m_s)

    scene = Scene(t, F_x, F_y, v_x, v_y)
    scene.set_shape(b)

    assert scene.get_shape() == b


def test_Scene_set_shape_2():

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    length = randrange(10e4)
    x_s = [randrange(-10e6, 10e6) for _ in range(length)]
    y_s = [randrange(-10e6, 10e6) for _ in range(length)]
    m_s = [randrange(1, 10e6) for _ in range(length)]

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    b = BodyT(x_s, y_s, m_s)

    scene = Scene(b, F_x, F_y, v_x, v_y)
    scene.set_shape(b)

    assert scene.get_shape() == b


def test_Scene_set_unbal_forces_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def new_F_x(t):
        return randrange(100, 1000) * t + randrange(-50, 50)

    def new_F_y(t):
        return randrange(-1000, -100) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)
    scene.set_unbal_forces(new_F_x, new_F_y)

    assert scene.get_unbal_forces() == (new_F_x, new_F_y)


def test_Scene_set_unbal_forces_2():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def new_F_x(t):
        return 0

    def new_F_y(t):
        return 0

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)
    scene.set_unbal_forces(new_F_x, new_F_y)

    assert scene.get_unbal_forces() == (new_F_x, new_F_y)


def test_Scene_set_unbal_forces_3():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)
    scene.set_unbal_forces(F_x, F_y)

    assert scene.get_unbal_forces() == (F_x, F_y)


def test_Scene_set_init_velo_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)

    new_v_x = randrange(-10e6, 10e6)
    new_v_y = randrange(-10e6, 10e6)

    scene.set_init_velo(new_v_x, new_v_y)

    assert scene.get_init_velo() == (new_v_x, new_v_y)


def test_Scene_set_init_velo_2():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)
    scene.set_init_velo(v_x, v_y)

    assert scene.get_init_velo() == (v_x, v_y)


def test_Scene_sim_1():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    t_final = randrange(1, 1000)
    nsteps = randrange(100, 100000)

    def F_x(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    def F_y(t):
        return randrange(-50, 50) * t + randrange(-50, 50)

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)

    mass = scene.get_shape().mass()

    def ode(w, t):
        return w[2], w[3], F_x(t) / mass, F_y(t) / mass

    cm_x = scene.get_shape().cm_x()
    cm_y = scene.get_shape().cm_y()

    results = scene.sim(t_final, nsteps)
    t_result = results[0]
    w_result = results[1]
    v = scene.get_init_velo()

    t_calc = [i * t_final / (nsteps - 1) for i in range(nsteps)]
    w_calc = sp.odeint(ode, [cm_x, cm_y, v[0], v[1]], t_calc)

    w_success = True
    for i, j in zip(w_calc, w_result):
        for a, b in zip(i, j):
            if not math.isclose(a, b, rel_tol=0.0001):
                w_success = False

    assert t_result == t_calc and w_success


def test_Scene_sim_2():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = 0
    v_y = 0

    t_final = randrange(1, 1000)
    nsteps = randrange(100, 100000)

    def F_x(t):
        return 0

    def F_y(t):
        return 0

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)

    mass = scene.get_shape().mass()

    def ode(w, t):
        return w[2], w[3], F_x(t) / mass, F_y(t) / mass

    cm_x = scene.get_shape().cm_x()
    cm_y = scene.get_shape().cm_y()

    results = scene.sim(t_final, nsteps)
    t_result = results[0]
    w_result = results[1]
    v = scene.get_init_velo()

    t_calc = [i * t_final / (nsteps - 1) for i in range(nsteps)]
    w_calc = sp.odeint(ode, [cm_x, cm_y, v[0], v[1]], t_calc)

    w_success = True
    for i, j in zip(w_calc, w_result):
        for a, b in zip(i, j):
            if not math.isclose(a, b, rel_tol=0.0001):
                w_success = False

    assert t_result == t_calc and w_success


def test_Scene_sim_3():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    t_final = randrange(1, 1000)
    nsteps = randrange(100, 100000)

    def F_x(t):
        return 0

    def F_y(t):
        return -9.81 * m

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)

    mass = scene.get_shape().mass()

    def ode(w, t):
        return w[2], w[3], F_x(t) / mass, F_y(t) / mass

    cm_x = scene.get_shape().cm_x()
    cm_y = scene.get_shape().cm_y()

    results = scene.sim(t_final, nsteps)
    t_result = results[0]
    w_result = results[1]
    v = scene.get_init_velo()

    t_calc = [i * t_final / (nsteps - 1) for i in range(nsteps)]
    w_calc = sp.odeint(ode, [cm_x, cm_y, v[0], v[1]], t_calc)

    w_success = True
    for i, j in zip(w_calc, w_result):
        for a, b in zip(i, j):
            if not math.isclose(a, b, rel_tol=0.0001):
                w_success = False

    assert t_result == t_calc and w_success


def test_Scene_sim_4():
    x = randrange(-10e6, 10e6)
    y = randrange(-10e6, 10e6)
    s = randrange(1, 10e6)
    m = randrange(1, 10e6)

    v_x = randrange(-10e6, 10e6)
    v_y = randrange(-10e6, 10e6)

    t_final = randrange(1, 1000)
    nsteps = randrange(100, 100000)

    def F_x(t):
        if t > 100:
            return 0
        else:
            return t**2

    def F_y(t):
        if t < 40:
            return -9.81 * m
        else:
            return 9.81 * m

    t = TriangleT(x, y, s, m)

    scene = Scene(t, F_x, F_y, v_x, v_y)

    mass = scene.get_shape().mass()

    def ode(w, t):
        return w[2], w[3], F_x(t) / mass, F_y(t) / mass

    cm_x = scene.get_shape().cm_x()
    cm_y = scene.get_shape().cm_y()

    results = scene.sim(t_final, nsteps)
    t_result = results[0]
    w_result = results[1]
    v = scene.get_init_velo()

    t_calc = [i * t_final / (nsteps - 1) for i in range(nsteps)]
    w_calc = sp.odeint(ode, [cm_x, cm_y, v[0], v[1]], t_calc)

    w_success = True
    for i, j in zip(w_calc, w_result):
        for a, b in zip(i, j):
            if not math.isclose(a, b, rel_tol=0.0001):
                w_success = False

    assert t_result == t_calc and w_success

### HELPER FUNCTIONS ###


def cm(z, m):
    weighted_sum = 0
    for i in range(len(z)):
        weighted_sum += z[i] * m[i]

    return weighted_sum / sum(m)


def moment(x, y, m):
    def mmom(x, y, m):

        running_sum = 0
        for i in range(len(x)):
            running_sum += m[i] * (x[i]**2 + y[i]**2)

        return running_sum

    cm_x = cm(x, m)
    cm_y = cm(y, m)

    mass = sum(m)

    return mmom(x, y, m) - mass * (cm_x**2 + cm_y**2)
