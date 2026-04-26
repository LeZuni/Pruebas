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
