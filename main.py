
import flet as ft
import flet_fastapi
import logging
import uvicorn
import sys


if sys.stdout.isatty():
    logging_format = "\033[93m%(levelname)s\033[0m[%(asctime)s] %(message)s"
else:
    logging_format = "%(levelname)s[%(asctime)s] %(message)s"

logging.basicConfig(level=logging.INFO, format=logging_format)

logger = logging.getLogger()


async def layout_simple(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Text('Hi flet!', bgcolor=ft.colors.YELLOW_100)
    )


async def layout_row_compact(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Row([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100),
            ft.VerticalDivider(width=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ], expand=True)
    )


async def layout_row_expand(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Row([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.VerticalDivider(width=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100, expand=True),
        ], expand=True)
    )


async def layout_row_3_area(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Row([
            ft.Text('Left Pane', bgcolor=ft.colors.YELLOW_100, width=100),
            ft.VerticalDivider(width=10),
            ft.Text('Content', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.VerticalDivider(width=10),
            ft.Text('Right Pane', bgcolor=ft.colors.YELLOW_100, width=100),
        ], expand=True)
    )


async def layout_col_compact(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ])
    )


async def layout_col_expand(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100, expand=True),
        ], expand=True))


async def layout_col_bottom(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_col_3_area(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Text('Content', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_col_3_area_scroll(page: ft.Page) -> None:
    page.title = "Hi flet!"
    contents = [ft.Text(f'Large content - {i}') for i in range(100)]
    
    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Column(contents, expand=True, scroll=ft.ScrollMode.ALWAYS),
            ft.Divider(height=10),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_col_3_area_scroll_fullwidth(page: ft.Page) -> None:
    page.title = "Hi flet!"
    contents = [ft.Text(f'Large content - {i}') for i in range(100)]
    
    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Row([ft.Column(contents, expand=True, scroll=ft.ScrollMode.ALWAYS)], expand=True),
            ft.Divider(height=10),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_3x3(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=2),
            ft.Row([
                ft.Text('Left Pane', bgcolor=ft.colors.YELLOW_100),
                ft.VerticalDivider(width=10),
                ft.Text('Content', bgcolor=ft.colors.YELLOW_100, expand=True),
                ft.VerticalDivider(width=10),
                ft.Text('Right Pane', bgcolor=ft.colors.YELLOW_100),
            ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.Divider(height=2),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_3x3_scroll(page: ft.Page) -> None:
    page.title = "Hi flet!"

    long_text = 'This is long text. ' * 1000

    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=2),
            ft.Row([
                ft.Text('Left Pane', bgcolor=ft.colors.YELLOW_100),
                ft.VerticalDivider(width=10),
                ft.Column([ft.Text(long_text, bgcolor=ft.colors.YELLOW_100)],
                          expand=True,
                          scroll=ft.ScrollMode.ALWAYS),
                ft.VerticalDivider(width=10),
                ft.Text('Right Pane', bgcolor=ft.colors.YELLOW_100),
            ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.Divider(height=2),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


async def layout_3x3_list_scroll(page: ft.Page) -> None:
    page.title = "Hi flet!"

    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=2),
            ft.Row([
                ft.Text('Left Pane', bgcolor=ft.colors.YELLOW_100),
                ft.VerticalDivider(width=10),
                ft.Column([ft.ListView([ft.Text(f'{i} Hi') for i in range(100)], width=300)],
                          scroll=ft.ScrollMode.ALWAYS),
                ft.Text('Right Pane', bgcolor=ft.colors.YELLOW_100, expand=True),
            ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.Divider(height=2),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))


logger.info('Start test_flet module.')

app = flet_fastapi.app(layout_col_3_area_scroll_fullwidth)


if __name__ == "__main__":
    logger.info('Start test_flet main.')

    uvicorn.run("main:app", port=8080, reload=True)
