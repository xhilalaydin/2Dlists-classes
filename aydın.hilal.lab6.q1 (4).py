# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:46:55 2023

@author: hilala-ug
"""
"""
a) Write a function formMatrix which gets an integer number n and creates and
returns a square 2-dimensional matrix of size n x n according to the below rule:
 The elements in the upper triangular part of the matrix will be assigned to the
sum of their row and column indices
 The elements in the lower triangular part of the matrix will be assigned to the
difference of their row and column indices
 The elements in the major diagonal of the matrix will be assigned to 0
(Assume n is 5 in the sample below).
0 1 2 3 4
1 0 3 4 5
2 1 0 5 6
3 2 1 0 7
4 3 2 1 0
b) Write a main to input the size of the matrix and display the matrix in matrix form
after calling the above function.
"""

def formMatrix(n):
    table=[]
    for row in range(n):
        table.append([])
        for col in range(n):
            if row > col:
                table[row].append(row-col)
            elif row == col:
                table[row].append(0)
            else:
                table[row].append(col+row)
    return table

n = int(input("enter table size: "))
a = (formMatrix(n))            

for row in range(len(a)):
    for col in range(len(a)):
        line= a[row][col]
        print(line,"", end=" ")
    print()
            