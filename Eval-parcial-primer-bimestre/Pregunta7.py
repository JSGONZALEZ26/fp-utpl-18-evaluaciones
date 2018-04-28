#Pregunta 7

sueldofijo:float = 360.4
sueldototal:float = 0
valoragregado = 0

ventas = float(input("Ingrese las ventas declaradas en el mes: "))

if (ventas<=500):
	valoragregado = sueldofijo * 0.05
	sueldototal = sueldofijo + valoragregado
else:
	if (ventas>500 and ventas<=1000):
		valoragregado = sueldofijo * 0.08
		sueldototal = sueldofijo + valoragregado
	else:
		if (ventas>1000 and ventas<=5000):
			valoragregado = sueldofijo * 0.1
			sueldototal = sueldofijo + valoragregado
		else:
			if (ventas>5000):
				valoragregado = sueldofijo * 0.15
				sueldototal = sueldofijo + valoragregado
				pass

print("Ventas realizadas por el empleado durante el mes: ",ventas,"\nSueldo correspondiente al empleado por dichas ventas",sueldototal)
		