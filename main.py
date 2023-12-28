def agregar_compra(lista_compras):
    monto_compra = float(input("ingrese el monto:"))
    nueva_compra = [monto_compra]
    lista_compras.append(nueva_compra)
    print("compra agregado correctamente")

def mostrar_compra(lista_compras):
    if not lista_compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(lista_compras, start=1):
            print(f"{i}.${compra}")

def mostrar_Total(lista_compras):
    total_gastado = sum(compra[0] for compra in lista_compras)
    print(f"Total gastado: ${total_gastado: .2f}")


compra = []
total_gastado = "0"

while True:
    print("Menu:")
    print("1.   Agregar Compra")
    print("2.   Mostrar compras")
    print("3.   Mostrar total gastado")
    print("4.    salir")

    opcion = input("Seleccione una opcion:")

    if opcion == "1":
        agregar_compra(compra)
    elif opcion == "2":
        mostrar_compra(compra)
    elif opcion == "3":
        mostrar_Total(compra)
    elif opcion == '4':
        print("¡Nos Vemos!")
        break
    else:
        print("Opción no válida, Debe elegir un numero")

















