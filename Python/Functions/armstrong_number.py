def is_armstrong(num):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum+=d**order
        temp=temp//10
    if num==sum:
        return True
    else:
        return False

print(is_armstrong(int(input())))