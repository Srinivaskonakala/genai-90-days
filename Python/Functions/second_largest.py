def second_largest(numbers):
    largest=numbers[0]
    second=None
    for num in numbers:
        if num>largest:
            second=largest
            largest=num
    return second

print(second_largest(list(map(int,input().split()))))