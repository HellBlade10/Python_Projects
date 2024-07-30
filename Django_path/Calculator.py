operation = int(input("Choose:\n"
"1 for add\n"
"2 for subtract\n"
"3 for multiply\n"
"4 for divide\n"
"=> "))
x = 0
sum = 0
difference = None
product = 1
divide = 1
value = []
while x==False:
    #Addition
    if operation == 1:
        numbers = input("Add number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            value.append(numbers)
            sum += numbers

    #Subtraction        
    elif operation == 2:
        numbers = input("Subtract number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            value.append(numbers)
            if difference == None:
                difference = int(numbers)
            else:
                difference -= numbers

    #Multiplication            
    elif operation == 3:
        numbers = input("Multiply number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            value.append(numbers)
            product *= numbers

    #Division
    elif operation == 4:
        numbers = input("Divide number? : ")
        if numbers == 'q':
            break
        else:
            numbers = int(numbers)
            if numbers != 0:
                value.append(numbers)
                divide /= numbers
            else:
                print("Error: Division by zero is not allowed")
                break


if operation == 1:
    print("Sum is {}".format(sum))
elif operation == 2:
    print("Difference is {}".format(difference))
elif operation == 3:
    print("Product is {}".format(product))
elif operation == 4:
    print("Quotient is {}".format(divide))
else:
    print("Invalid operation")


see = input("Do you want to checkl the entered values?(y/n): ")
if see == 'y':
    print(value)
else:
    print("Exiting the program")
