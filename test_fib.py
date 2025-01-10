import pytest
from gen_fib import my_genn

def test_fib_1():
    gen = my_genn()
    next(gen)
    result = gen.send(3)
    assert result == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

def test_fib_2():
    gen = my_genn()
    next(gen)
    result = gen.send(5)
    assert result == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_3():
    gen = my_genn()
    next(gen)
    result = gen.send(8)
    assert result == [0, 1, 1, 2, 3, 5, 8], "До n = 8"

def test_fib_4_zero():
    gen = my_genn()
    next(gen)
    result = gen.send(0)
    assert result == [0], "Список для n = 0 содержит только [0]"

def test_fib_5_large():
    gen = my_genn()
    next(gen)
    result = gen.send(16) 
    assert result[-1] <= 1000, "Последнее значение не превышает 1000"

def test_fib_6_negative():
    gen = my_genn()
    next(gen)
    with pytest.raises(ValueError, match="n должно быть неотрицательным"):
        gen.send(-5)

def test_fib_7_multiple_calls():
    gen = my_genn()
    next(gen)
    assert gen.send(2) == [0, 1], "До n = 2"
    assert gen.send(4) == [0, 1, 1, 2], "До n = 4"
    assert gen.send(6) == [0, 1, 1, 2, 3, 5], "До n = 6"
