from geomKernel import *
import random


def gift_wrapping(points):

    points_list = sort_points(points)

    vertices = []

    r0 = points_list[0]
    r = r0
    vertices.append(r)


    while True:

        u = random.choice(points_list)

        for t in points_list:
            
            if t == u:
                continue

            if is_CW(r, u, t) or is_collinear(r, u, t):
                u = t

        if u == r0:
            break
        
        r = u
        points_list.remove(r)
        
        vertices.append(r)

    return vertices


if __name__ == '__main__':

    from pprint import pprint

    points_list = gen_random_points(80, 2)
    hull_points = gift_wrapping(points_list)

    pprint(hull_points)
    show_convexHull(hull_points, points_list, title='Gift Wrapping')

