def add(a, b):
 return a + b

def length_of_list(my_list):
 return len(my_list)
 item = []
  
print("1: Add numbers")
print("2: Count items")
print("3: Remove an item")
print("4: Change an item")


choice = input("choose 1 or 2:")

if choice =="1":
 x = int(input("first number:"))
 y = int(input("second number:"))
 result = add(x, y)
 print("result:", result)

elif choice =="2":
 items = []
 i = 0
 
 while i < 3:
  item = input("enter item:")
  items.append(item)
  i = i + 1
 total = length_of_list(items)
 print("total items:", total)


elif choice =="3":
  items = []
  i = 0
  while i < 3:
    item = input("enter item")
    items.append(item)
    i = i + 1
  
  remove_target = input("enter item to remove: ")
  if remove_target in items:
    items.remove (remove_target)
    print(remove_target, "removed")

  else:
    print("item not found.")
  
elif choice =="4":
  items = []
  i = 0
  while i < 3:
    item = input("enter item: ")
    items.append(item)
    i = i + 1
  old = input("enter item to change: ")
  if old in items:
    new = input("enter new item: ")
    index = items.index(old)
    items[index] = new
    print(old,"changed to", new)
      
else:
 print("invalid choice")

print(add(3, 5))
print(length_of_list(["a","b","c"]))

