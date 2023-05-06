texto = input("Por favor ingrese un texto o frase cualquiera: ")
letra1 = input("Por favor ingrese una letra cualquiera: ")
letra2 = input("Por favor ingrese una segunda letra: ")
letra3 = input("Por favor ingrese una tercer letra: ")

texto = texto.lower() #convertir texto en minuscula
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

# consigna 1: contar las letras que se repiten en el texto
cantidad_letra1= (texto.count(letra1))
cantidad_letra2= (texto.count(letra2))
cantidad_letra3= (texto.count(letra3))

print("La letra1 se repite: ", cantidad_letra1, "\n"
      "La letra2 se repite: ", cantidad_letra2, "\n"
      "La letra3 se repite: ", cantidad_letra3
      )

# consigna 2: cuantas palabras hay en el texto

texto_lista = texto.split(' ') #convertir texto en lista, separado por un espacio en blanco
cantidad_palabras= (len(texto_lista)) # usar len para contar la cantidad de palabras
print("Hay", cantidad_palabras, "palabras en el texto")


# Consigna 3: Cual es la primera letra y cuál es la última. (Indexación) 
print ("primer letra del texto", texto[0], "\n"
       "ultima letra: ", texto[-1])
