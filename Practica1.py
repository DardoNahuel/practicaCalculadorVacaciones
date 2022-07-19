print("Bienvenido al servicio de vacaciones de Rappi\n")
nombre = input("Por favor, ingrese su nombre: \n")
clave = int(input("Hola " + nombre + " ingrese su clave: \n"))

if clave == 1:
    antiguedad = int(input("Por ultimo, ingrese su antiguedad: \n"))
    if antiguedad == 1:
        print(nombre + " usted pertenece al area de atencion al cliente y le corresponde 6 dias de vacaciones. ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print(nombre + " usted pertenece al area de atencion al cliente y le corresponde 14 dias de vacaciones. ")
    elif antiguedad >= 7:
        print(nombre + " usted pertenece al area de atencion al cliente y le corresponde 20 dias de vacaciones. ")
    else:
        print(nombre + " a usted aun no le corresponde vacaciones. ")
elif clave == 2:
    antiguedad = int(input("Por ultimo, ingrese su antiguedad: \n"))
    if antiguedad == 1:
        print(nombre + " usted pertenece al area de logistica y le corresponde 7 dias de vacaciones. ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print(nombre + " usted pertenece al area de logistica y le corresponde 15 dias de vacaciones. ")
    elif antiguedad >= 7:
        print(nombre + " usted pertenece al area de logistica y le corresponde 22 dias de vacaciones. ")
    else:
        print(nombre + " a usted aun no le corresponde vacaciones. ")
elif clave == 3:
    antiguedad = int(input("Por ultimo, ingrese su antiguedad: \n"))
    if antiguedad == 1:
        print(nombre + " usted pertenece al area de gerencia y le corresponde 10 dias de vacaciones. ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print(nombre + " usted pertenece al area de gerencia y le corresponde 20 dias de vacaciones. ")
    elif antiguedad >= 7:
        print(nombre + " usted pertenece al area de gerencia y le corresponde 30 dias de vacaciones. ")
    else:
        print(nombre + " a usted aun no le corresponde vacaciones. ")
else:
    print("La clave seleccionada no existe")
print("fin")
