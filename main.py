
import PySimpleGUI as psg
import pyperclip as pc

import Sorts

'''---Описание элементов интерфейса---'''


psg.theme("DarkBrown2")
rightClickMenu = ['', ['Copy', 'Paste']]
layout = [[psg.Text("отсортированная последовательность чисел", justification='center', size=(450, 1), font=('Arial', 15), text_color='yellow')],
          [psg.Multiline(key='output', size=(60, 4), disabled=True)],
          [psg.Text("количество сравнений элементов: ", size=(50, 1), font=('Arial', 10), text_color='yellow'),
           psg.Text("", size=(50, 1), key='compares', font=('Arial', 15), text_color='red', background_color='yellow')],
          [psg.Text("количество обменов элементов: ", size=(50, 1), font=('Arial', 10), text_color='yellow'),
           psg.Text("", size=(50, 1), key='swaps', font=('Arial', 15), text_color='red', background_color='yellow')],
          [psg.Text("количество затраченного времени: ", size=(50, 1), font=('Arial', 10), text_color='yellow'),
           psg.Text("", size=(50, 1), key='time', font=('Arial', 15), text_color='red', background_color='yellow')],
          [psg.Checkbox("cортировка по убыванию", default=False, key="check_order")],
          [psg.Combo(['Сортировка пузырьком','Коктейльная сортировка', 'Сортировка вставками', 'Сортировка расчёской',
                      'Сортировка Шелла', 'Сортировка деревом', 'Гномья сортировка','Сортировка выбором']
                     , size=(30, 1), key='sort_type', readonly=True, default_value='Сортировка пузырьком')],
          [psg.Text("введите последовательность чисел через пробел", size=(450, 1), justification='center', font=('Arial', 15), text_color='yellow')],
          [psg.Multiline(default_text="1 2 3", right_click_menu=rightClickMenu, key='input', size=(60, 4))],
          [psg.OK(size=(30,2)), psg.Cancel(size=(30,2))]]



window = psg.Window('Алгоритмы сортировки', layout,
                    size=(900, 450))


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
        try:
            pc.copy(window['input'].Widget.selection_get())
        except:
            pass
    elif event in 'Paste':
        window['input'].Update(window['input'].get() + pc.paste())
    elif event in 'OK':
        #нажатие на кнопку ввода - происходит обработка введённого массива чисел и вывод полученной информации
        elems = []
        ts = 0.0
        for elem in window['input'].get().split():
            try:
                elems.append(float(elem))
            except:
                pass
        compares, swaps, ts = s.sort(elems, sort_type=window['sort_type'].get(), reverse=window['check_order'].get())


        window['compares'].Update(compares)
        window['swaps'].Update(swaps)
        window['time'].Update("{:.{}f} sec".format(ts, 20))

        elems = [str(item) for item in elems]



        window['output'].Update(", ".join(elems))

#завершение программы и закрытие окна
window.close()

