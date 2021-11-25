def main():
    print("Введите стороны треугольника")
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])

    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if c ** 2 == a ** 2 + b ** 2:
            print("Треугольник прямоугольный")
        if c ** 2 < a ** 2 + b ** 2:
            print("Треугольник остроугольный")
        if c ** 2 > a ** 2 + b ** 2:
            print("Треугольник тупоугольный")
    else:
        print("Треугольник не существует")


if __name__ == '__main__':
    main()