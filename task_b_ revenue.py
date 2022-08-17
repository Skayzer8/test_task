def get_revenue(n: int, m: int, x: int) -> int:
    """
    Функция принимает на вход целые положительные числа:
    N - количество этажей,
    M - число этажей после которого увеличивается стоимость,
    X - стоимость квартиры на первом этаже.
    Возвращает (revenue) выручку от продажи всех квартир.
    """
    GROWTH_PRICE = 1000
    revenue = 0
    for i in range(n//m):
        for k in range(1, m+1):
            revenue += x + GROWTH_PRICE*i
    for i in range(n % m):
        revenue += (x + GROWTH_PRICE*(n//m))
    return revenue


n, m, x = int(input()), int(input()), int(input())

if __name__ == '__main__':
    print(get_revenue(n, m, x))


assert get_revenue(30, 10, 10000) == 330000
assert get_revenue(15, 5, 10000) == 165000
assert get_revenue(2, 1, 10000) == 21000
assert get_revenue(11, 3, 10000) == 125000
assert get_revenue(45, 10, 10000) == 530000
assert get_revenue(45, 10, 10000) == 530000
