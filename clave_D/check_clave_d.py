from clave_d import (
    multiplicar,
    sumaDivTresYCincoPlus,
    definicionOrtoedro,
    Ortoedro,
    VentaComputadoras,
    Computadora,
    getGithubUrl,
)

print("Clave D...")


# ejercicio 1 -->
result = multiplicar()
if result == 24:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")


# ejercicio 2 -->
result = sumaDivTresYCincoPlus()
if result == 100500:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")


# ejercicio 3 -->
result = definicionOrtoedro()
if result == {"area": 280, "volumen": 300}:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")


# ejercicio 4 -->
ortoedro = Ortoedro()
result = ortoedro.definicionOrtoedro()
if result == {"area": 280, "volumen": 300}:
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")


# ejercicio 5 -->
ventaCompus = VentaComputadoras()
# ventaCompus.orden(
#     Computadora("intel", "16gb", "nvidia", "240gb", 700.0, False, 0.0, False, 0.0)
# )
# ventaCompus.orden(
#     Computadora("amd", "16gb", "nvidia", "512gb", 750.0, True, 20.0, False, 0.0)
# )
# ventaCompus.orden(
#     Computadora("intel", "8gb", "nvidia", "240gb", 700.0, False, 0.0, False, 0.0)
# )
# ventaCompus.orden(
#     Computadora("amd", "16gb", "nvidia", "512gb", 700.0, True, 50.0, False, 0.0)
# )
# ventaCompus.orden(
#     Computadora("intel", "16gb", "nvidia", "1Tb", 700.0, True, 70.0, False, 0.0)
# )
# ventaCompus.orden(
#     Computadora("intel", "32gb", "nvidia", "2Tb", 900.0, False, 0.0, False, 0.0)
# )
# ejemplos
ventaCompus.orden()
result = ventaCompus.totalProcesadorIntel()
if result == "$3000.00":
    print("ejercicio05part01: pass")
else:
    print("ejercicio05part01: fail")

result = ventaCompus.totalRam16ConDescuento()
if result == "$2710.00":
    print("ejercicio05part02: pass")
else:
    print("ejercicio05part02: fail")


# ejercicio 6 -->
result = getGithubUrl()
if not result == "":
    print("ejercicio06: pass")
else:
    print("ejercicio06: fail")
