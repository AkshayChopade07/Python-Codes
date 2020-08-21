
                         #----Loops---#
    

# Loop : Repeating the code again and again until the statement is True OR condition is True.

# Inorder to reduce the complexity, more efficient,increase the speed of the code execute.

# Loops allows the execution of the statement OR a group of statements for more mutiple times.
    
# Once the condition becomes False,it stop the execution and comes out & control moves out of loop.

# Loops support : while,for and Nested.
    
# While Loop : It will execute until the Iteration of the statement OR argument is True.
    
# For Loop: It will executes the given iteration statement for specified number of times.
    # The boolean condition.
    # The initial value of the counting variable.
    # Incrementation of counting variable.
    
    

# while loop
    
count = 0
while count<8:
    print("Number:",count)
    count = count+1
print("Goodbye")

# for loop


flowers = ["jasmine","rose","lilly"]
for flower in flowers:
    print("current flower:",flower)
print("Good bye")




i = 10
while i<20:
    i = i+1
    print (i)
    


# Nested Loop #
    

for i in range(40,50):
    for j in range(5):
        print(i,j)





for x in range(3):
    for y in "Hi":
        print(x,y)



index = 0
numbers = [1, 2, 3, 4, 5]
while index < len(numbers):
    print(numbers[index])
    index = index + 1


numbers = [10, 12, 15, 18, 20]
for number in numbers:
    print(number)
    
    
value = {x:x for x in range(20)}
print(value)

mynewlist = [iter for iter in range(30)]
print(mynewlist)



#If we call the iter() function on an iterator it will always give us itself back.

numbers = [100, 200, 300]
iterator1 = iter(numbers)
iterator2 = iter(iterator1)

# Check if they are the same object
print(iterator1 is iterator2)

for number in iterator1:
    print(number)
    
    
    
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 10, 5, 8, 4, 1, 5, 3, 12]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)



# program to display student's marks from marks sheet
student_name = 'karthik'

marks = {'john': 90, 'kalyan': 55, 'Aanad': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No marks with that name is found')
    
    
    

fruits = ["banana", "apple", "orange", "mango"]
part = 0
while part < len(fruits):
    print(fruits[part])
    part = part + 1
print("completed the  end of list")



fruits = ["banana", "apple", "orange", "mango"]
part = 0
while True:
    if part >= len(fruits):
        break
    print(fruits[part])
    part = part + 1
print("completed the  end of list")

