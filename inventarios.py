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
