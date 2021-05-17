# written by: Kirill Mil
# modified and commented by: Bekzod Buyukov

from string import ascii_lowercase


def get_missing_symbols(symbols: str) -> str:
    """ Функция для получения не хватающих букв """

    # для начало организуем множество из всех букв
    # то есть, от a до z
    all_symbols = set(ascii_lowercase)

    # превращаем полученные от пользователя буквы
    # в множество, как делали уже выше
    input_symbols = set(symbols)

    # находим отсутствующие буквы путём вычитания
    # от множества всех букв множество букв
    # данный пользователем
    missing_symbols = all_symbols - input_symbols

    # полученное множество сортируем и записываем
    # в новую переменную
    sorted_missing_symbols = sorted(missing_symbols)

    # в качестве результата выполнения функции
    # возвращаем отсортированное множество 
    # не хватающих букв
    return "".join(sorted_missing_symbols)


# выполняем функцию сразу записываю будущий
# результат выводим в терминал
if __name__ == "__main__":
    print(get_missing_symbols("abcklmn"))