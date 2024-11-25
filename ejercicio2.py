while True:
    # Solicitar la altura de la persona
    altura = float(input("Ingrese la altura de la persona en metros: "))
    
    # Validar si la persona puede ingresar a la montaña rusa
    if altura >= 1.20:
        print("La persona puede ingresar a la atracción.")
    else:
        print("La persona NO puede ingresar a la atracción.")
    
    # Preguntar si desea registrar otra persona
    respuesta = input("¿Desea registrar otra persona? (si/no): ").strip().lower()
    
    # Verificar si el usuario desea finalizar
    if respuesta == 'no':
        print("Finalizando el registro.")
        break