import numpy as np
import matplotlib.pyplot as plt



def gen_random_points(size, dim):
    rng = np.random.default_rng()
    return [tuple(p) for p in rng.random((size, dim), dtype=np.float64)]


def sort_points(points, ascending=True):
    return sorted(points) if ascending else sorted(points, reverse=not ascending)


def show_convexHull(vertices, points):

    plt.scatter([p[0] for p in points], [p[1] for p in points])

    x = [p[0] for p in vertices]
    y = [p[1] for p in vertices]

    for i in range(len(vertices)):
        plt.plot([x[i], x[(i+1) % len(vertices)]], [y[i], y[(i+1) % len(vertices)]], 'bo--')
    
    plt.show()

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


def CCW(x1, x2, x3):
    matrix = create_orientation_matrix(x1, x2, x3)
    return -1 if np.linalg.det(matrix) > 0 else 1


def points_equal(x1, x2):
    for p1, p2 in zip(x1, x2):
        if p1 != p2:
            return False

    return True


def get_rightmost_index(points):
    return points.index(max(points))


def get_leftmost_index(points):
    return points.index(min(points))


def get_next_index_a(a_index, p_size, mode):

    if mode == 'upper':
        return (a_index + 1) % p_size
    else:
        return  a_index - 1 if a_index - 1 >= 0 else p_size - 1


def get_next_index_b(b_index, p_size, mode):

    if mode == 'upper':
        return b_index - 1 if b_index - 1 >= 0 else p_size - 1
    else:
        return (b_index + 1) % p_size
    

def check_subspace(cPoints1, cPoints2, a_index, a_index_next, a_random, b_index, b_index_prev, b_random, mode):

    flag_a = False
    flag_b = False

    if mode == 'upper':
        if not (is_CCW(cPoints1[a_index], cPoints1[a_index_next], a_random) and is_CCW(cPoints1[a_index], cPoints1[a_index_next], cPoints2[b_index])):
            flag_a = True
        
        if not (is_CW(cPoints2[b_index], cPoints2[b_index_prev], b_random) and is_CW(cPoints2[b_index], cPoints2[b_index_prev], cPoints1[a_index])):
            flag_b= True

    else:
        if (is_CW(cPoints1[a_index], cPoints1[a_index_next], a_random) and is_CCW(cPoints1[a_index], cPoints1[a_index_next], cPoints2[b_index])):
            flag_a = True
        
        if (is_CCW(cPoints2[b_index], cPoints2[b_index_prev], b_random) and is_CW(cPoints2[b_index], cPoints2[b_index_prev], cPoints1[a_index])):
            flag_b= True

    return flag_a, flag_b


def create_segments(points):

    segments = []

    points_size = len(points)

    for i in range(points_size):
        segments.append((points[i], points[(i + 1) % points_size]))
    
    return segments
