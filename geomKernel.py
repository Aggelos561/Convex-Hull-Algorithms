import numpy as np
import matplotlib.pyplot as plt



def gen_random_points(size, dim):
    rng = np.random.default_rng()
    return [tuple(p) for p in rng.random((size, dim))]


def sort_points(points):
    return sorted(points, key = lambda p: (p[0], p[1]))


def show_convexHull(vertices, points):

    plt.scatter([p[0] for p in points], [p[1] for p in points])

    x = [p[0] for p in vertices]
    y = [p[1] for p in vertices]

    for i in range(len(vertices)):
        plt.plot([x[i], x[(i+1) % len(vertices)]], [y[i], y[(i+1) % len(vertices)]], 'bo--')
    


def create_orientation_matrix(x1, x2, x3):
    return np.array([[1, x1[0], x1[1]], [1, x2[0], x2[1]], [1, x3[0], x3[1]]])


def is_collinear(x1, x2, x3):
    matrix = create_orientation_matrix(x1, x2, x3)
    return True if not np.linalg.det(matrix) else False


def is_CW(x1, x2, x3):
    matrix = create_orientation_matrix(x1, x2, x3)
    return True if np.linalg.det(matrix) < 0 else False


def is_CCW(x1, x2, x3):
    matrix = create_orientation_matrix(x1, x2, x3)
    return True if np.linalg.det(matrix) > 0 else False


def points_equal(x1, x2):
    for p1, p2 in zip(x1, x2):
        if p1 != p2:
            return False

    return True
