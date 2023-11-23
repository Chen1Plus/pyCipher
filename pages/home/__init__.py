from dataclasses import dataclass
from nicegui import ui

from engine import vigenere_core as vc
from pages.home.style import *


@dataclass
class Data:
    key: str = ''
    text: str = ''


def index():
    with (ui.column().classes(body)):
        ui.label('Vigenère Cipher').classes(h1)
        ui.input(
            label='Key',
            validation={'Invalid key. Only alphabetic characters are valid.': lambda key: key.isalpha()},
        ).classes('w-full max-w-xl mx-auto').bind_value(Data, 'key')
        ui.textarea(
            label='Text',
            validation={'Text is required': lambda text: text != ''},
        ).classes('w-full max-w-3xl mx-auto h-40') \
            .bind_value(Data, 'text').props('clearable')

        with ui.row().classes('mx-auto'):
            ui.button(
                'Encrypt',
                on_click=lambda: result.set_text(vc.encrypt(key=Data.key, text=Data.text)),
            )

        result = ui.label().classes('text-justify w-full max-w-3xl mx-auto')
