names = ['karthik','kiran','varun','praveen']
print('reading the values from list');
print(names[0]);
print(names[1]);
print(names[2]);
print(names[3]);
for name in names:
    statement = 'Hello there' +  name
    print(statement)


names = ['karthik','kiran','varun','praveen']
print('reading the values from list');
print(names[0]);
print(names[1]);
print(names[2]);
print(names[3]);
for name in names:
    statement = ' '.join(['Hello there', name,'srikanth'])
print(statement)    

test1="learn python"
test2="learn python"
print(id(test1))
print(id(test2))


mynewlist = [iter for iter in range(10)]
print(mynewlist)

listofplaces = ["hyderabad","mumbai","chennai","kolkata"]
first3letters = [place[0:3] for place in listofplaces if len(place)>3]
print(first3letters)

voiceofletters = ["capable","congrates","complain"]
first1letter = [letter[0:1] for letter in voiceofletters]
print(first1letter)

list3 = [[0]*2]
print(list3)
list3 = [[0]*2]*2
print(list3)


list1=[[1,2,3]+[2,4,6]]
list2=[2,3,4,5,6]
list3=[list1+list2]
print(list3)

sports = ["cricket","hockey","volleyball"]
print(sports)
sports.append("tennis")
print(sports)
sports.insert(2,"volleyball")
print(sports)
sports.remove("cricket")
print(sports)
sports.pop(2)
print(sports)
print(sports.index('hockey'))
print(sports.index('tennis'))
sports

sports=['kabadi','shettle','khokho']
print(sports)
sports.pop(2)
print(sports)

sportsCopy = sports.copy()
print(sportsCopy)


names = ['python','scripting','coding','multimedia','business']
print(names)
print(names[1])
print(names[4])
print(names[2])

print('most trending business in society:-'+names[2]);
print(names[1:4])

number=[0,2,3,4,5,6]
print(number[1:4])
print(number[1:3:5])
print(number[1:3:6])



        #---OOPS---#
# procedure oriented/structured oriented : Functions which are re-usable concept are
        # called procedure oriented,But if we want to group all functions into one class or one program
        # their is no availability in procedure oriented.
        # it will execute from top-to-bottom way
        
# Object oriented : which has the re-usability of functions.
        # it is bottom-up approach.
        # Encapsulation (if we want to bring all multiple methods into single entity or single method )
        # data hiding
        # polimorphism (function overloading,concept overloading)
        # Inheritance
        

    


#--- Classses in python---#

# which is one of the oops concept not only used in pyhton but also in many languages.
# class = blue print of object in Python.it is a keyword.
# An object can contain a number of functions (which we call methods) as well as data that is used by those functions.
# We call data items that are part of the object attributes.
# We use the class keyword to define the data and code that will make up each of the objects.
# The class keyword includes the name of the class and begins an indented block of code ,
    #  where we include the attributes (data) and methods (code)
# Almost all the codes is implemented using a special construct called classes.
# Programmers use classes to keep related things together. 
# This is done using the keyword “class,” which is a grouping of object-oriented constructs. 
# Python is an object oriented programming language. 
# Almost everything in Python is an object, with its properties and methods. 
# A Class is like an object constructor, or a "blueprint"  for creating objects.
# Python provides us with many built-in objects. 
##  And class which holds properties are called classes and methods which will be holds values.
    
    
    # For Ex: birds
      # propetites are : wings,legs,eyes,tail etc..,
      # Methods are: speaks,fly,sleep,eat,making sounds etc..,
      
      # Here bird is the main ''class'' 

#--Basic class syntax--#

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>



class bird:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
        
    def do_fly(self):
        if self.occupation == "flying with wings":
            print(self.name,"flying with wings")
        elif self.occupation == "shouts":
            print(self.name,"shouts load")
        
    def speaks(self):
        print(self.name,"says how to fly")
        
piegon = bird("piegon","flying with wings")
piegon.do_fly()
piegon.speaks()
            

#--Object oriented constructs--#




# Constructor is used to create an object of a class using the new keyword, 
  # where an object is also known as instance of a class. 
# Each object of a class will have its own state (instance variables) and access to methods of its class.

    #--Some important features of a constructor are ---#

  #1) A Constructor always must have the same name as the class.
  # 2) A  Constructor cannot have a return type.
  # 3) A constructor may have any access modifier like private, protected, default, public etc..

