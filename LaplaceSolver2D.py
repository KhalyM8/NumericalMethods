import numpy as np
import matplotlib.pyplot as plt

"""
The Variables are explained below:
nVariables - Amount of unknown Variables
nRows - Amount of Rows
nCol - Amount of Columns
dx - the spacing in the x direction
dy - the spacing in the y direction
top - boundary conditions for the top (Must be Uniform)
bottom - boundary conditions for the bottom (Must be uniform)
left - boundary conditions for the left side (Must be uniform)
right - boudnary conditions for the right side (Must be uniform)
nRowElements - number of elements in Rows
nColElements - number of elements in Columns

Last 2 are just for understanding however are identical

The plan, I need a data structure that will contain the sides along with their repective i values that contain it. DIctionairies?

"""

def solve2DLaplace(nVariables, dx = 1, dy=1, top=0,bottom=0,left=0,right=0, nRows=None,nCols=None):
    if nRows == None:
        nRows = int(nVariables**0.5)
    if nCols ==None:
        nCols = int(nVariables**0.5)


    nRowElements = nCols
    nColElements = nRows

    Boundaries = {"top":[],"bottom":[],"left":[],"right":[]}

    def Create_Matrix_2D_Laplace(nVariables,dx,dy, nRows, nRowElements, Boundaries):
        matrix = np.zeros((nVariables,nVariables))
        for i in range(nVariables):
            print(i)
            matrix[i][i] = 4*(dx**2+dy**2) #Own Tile
            if i < nRowElements: #hugging top wall
                Boundaries["top"].append(i)
                matrix[i][i+(nRowElements)] = -2*dx**2 #Below
                if i % nRowElements == 0: # hugging left wall
                    Boundaries["left"].append(i)
                    matrix[i][i+1] = -2*dy**2 #To the right
                    continue
                if (i+1) %nRowElements == 0: #Hugging right wall
                    Boundaries["right"].append(i)
                    matrix[i][i-1] = -2*dy**2 #To the left
                    continue
                matrix[i][i+1] = -2*dy**2 #To the right
                matrix[i][i-1] = -2*dy**2 #To the left
                continue
            if i >= (nRows-1)*nRowElements: #Hugging Bottom Wall
                Boundaries["bottom"].append(i)
                matrix[i][i-(nRowElements)] = -2*dx**2 #Above
                if i % nRowElements == 0: # hugging left wall
                    Boundaries["left"].append(i)
                    matrix[i][i+1] = -2*dy**2 #To the right
                    continue
                if (i+1) %nRowElements == 0: #Hugging right wall
                    Boundaries["right"].append(i)
                    matrix[i][i-1] = -2*dy**2 #To the left
                    continue
                matrix[i][i+1] = -2*dy**2 #To the right
                matrix[i][i-1] = -2*dy**2 #To the left   
                continue 
            if (i+1) %nRowElements == 0: #Hugging right wall
                Boundaries["right"].append(i)
                matrix[i][i-1] = -2*dy**2 #To the left
                matrix[i][i-(nRowElements)] = -2*dx**2  #Above
                matrix[i][i+(nRowElements)] = -2*dx**2  #Below
                continue
            if i % nRowElements == 0: # hugging left wall
                Boundaries["left"].append(i)
                matrix[i][i-(nRowElements)] = -2*dx**2  #Above
                matrix[i][i+(nRowElements)] = -2*dx**2  #Below
                matrix[i][i+1] = -2*dy**2 #To the right  
                continue
            
            matrix[i][i-1] = -2*dy**2 #To the left
            matrix[i][i-(nRowElements)] = -2*dx**2  #Above
            matrix[i][i+(nRowElements)] = -2*dx**2  #Below
            matrix[i][i+1] = -2*dy**2 #To the right 

        return matrix
    
    def Create_B_Vector(top,dy,dx,bottom,left,right,Boundaries):
        B = np.zeros(nVariables)
        for i in Boundaries["top"]:
            B[i] += top*2*dx**2
        for i in Boundaries["bottom"]:
            B[i] += bottom*2*dx**2
        for i in Boundaries["left"]:
            B[i] += left*2*dy**2
        for i in Boundaries["right"]:
            B[i] += right*2*dy**2
        return B

    
    A=Create_Matrix_2D_Laplace(nVariables,dx,dy,nRows,nRowElements, Boundaries)
    B = Create_B_Vector(top,dy,dx,bottom,left,right,Boundaries)
    u = np.linalg.inv(A) @ B
    print(Boundaries)
    print(A)
    print(u)
    return u

#solve2DLaplace(12, top=100,bottom=0,left=20,right=40, nCols=4,nRows=3)