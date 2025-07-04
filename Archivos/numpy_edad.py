import numpy as np
import matplotlib.pyplot as plt

edades = [38,25,42,18,32,16,22,43,39,27]
suma = np.sum(edades)
print("Suma:",suma)
datos = np.count_nonzero(edades)
print(datos)

prom = np.mean(edades)  
print("Promedio:", prom)

mediana = np.median(edades)
print("Mediana:", mediana)
min = np.min(edades)
print("min: ", min)
max
print("max: ", max)
ds = np.std(edades)
print("desviación:", ds)

x = np.linspace(1, 10, 10)
y = np.array(edades)

plt.plot(x, y, marker='o', linestyle='--', color='b')
plt.title('Gráfico de Edades')
plt.grid()
plt.show()

