# Задание 17.9.1 QAP1007

vvod = input("Введите последовательность чисел через пробел: ")

element = int(input("Введите любое число: "))

vvod = list(map(int, vvod.split()))

vvod.sort()

def bi_search(element, vvod) -> int:
    left, right = 0, len(vvod)
    while left < right:
        middle = (left + right) // 2
        if element > len(vvod):
            print("Введенное число не входит в этот диапаазон")
        elif vvod[middle] < element:
            left = middle + 1
        else:
            right = middle
        return left
print("Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу: ")
print(bi_search(element, vvod))

