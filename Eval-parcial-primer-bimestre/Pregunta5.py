#Pregunta 5

calificacion1 = float(input("Ingrese la calificación 1 del estudiante: "))
calificacion2 = float(input("Ingrese la calificación 2 del estudiante: "))
calificacion3 = float(input("Ingrese la calificación 3 del estudiante: "))
calificacion4 = float(input("Ingrese la calificación 4 del estudiante: "))

promedio=(calificacion1+calificacion2+calificacion3+calificacion4)/4

if (promedio<=69):
	print("El estudiante con el promedio de calificaciones: ",promedio," tiene una calificación de D")
else:
	if (promedio>=70 and promedio<=79):
		print("El estudiante con el promedio de calificaciones: ",promedio," tiene una calificación de C")
	else:
		if (promedio>=80 and promedio<=89):
			print("El estudiante con el promedio de calificaciones: ",promedio," tiene una calificación de B")
		else:
			if (promedio>=90 and promedio<=100):
				print("El estudiante con el promedio de calificaciones: ",promedio," tiene una calificación de A")
			pass
			
		