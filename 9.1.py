input_str = input("Введите значения h, a и b через ';': ")
h, a, b = map(int, input_str.split(';'))
current_height = 0                                          #запускаем счетчик высоты
days = 0                                                    #запускаем счетчик дней
while current_height < h:                                    
    days += 1
    current_height = current_height + a - b
else:
    print("На", days, "день")
