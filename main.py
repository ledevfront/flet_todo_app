import flet as ft
from time import sleep

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("LIST OF FRUITS:\n")
        ]),
        ft.Row(controls=[
            ft.Text("Apple"),
            ft.Text("Banana"),
            ft.Text('Mango')
        ]),
        ft.Row(controls=[
            ft.Text("salut tom"),
            ft.Text("heloo")
        ]),
        ft.Row(controls=[
            ft.Text("acceuill"),
            ft.Text("service"),
            ft.Text("about"),
            ft.Text("contact")
        ])
    )

ft.app(target=main)