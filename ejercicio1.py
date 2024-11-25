# Inicialización de contadores
aprobados = 0
reprobados = 0
desempeño_superior = 0

# Ciclo para 20 estudiantes
for i in range(1, 21):
    # Solicitar la nota del estudiante
    nota = float(input(f"Ingrese la nota definitiva del estudiante {i}: "))
    
    # Evaluación de la nota
    if nota < 3:
        print("El estudiante no ha aprobado el curso.")
        reprobados += 1
    elif 3 <= nota < 4.5:
        print("El estudiante ha aprobado el curso.")
        aprobados += 1
    elif nota >= 4.5:
        print("El estudiante ha aprobado el curso con un desempeño superior.")
        desempeño_superior += 1

# Mostrar los resultados finales
print("\nResumen de resultados:")
print(f"Cantidad de estudiantes que aprobaron el curso: {aprobados}")
print(f"Cantidad de estudiantes que no aprobaron el curso: {reprobados}")
print(f"Cantidad de estudiantes con desempeño superior: {desempeño_superior}")