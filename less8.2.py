n = int(input("Введите число N: "))
x = list(map(int, input("Введите N чисел через пробел ").split()))
x.insert(0,x.pop())
print (x)