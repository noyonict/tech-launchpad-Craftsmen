def multiply(*args):
    result = 1
    for value in args:
        result = value * result
    return result

print(multiply(2, 3, 4))
print(multiply(0.5, 4))
print(multiply(-2, 8))
print(multiply(10, 0))

