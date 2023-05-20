"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def check_age(age):
    if 0 <= age < 6:
       return 'Вы должны учиться в детском саду'
    if 6 <= age < 18:
       return 'Вы должны учиться в школе'
    if 18 <= age < 25:
       return 'Вы должны учиться в ВУЗе'
    return 'Вы должны работать'

def main():
    while True:
        try:
          user_input = input('Введите возраст: ')
          age = int(user_input)
          if age < 0 or age > 200:
             print('Возраст не может быть меньше 0 или больше 200')
             continue
          
          result = check_age(age)
          print(result)
          break
        except (TypeError, ValueError):
          print('Ошибка определения возраста: возраст должен быть числом')
if __name__ == "__main__":
    main()
