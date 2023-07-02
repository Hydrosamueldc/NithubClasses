
result1 = []
numb = [1,2,3,4,5,6,7]
results= [ i * 2 for i in numb]
print(results)

print("\n\n")

for x in numb:
   x*=2
   result1.append(x)
print(result1)

print("\n\n")

result1 = []
name = ['Emma', ' David', 'Harry', 'Affluence','Eslar']
for i in name:
   i= i.upper()
   result1.append(i)
print(result1)

print("\n\n")

results= [ x.upper() for x in name]
print(results)


print("\n\n")


num = [1,2,3,4,5,6]
def timesThree(num):
   return num * 3

results2=[]
for x in num:
    x=timesThree(x)
    print("x", x)
    results2.append(x)




print(results2)



   
   
