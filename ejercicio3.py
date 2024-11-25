# Inicialización de variables
temperaturas = []
contador = 0
suma_temperaturas = 0

# Ciclo para registrar las temperaturas de los últimos 15 días
while contador < 15:
    # Solicitar la temperatura del día
    temperatura = float(input(f"Ingrese la temperatura del día {contador + 1}: "))
    
    # Almacenar la temperatura en la lista y actualizar la suma
    temperaturas.append(temperatura)
    suma_temperaturas += temperatura
    contador += 1

# Calcular el promedio de las temperaturas
promedio = suma_temperaturas / 15

# Mostrar el promedio de las temperaturas
print(f"\nEl promedio de temperaturas de los últimos 15 días es: {promedio:.2f}°C")