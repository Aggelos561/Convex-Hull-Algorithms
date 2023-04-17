import numpy as np
from geomKernel import *
from quickHull import *



def get_bridge(cPoints1, cPoints2, mode):

    c1_size = len(cPoints1)
    c2_size = len(cPoints2)

    first_iter = True
    flag_a = False
    flag_b = False

    while True:

        if first_iter:
            a_index = get_rightmost_index(cPoints1)
            b_index = get_leftmost_index(cPoints2)
            first_iter = False
        
        else:
            if flag_a:
                a_index = get_next_index_a(a_index, c1_size, mode)
                flag_a = False
            if flag_b:    
                b_index = get_next_index_b(b_index, c2_size, mode)
                flag_b = False

        a_index_next = get_next_index_a(a_index, c1_size, mode)
        b_index_prev = get_next_index_b(b_index, c2_size, mode)

        a_random = cPoints1[0]
        while True:
            a_random = random.choice(cPoints1)
            if a_random != cPoints1[a_index] and a_random != cPoints1[a_index_next]:
                break

        b_random = cPoints2[0]
        while True:
            b_random = random.choice(cPoints2)
            if b_random != cPoints2[b_index] and b_random != cPoints2[b_index_prev]:
                break

        flag_a, flag_b = check_subspace(cPoints1, cPoints2, a_index, a_index_next, a_random, b_index, b_index_prev, b_random, mode)

        if flag_a or flag_b:
            continue
        else:
            return [cPoints1[a_index], cPoints2[b_index]]


def merge(convexPoints1, convexPoints2):
    
    upper_points = get_bridge(convexPoints1, convexPoints2, 'upper')
    lower_points = get_bridge(convexPoints1, convexPoints2, 'lower')

    convex = []
    
    print(upper_points)
    print(lower_points)

    p_left = convexPoints1[get_leftmost_index(convexPoints1)]

    found_start = False
    stop_circle = False
    while True:
        for p1 in convexPoints1:
            
            if p1 == p_left and not found_start:
                found_start = True
            
            if found_start:
                convex.append(p1)

                if p1 == lower_points[0]:
                    convex.append(lower_points[1])
                    stop_circle = True
                    break
        
        if stop_circle:
            break

    found_start = False
    stop_circle = False
    while True:

        print('AAA')
        for p2 in convexPoints2:

            if p2 == lower_points[1] and not found_start:
                found_start = True
                continue
            
            if found_start:
                convex.append(p2)

                if p2 == upper_points[1]:
                    
                    convex.append(upper_points[0])
                    stop_circle = True
                    break
        
        if stop_circle:
            break

    found_start = False
    stop_circle = False
    while True:

        print('BBB')
        for p1 in convexPoints1:

            if p1 == upper_points[0] and not found_start:
                
                if p1 == convex[0]:
                    stop_circle = True
                    break

                found_start = True
                continue

            if found_start:
                if p1 != convex[0]:
                    convex.append(p1)
                else:
                    stop_circle = True
                    break
                    
        if stop_circle:
            break

    return convex

def split(points):

    grouped_points = np.array_split(points, 2)
    points1, points2 = list(tuple(p) for p in grouped_points[0]), list(tuple(p) for p in grouped_points[1])

    if len(points1) <= 6 or len(points2) <= 6:
        convexPoints1 = quickHull(points1)
        convexPoints2 = quickHull(points2)
        
        return merge(convexPoints1, convexPoints2)
    
    convex1 = split(points1)
    convex2 = split(points2)

    return merge(convex1, convex2)



def divideAndConquer(points):

    points_list = sort_points(points)
    return split(points_list)




if __name__ == '__main__':
    points_list = gen_random_points(random.randint(100, 130), 2)
    vertices = divideAndConquer(points_list)
    show_convexHull(vertices, points_list)
