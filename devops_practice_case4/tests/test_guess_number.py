
import io
import random
import sys
from guess_number import check_guess, play_round, Bounds

def test_check_guess():
    assert check_guess(50, 10) == "low"
    assert check_guess(50, 99) == "high"
    assert check_guess(50, 50) == "hit"

class StdinStub:
    def __init__(self, inputs):
        self.inputs = list(inputs)
    def readline(self):
        return self.inputs.pop(0) if self.inputs else ""

def test_play_round_smoke(monkeypatch):
    rng = random.Random(42)
    b = Bounds(1, 10)
    stub = StdinStub(["5\n", "7\n", "9\n", "10\n", "8\n", "6\n", "3\n"])
    monkeypatch.setattr(sys, "stdin", stub)
    # smoke-test: функция должна выполниться и вернуть bool
    ok = play_round(attempts=7, bounds=b, rng=rng)
    assert isinstance(ok, bool)
