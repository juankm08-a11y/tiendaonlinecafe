import flet as ft

def añadir_producto(nombre_producto,precio_producto,on_click):
    return ft.Container(
        bgcolor=ft.Colors.YELLOW,
        padding=15,
        content = ft.Column([
                    ft.Text(nombre_producto,size=15,weight="bold"),
                    ft.Text(f"Precio:{precio_producto}$"),
                    ft.ElevatedButton("Añadir al carrito",icon = ft.Icons.ADD_SHOPPING_CART, on_click=on_click),
        ]),
    )