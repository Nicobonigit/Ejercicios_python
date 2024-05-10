def par(numero):
    if (numero==0):
        resultado=True
    else:
        if(numero % 2==0):
            resultado=True
        else:
            resultado=False
    return resultado
print(par(3))