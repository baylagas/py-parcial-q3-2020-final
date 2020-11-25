import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(num1, num2, num3):
    return num1 * num2 * num3


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    result = 0
    for number in range(1000, 2001):
        if number % 3 == 0:
            if number % 5 == 0:
                result += number
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud, altura):
    result = {}
    area = obtenerArea(longitud, latitud, altura)
    volumen = obtenerVolumen(longitud, latitud, altura)
    result["area"] = area
    result["volumen"] = volumen
    return result


def obtenerArea(longitud, latitud, altura):
    # A = 2(longitud · latitud + longitud · altura + latitud · altura)
    result = 2 * ((longitud * latitud) + (longitud * altura) + (latitud * altura))
    return result


def obtenerVolumen(longitud, latitud, altura):
    # V = longitud · latitud · altura
    result = longitud * latitud * altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self, longitud, latitud, altura):
        self.longitud = longitud
        self.latitud = latitud
        self.altura = altura
        self.area = 0
        self.volumen = 0

    def definicionOrtoedro(self):
        result = {}
        self.area = self.obtenerArea()
        self.volumen = self.obtenerVolumen()
        result["area"] = self.area
        result["volumen"] = self.volumen
        return result

    def obtenerArea(self):
        # A = 2(longitud · latitud + longitud · altura + latitud · altura)
        result = 2 * (
            (self.longitud * self.latitud)
            + (self.longitud * self.altura)
            + (self.latitud * self.altura)
        )
        return result

    def obtenerVolumen(self):
        # V = longitud · latitud · altura
        result = self.longitud * self.latitud * self.altura
        return result


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def __init__(self):
        self.computadoraLista = []

    def orden(self, computadora):
        self.computadoraLista.append(computadora)

    def totalProcesadorIntel(self):
        result = 0
        for compu in self.computadoraLista:
            if compu.procesador == "intel":
                result += compu.costo
        result = f"${result:.2f}"
        return result

    def totalRam16ConDescuento(self):
        result = 0
        for compu in self.computadoraLista:
            if compu.ram == "16gb":
                if compu.conDescuento:
                    result += compu.costo - compu.descuento
                else:
                    result += compu.costo
        result = f"${result:.2f}"
        return result


class Computadora:
    def __init__(
        self,
        procesador,
        ram,
        tarjeta_grafica,
        ssd,
        costo,
        conDescuento,
        descuento,
        conPlazo,
        cuota,
    ):
        self.procesador = procesador
        self.ram = ram
        self.tarjeta_grafica = tarjeta_grafica
        self.ssd = ssd
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento
        self.conPlazo = conPlazo
        self.cuota = cuota


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
