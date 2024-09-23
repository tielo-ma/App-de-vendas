import flet as ft


def main (page: ft.Page):
    page.bgcolor = '#000000'
    

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src =  elem.image_src
            else:
                elem.opacity = 0.5

                main_image.update()
                options.update()
   

    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        aspect_ratio=9/6,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         controls=[
             main_image :=ft.Image(
                 src='https://www.sindi.org.br/wp-content/uploads/2024/05/img_2512-scaled.jpg'
             ),

             options := ft.Row(
                 alignment=ft.MainAxisAlignment.CENTER,
                 controls=[
                     ft.Container(
                         image_src='https://www.sindi.org.br/wp-content/uploads/2024/05/img_2512-scaled.jpg',
                         width=60,
                         height=60,
                         opacity=1,
                         on_click=change_main_image
                     ),
                       ft.Container(
                         image_src='https://www.pecsite.com.br/wp-content/uploads/2022/04/Famoso_Cd_Arquivo_CRV.jpeg',
                         width=60,
                         height=60,
                         opacity=0.5,
                         on_click=change_main_image
                     ),
                       ft.Container(
                         image_src='https://www.comprerural.com/wp-content/uploads/2016/01/vaca-sindi.jpg',
                         width=60,
                         height=60,
                         opacity=0.5,
                         on_click=change_main_image
                     )
               
                 ]
             )
         ]
        )
    )
    

    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='LEILÃO',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='BOI RAÇA SINDI',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                
                ft.Text(value='Venda de sêmen', color=ft.colors.GREY, italic=True),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$1.999.00',
                            color=ft.colors.WHITE,
                            size=25,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 3 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Genealogia',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='raça sindi a vende dispon[ivel, agende uma vista para tirar as duvidas',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Prêmios',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Primeiro lugar na festa do boi 2023 ; segundo lugar na festa do boi em Itapecerica 2024',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),

                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Dar Lance',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Lance '),
                                ft.dropdown.Option(text='Arrematar'),

                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='1 unid'),
                                ft.dropdown.Option(text='2 unid'),
                                ft.dropdown.Option(text='3 unid'),
                                ft.dropdown.Option(text='4 unid'),
                                ft.dropdown.Option(text='5 unid'),
                            ]
                        )
                    ]
                ),

                ft.Container(expand=True),

                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.RED)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.AMBER
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }

                        
                    )
                ),

                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.RED)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.AMBER
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }
                    )
                )
            ]
        )
    )


    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )




    page.add(layout)
    


if  __name__ == '__main__':
    ft.app(target=main)