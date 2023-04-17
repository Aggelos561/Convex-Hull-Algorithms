from scipy.spatial import ConvexHull
from geomKernel import *
import random


def quickHull(points):
    return [points[index] for index in ConvexHull(points, qhull_options="QJ").vertices]


if __name__ == '__main__':
    points_list = gen_random_points(random.randint(3, 50), 2)
    vertices = quickHull(points_list)
    show_convexHull(vertices, points_list)
