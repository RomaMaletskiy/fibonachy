def fibonacci_number(n):
    if n < 0:
        raise ValueError("Індекс не може бути від'ємним.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def main():
    print("Добрий день! Дана програма розраховує числа Фібоначчі.")
    try:
        numbers = int(input("Введіть кількість чисел: "))
        
        if numbers <= 0:
            print("Кількість чисел повинна бути більшою за 0.")
        else:
            print("Числа Фібоначчі:")
            for i in range(numbers):
                print(f"{i + 1}: {fibonacci_number(i)}")
    except ValueError:
        print("Будь ласка, введіть коректне число.")


if __name__ == "__main__":
    main()
