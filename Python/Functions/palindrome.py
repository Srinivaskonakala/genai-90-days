def palindrome(num):
    rev=0
    temp=num
    while temp>0:
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if num==rev:
        return True
    else:
        return False

print(palindrome(int(input())))