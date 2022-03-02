                #Задание 1
# a = 'строка'
# b = 12
# c = 12.4
# d = False
# print(a,b,c,d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

                #Задание 2

# x = int(input('Введите количество секунд:'))
#                 #перевод в часы
# y = x // 360
#             #остаток
# z = x % 360
#             #перевод в минуты
# u = z // 60
#             #остаток секунд
# i = z % 60
# print(f'Перевод {x} секунд в формат ЧЧ:ММ:СС : {y}:{u}:{i}')

                #Задание 3
# inp = int(input('Введите число'))
# inp1 = inp * 11
# inp2 = inp * 111
# print(f'При введенном числе n , сумма чисел n, nn, nnn = {inp+inp1+inp2}')

                #Задание 4
# cpch = int(input('Введите целое трехзначное положительное число'))
# while cpch<=0:
#     cpch = int(input('Введите целое трехзначное положительное число'))
# f1 = cpch % 10
# f11 = cpch // 10
# f2 = f11 % 10
# f22 = f11 // 10
# f3 = f22 % 10
# if f1>f2:
#     if f1>f3:
#         print(f'самое большое число {f1}')
#     else :
#         print(f'самое большое число {f3}')
# elif f2>f1:
#     if f2>f3:
#         print(f'самое большое число {f2}')
#     else:
#         print(f'самое большое число {f3}')

                #Задание 5
# vyr = int(input('Введите значение выручки'))
# izd = int(input('Введите значение издержек'))
# if vyr>izd:
#     print(f'Прибыль компании равна : {vyr - izd}')
# else:
#     print(f'Убыток компании равен : {izd - vyr}')

                # Задание 6
# vyr = int(input('Введите значение выручки'))
# izd = int(input('Введите значение издержек'))
# if vyr>izd:
#     prib = vyr - izd
#     rent = prib / vyr
#     print(f'Рентабельность компании равна : {rent}')
#     sotr = int(input('Введите количество сотрудников'))
#     pribna1sotr = prib/sotr
#     print(f'Прибыль компании в расчете на 1 сотрудника равна : {pribna1sotr}')
# else:
#     print(f'Убыток компании равен : {izd - vyr}')

                # Задание 7
# rez = int(input('Введите первый результат'))
# cel = int(input('Введите цель спортсмена'))
# den = 1
# print(f'День {den} : {rez}')
# while rez<cel:
#     den = den +1
#     rez = rez * 1.1
#     print(f'День {den} : {rez:.2f}')
# print(f'В день {den}  спортсмен достиг результата - не менее {cel} км.')