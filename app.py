import flet as ft 
from components.carrito_compras import añadir_producto

def main(page:ft.Page):
    page.title = "Mi Primera Pagina en Flet"
    page.bgcolor = ft.Colors.GREEN_100
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    title = ft.Container (
        content = ft.Text(
            "Bienvenido a mi app de una tienda online de cafe",
            size=20,weight="bold",
            color=ft.Colors.ORANGE_400,
            font_family="Roboto",
            text_align=ft.TextAlign.CENTER
        ),  
        alignment=ft.alignment.center
    )
    
    def agregar_al_carrito(e):
        print("Producto añadido")
    
    lista_productos = ft.Column([
        añadir_producto("Capucchino",20000,agregar_al_carrito),
        añadir_producto("Frapucchino",25000, añadir_producto)
    ])
    
    
    page.add(
        title,
        lista_productos
    )
    
ft.app(main)