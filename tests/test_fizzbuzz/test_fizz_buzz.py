from src.tdd.fizz_buzz import fizz_buzz, value_generate


def test_fizz_buzz_value_generate():
    assert value_generate(1) == '1'
    assert value_generate(2) == '2'
    assert value_generate(3) == 'Fizz'
    assert value_generate(5) == 'Buzz'
    assert value_generate(15) == 'FizzBuzz'


def test_fizz_buzz():
    assert fizz_buzz(1) == ['1']
    assert fizz_buzz(2) == ['1', '2']
    assert fizz_buzz(3) == ['1', '2', 'Fizz']
    assert fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert fizz_buzz(15) == [
        '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'
    ]
