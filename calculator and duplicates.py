#-----------------------Calculator--------------------

def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

start = "start"

while start:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # Take input from the user 
    choice = input("Enter choice(1/2/3/4):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
       print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
       print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
       print(num1,"/",num2,"=", divide(num1,num2))
    else:
       print("Invalid input")
       
    start = input("Type 'start' to reload and 'no' or enter to exit: ")
    if start =="no":
           break





#--------------------------------Ushtrimi 1-----------------------------------------



def split(word):
    return [char for char in word]  #list comprehension
n=int(input("how many times you want to execute the program? "))
i=0
while range(i<n):
    i+=1
    example=input("Input your string: ")

    print("Your value: ",split(example))


#-------------------------------------------------------------------------------------

#--------------------------------Ushtrimi 2-----------------------------------------


def split(word1):
    return [char for char in word1]  #list comprehension
    return [char2 for char2 in word1]
n=int(input("how many times you want to execute the program? "))
i=0
while range(i<n):
    i+=1
    example=input("Input your first string: ")
    example2=input("Input your second string: ")

    print("Your first value: ",split(example))
    print("Your second value: ", split(example2))
    
   
    set_1, set_2 = set(example), set(example2)
    print("Your value is: ",list(set_1 & set_2))


