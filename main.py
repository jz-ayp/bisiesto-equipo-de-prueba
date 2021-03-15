# Año bisiesto
# Equipo 2: Roberto, Alejandra y Juan Pablo Valdez
# Fecha: 25/02/2021

#Entradas
a = int(input("Ingrese el año a verificar: "))

#Proceso
if a % 4 != 0: 
	print("El año ingresado no es bisiesto")
elif a % 4 == 0 and a % 100 != 0: 
	print("El año ingresado sí es bisiesto")
elif a % 4 == 0 and a % 100 == 0 and a % 400 != 0:
	print("El año ingresado sí no es bisiesto")
elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0: 
	print("El año ingresado sí es bisiesto")

