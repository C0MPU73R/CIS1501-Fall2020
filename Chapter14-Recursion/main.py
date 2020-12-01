def count_down(number):
    print(number)
    if number > 0:
        count_down(number-1)

count_down(10)


def bad_fib(nth):
    if nth <= 1:
        return 1
    return bad_fib(nth - 1) + bad_fib(nth - 2)


def _better_fib(nth, current_nth, current, previous):
    if nth == current_nth:
        return current + previous
    return _better_fib(nth, current_nth+1, current+previous, current)


def better_fib(nth):
    if nth <= 1:
        return 1
    return _better_fib(nth, 2, 1, 1)


def fib_iteratively(nth):
    if nth <= 1:
        return 1
    current_nth = 2
    previous = 1
    current = 1
    while current_nth != nth:
        next = current + previous
        previous = current
        current = next
        current_nth += 1
    return current + previous


print("FIB!!!")
for number in range(40):
    print(f'{number:2}', ":", better_fib(number), fib_iteratively(number))
