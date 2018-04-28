#Pregunta 6

mes=int(input("Ingrese un mes del año\n1. Enero\n2. Febrero\n3. Marzo\n4. Abril\n5. Mayo\n6. Junio\n7. Julio\n8. Agosto\n9. Septiembre\n10. Octubre\n11. Noviembre\n12. Diciembre\n"))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
	print("Ese mes tiene 31 días")
else:
	if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
		print("Ese mes tiene 30 días")
	else:
		if (mes == 2):
			print("Ese mes tiene 28 a 29 días dependiendo de que sea año bisiesto o no")
			pass

	