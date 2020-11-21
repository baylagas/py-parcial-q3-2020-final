import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
"""
def suma():
    return 0
"""
# finish-->


def suma(num1, num2):
    return num1 + num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""

"""
# start-->
def sumaPares():
    result = 0
    return result
"""
# finish-->


def sumaPares():
    result = 0
    for number in range(2, 1001, 2):
        result += number
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    valorAreaLateral = areaLateral(radio, altura)
    valorAreaCirculo = areaCirculo(radio)
    result = valorAreaLateral + valorAreaCirculo
    result = round(result, 2)
    return result


def areaLateral(radioX, alturaX):
    result = 2 * math.pi * radioX * alturaX
    return result


def areaCirculo(radioY):
    result = 2 * math.pi * radioY ** 2.0
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def areaTotalCilindro(self):
        valorAreaLateral = self.areaLateral()
        valorAreaCirculo = self.areaCirculo()
        result = valorAreaLateral + valorAreaCirculo
        result = round(result, 2)
        return result

    def areaLateral(self):
        result = 2 * math.pi * self.radio * self.altura
        return result

    def areaCirculo(self):
        result = 2 * math.pi * self.radio ** 2.0
        return result


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento

    nombre,lugar,costo,conDescuento,descuento
"""


class Restaurante:
    def __init__(self):
        self.pizzaList = []

    def ordenar(self, pizza):
        self.pizzaList.append(pizza)

    def costoTotal(self):
        result = 0
        for pizza in self.pizzaList:
            result += pizza.costo
        result = f"${result:.2f}"
        return result

    def costoTotalConDescuento(self):
        result = 0
        for pizza in self.pizzaList:
            if pizza.conDescuento:
                result += pizza.costo - pizza.descuento
            else:
                result += pizza.costo
        result = f"${result:.2f}"
        return result


class Pizza:
    def __init__(self, nombre, lugar, costo, conDescuento, descuento):
        self.nombre = nombre
        self.lugar = lugar
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/baylagas/py-parcial-q3-2020-final.git"
