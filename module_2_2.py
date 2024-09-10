first = input("Введите число 1: ")
second = input("Введите число 2: ")
third = input("Введите число 3: ")
if first == second and first == third:
    print(3)
if first == second or first == third or third == second:
    print(2)
else:
    print(0)