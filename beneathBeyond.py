import numpy as np
from geomKernel import *
from quickHull import *
import random



def find_possible_reds(segments, point):

    possible_reds = []

    for p1, p2 in segments:
        if p1 == point or p2 == point:
            possible_reds.append((p1, p2))
        
    return possible_reds


def find_known_point(red_seg, convex_points):
    
    point = convex_points[0]
    while True:
        point = random.choice(convex_points)

        if point != red_seg[0] and point != red_seg[1]:
            return point


def find_red_segment(possible_reds, point, convex_points):
    
    print(f'point = {point}')

    for possible_red in possible_reds:

        a1 = find_known_point(possible_red, convex_points)
        print(possible_red)
        print(a1)

        # Red
        if CCW(possible_red[0], possible_red[1], point) * CCW(possible_red[0], possible_red[1], a1) < 0:
           return possible_red
    
    return None




def beneathBeyond(points):
    
    points_list = sort_points(points, ascending=False)
    points_size = len(points_list)

    triangle_points = [p for p in reversed(points_list[:3])]
    
    convex_points = triangle_points
    convex_segments = create_segments(triangle_points)

    for k in range(3, points_size):
        
        point = points_list[k]

        possible_reds = find_possible_reds(convex_segments, points_list[k-1])

        red_segment = find_red_segment(possible_reds, point, convex_points)

        print(f'red segment = {red_segment}')
        break

    return triangle_points




if __name__ == '__main__':
    points_list = gen_random_points(random.randint(8, 8), 2)
    vertices = beneathBeyond(points_list)
    show_convexHull(vertices, points_list)
