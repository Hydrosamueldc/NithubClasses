# print((lambda x : 2 * x)(2))


# def add_num(x,y):
#     return x+y
# print(add_num(6,7))


# print((lambda x,y : x+y)(7,7))

# add_num = lambda x,y : x+y
# print(add_num(8,9))


# def mx(x,y):
#     if x > y:
#         return x
#     else:
#         return y
    
# print(mx(8,9))


# mx= lambda x,y: x if x>y else y
# print(mx(6.6,4))



# #### MAP FUNCTON 
# def sqr_num(lst1):
#     lst2 = []
#     for num in lst1:
#         lst2.append(num ** 2)
#     return lst2

# print (sqr_num([1,2,3,4,5]))



# sqr_num = [x**2 for x in range(1,7)]
# print(sqr_num)

# n=list(range(1,10))
# sqr_num =list(map(lambda x : x**2 , n))
# print(sqr_num)


# ## FILTER FUNCTION 
# def over_two(lst1):
#     lst2=[x for x in lst1 if x>2]
#     return lst2

# print(over_two(range(20)))



# n = list(range(10) )
# print(n)
# print(list(filter(lambda x : x>2,n)))


# from functools import reduce 
# n=[2,4,6,8]
# print(reduce(lambda x,y : x*y , n))


# names = input("Enter your names including your last name separated with commas: ")
# list_names = names.split(",")

# assignments = input("Enter assignment count of each student separated with commas: ")
# assign_values = assignments.split(",")

# grades = input("Enter student grades separated with commas: ")
# assign_grades = grades.split(",")

# for name, assignment, grade in zip(list_names, assign_values, assign_grades):
#     potential_grade = int(grade) + 2 * int(assignment)
#     message = f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to submit before you can graduate. Your current grade is {grade} and can increase to {potential_grade} if you submit all assignments before the due date.\n\n"
#     print(message)

while True:
    try:
        x=int(input("Roll your dice: "))
        break
    except:
        print("that is not a valid number! ")
    finally:
         print("\nCool, nice attempt\n")
