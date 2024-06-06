puntajes_diarios = []

n = 1
while n <= 15:
    puntaje_diario = int(input("Ingrese el puntaje del día " + str(n) + ": "))
    puntajes_diarios += [puntaje_diario]
    n += 1

dias_aprobados = []
n = 1
while n <= 15:
    if puntajes_diarios[n-1] >= 60:
        dias_aprobados += ["Día " + str(n)]
    n += 1

dias_no_aprobados = []
n = 1
while n <= 15:
    if puntajes_diarios[n-1] < 60:
        dias_no_aprobados += ["Día " + str(n)]
    n += 1

print()
print("Días con puntaje mayor o igual a 60 puntos:")
print(dias_aprobados)
print ()
print("Días con puntaje menor a 60 puntos:")
print(dias_no_aprobados)
print()