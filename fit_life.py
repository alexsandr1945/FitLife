"""
Проект FitLife - MVP версия 1.0
Определение индекса массы тела и суточной нормы потребления воды пользователем
"""
# Стандартная норма воды для поддержания водного баланса мл/кг
VOLUME_PER_KILOGRAM = 30
# Коэффициэнт для перевода единиц измерения объёма мл в л
RATIO = 1000


def calculate_bmi(weight: float, height: float) -> float:
    """
    Расчёт индекса массы тела
    (его значение округлено до одного знака после запятой)
    Формула ИМТ: вес разделить на (рост в квадрате)
    """
    return round(weight / (height ** 2), 1)


def calculate_water_norm(weight: float) -> float:
    """Расчёт нормы воды воды (мл):"""
    water_ml = weight * VOLUME_PER_KILOGRAM
    # Преобразуем норму воды из мл в л и окружляем до двух знаков после запятой
    return round(water_ml / RATIO, 2)


def main():
    """Основная функция"""
    # Знакомство (получение от пользователя имени и возраста)
    print()
    print('Здравствуйте! Вас приветствует проект FitLife - MVP версия 1.0')
    print(
        'Мы поможем определить вашу суточную норму потребления воды и '
        'индекс массы тела.',
    )
    print()
    user_name = input('Введите, пожалуйста, ваше имя: ')
    while True:
        try:
            user_age = int(
                input(f'Введите, {user_name}, пожалуйста,'
                      'ваш возраст (количество полных лет): ')
            )
            print()
            break
        except ValueError:
            print('Введенное значение должно быть целым числом!')
    # Сбор данных (получение от пользователя значений его веса и роста)
    while True:
        try:
            user_weight = float(
                input(f'Введите, {user_name}, пожалуйста, ваш вес (в кг): ')
            )
            break
        except ValueError:
            print('Введенное значение должно быть действительным числом!')
        print()
    while True:
        try:
            user_height = float(
                input(f'Введите, {user_name}, пожалуйста,'
                      'ваш рост (в метрах, например 1.75): ')
            )
            break
        except ValueError:
            print('Введенное значение должно быть действительным числом!')
    # Получение индекса массы тела и суточной нормы потребления воды
    bmi = calculate_bmi(user_weight, user_height)
    water_l = calculate_water_norm(user_weight)
    # Вывод отчёта для пользователя
    print()
    print(f'Отчёт для пользователя: {user_name} ({user_age} лет)')
    print('*' * 40)
    print(f'Ваш индекс массы тела: {bmi}')
    print(f'Рекомендуемая норма воды: {water_l} л. в день')
    print('*' * 40)
    print('Расчет окончен. Будьте здоровы!')
    print()


if __name__ == '__main__':
    main()
