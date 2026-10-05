def fibonacci(number):
    a=0
    b=1
    for i in range(number):
        print(a,end=" ")
        c=a+b
        a=b
        b=c

fibonacci(int(input()))
