
"""
Guess the Number (Case #4)
- Игра загадывает число от 1 до 100.
- Пользователь делает попытки угадать число.
- Подсказки: "Слишком маленькое"/"Слишком большое".
- Ограничение по количеству попыток (по умолчанию 7).
- Валидация ввода и обработка ошибок.
- Возможность задать параметры через аргументы CLI.
"""
from __future__ import annotations
import argparse
import random
import sys
from dataclasses import dataclass


@dataclass
class Bounds:
    low: int = 1
    high: int = 100

    def validate(self) -> None:
        if self.low >= self.high:
            raise ValueError("Нижняя граница должна быть меньше верхней.")


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Игра 'Угадай число' (консольная версия)"
    )
    p.add_argument("--attempts", type=int, default=7, help="Количество попыток (по умолчанию: 7)")
    p.add_argument("--low", type=int, default=1, help="Нижняя граница диапазона (вкл.)")
    p.add_argument("--high", type=int, default=100, help="Верхняя граница диапазона (вкл.)")
    return p.parse_args(argv[1:])


def read_int(prompt: str) -> int:
    print(prompt, end="", flush=True)
    s = sys.stdin.readline()
    if not s:
        raise EOFError("Ожидался ввод числа, но поток ввода закрыт.")
    s = s.strip()
    if s.startswith("+"):
        s = s[1:]
    if not s.isdigit() or not s:
        raise ValueError("Введите целое число.")
    return int(s)


def check_guess(secret: int, guess: int) -> str:
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "hit"


def play_round(attempts: int, bounds: Bounds, rng: random.Random | None = None) -> bool:
    if rng is None:
        rng = random.Random()
    bounds.validate()
    secret = rng.randint(bounds.low, bounds.high)

    print(f"Я загадал число от {bounds.low} до {bounds.high}. У вас {attempts} попыток.")
    for i in range(1, attempts + 1):
        try:
            guess = read_int(f"Попытка {i}/{attempts}. Ваше число: ")
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue
        except EOFError as e:
            print(f"Ошибка ввода: {e}")
            return False

        res = check_guess(secret, guess)
        if res == "hit":
            print(f"Поздравляю, вы угадали число {secret} за {i} попыток!")
            return True
        elif res == "low":
            print("Слишком маленькое.")
        else:
            print("Слишком большое.")

    print(f"Попытки закончились. Было загадано число: {secret}.")
    return False


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.attempts <= 0:
        print("Количество попыток должно быть положительным.")
        return 2
    try:
        b = Bounds(low=args.low, high=args.high)
        b.validate()
    except ValueError as e:
        print(f"Ошибка параметров: {e}")
        return 2

    _ = play_round(args.attempts, b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
