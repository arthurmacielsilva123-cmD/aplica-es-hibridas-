import flet as ft


def main(page: ft.Page):
    page.title = "app flex fuel"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT


    gasolina = ft.TextField(
        label="valor da gasolina",
        prefix_text= "R$",
        keyboard_type= ft.KeyboardType.NUMBER
    )
    etanol = ft.TextField(
        label="valor da etanol",
        prefix_text= "R$",
        keyboard_type= ft.KeyboardType.NUMBER
    )
    dlg_modal = ft.AlertDialog(
        modal= True,
        title=ft.Text("Melhor abastcer com:"),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("ok", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("flex fuel", size=35, weight= "bold"),
                alignment=ft.alignment.center,
            ),
            #expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md":4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md":4, "xl": 2})
            ]
        )
    )


ft.app(main)
