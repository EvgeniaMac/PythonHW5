# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

s = 'ABBCCCD'
def encode(s):

    encoding = ""  # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1

    return encoding
k = encode(s)
print(k)
def decode(k):
    code = ''
    count = ''
    for i in k:
        if i.isdigit():
            count += i
        else:
            code += i*int(count)
            count = ''
    return code
c=decode(k)
print(c)


# text = 'ABBCCCD'
# from itertools import groupby
# def rle(text):
#     return [(key, len(tuple(group))) for key, group in groupby(text)]
# print (rle(text))
