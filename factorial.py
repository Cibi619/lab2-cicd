def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print("Factorial of 5 =", factorial(5))