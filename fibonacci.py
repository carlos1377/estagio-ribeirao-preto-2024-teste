from functools import lru_cache


@lru_cache()
def fibonacci(num: int) -> int:
    if num in [0, 1]:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


def is_on_fibonacci_sequence(target: int) -> bool:
    if target == 0:
        return True

    value = 0
    n = 0

    while value < target:
        value = fibonacci(n)

        if value == target:
            return True
        if value > target:
            return False

        n = n + 1


some_fibonacci_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]

for num in some_fibonacci_values:
    print(is_on_fibonacci_sequence(num))

print(is_on_fibonacci_sequence(6))