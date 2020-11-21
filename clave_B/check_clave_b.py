from clave_b import (
    suma,
    sumaImpares,
    definicionEsfera,
    Esfera,
    Banco,
    Cliente,
    getGithubUrl,
)

print("Clave B...")


# ejercicio 1 -->
result = suma()
if result == 12:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")


# ejercicio 2 -->
result = sumaImpares()
if result == 250000:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")


# ejercicio 3 -->
result = definicionEsfera()
if result == {
    "perimetro": 75.39822368615503,
    "area": 1809.5573684677208,
    "volumen": 7238.229473870882,
}:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")


# ejercicio 4 -->
esfera = Esfera()
result = esfera.definicionEsfera()
if result == {
    "perimetro": 75.39822368615503,
    "area": 1809.5573684677208,
    "volumen": 7238.229473870882,
}:
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")

# ejercicio 5 -->
banco = Banco()
# banco.procesar(Cliente("balbino", "san salvador", 1, "abono", 250.0))
# banco.procesar(Cliente("rodrigo", "san salvador", 2, "retiro", 350.0))
# banco.procesar(Cliente("marta", "san salvador", 3, "abono", 400.0))
# banco.procesar(Cliente("rafael", "santa ana", 4, "abono", 500.0))
# banco.procesar(Cliente("balbino", "la libertad", 1, "abono", 250.0))
# banco.procesar(Cliente("marta", "san salvador", 3, "abono", 250.0))
# banco.procesar(Cliente("rodrigo", "san salvador", 2, "abono", 100.0))
banco.procesar()
# total de abonos en san salvador
totalAbonos = banco.abonosSanSalvador()
if totalAbonos == 1000.0:
    print("ejercicio05part01: pass")
else:
    print("ejercicio05part01: fail")

# total de abonos entre balbino y rodrigo
totalAbonos = banco.abonosBalYRod()
if totalAbonos == 600.0:
    print("ejercicio05part02: pass")
else:
    print("ejercicio05part02: fail")


# ejercicio 6 -->
result = getGithubUrl()
if not result == "":
    print("ejercicio06: pass")
else:
    print("ejercicio06: fail")
