list1 = set(map(int,input("Введите через пробел числа первого списка: ").split()))
list2 = set(map(int,input("Введите через пробел числа второго списка: ").split()))
x = list1.intersection(list2)
print(len(x))