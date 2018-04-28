#Pregunta 3

tiempoensegundos=int(input("Ingrese el tiempo en segundos: "))

tiempoenminutos = tiempoensegundos//60
tiempoensegundos2 = tiempoensegundos%60

print(tiempoensegundos," segundos es igual a ",tiempoenminutos," minuto(s) y ",tiempoensegundos2," segundos")