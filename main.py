# This is a 3V: G = A * B'

import PySimpleGUI
import sys
import subprocess
import numpy


G = [[0, 0], [0, 0]]
#G = lambda x, y, z, a, b, c, q, w, e, r, t, u: numpy\
#    .matmul([[x, y, z], [a, b, c]], numpy.array([[q, w, e], [r, t, u]]).transpose())


def math_numpy(A, B):
    global G
    G = numpy.matmul(A, numpy.array(B).transpose())
    return G


def frame():
    global G
    PySimpleGUI.theme('Dark')

    layout = [
        [PySimpleGUI.Button('Считать'), PySimpleGUI.Button('Перезапуск')],
        [PySimpleGUI.Text('Ниже введите данные: А и В матрицы размерностью 2*2')],
        [PySimpleGUI.InputText('0', size=(10, 10)), PySimpleGUI.InputText('0', size=(10, 10)),
         PySimpleGUI.InputText('0', size=(10, 10)), PySimpleGUI.InputText('0', size=(10, 10))],
        [PySimpleGUI.InputText('0', size=(10, 10)), PySimpleGUI.InputText('0', size=(10, 10)),
         PySimpleGUI.InputText('0', size=(10, 10)), PySimpleGUI.InputText('0', size=(10, 10))],

        [PySimpleGUI.Text("G = A * B' = ...")],

        [PySimpleGUI.InputText(G[0][0], size=(10, 10), key='aa'), PySimpleGUI.InputText(G[0][1], size=(10, 10), key='ab')],
        [PySimpleGUI.InputText(G[1][0], size=(10, 10), key='ba'), PySimpleGUI.InputText(G[1][1], size=(10, 10), key='bb')],

        [PySimpleGUI.Cancel()]
    ]
    window = PySimpleGUI.Window('Кислицына Таисия 01Б-20 Вар. №3', layout)
    while True:
        event, values = window.read()
        if event == 'Считать':
            A = [[int(values[0]), int(values[1])], [int(values[4]), int(values[5])]]
            B = [[int(values[2]), int(values[3])], [int(values[6]), int(values[7])]]
            math_numpy(A, B)
            window['aa'].update(value=G[0][0])
            window['ab'].update(value=G[0][1])
            window['ba'].update(value=G[1][0])
            window['bb'].update(value=G[1][1])
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
