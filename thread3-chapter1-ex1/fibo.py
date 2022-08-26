# Fibonacci numbers module

def fibonacci_with_generator(nth):
    a, b = 0, 1
    sequence_number = 0
    while sequence_number < nth:
        a, b = b, a+b
        yield b
        sequence_number += 1

def fibonacci_without_generator(nth):
    a, b = 0, 1
    sequence_number = 0
    while sequence_number < nth:
        a, b = b, a+b
        print(b, end=" ")
        sequence_number += 1

if __name__ == "__main__":
    import sys
    print("Fibonacci sequence with generator")
    for n_fibo in fibonacci_with_generator(int(sys.argv[1])):
        print(n_fibo, end=" ")
    print("\nFibonacci sequence without generator")
    fibonacci_without_generator(int(sys.argv[1]))