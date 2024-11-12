class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model  # название автомобиля (строка)
        if self.__is_valid_vin(__vin) and self.__is_valid_numbers(__numbers):
            self.__vin = __vin  # vin номер автомобиля (целое число)
            self.__numbers = __numbers  # номера автомобиля (строка)


    def __is_valid_vin(vin_number):
        if isinstance(Car.__is_valid_vin(vin_number)):
            raise IncorrectVinNumber('Некорректный тип vin_number')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin_number')
        return True

    def __is_valid_numbers(numbers):
        if not isinstance(Car.__is_valid_numbers(numbers)):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')



