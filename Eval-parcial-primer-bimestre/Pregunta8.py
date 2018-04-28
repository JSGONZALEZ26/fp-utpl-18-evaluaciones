#Pregunta 8

v1=str(input("Ingrese una letra: "))
v2=str(input("Ingrese una nueva letra: "))
v3=str(input("Ingrese una nueva letra: "))

if (v1<v2 and v1<v3):
	print("La primera letra que aparece en le abecedario es: ",v1)
else:
	if (v2<v1 and v2<v3):
		print("La primera letra que aparece en le abecedario es: ",v2)
	else:
		if (v3<v1 and v3<v2):
			print("La primera letra que aparece en le abecedario es: ",v3)
			pass

	
