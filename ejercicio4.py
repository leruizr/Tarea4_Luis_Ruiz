from datetime import datetime

def es_mayor_de_edad(fecha_nacimiento):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Calcular la edad en años
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Ajustar la edad si el cumpleaños aún no ha ocurrido en el año actual
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    # Determinar si es mayor de edad
    return edad >= 18

# Ejemplo de uso
fecha_str = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

# Convertir la fecha ingresada a un objeto datetime
try:
    fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
    
    if es_mayor_de_edad(fecha_nacimiento):
        print("La persona es mayor de edad.")
    else:
        print("La persona NO es mayor de edad.")
except ValueError:
    print("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato dd/mm/aaaa.")