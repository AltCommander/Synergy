
import math
import subprocess, sys, os
from factorial_calculator import parse_positive_int, compute_factorial

def test_parse_positive_int_ok():
    assert parse_positive_int("1") == 1
    assert parse_positive_int("+10") == 10
    assert parse_positive_int(" 7 ") == 7

def test_parse_positive_int_bad():
    for bad in ["", "  ", "-1", "0", "1.5", "abc", "+", "--2"]:
        try:
            parse_positive_int(bad)
            assert False, f"Expected ValueError for {bad!r}"
        except ValueError:
            pass

def test_compute_factorial_matches_math():
    for n in [1, 2, 5, 10, 20, 50]:
        assert compute_factorial(n) == math.factorial(n)

def run_cli(arg: str):
    proc = subprocess.run([sys.executable, "factorial_calculator.py", arg],
                          capture_output=True, text=True, cwd=os.path.dirname(__file__) or ".")
    return proc.returncode, proc.stdout + proc.stderr

def test_cli_ok():
    # Запуск из корня проекта
    code = subprocess.run([sys.executable, "factorial_calculator.py", "6"],
                          capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)) or ".")
    assert code.returncode == 0
    assert "6! = 720" in (code.stdout + code.stderr)
