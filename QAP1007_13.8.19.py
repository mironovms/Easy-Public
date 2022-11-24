# записываю сколько всего билетов
bilety = int(input("Здравствуйте! Сколько билетов вы хотите приобрести? : "))
# создаю пустой список возрастов по билетам
vozrast = []
summa = 0
# для каждого билета в цикле запрашиваю возраст b и добавляю в список
for x in range(bilety):
    vozrast.append(int(input("Введите возраст для  билета: ")))
    if vozrast[x] < 18:
        cost = 0
        summa += cost
    elif 18 <= vozrast[x] < 25:
        cost = 990
        summa += cost
    elif vozrast[x] >= 25:
        cost = 1390
        summa += cost
# если билетов больше 3 то применяю к сумме скидку 10%
if bilety > 3:
    summa = summa - (summa / 100 * 10)
# вывожу итоговую сумму
print("Сумма к оплате: ", summa)