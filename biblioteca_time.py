import time

cronometro = 3550

inicio = time.clock()

while True:
	cronometro += 1

	segundos = cronometro % 60
	horas = (cronometro - cronometro % (60 * 60)) / (60 * 60)
	minutos = (cronometro - cronometro % 60) / 60 - (horas * 60)

	if cronometro == 3560:
		break

	time.sleep(1)

final = time.clock() - inicio

print("{:.0f}h {:.0f}m {:.0f}s".format(horas, minutos, segundos))
print("A aplicação demorou {} segundos para finalizar.".format(final))

