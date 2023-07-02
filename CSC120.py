for i in range(0,10):
    print("*" * 50,end="\n")

for i in range(30):
    if i < 20:
        print('*' * i)
        i +=1

i=20
n=0
for i in range(30):
    if i < 20:
        print(i, i+n, i)
        i +=1
        n +=1
else:
    print("the end")

from math import sqrt,sin,cos,degrees
x=30
y=degrees(x)
print(sqrt(36))
print(cos(y))
print(sin(y))



from random import randint
for i in range(50):
    x = randint(3,6)
    print("x is a random number between 3 and 6:", x)



# from random import randint
# x=randint(1,50)
# y=randint(2,5)
# print(x,y)
# print(x**y)

# print("\n\n")

# import random
# x= random.uniform(1,10)
# print(x)
# print(round(x,2))

# print("\n\n")

# from random import randint
# x=randint(1,10)
# print(x)
# for i in range(x):
#     print("hydrosamuel")

# from random import randint
# for i in range(50):
#     x=randint(1,2)
#     y=randint(1,3)
#     p=randint(1,4)
#     q=randint(1,5)
#     print(x,y,p,q)



# word = "Hello, World!"
# print(word[2:9:2])

# text = "Hello, World!"
# print(text.replace("o", "e", 1))

# word = "Python"
# print(word.find("th"))

# word = "Python is the best"
# print(word.find("th"))

# text = "Hello, World!"
# print(text[::-1][::2])

# text = "Hello, World!"
# print(text.count("l", 5, 12))


# text = "Hello, World!"
# print(text.index("o", 5))
# print(text.split(",", 1))

# text = "Python is fun"
# print(text.split(" ", -1))

# text = "Python is a programming language"
# print(text[7:14][::-1])

# text = "Python"
# print(text.endswith("on"))

# text = "Hello, World!"
# print(text.replace("l", "X", 2))

# import random

# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# reversed_list = my_list[::-1]
# sum_of_elements = sum(reversed_list)
# print(sum_of_elements)

# my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# print(my_dict.items())


# a= (1,2,3,4,5,6)
# print(type(a))
# print(len(a))




# my_list = (1, 2, 3, 4, 5)
# my_tuple = (x for x in my_list if x % 2 == 0)  # Create a tuple with even numbers
# print(my_tuple)

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1:4:2])



# my_tuple = (1, 2, 3)
# print(my_tuple.count(4))

# my_tuple = (2, 4, 6, 8, 10)
# all_even = all(x % 2 == 0 for x in my_tuple)  # Check if all elements are even
# print(all_even)

# def square(x):
#     return x ** 2

# result = square(5) + square(3)
# print(result)

# def multiply_numbers(a, b=2):
#     return a * b

# result1 = multiply_numbers(5)
# result2 = multiply_numbers(3, 4)
# result3 = multiply_numbers(b=5, a=2)

# print(result1 + result2 + result3)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5) + factorial(3)
# print(result)
# print(2*8)

# a = int(input("a "))
# b = int(input("b "))
# c = int(input("c "))
# D = ((b**2)- (4*a*c))**0.5
# sol_1 = (-b + D)/2*a
# sol_2 = (-b - D)/2*a
# print(sol_1)
# print(sol_2)


def population_density(population, land_area):
    population_density= population/land_area
    return population_density

print(population_density(100,20))


def readable_timedelta(days):
    weeks = days//7
    days_r = days % 7
    return f"{weeks} week(s) and {days_r} day(s)"


print(readable_timedelta(100))

ade="werwyueiowwpwieyetwfwywoqiqeteywywtete"
print(ade.rsplit())
    

    
def word_count(document,search_item):
    words= document
    answer= 0
    for word in words:
        if word == search_item:
            answer +=1
    return answer



print(word_count("werwyueiowwpwieyetwfwywoqiqeteywywtete", "e")) 



def square_num(limit):
    answer = 0
    while(answer + 1)** 2 < limit :
        answer +=1
    return answer 

print(square_num(16))




#str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

    

