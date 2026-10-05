def remove_duplicate(numbers):
    unique=[]
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

print(remove_duplicate(list(map(int,input().split()))))