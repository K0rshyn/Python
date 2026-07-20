A = int(input("Баланс Майкла:"))
B = int(input("Баланс Ивана:"))
X = int(input("Минимальная сумма инвестиций:"))
if A >= X and B >= X:
    print("2")
elif A >= X and B < X:
    print("Mike")
elif A < X and B >= X:
    print("Ivan")
elif A < X and B < X and A + B >= X:
    print("1")
else :
    print("0")