print('Bienvenido a mi trivia sobre computación')
print('pondremos a prueba tus conocimientos')
nombre=input("ingresa tu nombre:")
print("\nHola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'enter' para enviar tu respuesta: \n")

print('pregunta 1: Es un número primo.Pondremos a prueba tus conocimientos')
print('a)1')
print('b)2')
print('c)4')
print('d)3')
respuesta_1=input("\nTu respuesta:")
while respuesta_1 not in ("a","b","c","d"):
  respuesta_1=input("debes repsonder a, b,c, o d. Ingresa nuevamente tu respuesta:")

if respuesta_1=="a":
  print("incorrecto!"), nombre, " no es un numero primo"

if respuesta_1=="b":
  print("incorrecto!"), nombre, " no es un numero primo"

if respuesta_1=="c":
  print("incorrecto!"), nombre, " no es un numero primo"

else:
  print ("muy bien", nombre, "!")


print('pregunta 2: Es una vocal.Pondremos a prueba tus conocimientos')
print('a)l')
print('b)r')
print('c)p')
print('d)a')
respuesta_1=input("\nTu respuesta:")
while respuesta_1 not in ("a","b","c","d"):
  respuesta_1=input("debes repsonder a, b,c, o d. Ingresa nuevamente tu respuesta:")

if respuesta_1=="a":
  print("incorrecto!"), nombre, " no es una vocal"

if respuesta_1=="b":
  print("incorrecto!"), nombre, " no es una vocal"

if respuesta_1=="c":
  print("incorrecto!"), nombre, " no es una vocal"

else:
  print ("muy bien", nombre, "!")


print('pregunta 3: Es un color primario')
print('a)manteca')
print('b)rosado')
print('c)lila')
print('d)rojo')
respuesta_1=input("\nTu respuesta:")
while respuesta_1 not in ("a","b","c","d"):
  respuesta_1=input("debes repsonder a, b,c, o d. Ingresa nuevamente tu respuesta:")

if respuesta_1=="a":
  print("incorrecto!"), nombre, " no es un color primario"

if respuesta_1=="b":
  print("incorrecto!"), nombre, " no es un color primario"

if respuesta_1=="c":
  print("incorrecto!"), nombre, " no es un color primario"

else:
  print ("muy bien", nombre, "!")