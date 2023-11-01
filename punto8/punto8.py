import multiprocessing
import random


def generoMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = random.randint(0, 1000)
    return mat

def sumaMat(mat):
    suma = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            suma += mat[i][j]
    return suma

if __name__ =='__main__':
    mat1 = [[0 for i in range(10)] for j in range(10)]
    mat2 = [[0 for i in range(10)] for j in range(10)]
    
    generoMat(mat1)
    generoMat(mat2)
    
    lista = []
    num_procesadores = multiprocessing.cpu_count()
    