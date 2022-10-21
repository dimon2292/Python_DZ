salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

a = spend * increase        #то на что увеличиваются траты
total_spend = 0             #счетчик всех трат за 10 мес
for i in range(months):
    if i == 0:              # траты первого месяца
        total_spend += spend
    else:                   #траты остальных месяцев
        spend += a
        total_spend += spend
    print(total_spend)

total_salary = salary * 10  #вся зп за 10 мес

need_money = total_spend - total_salary
print(round(need_money))
