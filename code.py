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
 
 
#4
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
def duplicate_count(s):
    s=s.lower()
    return len([x for x in set(s) if s.count(x) > 1])
      
# len(string) -len(set(string))    

#5
aden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
      
def to_jaden_case(string):
	split_text=string.split()
	revised_text=[]
	for i in split_text:
		revised_text.append(i.capitalize()[0]+i[1:])
	returned_text=" ".join(revised_text)
	return returned_text

