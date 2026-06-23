def one(number):
    """
    finds prime factors of number using for loop
    """
    print("\ndifficult.one: ")

    factors = []
    remaining = number
    for candidate in range(2, number + 1):
        while remaining % candidate == 0:
            if candidate not in factors: 
                factors.append(candidate)
            remaining = remaining // candidate
    print("\t", f"prime factors of {number} = {factors}")

def two(n):
    """
    calculates the nth term of the Fibonacci sequence using a while loop
    """
    print("\ndifficult.two: ")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else: 
        second_to_last = 0
        last = 1
        i=1
        while i < n:
            total = last + second_to_last
            second_to_last = last
            last = total
            i  += 1
        result = last
    print("\t", f"{n}th fibonacci term = {result}")

def three(word_one, word_two):
    """
    checks if given string is an anagram using for loop
    """
    print("\ndifficult.three: ")

    cleaned_one = word_one.replace(" ", "").lower()
    cleaned_two = word_two.replace(" ", "").lower()

    letter_counts = {}
    for letter in cleaned_one:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    for letter in cleaned_two:
        letter_counts[letter] = letter_counts.get(letter, 0) - 1

    is_anagram = True
    for count in letter_counts.values():
        if count != 0:
            is_anagram = False
            break
    
    if is_anagram:
        print("\t", f"{word_one} and {word_two} are anagrams")
    else:
        print("\t", f"{word_one} and {word_two} are not anagrams")

def four(first_term, common_difference, n):
    """
    Prints first n terms of arithmetic sequence using while loop
    """
    print("\ndifficult.four: ")
    term = first_term
    i = 0
    print("\t", f"first {n} terms (difference = {common_difference}) =", end = " ")
    while i < n:
        if i != n - 1:
            print(term, end = ", ")
        else:
            print(term)
        term = term + common_difference
        i += 1

def five(numbers):
    """
    finds the median of a given list of numbers using a for loop
    """
    print("\ndifficult.five: ")
    sorted_numbers = []
    remaining = list(numbers)
    for _ in range(len(numbers)):
        smallest = remaining[0]
        for value in remaining:
            if value < smallest:
                smallest = value
        sorted_numbers.append(smallest)
        remaining.remove(smallest)

    length = len(sorted_numbers)
    middle = length // 2
    if length % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) /2
    print("\t", f"median of {numbers} = {median}")

def six(number):
    """
    checks if given number is perfect number using while loop
    """
    print("\ndifficult.six: ")

    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    if number > 0 and total == number:
        print("\t", f"{number} is a perfect number")
    else:
        print("\t", f"{number} is not a perfect number")

def seven(number):
    """
    prints sum of a ll digits in a given number using for loop
    """
    print("\ndifficult.seven: ")

    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    print("\t", f"sum of digits in {number} = {total}")

def eight(sentence):
    """
    finds the longest word in given sentence using while loop
    """
    print("\ndifficult.eight: ")

    words = sentence.split()
    longest = ""
    i = 0
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1
    print("\t", f"longest word in {sentence} = {longest}")

def nine(sentence):
    """
    checks if a given string is a pangram using a for loop
    """
    print("\ndifficult.nine: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowered = sentence.lower()

    is_pangram = True
    for letter in alphabet:
        if letter not in lowered:
            is_pangram = False
            break
    
    if is_pangram:
        print("\t", f"{sentence} is a pangram")
    else:
        print("\t", f"{sentence} is not a pangram")

def ten():
    """
    prints prime numbers between 1 and 1000 using a while loop
    """
    print("\ndifficult.ten")

    primes = []
    number = 2
    while number <= 1000:
        is_prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            primes.append(number)
        number += 1
    print("\t", f"primes between 1 and 1000 = {primes}")

