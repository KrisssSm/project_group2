№4
а. n = int(input())
sum=0 #накопитель, который изначально равен 0
for i in range(1, n+1):
    sum=sum+i**3 #присваиваем накопителю значение суммы кубов от единицы до заданного числа
print(sum)
б. n = int(input())
first_factorial=1 #Приравниваем значение факториала на данном шаге к 1
sum=0 #изначально сумма равна нулю
for i in range(1, n+1):
    first_factorial = first_factorial * i #cчитаем факториал умножая числа в промежутке
    sum=sum+first_factorial #сумме прибавляем значение факториала на этом шаге
print(sum)
