
import PySimpleGUI as psg
import pyperclip as pc
import ctypes

import Sorts

'''---Описание элементов интерфейса---'''

user = ctypes.windll.user32
width = user.GetSystemMetrics(0)
heigth = user.GetSystemMetrics(1)
wunit = width // 40

psg.theme("DarkBrown2")
rightClickMenu = ['', ['Copy', 'Paste']]
layout = [[psg.Text("отсортированная последовательность чисел", justification='center', size=(wunit * 2, 1), font=('Arial', 15), text_color='yellow')],
          [psg.Multiline(key='output', size=(wunit * 2, 5), disabled=True)],
          [psg.Text("количество сравнений элементов: ", size=(wunit * 1, 1), font=('Arial', 10), text_color='yellow'),
           psg.Text("", size=(wunit * 1, 1), key='compares', font=('Arial', 15), text_color='red', background_color='yellow')],
          [psg.Text("количество обменов элементов: ", size=(wunit * 1, 1), font=('Arial', 10), text_color='yellow'),
           psg.Text("", size=(wunit * 1, 1), key='swaps', font=('Arial', 15), text_color='red', background_color='yellow')],
          [psg.Checkbox("cортировка по убыванию", default=False, key="check_order")],
          [psg.Combo(['Сортировка пузырьком','Коктейльная сортировка', 'Сортировка вставками', 'Сортировка расчёской',
                      'Сортировка Шелла', 'Сортировка деревом', 'Гномья сортировка','Сортировка выбором']
                     , size=(wunit, 1), key='sort_type', readonly=True, default_value='Сортировка пузырьком')],
          [psg.Text("введите последовательность чисел через пробел", size=(wunit * 2, 1), justification='center', font=('Arial', 15), text_color='yellow')],
          [psg.Multiline(default_text="1 2 3", right_click_menu=rightClickMenu, key='input', size=(wunit * 2, 5))],
          [psg.OK(size=(wunit * 1,2)), psg.Cancel(size=(wunit * 1,2))]]



window = psg.Window('Алгоритмы сортировки', layout,
                    size=(width // 2, heigth // 2))


s = Sorts.Sorts()


'''---Цикл обработки событий интерфейса (нажатие кнопок и т.п.), в зависимости от события выбираем
нужное действие (имя события совпадает с параметром 'key' элемента, который описан в списке layout)---'''


while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED, "Cancel"):
        #нажатие на кнопку закрытия окна программы и выход из цикла обработки событий
        break
    elif event in 'Copy':
        #при нажатии правой кнопкой мыши вызывается меню с вариантами (скопировать, вставить)
        #но при вставке выделенный текст не меняется, а лишь идёт добавление в конец текущего текста
        pc.copy(window['input'].Widget.selection_get())
    elif event in 'Paste':
        window['input'].Update(window['input'].get() + pc.paste())
    elif event in 'OK':
        #нажатие на кнопку ввода - происходит обработка введённого массива чисел и вывод полученной информации
        elems = []
        for elem in window['input'].get().split():
            try:
                elems.append(float(elem))
            except:
                pass
        compares, swaps = s.sort(elems, sort_type=window['sort_type'].get(), reverse=window['check_order'].get())


        window['compares'].Update(compares)
        window['swaps'].Update(swaps)

        elems = [str(item) for item in elems]



        window['output'].Update(", ".join(elems))

#завершение программы и закрытие окна
window.close()

