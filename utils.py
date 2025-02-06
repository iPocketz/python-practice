def find_max(numbers):
    maximum = 0
    for x in numbers:
        if x > maximum:
            maximum = x
    return maximum