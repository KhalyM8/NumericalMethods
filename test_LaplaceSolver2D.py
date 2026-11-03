from LaplaceSolver2D import solve2DLaplace
import numpy as np

def test_solver():
    assert np.allclose(solve2DLaplace(9,dx=0.1,dy=0.1, top=100,bottom=0,left=20,right=40), np.array([54.28571429, 63.92857143, 61.42857143,
        33.21428571, 40.00000000, 41.78571429,
        18.57142857, 21.07142857, 25.71428571])) #Sqaure Geometry Test
    assert np.allclose(solve2DLaplace(12,dx=0.1,dy=0.1, top=100,bottom=0,left=20,right=40, nCols=3,nRows=4), np.array([
    55.55188413, 65.74284416, 62.82461140,
    36.46469236, 44.59488111, 45.55560145,
    25.71200419, 30.61638649, 34.80291328,
    15.76693789, 17.35574739, 23.03966517,
])) #More Rows than Columns Test
    assert np.allclose(solve2DLaplace(12, dx=0.1,dy=0.1,top=100,bottom=0,left=20,right=40, nCols=4,nRows=3), np.array([
    54.90754891, 66.01820109, 68.16873873, 62.86453816,
    33.61199455, 40.99651673, 43.79221566, 43.28941390,
    18.54391255, 20.56365564, 22.71419327, 26.50090179,
])) #More Columns than Rows Test

