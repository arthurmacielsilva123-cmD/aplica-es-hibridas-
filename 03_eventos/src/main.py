import flet as ft


def main(page: ft.Page):
    #função do evento
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()

    #declaração de pagina
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHTf

        #declaração de variavel 
    nome = ft.TextField(label="Informe seu nome:", on_submit=exibir_nome)# textfield é o input
    nome_saida = ft.Text()# text é o print


    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com eventos", size=35, weight="bold", font_family= "Arial"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        nome,
        ft.ElevatedButton("Aperta ai arrombado", on_click= exibir_nome, color= "Branco"),
        nome_saida
         
    )
ft.app(main)