# A constructor is a special type of method (function) which is used to initialize the instance members of the class.
# Constructor can be parameterized and non-parameterized as well. 
# Constructor definition executes when we create object of the class. 
# Constructors will verify that,if enough resources are their for object to perform any starting task.
# While creating an object, a constructor can accept arguments if necessary. 
# When we create a class without a constructor,Python automatically creates a default constructor that doesn't do anything.
# basically constructors in python will help usto invoke the member function.
  # to over come Arithmetic function with specified object like.
   # A = 100  OR  (A.Add(2,3)) to overcome this kind which we want to invoke  member function we use constructor.

#--Non-parameterized--#
    
class Student:
    def __init__(self):
        print("it is non parametrized constructor")
    def show(self,name):
        print("Hi",name)  
student = Student()  
student.show("John") 
    
    
#---parameterized--# to re-use particular custom value for instances in applications.

class Student:
    def __init__(self, name):
        print("It is parametrized constructor")  
        self.name = name
    def show(self):
        print("Hi",self.name)  
student = Student("John")  
student.show()  



stuff = list()
dir(stuff)

dir(stuff)

stuff = str()
dir(stuff)

def fullname():
    return "karthik muskula"
print(fullname()) 

def ball():
    return "playing with football"     
print(ball())        



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("sandy", 30)
p1.myfunc()







class Arithmetic:
    def Add(self,x,y):
        return x + y
    def Subtract(self,x,y):
        return x - y
    def Multiply(self,x,y):
        return x * y
    def Divide (self,x,y):
        return x / y
    
a = Arithmetic()
print(a.Add(3,5))
print(a.Subtract(2,200))
print(a.Multiply(3,6))
print(a.Divide(20,4))

b = Arithmetic()
print(b.Add(23,45))
print(b.Divide(2,6))
print(b.Multiply(3,6))
print(b.Subtract(3,8))


5/17
5//17


