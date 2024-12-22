import math
import re
from collections import Counter


def get_rev_string(input):
    # Approach 1
    '''
    reverse_string=''
    for char in input:
        reverse_string=char+reverse_string
    print(reverse_string)
    '''

    # Approach 2
    # print(input[::-1])

    # Approach 3
    reverse_string = ''.join(reversed(input))
    print(reverse_string)


def get_reverse_of_list(input):
    print('input list ', input)
    # Approach 1
    '''
    input.reverse()
    print('rev list ',input)
    '''
    # Approach 2
    print('rev list ', input[::-1])


def get_largest_element_in_list(input):
    # Approach 1
    '''
    list(input).sort(reverse=True)
    print('sorted list descending ',input)
    list(input).sort()
    print('sorted list ascending ',input)
    print('largest element ',input[-1])
    '''
    # Approach 2
    # print('largest element ',max(input))

    # Approach 3
    largest = input[0]
    for i in input:
        if i > largest:
            largest = i
    print('largest num ', largest)


def get_reverse_of_number(input):
    # Approach 1
    '''
    reverse =0
    while input>0:
        reverse=(reverse*10)+(input%10)
        input // 10 #This is floor division meaning decimal point gets removed from result
    print('reverse number ',reverse)
    return reverse
    '''

    # Approach 2
    # print('reverse number',str(input)[::-1])
    # return str(input)[::-1]

    # Approach 3 if input is negative number
    sign = -1 if input < 0 else 1
    input = input * sign
    rev = int(str(input)[::-1]) * sign
    print('reverse number ', rev)
    return rev


def is_palindrome(input):
    # Approach 1
    if str(input) == str(input)[::-1]:
        print('is palindrome')
        return True
    else:
        print('Not palindrome')
        return False

    # Approach 2
    flag = True if str(input) == str(input)[::-1] else False
    print('flag is ', flag)
    return flag

    # Approach 3
    val = ''.join(reversed(input))
    flag = True if input == val else False
    print('Flag is ', flag)
    return flag

    # Approach 4
    result = True
    left = 0
    right = len(input) - 1
    while left < right:
        if input[left] != input[right]:
            result = False
        left += 1
        right -= 1
    print('result val ', result)
    return result


def get_factorial(input):
    # Approach 1
    fact = 1
    while (input > 0):
        fact *= input
        input -= 1
    print('Factorial value ', fact)

    # Approach 2
    fact = 1
    for _ in range(2, input + 1):
        fact *= _
    print('factorial value ', fact)

    # Approach 3
    if input == 0 or input == 1:
        return input * get_factorial(input - 1)
    else:
        return 1

    # Approach 4
    fact = math.prod([i for i in range(1, input + 1)])
    print('factorial val ', fact)


def get_fibonacci_series(input):
    # here fetch fibonacci series till the input value
    # Approach 1 using recursion
    a, b = 0, 1
    c = a + b
    a = b
    b = c
    print('c val ', c)
    if (c < input):
        get_fibonacci_series(a, b, input)

    # Approach 2 using recursion
    if input <= 1:
        return input
    return get_fibonacci_series(input - 1) + get_fibonacci_series(input - 2)

    # Approach 3 using For loop
    if input <= 1:
        return input
    a, b = 0, 1
    for _ in range(2, input + 1):
        c = a + b
        a, b = b, c
    return b


def get_prime_numbers(input):
    # Approach 1
    final_primes = []
    if input in (0, 1):
        print('No primes in given range')
        return 0
    elif input > 1:
        for i in range(2, input + 1):
            primes = []
            for j in range(1, i + 1):
                if i % j == 0:
                    primes.append(j)
            print('primes ', primes)
            if primes == [1, i]:
                final_primes.append(i)
    print('Final prime list ', final_primes)
    return primes


def is_anagram(input1, input2):
    # Approach 1 easiest
    if sorted(input) == sorted(input2):
        print('result True')
        return True
    else:
        print('result False')
        return False

    # Approach 2 example : rescue, secure
    if len(input1) != len(input2):
        print('result False')
        return False
    else:
        print('input1 ', dict(Counter(input1)))
        print('input2 ', dict(Counter(input2)))
        sorted_1 = sorted(dict(Counter(input1)).items(), key=lambda x: (x[0], x[1]), reverse=True)
        sorted_2 = sorted(dict(Counter(input2)).items(), key=lambda x: (x[0], x[1]), reverse=True)
        if sorted_1 == sorted_2:
            print('result True')
            return True
        else:
            print('result False')
            return False

    # Approach 3
    count1 = {}
    for i in input1:
        if i not in count1.keys():
            count1[i] = 1
        else:
            count1[i] = count1.get(i) + 1
    count2 = {}
    for i in input2:
        if i not in count2.keys():
            count2[i] = 1
        else:
            count2[i] = count2.get(i) + 1
    print('Count1 ', count1)
    print('Count2 ', count2)
    sorted_1 = sorted(dict(input1).items(), key=lambda x: (x[0], x[1]), reverse=True)
    sorted_2 = sorted(dict(input2).items(), key=lambda x: (x[0], x[1]), reverse=True)
    if sorted_1 == sorted_2:
        print('result True')
        return True
    else:
        print('result False')
        return False


