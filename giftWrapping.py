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
    points_list = gen_random_points(random.randint(10, 80), 2)
    vertices = gift_wrapping(points_list)
    show_convexHull(vertices, points_list)

