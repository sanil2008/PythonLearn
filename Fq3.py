first = int(input())
second = int(input())
third = int(input())
if((first > second ) and (first > third)):
    print(first,'is greatest')
elif((second > first) and (second > third)):
    print(second,'is greatest')
else:
    print(third,'is greatest')
if((first < second ) and (first < third)):
    print(first,'is smallest')
elif((second < first) and (second < third)):
    print(second,'is smallest')
else:
    print(third,'is smallest')



num1 = max(first,second,third)
num2 = min(first,second,third)
print(num1,"is greatest",num2,"is smallest")