def reverse_each_word_in_sentence(input):
    # Approach 1
    words = str(input).split(' ')
    reverse_words = [''.join(reversed(i)) for i in words]
    print('reverse words ', reverse_words)

    # Approach 2
    words = str(input).split(' ')
    reverse_words = [i[::-1] for i in words]
    print('reverse words ', reverse_words)


def remove_duplicates_from_string(input):
    # Approach 1
    print(set(input))

    # Approach 2
    a = []
    for i in input:
        if i not in a:
            a.append(i)
    print('a val ', a)


def find_second_highest_element():
    dict_a = {'asdklfhkjnk': 1, 'askdfhkjdscasas': 2, 'skoidjjfhj': 1}
    sort_by_values = sorted(dict(dict_a).items(), key=lambda x: x[1], reverse=True)
    print('result ', dict(sort_by_values)[1])
    print('Second highest element ', sort_by_values[1])
    # remove second highest element
    del sort_by_values[1]
    print('Dictionary after removing second element ', sort_by_values)


def find_second_highest_element_in_sentence():
    s = "India is my country"
    aa = s.split(" ")
    result = []
    for i in aa:
        result.append(len(i))
    result.sort()
    print(result[-2])
    dict_a = {}
    for i in aa:
        dict_a[i] = len(i)
    sort_by_values = sorted(dict(dict_a).items(), key=lambda x: x[1], reverse=True)
    print('Second highest element ', sort_by_values[1])


def find_common_elements_in_two_lists():
    a = [1, 2, 3, 4, 56, 5, 2, 3]
    b = [4, 6, 8, 2, 34, 1, 3, 9, 8, 4, 0]
    result = []
    for i in a:
        if i in b:
            result.append(i)
    print('Common elements ', set(result))


def demonstrate_try_catch(numerator, denominator):
    try:
        result = numerator / denominator
        print(f'result: {result}')
    except ZeroDivisionError:
        print('Error: cannot divide by zero')
    except TypeError:
        print('Please provide numbers for division')
    finally:
        print('Execution of divide numbers function complete')


def remove_duplicates_from_array():
    input = [1, 34, 6, 3, 4, 2, 4, 1, 6, 445, 3]
    list_a = []
    for i in input:
        if i not in list_a:
            list_a.append(i)
    print(f'unique values in array {list_a}')

    input2 = [1, 34, 6, 3, 4, 2, 4, 1, 6, 445, 3]
    print('unique values using set ', list(set(input)))


def swap_without_third_variable():
    a, b = 1, 2
    print('BEFORE a, b', a, b)
    a = a + b
    b = a - b
    a = a - b
    print('AFTER a, b', a, b)

def extract_vowels_consonants():
    a = "kasdnhfjhkj3rfIjdnk35492"
    vowelChars = "AEIOUaeiou"
    vowels=[]
    consonants=[]
    for i in a:
        if i.isalpha():
            if i in vowelChars:
                vowels.append(i)
            else:
                consonants.append(i)
    print('Vowels ',set(vowels))
    print('Consonants ',set(consonants))


def reverse_substrings(input_string):
    # Step 1: Split the input string into parts (non-numeric and numeric)
    parts = re.split('(\d+)', input_string)

    # Step 2: Reverse non-numeric parts
    for i in range(len(parts)):
        if not parts[i].isdigit():  # check if the part is non-numeric
            parts[i] = parts[i][::-1]

    # Step 3: Join all parts together to get the final output
    return ''.join(parts)



demonstrate_try_catch(10, 2)  # valid
demonstrate_try_catch(10, 0)  # div by zero
demonstrate_try_catch(10, 'b')  # invalid input
remove_duplicates_from_array()
find_second_highest_element_in_sentence()
find_common_elements_in_two_lists()
swap_without_third_variable()
extract_vowels_consonants()