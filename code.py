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

def to_jaden_case(string):        
    return " ".join(i.capitalize() for i in string.split())

import string

def toJadenCase(aaa):
    return string.capwords(aaa)
#6
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        if len(sentence[i]) > 4:
            sentence[i] = ''.join(reversed(sentence[i]))
    return ' '.join(sentence)

print(spin_words("Welcome"))    # => "emocleW"



def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split()])

#6
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

# slow one
def unique_in_order(iterable):
    iterable = list(iterable)
    while True:
        for x in range(len(iterable)):
            if iterable[x]==iterable[x-1]:
                del iterable[x]
                break
            if x==len(iterable)-1:
                return iterable	
# quick one
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result

# groupby
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

#7 kadane's algorithm
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):

    sums = []
    for j, e in enumerate(arr):
        sums.append(e) 
        for i in range(j + 1, len(arr)): 
            e += arr[i]
            sums.append(e)
    if all(i<0 for i in arr):
        return 0
    else:
        max_sum = max(sums)
        return max_sum

def max_sequence(arr):

    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg


# simple is better
def max_sequence(arr): 

    return max([sum(arr[i:j]) for i in range(len(arr)+1) for j in range(len(arr)+1)])
