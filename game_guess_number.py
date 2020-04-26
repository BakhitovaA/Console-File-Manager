"""
Человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100. 
Компьютер начинает его отгадывать, предлагая игроку варианты чисел. 
Игра продолжается до тех пор пока компьютер не отгадает число.
Игрок общается с компьютером знаками “=”, “>” и “<” с клавиатуры..
"""
import random


def start_game():
    user_answer = ''
    left_interval = 0
    right_interval = 100

    user_number = int(input('Начинаем игру! Загадайте число от 1 до 100 для компьютера: '))

    while user_number < left_interval or user_number > right_interval:
        user_number = int(input('Число должно быть в диапазоне от 0 до 100 включительно. Введите число еще раз: '))
    else:
        while user_answer != '=':
            if right_interval >= left_interval:
                auto_number = random.randint(left_interval, right_interval)
                user_answer = input(f'Загаданное число - это {auto_number}? Введите >, < или =: ')
                while user_answer != '>' and user_answer != '<' and user_answer != '=':
                    print('Введите корректный ответ! Можно вводить знаки >, < или =')
                    user_answer = input(f'Загаданное число - это {auto_number}? Введите >, < или =: ')
                if user_answer == '>':
                    left_interval = auto_number + 1  # исключаем уже выводимое число
                elif user_answer == '<':
                    right_interval = auto_number - 1  # исключаем уже выводимое число
            else:
                print('Вы что-то перепутали. Нет больше чисел в выбранном диапазоне. Конец игры.')
                break
        else:
            print('Ура! Копьютер угадал число!')

    print("Спасибо за игру!")
