
def recursive_nth_fibo(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        fib_sum = recursive_nth_fibo(number - 1) + recursive_nth_fibo(number - 2)

    return fib_sum


def main():
    fibon_sum = recursive_nth_fibo(5)
    return fibon_sum


if __name__ == "__main__":
    print(main())
