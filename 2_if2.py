"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

# из задания не совсем понятно, что делать, если первая строка короче второй
# или если первая длиннее, а вторая 'learn' - возвращать 2 или 3 ?
# поэтому закодил всё прямолинейно по ТЗ)
def compare_strings(str1, str2):
    if (not isinstance(str1, str)) or (not isinstance(str2, str)):
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3
    raise ValueError('Аргументы не подходят ни под одно из условий')

def main():
    print(compare_strings('abc', 1))
    print(compare_strings(1, 'abc'))
    print(compare_strings('abc', 'abc'))
    print(compare_strings('abc', 'a'))
    print(compare_strings('abc', 'learn'))
    print(compare_strings('abc', 'def'))
    
if __name__ == "__main__":
    main()
