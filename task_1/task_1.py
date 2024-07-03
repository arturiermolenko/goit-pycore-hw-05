def caching_fibonacci():
    """Outer function for caching fibonacci"""
    cache = {}

    def fibonacci(n):
        """Fibonacci function"""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))  # Output 55
    print(fib(15))  # Output 610
