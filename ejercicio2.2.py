import copy 
def calcular_determinante(matriz):
    suma = 0
    if len(matriz) == 2 and len(matriz[0]) ==2:
        suma = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
        return suma
    else:
        for i in range(len(matriz)):
            aux = copy.deepcopy(matriz)
            aux.remove(matriz[0])
            for j in range(len(aux)):
                aux[j] = aux[j][0:i] + aux[j][i+1:]
            suma += (-1) ** (i % 2) * matriz[0][i] * calcular_determinante(aux)
        return suma

print((calcular_determinante([[3,1,2], [3,4,4], [5,6,3]])))
        
