def add(x,y): 
	op=str(x+y)
	print("The sum is "+op+".")
	input("")

def sub(x,y):
	op=str(x-y)
	print("The difference is "+op+".")
	input("")

def mul(x,y):
	op=str(x*y)
	print("The product is "+op+".")
	input("")

def div(x,y):
	op=str(x/y)
	print("The product is "+op+".")
	input("")

print("Welcome to the Simple Calculator")
answer=int(input("Please choose which operation you would like to perform:\n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division\n"))
num_1=int(input("Please input the first number: "))
num_2=int(input("Please input the second number: "))
if answer==1:
	add(num_1,num_2)
elif answer==2: 
	sub(num_1,num_2)
elif answer==3: 
	mul(num_1,num_2)
elif answer==4: 
	div(num_1,num_2)
else: 
	print("Error! Invalid Choice")





