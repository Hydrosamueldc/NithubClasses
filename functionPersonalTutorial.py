def greet(name):
    print("hello", name )
    print("congratulation you can now define a function")
greet("hydrosamuel")

def add_numbers(n1 , n2):
    the_sum = n1 + n2 
    print("The sum is " ,the_sum)
add_numbers(6,9)


def increment(number , by):
    return number + by


print(increment(6,by=3))



def increment(number , by=2):
    return number + by


print(increment(53))


def multiply(x,y):
    return x * y

print(multiply(4,5))


#write a function that multiply numbers 
def multiply(*numbers):
    total = 1
    for number in numbers:
        total*=number
    return(total)
    
print(multiply(2,3,4,5,6))



#write a program that save information of a user 
def save_user_info(**user):
    print(user)


save_user_info(id=1, name="hydrosamuel", age= 15)


# we use double ASTERIK ** to assign multiple keys values pairs 


def save_user_info(**user):
    print(user['name'])


save_user_info(id=1, name="hydrosamuel", age= 15)


# SCOPE in programing refer to a region of the code where a variable is defined
# def greet(name):
#     message = a 
# the scope of the message and name variable is the greet function
# this variale(s) in the scope of a function are refers as LOCAL VARIABLE 
# which means they dont exist anywhere else 
# 
# 
# 
# name= 'hydrosamuela'
# def greet():
#     message = a
# 
# name here is a GLOBAL VARIABLE 


# write a program if divisible by 3 it return Fizz and if divisible by 5 it return Buzz
# And if divisble by both 3 and 5 it retun FizzBuzz

def fizz_buzz(input):
    if (input % 3==0) and (input % 5==0):
        return 'FizzBuzz'
    if input % 3== 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input 


print(fizz_buzz(40))


# Write a code that tell if the guess number from a user is correct 
guess_no = 8
def guess(input): 
    if guess_no  == input:
        print("Congratulation you guess correctly")
    else:
        print("try one more time, you are wrong")
    

guess(10)
    







