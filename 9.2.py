input_str = input("Введите значения h, a и b через ';': ")      
h, a, b = map(int, input_str.split(';'))
import math                                                     #импортируем модуль из библиотеки
d =  a - b                                                      #вычисляем разницу между  подъемом и спуском
n = h / d                                                       #вычисляем на сколько сможет подняться за день
r = h % d                                                       #учитываем остаток от деления
if r  ==  0:
    print(math.ceil(n))
else:
    print(math.ceil(n + 1))