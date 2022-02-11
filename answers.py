import pandas as pd


def strochka(s):
    d = [str(x) for x in znach[s]]
    while 'nan' in d:
        d.remove('nan')
    k=[]
    for t in range(len(d)):
        k.append('|'+str(s)+'/'+str(t+1)+'| '+d[t])
    return k


exel_1 = 'answers.xlsx'
znach = pd.read_excel(exel_1, sheet_name='Лист1')
endic = []  # конечный массив
q = [str(i) for i in znach[19]]  # список 19
w = [str(i) for i in znach[20]]  # список 20
e = [str(i) for i in znach[21]]  # список 21
p = []  # список 19-21
for i in range(102):
    stroka = '|19/' + str(i + 1) + '| ' + q[i] + ' |20/' + str(i + 1) + '| ' + w[i] + ' |21/' + str(i + 1) + '| ' + e[
        i]  # ответы 19-21 одно задание
    p.append(str(stroka))

endic.append(strochka(1))
endic.append(strochka(2))
endic.append(strochka(3))
endic.append(strochka(4))
endic.append(strochka(5))
endic.append(strochka(6))
endic.append(strochka(7))
endic.append(strochka(8))
endic.append(strochka(9))
endic.append(strochka(10))
endic.append(strochka(11))
endic.append(strochka(12))
endic.append(strochka(13))
endic.append(strochka(14))
endic.append(strochka(15))
endic.append(strochka(16))
endic.append(strochka(17))
endic.append(strochka(18))
endic.append(p)
endic.append(p)
endic.append(p)
endic.append(strochka(22))
endic.append(strochka(23))
endic.append(strochka(24))
endic.append(strochka(25))
endic.append(strochka(26))
endic.append(strochka(27))

