import logging


a, b, c = float(input("Коэффициент a: ")), float(input("Коэффициент b: ")), float(input("Коэффициент c: "))


def get_roots(a: float, b: float, c: float) -> [float, float]:
    """
    Функция определяет дискриминант и возвращает корни уравнения
    """
    D = b ** 2 - 4 * a * c
    if D < 0:
        logging.basicConfig(filename='Quadratic_equation.log', level=logging.ERROR, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.error("Failure")
        return "Введите другие коэффициенты"
    elif D > 0:
        x_1 = (-1 * b + D ** 0.5) / (2 * a)
        x_2 = (-1 * b - D ** 0.5) / (2 * a)
        logging.basicConfig(filename='Quadratic_equation.log', level=logging.INFO, filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.info("Success")
        return x_1.__round__(2), x_2.__round__(2)
    elif D == 0:
        x = (-1 * b) / (2 * a)
        logging.info("Success")
        return x.__round__(2)


result = get_roots(a, b, c)
print(f"Решение уравнения:", *result)
