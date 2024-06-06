palabras = []
contador = 0

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras[contador:contador] = [palabra]
    contador = contador + 1

if contador == 0:
    print("No se ingresaron palabras.")
else:
    palabra_mas_larga = palabras[0]
    caracteres_mas_largos = 0
    for i in range(contador):
        caracteres_palabra = 0
        for caracter in palabras[i]:
            caracteres_palabra = caracteres_palabra + 1
        if caracteres_palabra > caracteres_mas_largos:
            palabra_mas_larga = palabras[i]
            caracteres_mas_largos = caracteres_palabra
    print("La palabra con la mayor cantidad de caracteres es '" + palabra_mas_larga + "' con " + str(caracteres_mas_largos) + " caracteres.")