
nombres = []

for i in range(7):
    nombre = input("Ingrese el nombre de la persona " + str(i+1) + ": ")
    nombres += [nombre]

nombres_filtrados = []
for nombre in nombres:
    if nombre[-1] == "a" or nombre[-1] == "A":
        nombres_filtrados += [nombre]

nombres_eliminados = [nombre for nombre in nombres if nombre not in nombres_filtrados]
print()
print("Lista original:")
print(nombres)
print()
print("Lista de nombres que terminan en a: " )
print(nombres_filtrados)
print()
print("Lista con nombres eliminados: ")
print(nombres_eliminados)
print()




