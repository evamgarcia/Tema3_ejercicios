def calcular_determinante(matriz):
    return (matriz[0][0]*matriz[1][1]*matriz[2][2])+ (matriz[1][0]*matriz[2][1]*matriz[0][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0]) - (matriz[0][2]*matriz[1][1]*matriz[2][0]) - (matriz[0][1]*matriz[1][0]*matriz[2][2]) - (matriz[0][0]*matriz[2][1]*matriz[1][2])
print("El determinante de la matriz dada es: " + str(calcular_determinante([[3, 4, 3], [1, 2, 3], [0, 2,3]])))
