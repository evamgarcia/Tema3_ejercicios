def hanoi(discos, Aguja_1=1, Aguja_2=2, Aguja_3 =3):
    if discos ==1: 
        return(Aguja_1, "se mueve a la ", Aguja_3)
    else:
        hanoi(discos-1, Aguja_1, Aguja_3, Aguja_2)
        print(Aguja_1, "se mueve a ", Aguja_3)
        hanoi(discos-1, Aguja_2, Aguja_1, Aguja_3)
    return 