# Convex Hull Algorithms in Python

## Algorithms Included

1. **Beneath Beyond Convex Hull Algorithm**
   - File: `beneathBeyond.py`
   - The Beneath Beyond algorithm is implemented here to compute the convex hull of a set of points in 2D space.

2. **Divide and Conquer Convex Hull Algorithm**
   - File: `divideAndConquer.py`
   - This repository includes a Divide and Conquer algorithm to efficiently find the convex hull of a set of points.

3. **Gift Wrapping Convex Hull Algorithm**
   - File: `giftWrapping.py`
   - The Gift Wrapping algorithm, also known as the Jarvis March algorithm, is implemented here to calculate the convex hull of a set of points.

4. **Quickhull Algorithm with scipy for 2D and 3D Convex Hull**
   - File: `quickHull.py`
   - The Quickhull algorithm is implemented using the scipy library to find the convex hull of 2D and 3D point sets.

## Utility Functions

1. **geomKernel.py**
   - File: `geomKernel.py`
   - This file contains essential helper functions used by all the convex hull algorithms implemented in this repository.
     
## Additional Scripts

1. **collinearTest.py**
   - File: `collinearTest.py`
   - The `collinearTest.py` script checks the convex hulls that have collinear points. It validates the algorithms' behavior and correctness when dealing with collinear cases.

2. **calcTime.py**
   - File: `calcTime.py`
   - The `calcTime.py` script measures the execution time of each convex hull algorithm for different point set sizes. It provides insights into the algorithm's performance under varying input scenarios.

## Visualization

1. **Visualize Beneath Beyond Convex Hull**
   - File: `visualizeBeneathBeyond.py`
   - For better understanding and debugging, the `visualizeBeneathBeyond.py` script offers step-by-step visualization of the Beneath Beyond algorithm. It helps visualize the construction of the convex hull at each iteration.

## Execution

2. Run any of the algorithms:

   ```bash
   python beneathBeyond.py
   python divideAndConquer.py
   python giftWrapping.py
   python quickHull.py
   python collinearTest.py
   python calcTime.py
   python visualizeBeneathBeyond.py
   ```
