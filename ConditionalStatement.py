# write a code that  print a range(100) and print fuzz when multiple 3 and Fuss when multiple 5
#  and print FissBuss when multiple  of 3 and 5 using while loop

counter = 1
while counter <=100:
    if (counter % 3) and (counter % 5):
        print("FIZZBUZZ")
    elif counter % 3:
        print("FIZZ")
    elif counter % 5:
        print("BUZZ")
    else:
        print(counter)
    counter +=1

print("\n\n")

#contiue and break are similar 
# break terminate a code entirely 
# while continue will not excute  any code below it
names =["Hydro", "Affluence", "Eslar", "Yasir"]
for i in names:
    print((i))

print("\n\n")


for i in range(100):
    if (i % 3) and (i % 5):
        print("FIZZBUZZ")
    elif i % 3:
        print("FIZZ")
    elif i % 5:
        print("BUZZ")
    else:
        print(i)


print("/n/n")

# enumerate is use to print index of a sequence we are iterating 

for idx,num in enumerate(names):
    print(idx,num)z


print("/n/n")

#using for nested loop  print prime number in range(100)

for num in range(101):