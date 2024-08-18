import random
import logging


class RangeError(Exception):
    pass


def get_random(a: int, b: int) -> int:
    """
    Функция возвращает случайное число из введенного диапазона
    """
    if a < 0 or a > b:
        error_message = "Введен неверный диапазон"
        raise RangeError(error_message)
    else:
        return random.randint(a, b)


def main():
    a, b = int(input("Введите начало диапазона: ")), int(input("Введите конец диапазона: "))
    try:
        result = get_random(a, b)
    except RangeError as e:
        logging.basicConfig(filename="Random_numbers.log", level=logging.ERROR, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.error(e)
        result = e
        raise
    else:
        logging.basicConfig(filename="Random_numbers.log", level=logging.INFO, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.info("Число сгенерировано")
    print("Сгенерированное число:", result)


if __name__ == '__main__':
    main()
