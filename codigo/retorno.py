def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma

def mulplicar(numero1, numero2):
    r = 0
    for i in range(numero2):
        r = sumar(r,numero1)

respuesta = sumar(4,7)
mult = respuesta * 3
print(mult)