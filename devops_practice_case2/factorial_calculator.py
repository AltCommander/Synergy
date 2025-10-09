
"""
Factorial Calculator (Case #2)
- Запрашивает у пользователя положительное целое число.
- Валидирует ввод (целое, > 0).
- Считает факториал с помощью math.factorial (оптимизированная C-реализация).
- Обрабатывает ошибки (нечисловой ввод, отрицательные, ноль, переполнение не актуально — Python big int).
- Опционально: поддержка запуска с аргументом командной строки.
"""
from __future__ import annotations
import math
import sys


def parse_positive_int(s: str) -> int:
    s = s.strip()
    if not s:
        raise ValueError("Пустой ввод.")
    # Поддержка знака '+'
    if s.startswith('+'):
        s = s[1:]
    # Запрет знака '-'
    if s.startswith('-'):
        raise ValueError("Число должно быть положительным.")
    # Целое число
    if not s.isdigit():
        raise ValueError("Ожидалось положительное целое число.")
    n = int(s)
    if n <= 0:
        raise ValueError("Число должно быть больше нуля.")
    return n


def compute_factorial(n: int) -> int:
    # Используем math.factorial — оптимизированную реализацию на C
    return math.factorial(n)


def main(argv: list[str]) -> int:
    # Неблокирующий режим: число можно передать аргументом
    if len(argv) >= 2:
        raw = argv[1]
    else:
        print("Введите положительное целое число: ", end="", flush=True)
        raw = sys.stdin.readline()

    try:
        n = parse_positive_int(raw)
        result = compute_factorial(n)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return 2
    except Exception as e:
        # Непредвиденные ошибки
        print(f"Непредвиденная ошибка: {e.__class__.__name__}: {e}")
        return 1

    # Вывод результата. Для больших чисел показываем длину.
    digits = len(str(result))
    if digits > 2000:
        # Чтобы не захламлять консоль, сокращаем вывод
        print(f"n = {n}")
        print(f"Факториал содержит {digits} цифр.")
    else:
        print(f"{n}! = {result}")
        print(f"Цифр в результате: {digits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
