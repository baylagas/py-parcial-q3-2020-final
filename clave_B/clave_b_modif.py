import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(num1, num2, num3):
    return num1 + num2 + num3


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    result = 0
    for number in range(1, 1001, 2):
        result += number
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera(radio):
    perimetro = obtenerPerimetro(radio)
    area = obtenerArea(radio)
    volumen = obtenerVolumen(radio)
    result = {}
    result["perimetro"] = perimetro
    result["area"] = area
    result["volumen"] = volumen
    return result


def obtenerPerimetro(radioX):
    result = 2 * math.pi * radioX
    return result


def obtenerArea(radioY):
    result = 4 * math.pi * radioY ** 2
    return result


def obtenerVolumen(radioZ):
    result = (4 / 3) * math.pi * radioZ ** 3
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def definicionEsfera(self):
        perimetro = self.obtenerPerimetro()
        area = self.obtenerArea()
        volumen = self.obtenerVolumen()
        result = {}
        result["perimetro"] = perimetro
        result["area"] = area
        result["volumen"] = volumen
        return result

    def obtenerPerimetro(self):
        result = 2 * math.pi * self.radio
        return result

    def obtenerArea(self):
        result = 4 * math.pi * self.radio ** 2
        return result

    def obtenerVolumen(self):
        result = (4 / 3) * math.pi * self.radio ** 3
        return result


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto

    nombre,lugar,cuenta,transaccion,monto
"""


class Banco:
    def __init__(self):
        self.clienteList = []

    def procesar(self, cliente):
        self.clienteList.append(cliente)

    def abonosSanSalvador(self):
        result = 0.0
        for pepito in self.clienteList:
            if pepito.transaccion == "abono":
                if pepito.lugar == "san salvador":
                    result += pepito.monto
        return result

    def abonosBalYRod(self):
        result = 0.0
        for cliente in self.clienteList:
            if cliente.nombre in ["balbino", "rodrigo"]:
                if cliente.transaccion == "abono":
                    result += cliente.monto
        return result


class Cliente:
    def __init__(self, nombre, lugar, cuenta, transaccion, monto):
        self.nombre = nombre
        self.lugar = lugar
        self.cuenta = cuenta
        self.transaccion = transaccion
        self.monto = monto


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
