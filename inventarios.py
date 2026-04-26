# Inventario: {nombre: {"precio": float, "cantidad": int}}
inventario = {}

def agregar_producto():
    nombre = input("Nombre del producto: ").lower()
    
    if nombre in inventario:
        print("El producto ya existe.")
        return
    
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print("Producto agregado correctamente.")
def listar_productos():
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("\n--- Lista de productos ---")
    for nombre, datos in inventario.items():
        print(f"Producto: {nombre}")
        print(f"Precio: Q{datos['precio']}")
        print(f"Cantidad: {datos['cantidad']}")
        print("-------------------------")
def actualizar_cantidad():
    nombre = input("Nombre del producto a actualizar: ").lower()
    
    if nombre not in inventario:
        print("El producto no existe.")
        return
    
    nueva_cantidad = int(input("Nueva cantidad: "))
    inventario[nombre]["cantidad"] = nueva_cantidad
    print("Cantidad actualizada.")
    
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").lower()
    
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado.")
    else:
        print("El producto no existe.")

def calcular_valor_total():
    total = 0
    for datos in inventario.values():
        total += datos["precio"] * datos["cantidad"]
    
    print(f"Valor total del inventario: Q{total}")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar cantidad")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

# Ejecutar programa
menu()