class WineStore:
    instances = 0
    def __init__(self,attrib1,attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        WineStore.instances += 1
        
b1 = WineStore("","")
b2 = WineStore("","")

print("WineStore.instances:",WineStore.instances)        



class Arithmetic:
    
    def __init__(self,attrib1,attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        print(self.attrib1)
        print(self.attrib2)
        
    def Add(self):
        return self.attrib1 + self.attrib2
    def subtract(self):
        return self.attrib1 - self.attrib2
    def Multiply(self):
        return self.attrib1 * self.attrib2
    def Divide(self):
        return self.attrib1 / self.attrib2
    
a = Arithmetic(200,300)
print(a.Add())
print(a.subtract())
print(a.Multiply())
print(a.Divide())

b = Arithmetic(2,3)
print(b.Add())
print(b.subtract())
print(b.Multiply())
print(b.Divide())      



def Arithmetic():
    return "x+y=100"
print(Arithmetic)

x=100
y=200
print(x+y)



class people:
    
    def __init__(self,id,firstname,secondname,lastname):
        self.id = id
        self.firstname = firstname
        self.secondname = secondname
        
        
class customer(people):
    
    def __init__(self,id,firstname,secondname,lastname,totalspend):
        people.__init__(self,id,firstname,secondname,lastname,totalspend)
        self.totalspend = totalspend
        
    def getDetails(self):
        return "%s %s (customer %i) has spent %s in total." % (self.firstname,self.secondname,self.lastname,self.totalspend)
    
customer = customer(
        13,
        "karthik",
        "muskula",
        123
        )   





x='one with long'
print(x.upper())
x1 = 'my name is karthik'
x2 = 'karthik calling karthik'
x3 = x1 + x2 
print(x3)



# OOPS Concepts #




class MyClass:
    def MyFunc(self):
        return "Hello World"
    
k = Myclass() 
print(k.MyFunc())
    
    
class Sample:
    firstname = "ExcelR";
    lastname = "Bangalore";
    def fullname():
        return this.firstname+" "+ this.lastname;
    
class Myclass:
    def MyFunc(self):
        return "Hello world"
    

k = Myclass()
print(k.MyFunc())
    

def fullname():
    return "hello world"
print(fullname())
       
     
class Arithmetic:
    def Add(self,x,y):
        return x+y
    def Subtract(self,x,y):
        return x-y
    def Multiply(self,x,y):
        return x*y
    def Divide(self,x,y):
        return x/y

arth = Arithmetic()
arth.Add(10,2)   
arth.Subtract(10,2)
arth.Multiply(10,2)



class WineStore:
    instances = 0
    def __init__(self,attrib1,attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        WineStore.instances+=1

        
b1 = WineStore(10,10)
b2 = WineStore(10,10)
print("WineStore.instances:",WineStore.instances)



class Arithmetic:
    def __init__(self,attrib1,attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        print(self.attrib1)
        print(self.attrib2)
        
    def Add(self):
        return self.attrib1 + self.attrib2
    def Subtract(self):
        return self.attrib1 - self.attrib2
    def Multiply(self):
        return self.attrib1 * self.attrib2
    def Divide (self):
        return self.attrib1 / self.attrib2
    def fullname(self):
        return self.attrib1 / self.attrib2
       
   
    
a = Arithmetic(200,300)
print(a.Add())
print(a.Subtract())
print(a.Multiply())
print(a.Divide())

b = Arithmetic(10,30)
print(b.Add())
print(b.Subtract())
print(b.Multiply())
print(b.Divide())
        


class Arithmetic:
    
    def __init__(self,attrib1,attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        
    def Add(self,x,y):
        return x+y
    def Subtract(self,x,y):
        return x-y
    def Multiply(self,x,y):
        return x*y
    def Divide(self,x,y):
        return x/y
    
a = Arithmetic(2,3)
print(a.Add(2,3)) 

   



def __new__(cls):
    if cls.instance is None:
        cls.instance = super().__new__(cls)
    return cls.instance



# Inheritance
    
# Inherting the object which is created in class that can inherit the code of class
    # from simple way as,parent to child.
    
    
# Inheriting the other class i.e,,base class,Acccring the parent class properties into child is called inheritance.
  
# Their are couple types of Inheritance.
    # Single inheritance
    # Multiple inheritance
    # Multi-level Inheritance
    # Hybrid inheritance
    # Heirarchiel inheritance.,Mostly we uses single level inheritance to over complecated.



class OnlyOne :
    class __OnlyOne:
        def __init__(self,arg):
            self.val = arg
        def __str__(self):
            return repr(self)+self.val 
    instance = None
    def __init__(self,arg):   
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
            
    def __getattr__(self,name):
        return getattr(self.instance,name)

    
    
      

x = OnlyOne('Rose')
print(x)
y = OnlyOne('jasmine')
print(y)
z = OnlyOne('sunflower')
print(z)
print(x)
print(y)
print('x')
print('y')
print('z')
output = ''


class Person:
    
    def __init__(self,id,firstname,lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        
    class Customer(Person):
        
        def __init__(self,id,firstname,lastname,totalspend):
            Person.__init__(self,id,firstname,lastname)
            self.totalspend = totalspend
            
        def getDetails(self):
            return "%s %s (customer %i) has spent %s in total."(self.firstname,self.lastname,self.id,self.totalspend)
            
customer = Customer(12,
    "karthik",
    "reddy",
    1000)

Person = Person(12,"karthik","reddy")


customer.getDetails(Person)


normal_list = [2,4,5,7,9]
class CustomSequences():
    def __len__(self):
        return 5       
     
            
    
# FIle I/O
        
    
         
path = 'sample.txt'
days_file = open(path, 'r')            
days = days_file.read().split("\n")
days_file.close()

new_path = 'newsample.txt'
title = 'Days of the week\n'      
new_days = open(new_path,'w')   
new_days.write(title)  
for i in days:
    new_days.write(i+"\n")
new_days.close()



getcwdb()
chdir()




print ("python is case sensitive,", "isn't it?")      

f = open("sample.txt")            
days = f.read().split("\n")            

# Multiple derived        
        
class Animal:
    def eat(self):
        print('Eating...')
        
class horse(Animal):
    def run(self):
        print('Running...')

class babyhorse(horse):
    def weep(self):
        print('weeping...')
        
class newhorse(babyhorse):
    def drink(self):
        print('drinking...')

h=newhorse()
h.eat()
h.run()
h.weep()
h.drink()


# multi derived

class First():
    def __init__(self):
        super(First,self).__init__()
        print("first")
        
class Second():
    def __init__(self):
        super(Second,self).__init__()
        print("second")       
        
class Third(Second,First):
    def __init__(self):
        super(Third,self).__init__ ()
        print("third")  

Third()
    
print("\n")
class Fourth(First,Second):
    def __init__(self):
        super(Fourth,self).__init__()
        print("Fourth")

Fourth()

class fifth(First,Second):
    def __init__(self):
        super(fifth,self).__init__()
        print("fifth")
        
fifth()


# Importing data set and ploting in python #
   
import os
os.getcwd()
import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("mtcars")


     
import os
os.getcwd()
import pandas as pd
import matplotlib.pyplot as plt
fraud = pd.read_csv("Fraud_check.csv") 
fraud.columns   
fraud.Undergrad.value_counts().plot(kind="bar")
fraud["Marital.Status"].value_counts().plot(kind="bar")
fraud["Marital.Status"].value_counts().plot(kind="pie")
pd.crosstab(fraud.Undergrad,fraud["Marital.Status"]).plot(kind="bar")
pd.crosstab(fraud.Undergrad,fraud["Urban"]).plot(kind="bar")
fraud["Taxable.Income"].groupby(fraud["Undergrad"]).mean().plot(kind="bar")
fraud["Taxable.Income"].groupby(fraud["Undergrad"]).mean().plot(kind="bar")
fraud.iloc[:,2:4].plot(kind="line")         
plt.plot(fraud["City.Population"],fraud["Taxable.Income"],"bo")
fraud["City.Population"].groupby(fraud["Marital.Status"]).mean()

# Exceptions in python #
# Exceptions #



anil = 'coming to office'
print(anil)

print(0/0))
print(0/0)


x = 15
if x > 10:
    raise Exception('x should not exceed 10 . the value of x was:' ,x)


try: 
    print (1/0)
except ValueError:
        print("You can't divide by zero, you're silly.")

while True:
    try:
        x = int(input("Please enter a  valid number: "))
        print ("hello")
        break
    except ValueError:
        print(" Their was no valid number.  Try again...")
        
try:
    x = 2+3
except:
    print('it does\'t work!')
else:
    print('will run when there is no exception')

try:
    y =10
    print('True')
except:
    print('wrong information')



    


    


#------Condition statements--------#

# If the statement is True then IF condition will pass.
# If the statement is False then Else condition will pass.
# Elif is the shirtform of Else.It will to check for multiple Expressions (or) Multiple conditions.
# Nested statements which we declare or given the other statement of variable (or) code instead of parent 
    # to child is called nested if else statement.
# The statement inside a statement is called Nested statement.


if not (3>4):
    print ("No")

    

person = 5

if person < 3:
    print ("A")
elif person <5:
    print ("B")
elif person < 6:
    print ("C")
elif person < 7:
    print ("D")
else:
    print ("None")

    
# % reminder to comparison

if (12%3==0) and (12%2==0):
    print ("first")
    
elif 6%2==0:
    print ("second")  
elif 10%5==10:
    print ("No")
else:
    print ("no other conditions satisfying")
    



x = list(range(20))

for i in x:
    if i%2==0:
        print ("even")
    elif not i%2==0:
        print ("odd")
    else:
        print ("IDK")


n = int(input("Number = "))
if n>0:
    print("the absolute value")
    
    
n=int(input("enter number ="))
if n<5:
    print("the absolute value",n)
    
    
n=int(input("Number= "))
if n<0:
    print("the absolute value",n)
else:
    print("the absolute value",-n)
    
    
    
n = int(input("number"))
if n<0:
    print("the correct number",n)
    print("the correct number",n)
    print("the correct number",n)
else:
    print("the correct number",-n)
    print("the correct number",-n)
    
    # we should not give keywords as variables #
    
sumofnumber = 30+60  
print(sumofnumber)




a = int(input("value"))
if a>5:
    print("the absolute value",-a)
    print("the absolute value",-a)
else:
    print("the absolute value",a)
    print("the absolute value",a)
    
    
    
name = input("name")
if name=='karthik':
    print("the name entered is",name)
elif name =='varun':
    print("the name entered is",name)
elif name =='kalyan':
    print("the name entered is",name)
else:
    print("the name entered is not valid")
    


# Nested IF statement ,Else statement
    
name = "man"
manname = "karthik"
if name == "man":
    if manname == "karthik":
        print("valid name")
    print("name entered is karthik")
else:
    print("name entered is invalid")
    
    
name = "man"
manname = "sultan"
if name == "sultan":
   if manname == "sultan":
       print("valid name")
       print("name entered is valid")
else:
    print("name entered is invalid ")
    
    
    
place = "utey"
chennaiplace = "india"
if place == "russia":
    if chennaiplace == "india":
        print("the valid place")
        print("the valid information")
else:
    print("invalid place")
    print("invalid place")
    
    
    
    
    
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
    

for i in range(0,4):
    for j in range(0,5):
        print(i,j)



for i in range(6):
    print("a")
    for j in range(10):
        print("b")



for x in range(3):
    for y in "Hi":
        print(x,y)


score=100
while score < 200:
    print('hi your score is less')
    score = score+1
print('no score')
marks=30
while marks >=10:
        print('you have no marks')
        marks=marks-1
print('no marks')



value = {x:x for x in range(20)}
print(value)

mynewlist = [iter for iter in range(30)]
print(mynewlist)











