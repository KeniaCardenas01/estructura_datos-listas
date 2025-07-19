import base_datos as base

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar par de números")
        print("2. Eliminar último par")
        print("3. Insertar par en posición específica")
        print("4. Eliminar par específico")
        print("5. Buscar índice de par")
        print("6. Contar repeticiones de un par")
        print("7. Ordenar lista de pares")
        print("8. Invertir lista de pares")
        print("9. Ver lista actual")
        print("10. Crear tupla PAR")
        print("11. Crear tupla IMPAR")
        print("12. Gestionar tuplas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1, num2 = int(input("Número 1: ")), int(input("Número 2: "))
            base.agregar_par(num1, num2)

        elif opcion == "2":
            eliminado = base.eliminar_ultimo_par()
            print("Eliminado:", eliminado)

        elif opcion == "3":
            pos = int(input("Posición: "))
            num1, num2 = int(input("Número 1: ")), int(input("Número 2: "))
            base.insertar_par(pos, num1, num2)

        elif opcion == "4":
            num1, num2 = int(input("Número 1: ")), int(input("Número 2: "))
            base.eliminar_par([num1, num2])

        elif opcion == "5":
            num1, num2 = int(input("Número 1: ")), int(input("Número 2: "))
            idx = base.buscar_par([num1, num2])
            print("Índice:", idx)

        elif opcion == "6":
            num1, num2 = int(input("Número 1: ")), int(input("Número 2: "))
            print("Repeticiones:", base.contar_par([num1, num2]))

        elif opcion == "7":
            base.ordenar_lista()
            print("Lista ordenada.")

        elif opcion == "8":
            base.invertir_lista()
            print("Lista invertida.")

        elif opcion == "9":
            print("Lista de pares:", base.obtener_lista())

        elif opcion == "10":
            num1, num2 = int(input("Número PAR 1: ")), int(input("Número PAR 2: "))
            res = base.crear_tupla_par(num1, num2)
            print("Tupla creada:", res if res else "No es válida")

        elif opcion == "11":
            num1, num2 = int(input("Número IMPAR 1: ")), int(input("Número IMPAR 2: "))
            res = base.crear_tupla_impar(num1, num2)
            print("Tupla creada:", res if res else "No es válida")

        elif opcion == "12":
            submenu_tuplas()

        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida")

def submenu_tuplas():
    while True:
        print("\n--- Submenú de Tuplas ---")
        print("1. Ver tuplas pares")
        print("2. Ver tuplas impares")
        print("3. Modificar tupla par")
        print("4. Modificar tupla impar")
        print("5. Eliminar tupla par")
        print("6. Eliminar tupla impar")
        print("0. Volver")

        op = input("Seleccione una opción: ")

        if op == "1":
            print("Tuplas pares:", base.obtener_tuplas_pares())

        elif op == "2":
            print("Tuplas impares:", base.obtener_tuplas_impares())

        elif op == "3":
            idx = int(input("Índice de la tupla a modificar: "))
            n1, n2 = int(input("Nuevo número 1: ")), int(input("Nuevo número 2: "))
            base.modificar_tupla("par", idx, [n1, n2])

        elif op == "4":
            idx = int(input("Índice de la tupla a modificar: "))
            n1, n2 = int(input("Nuevo número 1: ")), int(input("Nuevo número 2: "))
            base.modificar_tupla("impar", idx, [n1, n2])

        elif op == "5":
            idx = int(input("Índice de la tupla a eliminar: "))
            base.eliminar_tupla("par", idx)

        elif op == "6":
            idx = int(input("Índice de la tupla a eliminar: "))
            base.eliminar_tupla("impar", idx)

        elif op == "0":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
