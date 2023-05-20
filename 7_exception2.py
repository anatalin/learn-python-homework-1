"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price_value = float(price)
        discount_value = float(discount)
        max_discount_value = int(max_discount)
    except (ValueError, TypeError):
        return f'Переданы некорректные, ожидаются (float, float, int)'

    price_value = abs(price_value)
    discount_value = abs(discount_value)
    max_discount_value = abs(max_discount_value)
    if max_discount_value >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount_value >= max_discount_value:
        return price_value
    else:
        return price_value - (price_value * discount_value / 100)
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
