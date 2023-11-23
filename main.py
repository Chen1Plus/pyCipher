from nicegui import ui, native
from pages import home


@ui.page('/')
def index():
    home.index()


ui.run(reload=False, port=native.find_open_port())
