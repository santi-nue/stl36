#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from nicegui import ui

def main():


    ui.label('Hello NiceGUI!')
    ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

    ui.run(native=True)



if __name__ == '__main__':
    main()
