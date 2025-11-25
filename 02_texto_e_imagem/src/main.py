import flet as ft


def main(page: ft.Page):

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text(
                    "ducati streetfighter v4.",
                    size=40,
                    weight="bold",
                    font_family="Arial black",
                ),
                alignment=ft.alignment.center,
            )
        ),
        ft.Container(
            ft.Image(
                src="page-image.jpg",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Não foi possível carregar a imagem."),
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    )


ft.app(main)
