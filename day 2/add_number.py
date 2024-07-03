# First Approach
# firstNumber = input( "Enter first number:\n")
# firstNum = int(firstNumber)
# # print( type(firstNum))

# secondNumber = input( "Enter second number:\n")
# secondNum = int(secondNumber)

# sum = firstNum + secondNum
# strSum = str(sum)
# # print( type(sum))

# print("The sum is:" +strSum)



# Second Approach
two_digit_num = input("Enter two numbers: ") #this always give output in string data type

firstNum = int(two_digit_num[0])
secondNum = int(two_digit_num[1])

sum = str(firstNum + secondNum)
print("The sum is: " + sum)
