from scipy.spatial import ConvexHull
from geomKernel import *
import random


def quickHull(points):
    return [points[index] for index in ConvexHull(points, qhull_options="QJ").vertices]

def quickHull3D(points):
    return ConvexHull(points, qhull_options="QJ").vertices


if __name__ == '__main__':

    points_list = gen_random_points(random.randint(10, 80), 2)
    vertices = quickHull(points_list)
    show_convexHull(vertices, points_list)

    points = np.array([np.array(p) for p in gen_random_points(random.randint(10, 80), 3)])
    hull = ConvexHull(points)
    show_convexHull3D(hull, points)
