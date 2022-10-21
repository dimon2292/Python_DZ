src = not False and True or False and not True

# TODO расписать упрощение выражения
src = True and True or False and True # избавляемся от отрицаний
src = True or False # избавляемся от логического И
src = True # избавляемся от логического ИЛИ
result = True  # TODO подставить результат выражения

print(src == result)
