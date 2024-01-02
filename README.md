# Flet Layout Example

## layout_simple

![layout_simple](images/layout_simple.png)

```python
    await page.add_async(
        ft.Text('Hi flet!', bgcolor=ft.colors.YELLOW_100)
    )
```

## layout_row_compact

![layout_row_compact](images/layout_row_compact.png)

```python
    await page.add_async(
        ft.Row([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100),
            ft.VerticalDivider(width=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ], expand=True)
    )
```

## layout_row_expand

![layout_row_expand](images/layout_row_expand.png)

```python
    await page.add_async(
        ft.Row([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.VerticalDivider(width=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100, expand=True),
        ], expand=True)
    )
```

## layout_row_3_area

![layout_row_3_area](images/layout_row_3_area.png)

```python
    await page.add_async(
        ft.Row([
            ft.Text('Left Pane', bgcolor=ft.colors.YELLOW_100, width=100),
            ft.VerticalDivider(width=10),
            ft.Text('Content', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.VerticalDivider(width=10),
            ft.Text('Right Pane', bgcolor=ft.colors.YELLOW_100, width=100),
        ], expand=True)
    )
```

## layout_col_compact

![layout_col_compact](images/layout_col_compact.png)

```python
    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ])
    )
```

## layout_col_expand

![layout_col_expand](images/layout_col_expand.png)

```python
    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100, expand=True),
        ], expand=True))
```

## layout_col_bottom

![layout_col_bottom](images/layout_col_bottom.png)

```python
    await page.add_async(
        ft.Column([
            ft.Text('Hi', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('flet', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))
```

## layout_col_3_area

![layout_col_3_area](images/layout_col_3_area.png)

```python
    await page.add_async(
        ft.Column([
            ft.Text('Header', bgcolor=ft.colors.YELLOW_100),
            ft.Divider(height=10),
            ft.Text('Content', bgcolor=ft.colors.YELLOW_100, expand=True),
            ft.Divider(height=10),
            ft.Text('Footer', bgcolor=ft.colors.YELLOW_100),
        ], expand=True))
```

## layout_3x3

![layout_3x3](images/layout_3x3.png)

```python
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
```

## layout_3x3_scroll

![layout_3x3_scroll](images/layout_3x3_scroll.png)

```python
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
```
