#entrada
año = int(input("ingrese un año: "))

#proceso
if año%4 == 0 and año%100 != 0:
  resultado = "Ese año sí es bisiesto"
elif año%4 == 0 and año%100 == 0 and año%400 == 0:
  resultado = "Ese año sí es bisiesto"
elif año%4 == 0 and año%100 == 0 and año%400 != 0:
  resultado = "Ese año no es bisiesto"
elif año%4 != 0:
  resultado = "Ese año no es bisiesto"

#salida
print(resultado)

