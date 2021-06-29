number = [5,6,7]
first = int(input())
if(first == number[0] ):
   print('YES')
   second = int(input())
   if(second == number[1]):
      print('YES')
      third = int(input())
      if(third == number[2]):
          print('YES')
      else:
          print('NO YOU LOST')
   else:
       print('NO YOU LOST')
else:
    print('NO YOU LOST')          
