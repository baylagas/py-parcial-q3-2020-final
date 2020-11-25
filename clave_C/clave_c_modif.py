import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1, num2):
    return num1 * num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    result = 0
    for number in range(1, 1001):
        if number % 3 == 0:
            if number % 5 == 0:
                result += number
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def definicionCono(radio, altura):
    result = {}
    generatriz = obtenerGeneratriz(radio, altura)
    area = obtenerArea(radio, generatriz)
    volumen = obtenerVolumen(radio, altura)
    result["generatriz"] = generatriz
    result["area"] = area
    result["volumen"] = volumen
    return result


def obtenerGeneratriz(radio, altura):
    # square_root(altura^2 + radio^2)
    result = math.sqrt((altura ** 2) + (radio ** 2))
    return result


def obtenerArea(radio, generatriz):
    # pi*radio*(radio+generatriz)
    result = math.pi * radio * (radio + generatriz)
    return result


def obtenerVolumen(radio, altura):
    # (1/3)*pi*radio^2*altura
    result = (1 / 3) * math.pi * (radio ** 2) * altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        self.generatriz = 0
        self.area = 0
        self.volumen = 0

    def definicionCono(self):
        result = {}
        self.generatriz = self.obtenerGeneratriz()
        self.area = self.obtenerArea()
        self.volumen = self.obtenerVolumen()
        result["generatriz"] = self.generatriz
        result["area"] = self.area
        result["volumen"] = self.volumen
        return result

    def obtenerGeneratriz(self):
        # square_root(altura^2 + radio^2)
        result = math.sqrt((self.altura ** 2) + (self.radio ** 2))
        return result

    def obtenerArea(self):
        # pi*radio*(radio+generatriz)
        result = math.pi * self.radio * (self.radio + self.generatriz)
        return result

    def obtenerVolumen(self):
        # (1/3)*pi*radio^2*altura
        result = (1 / 3) * math.pi * (self.radio ** 2) * self.altura
        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento

    nombre,lugar,descripcion,costo,conDescuento,descuento
"""


class CentroMedico:
    def __init__(self):
        self.pacienteLista = []

    def registrar(self, paciente):
        self.pacienteLista.append(paciente)

    def totalCostoSanSalvador(self):
        result = 0
        for paciente in self.pacienteLista:
            if paciente.lugar == "san salvador":
                result += paciente.costo
        result = f"${result:.2f}"
        return result

    def totalCostoConDescuento(self):
        result = 0
        for paciente in self.pacienteLista:
            if paciente.conDescuento:
                result += paciente.costo - paciente.descuento
            else:
                result += paciente.costo
        result = f"${result:.2f}"
        return result


class Paciente:
    def __init__(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.nombre = nombre
        self.lugar = lugar
        self.descripcion = descripcion
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
