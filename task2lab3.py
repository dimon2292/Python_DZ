def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_

    new_str = str_.lower()
    dict_ = {}
    for i in new_str:
        if i.isalpha():
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dict_ = get_count_char(main_str)

def percentage(old_dict):
    new_dict = {}
    count = sum(old_dict.values())
    print(count)
    for i in (old_dict):
        new_dict[i] = round(100 * old_dict[i] / count, 2)

    return new_dict

print(percentage(dict_))
