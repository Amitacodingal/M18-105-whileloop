#Input the number to find sum of terms
n = int(input("Enter the value of terms: ") )

sum = 0 

while i <= n: #loop will run from 1 to n
    sum = sum+i
    i = i+1

print("\nSum =", sum)

#infinite loop
i=0
while i<=0:
    print("I will run forever")
    
    
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    
    
 #highest common factor
 

num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

#calculate the HCF of user entered number
while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1   

print("HCF of num1 and num2 is",hcf)


#palindrome number
num = int(input("Enter a number: "))
rev = 0
#check each digit are the same backward and forward
temp = num
while temp>0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)
#display the result
if rev==num:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
   
