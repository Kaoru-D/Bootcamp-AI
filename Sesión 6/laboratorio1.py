do = True
while do or option != 0:
    do = False
    print("Menú del laboratorio 1")
    print("1. Bienvenida")
    print("2. Área de un triángulo")
    print("3. Circunferencia de un círculo")
    print("4. Calcular sueldo mensual")
    print("5. Sueldo con comisiones")
    print("0. Salir")
    option = int(input("Seleccione una opción: "))
    if option == 1:
        #Ejercicio 1
        #Crear un programa que solicite el nombre del cliente y lo muestre en pantalla
        #para este proceso se debe solicitar el nombre con la función input() y guardarlo en una variable
        nombre=input("Ingrese su nombre: ")
        print(f"Bienvenido {nombre}")

    if option == 2:
        #Ejercicio 2
        #Crear un programa que solicite base y altura e imprima el área de un triángulo
        #para este proceso se debe tener en cuenta que el área de un triángulo es (base*altura)/2,
        #por lo que se debe solicitar los datos de la base y la altura con las funciones input() y float() para convertir el valor a un número decimal.
        base=float(input("Ingrese la base del triángulo: "))
        altura=float(input("Ingrese la altura del triángulo: "))
        area=(base*altura)/2
        print(f"El área del triángulo es de {area}")
        
    if option == 3:
        #Ejercicio 3
        #Cree un programa que pida el radio de un círculo e imprima la circunferencia
        #para este proceso se debe tener en cuenta que la circunferencia de un círculo es 2*π*radio,
        radio=float(input("Ingrese el radio del círculo: "))
        circunferencia=2*3.14*radio
        print(f"La circunferencia del círculo es de {circunferencia}")
        
    if option == 4:
        #Ejercicio 4
        #Crear un programa que permita calcular el sueldo mensual de un trabajador teniendo en
        #cuenta los días trabajados y el valor del día.
        #El sueldo se calcula multiplicando los dias trabajados por el valor del dia
        cantidadDias=int(input("Ingrese los días que ha trabajado: "))
        valorDia=47450
        sueldo=cantidadDias*valorDia
        print(f"Su sueldo mensual es de {sueldo}")
        
    if option == 5:
        #Ejercicio 5
        #Un vendedor recibe un sueldo base más un 10% extra por comisión de su venta. El
        #vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
        #ventas que realiza en un mes y el total que recibirá en el mes tomando en cuenta su
        #sueldo base y comisiones.
        #El programa debe preguntar al usuario su sueldo base y el valor de sus tres ventas.Luego
        #el programa debe mostrar el total que recibira en el mes sumando su sueldo base y sus comisiones.
        sueldoBase=int(input("Ingrese su sueldo al mes: "))
        comision=0.10
        venta1=int(input("Ingrese el valor de su primera venta: "))
        venta2=int(input("Ingrese el valor de su segunda venta: "))
        venta3=int(input("Ingrese el valor de su tercera venta: "))
        comision1=venta1*comision
        comision2=venta2*comision
        comision3=venta3*comision
        total=comision1+comision2+comision3+sueldoBase
        print(f"Usted obtiene por estas ventas un total de {total}")


    if option == 0:
        do = True
        exit()