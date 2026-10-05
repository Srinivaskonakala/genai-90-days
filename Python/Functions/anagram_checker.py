def anagram(str1, str2):
    return sorted(str1)==sorted(str2)
str1=input()
str2=input()
print(anagram(str1,str2))
