from clave_a import (
    suma,
    sumaPares,
    areaTotalCilindro,
    Cilindro,
    Restaurante,
    Pizza,
    getGithubUrl,
)

print("Clave A...")


# ejercicio 1 -->
result = suma()
if result == 6:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")


# ejercicio 2 -->
result = sumaPares()
if result == 250500:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")


# ejercicio 3 -->
result = areaTotalCilindro()
if result == 376.99:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")


# ejercicio 4 -->
cilindro1 = Cilindro()
result = cilindro1.areaTotalCilindro()
if result == 376.99:
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")


# ejercicio 5 -->
Restaurante = Restaurante()
# Restaurante.ordenar(Pizza("suprema", "san salvador", 4.99, True, 0.99))
# Restaurante.ordenar(Pizza("hawaiana", "la lipertad", 5.99, False, 0.00))
# Restaurante.ordenar(Pizza("meat lovers", "san salvador", 6.99, True, 0.99))
# Restaurante.ordenar(Pizza("hawaiana", "san salvador", 5.99, True, 1.99))
# Restaurante.ordenar(Pizza("cuatro quesos", "santa ana", 3.99, False, 0.00))
# Restaurante.ordenar(Pizza("super suprema", "la libertad", 7.99, True, 2.99))
Restaurante.ordenar()
costoTotal = Restaurante.costoTotal()
if costoTotal == "$35.94":
    print("ejercicio05part01: pass")
else:
    print("ejercicio05part01: fail")

costoTotalConDesc = Restaurante.costoTotalConDescuento()
if costoTotalConDesc == "$28.98":
    print("ejercicio05part02: pass")
else:
    print("ejercicio05part02: fail")

# ejercicio 6 -->
result = getGithubUrl()
if not result == "":
    print("ejercicio06: pass")
else:
    print("ejercicio06: fail")
