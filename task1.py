# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def list_(count = 16) -> list:
    list_ = []
    for i in range(count):
        dict_dec = {}
        dict_bin = {}
        dict_hex = {}
        dict_oct = {}
        dict_dec['dec'] = dict_dec.get('dec', i)
        dict_bin['bin'] = dict_bin.get('bin', bin(i))
        dict_hex['hex'] = dict_hex.get('hex', hex(i))
        dict_oct['oct'] = dict_oct.get('oct', oct(i))
        final_dict = {**dict_bin, **dict_dec, **dict_hex, **dict_oct }
        list_.append(final_dict)
    return list_


pprint(list_())

