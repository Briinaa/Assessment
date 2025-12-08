def add(a, b):
 return a + b

def length_of_list(my_list):
 return len(my_list)

print("1: Add numbers")
print("2: Count items")

choice = input("choose 1 or 2:")

if choice =="1":
 x = int(input("first number:"))
 y = int(input("second number:"))
 result = add(x, y)
 print("result:", result)

elif choice =="2":
 items = []
 i = 0
 
