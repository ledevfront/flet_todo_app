import flet as ft
from time import sleep

def main(page: ft.Page):
    text = ft.Text()
    page.add(text)
    for i in range(1,11):
        text.value = "count"+str(i)
        page.update()
        sleep(1)


ft.app(target=main)