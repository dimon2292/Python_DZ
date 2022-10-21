money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while money_capital >= 0:

    money_capital += salary
    money_capital -= spend
    print(money_capital)
    if money_capital >= 0:
        spend *= 1.05
        print(spend, money_capital)
        month += 1




print(month)
