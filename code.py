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

def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


# elegant:)
def max_sequence(arr): 

    return max([sum(arr[i:j]) for i in range(len(arr)+1) for j in range(len(arr)+1)])

#8
Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]

def delete_nth(order,max_e):
    resp = []
    for i in order:
        if resp.count(i) < max_e:
            resp.append(i)
    return resp

def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ] 

#9
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

def likes(names):
	if len(names) ==0:
		return 'no one likes this'
	elif len(names) ==1:
		return '%s likes this' % names[0]
	elif len(names)==2:
		return '%s and %s like this' % (names[0], names[1])
	elif len(names)==3:
		return '%s, %s and %s others like this' % (names[0], names[1], len(names)-2) 

def likes(names):
	n= len(names)
	return {
	    0: 	'no one likes this',
	    1:  '{} likes this',
	    2:  '{} and {} like this',
	    3:  '{}, {} and {} like this',
	    4:  '{}, {} and {others} others like this'
	}[min(4, n)].format(*names[:3], others=n-2)

#10
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountain desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
#     for i in range(len(arr)-1): 
      for i in range(len(arr)):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr 

arr=["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))

