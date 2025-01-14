def two_sum():
    nums=[2,7,11,15]
    target=9
    map={}
    for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in map.keys():
            return [map[compliment],i]
        map[nums[i]]=i
    return []

def is_palindrome():
    input="ADCDA"
    result=True
    left=0;
    right=len(input)-1
    while left<right:
        if input[left]!=input[right]:
            result=False
        left+=1
        right-=1
    return result

def roman_to_integer():
    roman="MMMDCCXXIV"
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total=0
    for i in range(len(roman)):
        current=roman_map[roman[i]]
        if i+1<len(roman) and current<roman_map[roman[i+1]]:
            total -=current
        else:
            total += current
    return total

def single_number():
    input=[4,1,2,1,2]
    result=0
    for i in input:
        result ^= i
    return result

def intersectionOfTwoArrays():
    nums1=[4,9,5]
    nums2=[9,4,9,8,4]
    result=list(set(nums1) & set(nums2))
    return result

def fizzbuzz():
    n=10
    result=[]
    for i in range(1,18):
        if i%3==0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        elif i%3!=0 and i%5!=0:
            result.append(str(i))
    return result

def to_lower_case():
    input = "here"
    output=""
    for i in input:
        ascii=ord(i)
        if ascii>=65 and ascii<=90:
            output+=chr(ascii+32)
        else:
            output+=chr(ascii)
    return output

def house_robber():
    input=[2, 7, 9, 3, 1]
    #input=[1, 7, 6, 4, 3, 2, 2]
    if input is None or len(input)==0:
        return 0
    if len(input)==1:
        return input

    prev1=input[0]
    prev2=max(input[0],input[1])

    for i in range(2,len(input)):
        current=max(prev2,input[i]+prev1)
        prev1=prev2
        prev2=current
    return prev2






print('two sum output ',two_sum())
print('is palindrome output ',is_palindrome())
print('roman to integer conversion output ',roman_to_integer())
print("Single number in an array ",single_number())
print('intersection or common of 2 arrays ',intersectionOfTwoArrays())
print("FizzBuzz ",fizzbuzz())
print("Upper to Lower ",to_lower_case())
print("House robber output ",house_robber())