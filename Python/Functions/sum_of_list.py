def list_sum(numbers):
    total=0
    for num in numbers:
        total+=num
    return total

print(list_sum(list(map(int,input().split()))))