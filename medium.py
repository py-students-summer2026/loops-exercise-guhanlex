def one(numbers):
    """
    Finds largest element in list using for loop
    """
    print("\nmedium.one:")

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    print("\t", f"largest in {numbers} = {largest}")

def two(numbers): 
    """
    Calculates average of list using while loop
    """
    print("\nmedium.two:")

    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    average = total / len(numbers)
    print("\t", f"average of {numbers} = {average}")

def three(text):
    """
    checks if given string is palindrome using for loop
    """
    print("\nmedium.three: ")

    is_palindrome = True
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            is_palindrome = False
            break
    
    if is_palindrome:
        print("\t", f"{text} is a palindrome")
    else:
        print("\t", f"{text} is not a palindrome")
    
def four(first_term, common_ratio, n):
    """
    prints first n terms of geometric sequence using while loop
    """
    print("\nmedium.four: ")
    
    term = first_term
    i = 0
    print("\t", f"first {n} terms (ratio={common_ratio}) =", end=" ")
    while i < n:
        if i != n - 1:
            print(term, end=', ')
        else:
            print(term)
        term = term * common_ratio
        i += 1

def five(numbers):
    """
    Finds second largest element in given list using for loop
    """

    print("\nmedium.five: ")
    
    largest = float("-inf")
    second_largest = float("-inf")
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    print("\t", f"second largest in {numbers} = {second_largest}")

def six(number):
    """
    Calculates factorial of a given number using while loop
    """
    print("\nmedium.six: ")

    original = number
    product = 1
    while number > 1:
        product *= number
        number -= 1
    print("\t", f"{original} factorial = {product}")

def seven(number):
    """
    Checks if given number is a perfect square using for loop
    """
    print("\nmedium.seven: ")

    is_perfect_square = False
    root = 0
    for i in range(number + 1):
        if i * i == number:
            is_perfect_square = True
            root = i
            break

    if is_perfect_square:
        print("\t", f"{number} is a perfect square ({root} * {root})")
    else:
        print("\t", f"{number} is not a perfect square")

def eight():
    """
    Prints sum of all prime numbers between 1 and 100 using while loop
    """ 
    print("\nmedium.eight: ")
    total = 0 
    number = 2
    while number <= 100:
        is_prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            total += number
        number += 1
    print("\t", f"sum of primes between 1 and 100 = {total}")

def nine(sentence):
    """
    Counts the number of words in sentence using for loop
    """
    print("\nmedium.nine: ")
    delimiters = [",", ".", "!", "?"]
    normalized = sentence
    for delimiter in delimiters:
        normalized = normalized.replace(delimiter, " ")

    words = normalized.split()
    count = 0
    for word in words:
        count +=1
    print("\t", f"# words in {sentence} = {count}")

def ten(list_one, list_two):
    """Prints common elements between two lists using while loop
    """
    print("\nmedium.ten: ")

    common = []
    i = 0
    while i < len(list_one):
        j = 0
        while j < len(list_two):
            if list_one[i] == list_two[j] and list_one[i] not in common:
                common.append(list_one[i])
            j += 1
        i += 1
    print("\t", f"common elements between {list_one} and {list_two} = {common}")

    

