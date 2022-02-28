"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array.
    
    >>> output_all_items([1, 'hello', True])
    1
    'hello'
    True
    
    """
    for item in items:
        print(item)



def get_all_evens(nums):
    """Given an array of numbers, return an array of all even numbers.

    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums




def get_odd_indices(items):
    """Return all odd indecies

    >>> get_odd_indices([1, 'hello', true, 500])
    ['hello', 500]
    """
    odd_indices = []

    for i, item in enumerate(items):
        if i % 2 == 1:
            odd_indices.append(item)

    return odd_indices


def print_as_numbered_list(items):
    """Return count and item in list

    >>> print_as_numbered_list([1, 'hello', true])
    1. 1
    2. hello
    3. true 
    """
    count = 1
    for item in items:
        print(f"{count} : {item}")
        count+=1



def get_range(start, stop):
    """Return nums in range

    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    
    >>> get_range(1, 3)
    [1, 2]  
    """
    nums = []

    i = start
    while i < stop:
        nums.append(i)
        i += 1

    return nums

def censor_vowels(word):
    """Return the word with '*' replacing each vowel
    
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    """
    new_list = []
    for letter in word:
        if letter in 'aeiou':
            new_list.append('*')
        else:
            new_list.append(letter)
    return "".join(new_list)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case.
    
    >>> snake_to_camel('hello world')
    'HelloWorld'   
    """
    camel_case = []

    for word in string.split("_"):
        camel_case.append(word[0].upper() + word[1:])

    return "".join(camel_case)


def longest_word_length(words):
    """Return the length of the longest word in the given array of words.

    >>> longest_word_length(['hello', 'world'])
    5

    >>> longest_word_length(['jellyfish', 'zebra'])
    9
    
    """
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest



def truncate(string):
    """Truncate repeating characters into one character.
    
    >>> truncate('aaaabbbbcccca');
    'abca'

    >>> truncate('hi***!!!! wooow');
    'hi*! wow'
    
    """
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced.
    
    >>> has_balanced_parens('()')
    True

    >>> has_balanced_parens('((This) (is) (good))')
    True
    
    >>> has_balanced_parens('(Oh no!)(')
    False

    """
    
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
    
            if parens < 0:
                return False
    
    return parens == 0


def compress(string):
    """Return a compressed version of the given string.
    
    >>> compress('aabbaabb')
    'a2b2a2b2'

    >>> compress('abc')
    'abc'

    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'

    """

    curr_char = ""
    char_count = 0
    compressed = []

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)

    


