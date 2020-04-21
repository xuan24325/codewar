#1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
      result = []
      for i in range(1,number):
        if i % 3 ==0 or i%5==0:
           result.append(i)
      return sum(result)

#2 
A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square

def is_square(n):
    if n < 0:
        return False
    else:
        for i in range(0, int(n/2+2)):
            if (i * i) == n:
                return True
        return False
        
 #3 
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
 
 
