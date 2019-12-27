﻿Tasks Python 3

### Programmin Zero
* Понятие алгоритма, переменные, 
* Простые - типы данных.
* Ветвления. Циклы.
* единицы данных - bit, byte
* системы счисления - decimal,binary,hexademical,octal
* Массивы, коллекции 
и функции


### Level 0
* Python - REPL, IDE, console, Jupyter
* math operations
* синтаксис, identations, comments
* Оператор присваивания 
* переменные
* простые типы данных - int, float, str, bool, None 
* встроенные функции print,len,type, int,float,bool,str,dir,help,input

[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
* документация




### Level 1
* types - list, tuple, object
* Функции (functions & arguments), циклы (loops), условия (conditions), code flow (ветвления)
* встроенные функции - sum, min,max, sorted,any,all,reversed,pow




> Написать функцию **calc**, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

> Написать функцию **get_season_name**, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень). В случае если аргумент не входит в числа от 1 до 12 - вернуть None.



### Level 2 
* types - Dictionaries, Sets,callable
* modules - random, string
* methods - list, string, dict


> Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
> Выведите все элементы, которые меньше 5.


```Python
#Самый простой вариант, который первым приходит на ум — использовать цикл for:

for elem in a:
    if elem < 5:
        print(elem)
#Также можно воспользоваться функцией filter, которая фильтрует элементы #согласно заданному условию:

print(list(filter(lambda elem: elem < 5, a)))
#И, вероятно, наиболее предпочтительный вариант решения этой задачи — списковое #включение:

print([elem for elem in a if elem < 5])
```
> Даны списки:
> 
> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
> 
> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
> 
> Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
> 

```Python
#И снова мы можем воспользоваться циклом for:

result = []
for elem in a:
    if elem in b:
        result.append(elem)
#Или функцией filter:

result = list(filter(lambda elem: elem in b, a))
#Или списковым включением:

result = [elem for elem in a if elem in b]

#А можно привести оба списка к множествам и найти их пересечение:

result = list(set(a) & set(b))

# Однако в таком случае каждый элемент встретится 
# в результирующем списке лишь один раз, #т.к. множество поддерживает #уникальность входящих в него элементов. Первые два решения (с фильтрацией) # оставят все дубли на своих местах.
```






> Отсортируйте словарь по значению в порядке возрастания и убывания.

```Python
#Импортируем нужный модуль и объявляем словарь:
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

#Сортируем в порядке возрастания:
result = dict(sorted(d.items(), key=operator.itemgetter(1)))

#И в порядке убывания:

result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
```


> 4 Напишите программу для слияния нескольких словарей в один.

```Python
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
```

```Python
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
```

```Python
result = {**dict_a, **dict_b, **dict_c}
```


> 5 Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

```Python
#Можно воспользоваться функцией sorted:

result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
#Аналогичный результат можно получить с помощью функции nlargest из модуля #heapq:

from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
```


> 6 Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.

```Python
#Второй аргумент функции int отвечает за указание основания системы счисления:
print(int('ABC', 16))
```

> 88 Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

```Python
#Тут всё просто, достаточно сравнить строку с её обратной версией, для чего #можно использовать встроенную функцию reversed:

def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('abba'))
#Того же эффекта можно добиться с помощью срезов:

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('abba')
```



> 77 Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.

```Python
def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n, 0)):
      print(row)
      row = [left + right for left, right in zip(row + y, y + row)]
   
pascal_triangle(6) 

```


> 9 Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

```Python
def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)
```

> 101 Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

```Python
values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)
```


> Выведите первый и последний элемент списка.

```Python
lst = [1, 2, 3, 4, 5]
print(f'Первый: {lst[0]}; последний: {lst[-1]}')
```

> 12  Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.

```Python
def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]

print(get_extension('abc.py'))
print(get_extension('abc'))  # raises ValueError
print(get_extension('.abc'))   # raises ValueError
print(get_extension('.abc.def.'))   # raises ValueError
```





> 13 При заданном целом числе n посчитайте n + nn + nnn.

```Python
def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(5)
```

> 14 Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

```Python
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
]

for x in numbers:
    if x == 237:
        break
    elif x % 2 == 0:
        print(x)
```


> 15 Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

```Python
set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

print(set_1 - set_2)
```


>16 Выведите список файлов в указанной директории.

```Python
from os import listdir
from os.path import isfile, join
files = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files)
```






> 17 Сложите цифры целого числа.

```Python
def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))
```



> 1898 Посчитайте, сколько раз символ встречается в строке.

```Python
string = 'Python Software Foundation'
string.count('o')
```






> 1129 Поменяйте значения переменных местами.

```Python
#Можно написать монструозную конструкцию в стиле языка C:

x = 5
y = 10
temp = x
x = y
y = temp
#Но в Python есть более удобный способ для решения этой задачи:

x = 5
y = 10
x, y = y, x
```

> 212 С помощью анонимной функции извлеките из списка числа, делимые на 15.

```Python
nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))
```

> 221 Нужно проверить, все ли числа в последовательности уникальны.

```Python
def all_unique(numbers):
    return len(numbers) == len(set(numbers))
```



> 

```Python

```



> 22 Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

```Python
import collections

text = 'lorem ipsum dolor sit amet amet amet'
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(common, longest)
```
