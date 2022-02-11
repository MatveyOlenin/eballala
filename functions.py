import random
import constants
import time
import answers as an

a = [128, 222, 76, 191, 281, 169, 274, 228, 238, 211, 97, 295, 105, 329, 493, 116, 273, 134, 0, 0, 0, 211, 161,
     190, 192, 72, 96, 102]


def n_po_k(n, k):  # n - номер, k - к-во нужных задач
    teht = ''
    if n > 27:
        teht += 'номер задания не может быть больше 27\n'
    elif n == 0:
        teht += 'номер задания не может быть равен 0\n'
    elif n < 0:
        teht += 'номер задания не может быть отрицательным\n'
    if n == 19 or n == 20 or n == 21:
        n = 28
    if k > constants.a[n - 1]:
        teht += 'в файле больше', constants.a[n - 1], 'задач\n'
    elif k < 0:
        teht += 'количество нужных задач не может быть отрицательно\n'
    elif k == 0:
        teht += 'количество нужных задач не может быть равно 0\n'
    if 0 < n <= 28 and 0 < k <= constants.a[n - 1]:
        mas = []  # конечный массив
        while len(set(mas)) != k:
            mas.append(int(random.randint(1, constants.a[n - 1])))
        return list((set(mas)))


def write(n, k):
    stroka = ''
    for i in sorted(n_po_k(n, k)):
        stroka += str(i) + '  '
    return stroka


def convert_to_preferred_format1(sec):
    o = []
    sec=round(sec)
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minuts = sec // 60
    sec %= 60
    o.append(hour)
    o.append(minuts)
    o.append(sec)
    if o[0] != 0:
        return f'Вы потратили {o[2]} секунд, {o[1]} минут и {o[0]} часов на выполнение заданий'
    else:
        if o[1] == 0:
            if o[2] == 0:
                return f'Вы потратили 0 секунд на выполнение заданий, это невозможно'
            else:
                return f'Вы потратили {o[2]} секунд на выполнение заданий'
        else:
            return f'Вы потратили {o[2]} секунд и {o[1]} минут на выполнение заданий'


def convert_to_preferred_format2(sec, n):
    o = []
    sec = round(sec / n)
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minuts = sec // 60
    sec %= 60
    o.append(hour)
    o.append(minuts)
    o.append(sec)
    if o[0] != 0:
        return f'В среднем на каждую задачу вы потратили {o[2]} секунд, {o[1]} минут и {o[0]} часов'
    else:
        if o[1] == 0:
            if o[2] == 0:
                return f'Вы потратили 0 секунд на выполнение заданий, это невозможно'
            else:
                return f'В среднем на каждую задачу вы потратили {o[2]} секунд'
        else:
            return f'В среднем на каждую задачу вы потратили {o[2]} секунд и {o[1]} минут'


def ending(n, k):
    print(f'Задания номера {str(n)} :\n{write(n, k)}\n Время началось, напиши "ready" и я отправлю тебе время, '
          f'за которое ты выполнял программу и среднее время на каждое задание, а также ответы на них')
    time_start = time.time()
    finished = input()
    if finished.lower() == 'ready':
        time_end = time.time() - time_start
        print(convert_to_preferred_format1(time_end))
        print(convert_to_preferred_format2(time_end, n))
