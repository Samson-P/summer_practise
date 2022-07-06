# This is a 3V

import PySimpleGUI
import numpy
import matplotlib.pyplot as plt
import io
from PIL import Image


def render(a, b, c):
    y1 = lambda x: -1/a * x + b
    y2 = lambda x: numpy.sin(c*x)
    fig = plt.subplots()
    x = numpy.linspace(-3, 3, 100)
    plt.plot(x, y1(x))
    plt.plot(x, y2(x))
    plt.savefig('graph_var_3.png')
    path = "graph_var_3.png"
    return path


def frame():
    image = Image.open(render(1, 1, 1))
    image.thumbnail((600, 600))
    bios = io.BytesIO()

    PySimpleGUI.theme('Dark')

    layout = [
        [PySimpleGUI.Button('Считать'), PySimpleGUI.Button('Перезапуск')],
        [PySimpleGUI.Text('Ниже введите данные a, b и c:')],
        [PySimpleGUI.Text('Введите значение параметра а = '), PySimpleGUI.InputText('1', size=(10, 10))],
        [PySimpleGUI.Text('Введите значение параметра b = '), PySimpleGUI.InputText('1', size=(10, 10))],
        [PySimpleGUI.Text('Введите значение параметра c = '), PySimpleGUI.InputText('1', size=(10, 10))],

        [PySimpleGUI.Text("Графики функций y1 = -1 / a * x + b и y2 = sin(c * x)")],
        [PySimpleGUI.Image(data=bios.getvalue(), key='graph')],

        [PySimpleGUI.Cancel()]
    ]
    window = PySimpleGUI.Window('Кислицына Таисия 01Б-20 Вар. №3', layout)
    while True:
        event, values = window.read()
        if event == 'Считать':
            a = int(values[0])
            b = int(values[1])
            c = int(values[2])
            image = Image.open(render(a, b, c))
            image.thumbnail((600, 600))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window['graph'].update(data=bio.getvalue())
        if event == 'Cancel':
            layout2 = [
                [PySimpleGUI.Text('Хотите выйти из программы?')],
                [PySimpleGUI.Text('Не сохраненные данные будут потеряны.')],
                [PySimpleGUI.Button('да'), PySimpleGUI.Cancel()]
            ]
            question = PySimpleGUI.Window('Осторожно!', layout2)
            k, b = question.read()
            question.close()
            if k == 'да':
                window.close()
                return 0
                break
            del layout2, k, b, question
        if event in (None, None):
            return 0
            break
        if event == 'Перезапуск':
            layout2 = [
                [PySimpleGUI.Text('Хотите перезапустить окно?')],
                [PySimpleGUI.Text('Введенный текст будет потерян =/')],
                [PySimpleGUI.Button('да'), PySimpleGUI.Cancel()]
            ]
            question = PySimpleGUI.Window('Внимание!', layout2)
            k, b = question.read()
            question.close()
            if k == 'да':
                window.close()
                G = [[0, 0], [0, 0]]
                return 1
                break

            del layout2, k, b, question


if __name__ == '__main__':
    while True:
        out = frame()
        if out == 0:
            break
