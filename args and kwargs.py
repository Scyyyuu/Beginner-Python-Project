# *args
# **kwargs

def multiplication (*numbers):
     total = 1
     for number in numbers:
         total *= number
     return total

print (multiplication(9, 8))

def addition (*add_nums):
    total = 0
    for add_num in add_nums:
        total += add_num
    return total

print (addition(2,5))

def substraction (*sub_nums):
    total = sub_nums[0]
    for sub_num in sub_nums[1:]:
        total -= sub_num
    return total

print (substraction(10, 5, 2))

def division (*div_nums):
    total = div_nums[0]
    for div_num in div_nums[1:]:
        total /= div_num
    return total

print (division(81, 9))