import logging


def get_average(data: list) -> float:
    """
    Функция находит среднее арифметическое чисел списка
    """
    length = len(data)
    try:
        summa = sum([int(i) for i in data])
    except Exception:
        logging.basicConfig(filename="Arithnetic_mean.log", level=logging.ERROR, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.error("Ошибка при вводе данных")
        raise Exception("ОШИБКА! Передайте в функцию список чисел через пробел")
    else:
        return (summa/length).__round__(2)


def main():
    data = input("Введите список чисел: ").split()
    result = get_average(data)
    logging.basicConfig(filename="Arithnetic_mean.log", level=logging.INFO, filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Среднее арифметическое найдено")
    print("Результат:", result)


if __name__ == "__main__":
    main()

