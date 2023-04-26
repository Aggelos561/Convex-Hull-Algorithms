from scipy.spatial import ConvexHull
from geomKernel import *


def quickHull(points):
    return [points[index] for index in ConvexHull(points, qhull_options="QJ Pp").vertices]

def quickHull3D(points):
    return ConvexHull(points, qhull_options="QJ").vertices


if __name__ == '__main__':

    from pprint import pprint

    points_list = gen_random_points(80, 2)
    hull_points = quickHull(points_list)

    pprint(hull_points)
    show_convexHull(hull_points, points_list, title='Quick Hull')


    points = np.array([np.array(p) for p in gen_random_points(50, 3)])
    hull = ConvexHull(points)

    pprint(hull.points)
    show_convexHull3D(hull, points)
